from __future__ import print_function

import sys
import json
import time
import cProfile
import pstats
import argparse
import utils
from datetime import datetime

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

try:
    import gevent_openssl
    gevent_openssl.monkey_patch()
except ImportError:
    pass

import grequests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = None
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
    parser.add_argument('--log-level', '-l', action='store', required=False,
                        default='INFO', help='Log level as per logging module.')
    parser.add_argument('--url-count', action='store', required=False,
                        default=100, help='Call url these many times.')
    parser.add_argument('--profile-code', '-p', action='store_true',
                        required=False, default=False,
                        help='Flag to enable/disable code profiling')
    parser.add_argument('--profile-stats-count', action='store',
                        required=False, default=-1,
                        help='Number of profiled stats to print')
    parser.add_argument('--trace-calls', '-t', action='store_true',
                        required=False, default=False,
                        help='Flag to enable/disable code profiling')
    parser.add_argument('--socket-class', action='store_true',
                        required=False, default=False,
                        help='Get and print underlying socket class')
    return vars(parser.parse_args(sys.argv[1:]))


def setup_tracing():
    """ Setup function call tracing """
    # https://stackoverflow.com/questions/8315389/how-do-i-print-functions-as-they-are-called
    def tracefunc(frame, event, arg, indent=None):
        ''' Trace function calls '''
        if indent is None:
            indent = [0]
        curr_time = datetime.fromtimestamp(time.time()).strftime("%H:%M:%S.%f")
        func_info = ':'.join(str(x) for x in [frame.f_code.co_filename,
                                              frame.f_lineno,
                                              frame.f_code.co_name])
        if event == "call":
            indent[0] += 2
            print(">" + curr_time + " call",
                  "level:" + str(indent[0]), func_info)
        elif event == "return":
            print("<" + curr_time + " exit",
                  "level:" + str(indent[0]), func_info)
            indent[0] -= 2
        return tracefunc
    sys.settrace(tracefunc)
    return True


def make_requests(url, url_count, profile_code):
    """ Make parallel https requests """
    url_count = int(url_count)
    all_page_ids = set(range(url_count))

    pending_requests = []
    for i in range(url_count):
        pending_requests.append(
            grequests.get(url, params={'page': i}, verify=False)
        )

    if profile_code:
        pr.enable()

    all_responses = grequests.map(pending_requests)

    if profile_code:
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

    logger.info('len(all_page_ids) = ' + str(len(all_page_ids)))
    logger.info('len(valid_page_ids) = ' + str(len(valid_page_ids)))
    logger.info('len(invalid_page_ids) = ' + str(len(invalid_page_ids)))

    if invalid_page_ids:
        print(json.dumps(invalid_responses))


def get_socket_class(url):
    """ Get underlying request socket class """
    req = grequests.get(url, params={'page': 1}, verify=False)
    conn_pool = req.session.get_adapter(url).get_connection(url)
    conn_pool.urlopen('GET', url)
    conn = conn_pool.pool.get()
    return conn.sock.__class__


def format_profiler_stats(stats_count):
    """ Format profiler stats """
    stats_count = int(stats_count)
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

    global logger
    logger = utils.setup_logging(args['log_level'])
    logger.info('START')

    if args['trace_calls']:
        setup_tracing()

    make_requests(args['url'], args['url_count'], args['profile_code'])

    if args['socket_class']:
        socket_class = get_socket_class(args['url'])
        logger.info('socket_class = ' + str(socket_class))
        return 0

    if args['profile_code']:
        print(format_profiler_stats(args['profile_stats_count']).getvalue())

    total_time = datetime.now() - start_time
    logger.info('total_time={}'.format(total_time))
    logger.info('END')
    return 0


if __name__ == '__main__':
    sys.exit(main())
