""" Call n urls sequentially """

from __future__ import print_function

import sys
import argparse
import logging
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def parse_cmdline():
    """ Parse command line """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', action='store', required=True,
                        help='URL to GET')
    parser.add_argument('--url-count', action='store', required=False, default=100,
                        help='Call url these many times.')
    return vars(parser.parse_args(sys.argv[1:]))

def make_requests(url, url_count):
    """ Make parallel https requests """
    url_count = int(url_count)

    all_responses = []
    for i in range(url_count):
        requests.get(url, params={'page': i}, verify=False)

    return all_responses

def main():
    """ Main function """
    args = parse_cmdline()

    logging.info('START')
    make_requests(args['url'], args['url_count'])
    logging.info('END')

if __name__ == '__main__':
    main()
