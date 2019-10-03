import gevent.monkey
gevent.monkey.patch_all()

import urllib3
import utils
import sys
import gevent
import requests
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch(url, i):
    response = requests.get(url, params={'page': i}, verify=False)
    result = response.json()
    return result


def test_gevent_requests(url, url_count):
    threads = []
    for i in range(url_count):
        threads.append(gevent.spawn(fetch, url, i))
    gevent.joinall(threads)


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
    test_gevent_requests(url, url_count)
    end_time = int(round(time.time() * 1000))
    logger.info("END")
    logger.info("time = {} seconds".format((end_time - start_time) / 1000.0))

