import gevent.monkey
# gevent.monkey.patch_all(select=False)
gevent.monkey.patch_all()

import requests
import time
import gevent
import sys
import utils
import urllib3
import cProfile
import pstats
from datetime import datetime


try:
    # python 2.7
    from StringIO import StringIO
except ImportError:
    # python 3.6
    from io import StringIO

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
pr = cProfile.Profile()

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

def format_profiler_stats(stats_count=50):
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



def fetch(url, i):
    response = requests.get(url, params={'page': i}, verify=False)
    result = response.json()
    return result


def test_gevent_requests(url, url_count):
    threads = []
    pr.enable()
    for i in range(url_count):
        threads.append(gevent.spawn(fetch, url, i))
    gevent.joinall(threads)
    pr.disable()


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
    # setup_tracing()
    start_time = int(round(time.time() * 1000))
    test_gevent_requests(url, url_count)
    end_time = int(round(time.time() * 1000))
    logger.info("END")
    print("")
    logger.info("total_time = {} seconds".format(
        (end_time - start_time) / 1000.0))
    # print(format_profiler_stats().getvalue())
