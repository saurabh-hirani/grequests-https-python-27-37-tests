Table of Contents
=================

   * [Stage 1: Python 2.7](#stage-1-python-27)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)


# Stage 1: Python 2.7

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
```

## Fetch URLs

- Command:

```
./docker-exec.sh test_grequests_python27_1 \
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
--------------------------------
+ docker exec -it test_grequests_python27_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-17 15:30:54,977 - python27_1 - START
2019-03-17 15:30:56,015 - python27_1 - len(all_page_ids) = 10
2019-03-17 15:30:56,016 - python27_1 - len(valid_page_ids) = 10
2019-03-17 15:30:56,016 - python27_1 - len(invalid_page_ids) = 0
2019-03-17 15:30:56,019 - python27_1 - total_time=0:00:01.048203
2019-03-17 15:30:56,020 - python27_1 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python27_1 \
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
--------------------------------
+ docker exec -it test_grequests_python27_1 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 05:05:40,334 - python27_1 - START
2019-03-24 05:05:40,341 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,345 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,347 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,349 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,351 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,353 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,354 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,356 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,357 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:40,358 - python27_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:05:41,372 - python27_1 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 05:05:41,373 - python27_1 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 05:05:41,377 - python27_1 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 05:05:41,381 - python27_1 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 05:05:41,382 - python27_1 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 05:05:41,382 - python27_1 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 05:05:41,383 - python27_1 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 05:05:41,384 - python27_1 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 05:05:41,385 - python27_1 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 05:05:41,385 - python27_1 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 05:05:41,386 - python27_1 - len(all_page_ids) = 10
2019-03-24 05:05:41,386 - python27_1 - len(valid_page_ids) = 10
2019-03-24 05:05:41,386 - python27_1 - len(invalid_page_ids) = 0
2019-03-24 05:05:41,388 - python27_1 - total_time=0:00:01.059315
2019-03-24 05:05:41,389 - python27_1 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python27_1 \
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
--------------------------------
+ docker exec -it test_grequests_python27_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-20 11:01:32,051 - python27_1 - START
2019-03-20 11:01:33,382 - python27_1 - len(all_page_ids) = 10
2019-03-20 11:01:33,382 - python27_1 - len(valid_page_ids) = 10
2019-03-20 11:01:33,382 - python27_1 - len(invalid_page_ids) = 0
         19250 function calls (18819 primitive calls) in 1.328 seconds

   Ordered by: cumulative time
   List reduced from 474 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.329    1.329 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.328    1.328 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.000    0.000    1.328    1.328 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.001    0.000    1.308    1.308 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.306    1.306 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.299    1.299 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.002    0.000    1.297    1.297 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.001    0.000    1.297    1.297 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
     10/1    0.001    0.000    1.297    1.297 /usr/local/lib/python2.7/httplib.py:431(begin)
     70/7    0.006    0.000    1.295    0.185 /usr/local/lib/python2.7/socket.py:410(readline)
     10/1    0.001    0.000    1.294    1.294 /usr/local/lib/python2.7/httplib.py:392(_read_status)
     10/1    0.001    0.000    1.294    1.294 /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:448(recv)
     10/1    0.983    0.098    1.281    1.281 /usr/local/lib/python2.7/site-packages/gevent/_sslgte279.py:298(read)
       10    0.001    0.000    0.087    0.009 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
       10    0.000    0.000    0.042    0.004 /usr/local/lib/python2.7/site-packages/requests/adapters.py:292(get_connection)
       10    0.001    0.000    0.040    0.004 /usr/local/lib/python2.7/site-packages/requests/models.py:307(prepare)
       10    0.000    0.000    0.037    0.004 /usr/local/lib/python2.7/site-packages/urllib3/poolmanager.py:267(connection_from_url)
       70    0.003    0.000    0.037    0.001 /usr/local/lib/python2.7/site-packages/requests/sessions.py:49(merge_setting)
     10/1    0.001    0.000    0.035    0.035 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:382(_resolve_addr)
     20/1    0.001    0.000    0.035    0.035 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:179(getaddrinfo)



2019-03-20 11:01:33,391 - python27_1 - total_time=0:00:01.344471
2019-03-20 11:01:33,391 - python27_1 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python27_1 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python27_1 \
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
--------------------------------
+ docker exec -it test_grequests_python27_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-20 11:10:13,668 - python27_1 - START
2019-03-20 11:10:14,739 - python27_1 - len(all_page_ids) = 10
2019-03-20 11:10:14,739 - python27_1 - len(valid_page_ids) = 10
2019-03-20 11:10:14,739 - python27_1 - len(invalid_page_ids) = 0
2019-03-20 11:10:15,750 - python27_1 - socket_class = <class 'gevent._sslgte279.SSLSocket'>
+ set +x
================================
```