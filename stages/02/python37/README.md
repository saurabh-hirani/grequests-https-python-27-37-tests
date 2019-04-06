Table of Contents
=================

   * [Stage 2: Python 3.7](#stage-2-python-37)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 2: Python 3.7

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
./docker-exec.sh test_grequests_python37_2 \
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
--------------------------------
+ docker exec -it test_grequests_python37_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 05:15:04,212 - python37_2 - START
2019-03-24 05:15:14,313 - python37_2 - len(all_page_ids) = 10
2019-03-24 05:15:14,314 - python37_2 - len(valid_page_ids) = 10
2019-03-24 05:15:14,314 - python37_2 - len(invalid_page_ids) = 0
2019-03-24 05:15:14,318 - python37_2 - total_time=0:00:10.111726
2019-03-24 05:15:14,319 - python37_2 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python37_2 \
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
--------------------------------
+ docker exec -it test_grequests_python37_2 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 05:15:43,658 - python37_2 - START
2019-03-24 05:15:43,666 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,671 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,672 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,673 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,674 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,675 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,678 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,680 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,681 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:43,682 - python37_2 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:15:44,694 - python37_2 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 309
2019-03-24 05:15:45,710 - python37_2 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 309
2019-03-24 05:15:46,726 - python37_2 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 309
2019-03-24 05:15:47,737 - python37_2 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 309
2019-03-24 05:15:48,752 - python37_2 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 309
2019-03-24 05:15:49,764 - python37_2 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 309
2019-03-24 05:15:50,775 - python37_2 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 309
2019-03-24 05:15:51,785 - python37_2 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 309
2019-03-24 05:15:52,797 - python37_2 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 309
2019-03-24 05:15:53,809 - python37_2 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 309
2019-03-24 05:15:53,810 - python37_2 - len(all_page_ids) = 10
2019-03-24 05:15:53,810 - python37_2 - len(valid_page_ids) = 10
2019-03-24 05:15:53,810 - python37_2 - len(invalid_page_ids) = 0
2019-03-24 05:15:53,812 - python37_2 - total_time=0:00:10.159028
2019-03-24 05:15:53,812 - python37_2 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python37_2 \
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
--------------------------------
+ docker exec -it test_grequests_python37_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 05:16:54,325 - python37_2 - START
2019-03-24 05:17:04,915 - python37_2 - len(all_page_ids) = 10
2019-03-24 05:17:04,915 - python37_2 - len(valid_page_ids) = 10
2019-03-24 05:17:04,915 - python37_2 - len(invalid_page_ids) = 0
         30166 function calls (29881 primitive calls) in 10.586 seconds

   Ordered by: cumulative time
   List reduced from 711 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   10.588   10.588 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000   10.587   10.587 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000   10.587   10.587 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.001    0.000   10.562   10.562 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000   10.559   10.559 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000   10.552   10.552 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000   10.549   10.549 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
       10    0.000    0.000   10.101    1.010 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
       10    0.001    0.000   10.099    1.010 /usr/local/lib/python3.7/http/client.py:289(begin)
       30    0.001    0.000   10.053    0.335 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:139(wait_for_read)
       30    0.002    0.000   10.053    0.335 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:87(poll_wait_for_socket)
       31    0.001    0.000   10.049    0.324 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:41(_retry_on_intr)
       30    0.001    0.000   10.049    0.335 /usr/local/lib/python3.7/site-packages/urllib3/util/wait.py:99(do_poll)
       31   10.048    0.324   10.048    0.324 {method 'poll' of 'select.poll' objects}
       10    0.001    0.000   10.041    1.004 /usr/local/lib/python3.7/http/client.py:256(_read_status)
       70    0.001    0.000   10.041    0.143 {method 'readline' of '_io.BufferedReader' objects}
       10    0.000    0.000   10.039    1.004 /usr/local/lib/python3.7/socket.py:575(readinto)
    20/10    0.002    0.000   10.039    1.004 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)
     10/1    0.001    0.000    9.536    9.536 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:831(_validate_conn)
     10/1    0.001    0.000    9.536    9.536 /usr/local/lib/python3.7/site-packages/urllib3/connection.py:299(connect)



2019-03-24 05:17:04,928 - python37_2 - total_time=0:00:10.607487
2019-03-24 05:17:04,928 - python37_2 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python37_2 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python37_2 \
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
--------------------------------
+ docker exec -it test_grequests_python37_2 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 05:19:06,095 - python37_2 - START



2019-03-24 05:19:16,182 - python37_2 - len(all_page_ids) = 10
2019-03-24 05:19:16,183 - python37_2 - len(valid_page_ids) = 10
2019-03-24 05:19:16,183 - python37_2 - len(invalid_page_ids) = 0
2019-03-24 05:19:17,197 - python37_2 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```