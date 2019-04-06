Table of Contents
=================

   * [Stage 3: Python 3.7](#stage-3-python-37)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 3: Python 3.7

## Check installed modules

- Command: 

```
cat requirements.txt
```

- Sample output:

```
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
```

## Fetch URLs

- Command:

```
./docker-exec.sh test_grequests_python37_3 \
  /usr/local/bin/python /app/test_grequests_v2.py \
  --url https://https_server:8081/delay/1 --url-count 10
```

- Sample output:

```
================================
--------------------------------
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
--------------------------------
+ docker exec -it test_grequests_python37_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 06:52:59,775 - python37_3 - START
2019-03-24 06:53:09,901 - python37_3 - len(all_page_ids) = 10
2019-03-24 06:53:09,901 - python37_3 - len(valid_page_ids) = 10
2019-03-24 06:53:09,901 - python37_3 - len(invalid_page_ids) = 0
2019-03-24 06:53:09,902 - python37_3 - total_time=0:00:10.138915
2019-03-24 06:53:09,903 - python37_3 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python37_3 \
  /usr/local/bin/python /app/test_grequests_v2.py \
  --log-level DEBUG \
  --url https://https_server:8081/delay/1 --url-count 10
```

- Sample output:

```
================================
--------------------------------
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
--------------------------------
+ docker exec -it test_grequests_python37_3 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 06:53:33,323 - python37_3 - START
2019-03-24 06:53:33,327 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,332 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,333 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,334 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,335 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,336 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,338 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,339 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,340 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:33,341 - python37_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:53:34,360 - python37_3 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 309
2019-03-24 06:53:35,381 - python37_3 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 309
2019-03-24 06:53:36,388 - python37_3 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 309
2019-03-24 06:53:37,391 - python37_3 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 309
2019-03-24 06:53:38,399 - python37_3 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 309
2019-03-24 06:53:39,404 - python37_3 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 309
2019-03-24 06:53:40,411 - python37_3 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 309
2019-03-24 06:53:41,416 - python37_3 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 309
2019-03-24 06:53:42,422 - python37_3 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 309
2019-03-24 06:53:43,426 - python37_3 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 309
2019-03-24 06:53:43,427 - python37_3 - len(all_page_ids) = 10
2019-03-24 06:53:43,427 - python37_3 - len(valid_page_ids) = 10
2019-03-24 06:53:43,427 - python37_3 - len(invalid_page_ids) = 0
2019-03-24 06:53:43,429 - python37_3 - total_time=0:00:10.111593
2019-03-24 06:53:43,429 - python37_3 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python37_3 \
   /usr/local/bin/python /app/test_grequests_v2.py \
   --url https://https_server:8081/delay/1 --url-count 10 \
   --profile-code --profile-stats-count 20
```

- Sample output:

```
================================
--------------------------------
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
--------------------------------
+ docker exec -it test_grequests_python37_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 06:54:07,858 - python37_3 - START
2019-03-24 06:54:18,413 - python37_3 - len(all_page_ids) = 10
2019-03-24 06:54:18,413 - python37_3 - len(valid_page_ids) = 10
2019-03-24 06:54:18,414 - python37_3 - len(invalid_page_ids) = 0
         30276 function calls (29951 primitive calls) in 10.552 seconds

   Ordered by: cumulative time
   List reduced from 717 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.554   10.554 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000   10.553   10.553 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000   10.553   10.553 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000   10.522   10.522 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000   10.519   10.519 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000   10.511   10.511 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000   10.509   10.509 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       10    0.000    0.000   10.081    1.008 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
       10    0.001    0.000   10.080    1.008 /usr/local/lib/python3.7/http/client.py:289(begin)
       10    0.001    0.000   10.028    1.003 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       70    0.001    0.000   10.028    0.143 {method 'readline' of '_io.BufferedReader' objects}
       10    0.000    0.000   10.027    1.003 /usr/local/lib/python3.7/socket.py:575(readinto)
    20/10    0.002    0.000   10.026    1.003 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)
       10    0.000    0.000   10.019    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       10    0.001    0.000   10.019    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       11    0.000    0.000   10.018    0.911 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
       10    0.000    0.000   10.017    1.002 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
       11   10.017    0.911   10.017    0.911 {method 'poll' of 'select.poll' objects}
     10/1    0.001    0.000    9.497    9.497 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.001    0.000    9.497    9.497 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)



2019-03-24 06:54:18,425 - python37_3 - total_time=0:00:10.574559
2019-03-24 06:54:18,426 - python37_3 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python37_3 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python37_3 \
/usr/local/bin/python /app/test_grequests_v2.py \
--url https://https_server:8081/delay/1 --url-count 10 \
--socket-class
```

- Sample output:

```
================================
--------------------------------
urllib3==1.24.1
requests==2.21.0
gevent==1.4.0
grequests==0.3.0
pyopenssl==19.0.0
gevent-openssl==1.2
--------------------------------
+ docker exec -it test_grequests_python37_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 06:55:52,675 - python37_3 - START
2019-03-24 06:56:02,755 - python37_3 - len(all_page_ids) = 10
2019-03-24 06:56:02,755 - python37_3 - len(valid_page_ids) = 10
2019-03-24 06:56:02,755 - python37_3 - len(invalid_page_ids) = 0
2019-03-24 06:56:03,769 - python37_3 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```
