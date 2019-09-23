Table of Contents
=================

   * [Stage 2: Python 2.7](#stage-2-python-27)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 2: Python 2.7

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
```

## Fetch URLs

- Command:

```
./docker-exec.sh test_grequests_python27_2 \
  /usr/local/bin/python /app/test_grequests_v1.py \
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
--------------------------------
+ docker exec -it test_grequests_python27_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 04:58:52,092 - python27_2 - START
2019-03-24 04:59:02,198 - python27_2 - len(all_page_ids) = 10
2019-03-24 04:59:02,198 - python27_2 - len(valid_page_ids) = 10
2019-03-24 04:59:02,198 - python27_2 - len(invalid_page_ids) = 0
2019-03-24 04:59:02,200 - python27_2 - total_time=0:00:10.111690
2019-03-24 04:59:02,200 - python27_2 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python27_2 \
  /usr/local/bin/python /app/test_grequests_v1.py \
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
--------------------------------
+ docker exec -it test_grequests_python27_2 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 05:12:24,440 - python27_2 - START
2019-03-24 05:12:24,445 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,449 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,452 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,453 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,455 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,457 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,458 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,460 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,462 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:24,464 - python27_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:12:25,478 - python27_2 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 05:12:26,491 - python27_2 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 05:12:27,501 - python27_2 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 05:12:28,511 - python27_2 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 05:12:29,520 - python27_2 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 05:12:30,530 - python27_2 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 05:12:31,541 - python27_2 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 05:12:32,547 - python27_2 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 05:12:33,562 - python27_2 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 05:12:34,573 - python27_2 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 05:12:34,576 - python27_2 - len(all_page_ids) = 10
2019-03-24 05:12:34,576 - python27_2 - len(valid_page_ids) = 10
2019-03-24 05:12:34,576 - python27_2 - len(invalid_page_ids) = 0
2019-03-24 05:12:34,577 - python27_2 - total_time=0:00:10.141192
2019-03-24 05:12:34,577 - python27_2 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python27_2 \
   /usr/local/bin/python /app/test_grequests_v1.py \
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
--------------------------------
+ docker exec -it test_grequests_python27_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 05:00:09,258 - python27_2 - START
2019-03-24 05:00:19,788 - python27_2 - len(all_page_ids) = 10
2019-03-24 05:00:19,789 - python27_2 - len(valid_page_ids) = 10
2019-03-24 05:00:19,789 - python27_2 - len(invalid_page_ids) = 0
         23635 function calls (23338 primitive calls) in 10.527 seconds

   Ordered by: cumulative time
   List reduced from 535 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.527   10.527 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000   10.526   10.526 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000   10.526   10.526 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.001    0.000   10.501   10.501 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000   10.499   10.499 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000   10.490   10.490 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000   10.488   10.488 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       10    0.000    0.000   10.067    1.007 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
       10    0.001    0.000   10.065    1.007 /usr/local/lib/python2.7/httplib.py:431(begin)
       30    0.001    0.000   10.050    0.335 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       30    0.004    0.000   10.049    0.335 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       31    0.001    0.000   10.043    0.324 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:45(_retry_on_intr)
       70    0.007    0.000   10.042    0.143 /usr/local/lib/python2.7/socket.py:410(readline)
       30    0.001    0.000   10.042    0.335 /usr/local/lib/python2.7/site-packages/urllib3/util/wait.py:99(do_poll)
       31   10.041    0.324   10.041    0.324 {built-in method poll}
       10    0.001    0.000   10.033    1.003 /usr/local/lib/python2.7/httplib.py:392(_read_status)
    20/10    0.002    0.000   10.030    1.003 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     10/1    0.001    0.000    9.478    9.478 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.002    0.000    9.478    9.478 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:299(connect)
     10/1    0.001    0.000    9.465    9.465 /usr/local/lib/python2.7/site-packages/urllib3/connection.py:145(_new_conn)



2019-03-24 05:00:19,799 - python27_2 - total_time=0:00:10.547536
2019-03-24 05:00:19,799 - python27_2 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python27_2 \
 /usr/local/bin/python /app/test_grequests_v1.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python27_2 \
/usr/local/bin/python /app/test_grequests_v1.py \
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
--------------------------------
+ docker exec -it test_grequests_python27_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 05:00:39,453 - python27_2 - START
2019-03-24 05:00:49,576 - python27_2 - len(all_page_ids) = 10
2019-03-24 05:00:49,576 - python27_2 - len(valid_page_ids) = 10
2019-03-24 05:00:49,576 - python27_2 - len(invalid_page_ids) = 0
2019-03-24 05:00:50,588 - python27_2 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```
