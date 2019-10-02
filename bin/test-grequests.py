import time
import grequests
import sys
import utils

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://localhost:8081/delay/1'
if sys.argv[1] == 'https':
    url = 'https://localhost:8082/delay/1'
url_count = 5

def test_grequests():
    pending_requests = []
    for i in range(url_count):
        pending_requests.append(
            grequests.get(url, params={'page': i}, verify=False)
        )
    all_responses = grequests.map(pending_requests)
    return all_responses


if __name__ == '__main__':
    logger = utils.setup_logging('DEBUG')
    logger.info("START")
    start_time = int(time.time())
    test_grequests()
    end_time = int(time.time())
    logger.info("END")
    logger.info("time = {} seconds".format(end_time - start_time))
