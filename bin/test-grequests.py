import time
import grequests
import sys
import utils

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_grequests(url, url_count):
    pending_requests = []
    for i in range(url_count):
        pending_requests.append(
            grequests.get(url, params={'page': i}, verify=False)
        )
    all_responses = grequests.map(pending_requests)
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
    logger.info("START")
    start_time = int(round(time.time() * 1000))
    test_grequests(url, url_count)
    end_time = int(round(time.time() * 1000))
    logger.info("END")
    logger.info("time = {} seconds".format((end_time - start_time) / 1000.0))
