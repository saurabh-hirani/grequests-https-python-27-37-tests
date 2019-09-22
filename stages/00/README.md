
Table of Contents
=================

   * [Disclaimer](#disclaimer)
   * [Pre-requisites](#pre-requisites)
   * [Stage 0: Python 2.7](#stage-0-python-27)
      * [Fetch URLs with profiling](#fetch-urls-with-profiling)
   * [Stage 0: Python 3.7](#stage-0-python-37)
      * [Fetch URLs with profiling](#fetch-urls-with-profiling-1)

# Disclaimer

This stage does not use virtualenv and depicts how my system behaved when I ran
the same code against Python2 and Python3. Running the below commands on your system
against Python 2 or 3 may give you different response times. We will figure out why
that happens in stages - [01](../01) through [04](../04) as they are contained
virtualenv setups.

# Pre-requisites

- Run a local https server

```
./server/generate_https_keys.sh
./server/run_https_server.sh
```

# Stage 0: Python 2.7

## Fetch URLs with profiling

- Command:

```
python2 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 10
```

- Sample output:

```
len(all_page_ids) = 10
len(valid_page_ids) = 10
len(invalid_page_ids) = 0
         28552 function calls (28044 primitive calls) in 10.170 seconds

   Ordered by: cumulative time
   List reduced from 660 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.170   10.170 /usr/local/lib/python2.7/site-packages/gevent/hub.py:566(run)
      2/1    0.000    0.000   10.170   10.170 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000   10.170   10.170 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.000    0.000   10.170   10.170 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.000    0.000   10.167   10.167 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.000    0.000   10.166   10.166 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.000    0.000   10.166   10.166 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.000    0.000   10.166   10.166 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       30    0.000    0.000   10.093    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       30    0.000    0.000   10.093    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       31    0.000    0.000   10.092    0.326 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:45(_retry_on_intr)
       30    0.000    0.000   10.092    0.336 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:99(do_poll)
       31   10.092    0.326   10.092    0.326 {built-in method poll}
       10    0.000    0.000   10.022    1.002 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:1084(getresponse)
       10    0.000    0.000   10.022    1.002 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:431(begin)
       70    0.000    0.000   10.021    0.143 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py:410(readline)
       10    0.000    0.000   10.020    1.002 /usr/local/Cellar/python@2/2.7.15_3/Frameworks/Python.framework/Versions/2.7/lib/python2.7/httplib.py:392(_read_status)
    20/10    0.000    0.000   10.020    1.002 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     10/1    0.000    0.000    9.165    9.165 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.000    0.000    9.162    9.162 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:299(connect)



total_time=0:00:10.283865
```

# Stage 0: Python 3.7

## Fetch URLs with profiling

- Command:

```
python3 ./bin/test_grequests_v1.py --url https://localhost:8082/delay/1 --url-count 10
```

- Sample output:

```
len(all_page_ids) = 10
len(valid_page_ids) = 10
len(invalid_page_ids) = 0
         62872 function calls (62309 primitive calls) in 1.157 seconds

   Ordered by: cumulative time
   List reduced from 690 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.157    1.157 /usr/local/lib/python3.7/site-packages/gevent/hub.py:566(run)
      2/1    0.000    0.000    1.157    1.157 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.157    1.157 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.000    0.000    1.157    1.157 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.000    0.000    1.155    1.155 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.000    0.000    1.155    1.155 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.000    0.000    1.155    1.155 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.000    0.000    1.155    1.155 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.154    1.154 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py:1277(getresponse)
     10/1    0.000    0.000    1.151    1.151 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py:289(begin)
     10/1    0.000    0.000    1.150    1.150 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/http/client.py:256(_read_status)
     70/7    0.000    0.000    1.143    0.163 {method 'readline' of '_io.BufferedReader' objects}
     10/1    0.000    0.000    1.143    1.143 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/socket.py:575(readinto)
     10/1    0.000    0.000    1.142    1.142 /usr/local/lib/python3.7/site-packages/gevent/_ssl3.py:494(recv_into)
     10/1    0.992    0.099    1.142    1.142 /usr/local/lib/python3.7/site-packages/gevent/_ssl3.py:312(read)
       10    0.000    0.000    0.084    0.008 /usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7/ssl.py:474(load_default_certs)
       10    0.084    0.008    0.084    0.008 {method 'set_default_verify_paths' of '_ssl._SSLContext' objects}
     10/1    0.000    0.000    0.029    0.029 /usr/local/lib/python3.7/site-packages/gevent/_socketcommon.py:382(_resolve_addr)
     20/1    0.000    0.000    0.029    0.029 /usr/local/lib/python3.7/site-packages/gevent/_socketcommon.py:207(getaddrinfo)
     20/1    0.000    0.000    0.028    0.028 /usr/local/lib/python3.7/site-packages/gevent/resolver/thread.py:64(getaddrinfo)



total_time=0:00:01.215995
```
