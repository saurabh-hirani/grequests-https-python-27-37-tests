import time
import requests
import sys
import utils

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_requests(url, url_count):
    all_responses = []
    for i in range(url_count):
        response = requests.get(url, params={'page': i}, verify=False)
        all_responses.append(response)
    return all_responses


if __name__ == '__main__':
    protocol = port = url_count = None

    protocol = sys.argv[1]
    if protocol == 'https':
        port = 8082
    else:
        port = 8081
    url = '{}://localhost:{}/delay/1'.format(protocol, port)

    url_count = int(sys.argv[2])

    logger = utils.setup_logging('DEBUG')
    print("")
    logger.info("START")
    start_time = int(round(time.time() * 1000))
    test_requests(url, url_count)
    end_time = int(round(time.time() * 1000))
    logger.info("END")
    print("")
    logger.info("total_time = {} seconds".format(
        (end_time - start_time) / 1000.0))
    print("")
