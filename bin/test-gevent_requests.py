import gevent.monkey
gevent.monkey.patch_all()

import time
import requests
import gevent
import sys
import utils

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fetch(i):
    url = 'http://localhost:8081/delay/1'
    if sys.argv[1] == 'https':
        url = 'https://localhost:8082/delay/1'
    response = requests.get(url, params={'page': i}, verify=False)
    result = response.json()
    return result

def gevent_requests():
    threads = []
    for i in range(0, 5):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

if __name__ == '__main__':
    logger = utils.setup_logging('DEBUG')
    logger.info("START")
    start_time = int(time.time())
    gevent_requests()
    end_time = int(time.time())
    logger.info("END")
    logger.info("time = {} seconds".format(end_time - start_time))
