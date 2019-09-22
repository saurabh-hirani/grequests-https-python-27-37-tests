from __future__ import print_function

import grequests
from datetime import datetime
import argparse
import pstats
import cProfile
import json
import sys
import urllib3

try:
    # python 2.7
    from StringIO import StringIO
except ImportError:
    # python 3.6
    from io import StringIO

try:
    # python2.7
    import urlparse
except ImportError:
    # python3.6
    import urllib.parse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pr = cProfile.Profile()


def _get_page_id_from_response(response):
    """ Parse response and get page_id from query_string """
    try:
        query_string = urlparse.urlparse(response.request.path_url).query
    except Exception:
        query_string = urllib.parse.urlparse(response.request.path_url).query
    return query_string.split('=')[1]


def parse_cmdline():
    """ Parse command line """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', action='store', required=True,
                        help='URL to GET')
    parser.add_argument('--url-count', action='store', required=False,
                        default=100, help='Call url these many times.')
    return vars(parser.parse_args(sys.argv[1:]))


def make_requests(url, url_count):
    """ Make parallel https requests """
    url_count = int(url_count)
    all_page_ids = set(range(url_count))

    pending_requests = []
    for i in range(url_count):
        pending_requests.append(grequests.get(
            url, params={'page': i}, verify=False))

    pr.enable()

    all_responses = grequests.map(pending_requests)

    pr.disable()

    valid_responses = [
        x for x in all_responses if x is not None and x.status_code == 200
    ]

    invalid_responses = [
        x for x in all_responses if x is None or x.status_code != 200
    ]

    valid_page_ids = set([int(_get_page_id_from_response(x))
                          for x in valid_responses])
    invalid_page_ids = all_page_ids - valid_page_ids

    print('len(all_page_ids) = ' + str(len(all_page_ids)))
    print('len(valid_page_ids) = ' + str(len(valid_page_ids)))
    print('len(invalid_page_ids) = ' + str(len(invalid_page_ids)))

    if invalid_page_ids:
        print(json.dumps(invalid_responses))


def format_profiler_stats():
    """ Format profiler stats """
    stats_count = 20
    s = StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    if stats_count != -1:
        ps.print_stats(stats_count)
    else:
        ps.print_stats(stats_count)
    return s


def main():
    """ Main function """
    start_time = datetime.now()
    args = parse_cmdline()

    make_requests(args['url'], args['url_count'])

    print(format_profiler_stats().getvalue())
    total_time = datetime.now() - start_time
    print('total_time={}\n'.format(total_time))

    return 0


if __name__ == '__main__':
    sys.exit(main())
