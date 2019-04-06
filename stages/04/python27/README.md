Table of Contents
=================

   * [Stage 4: Python 2.7](#stage-4-python-27)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 4: Python 2.7

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
./docker-exec.sh test_grequests_python27_4 \
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
+ docker exec -it test_grequests_python27_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:08:10,814 - python27_4 - START
2019-03-24 07:08:11,861 - python27_4 - len(all_page_ids) = 10
2019-03-24 07:08:11,861 - python27_4 - len(valid_page_ids) = 10
2019-03-24 07:08:11,861 - python27_4 - len(invalid_page_ids) = 0
2019-03-24 07:08:11,863 - python27_4 - total_time=0:00:01.054416
2019-03-24 07:08:11,864 - python27_4 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python27_4 \
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
+ docker exec -it test_grequests_python27_4 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:08:31,500 - python27_4 - START
2019-03-24 07:08:31,506 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,510 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,511 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,513 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,514 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,516 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,517 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,518 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,520 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:31,521 - python27_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:08:32,532 - python27_4 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 07:08:32,535 - python27_4 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 07:08:32,541 - python27_4 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 07:08:32,542 - python27_4 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 07:08:32,544 - python27_4 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 07:08:32,545 - python27_4 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 07:08:32,546 - python27_4 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 07:08:32,547 - python27_4 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 07:08:32,547 - python27_4 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 07:08:32,548 - python27_4 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 07:08:32,549 - python27_4 - len(all_page_ids) = 10
2019-03-24 07:08:32,549 - python27_4 - len(valid_page_ids) = 10
2019-03-24 07:08:32,549 - python27_4 - len(invalid_page_ids) = 0
2019-03-24 07:08:32,550 - python27_4 - total_time=0:00:01.054303
2019-03-24 07:08:32,550 - python27_4 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python27_4 \
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
+ docker exec -it test_grequests_python27_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 07:08:50,207 - python27_4 - START
2019-03-24 07:08:51,641 - python27_4 - len(all_page_ids) = 10
2019-03-24 07:08:51,641 - python27_4 - len(valid_page_ids) = 10
2019-03-24 07:08:51,641 - python27_4 - len(invalid_page_ids) = 0
         23616 function calls (23165 primitive calls) in 1.431 seconds

   Ordered by: cumulative time
   List reduced from 535 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.432    1.432 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.431    1.431 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.431    1.431 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000    1.408    1.408 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.406    1.406 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.399    1.399 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.396    1.396 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.396    1.396 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
     10/1    0.001    0.000    1.396    1.396 /usr/local/lib/python2.7/httplib.py:431(begin)
     70/7    0.006    0.000    1.394    0.199 /usr/local/lib/python2.7/socket.py:410(readline)
     10/1    0.001    0.000    1.393    1.393 /usr/local/lib/python2.7/httplib.py:392(_read_status)
     10/1    0.000    0.000    1.393    1.393 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     10/1    0.000    0.000    1.379    1.379 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)
     30/1    0.983    0.033    1.379    1.379 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)
       10    0.001    0.000    0.098    0.010 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
     10/1    0.001    0.000    0.068    0.068 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:382(_resolve_addr)
     20/1    0.001    0.000    0.068    0.068 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:179(getaddrinfo)
     20/1    0.001    0.000    0.068    0.068 /usr/local/lib/python2.7/site-packages/gevent/resolver/thread.py:64(getaddrinfo)
     20/1    0.003    0.000    0.067    0.067 /usr/local/lib/python2.7/site-packages/gevent/pool.py:138(apply)
       10    0.001    0.000    0.064    0.006 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)



2019-03-24 07:08:51,651 - python27_4 - total_time=0:00:01.449395
2019-03-24 07:08:51,651 - python27_4 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python27_4 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python27_4 \
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
+ docker exec -it test_grequests_python27_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 07:09:37,513 - python27_4 - START
2019-03-24 07:09:38,570 - python27_4 - len(all_page_ids) = 10
2019-03-24 07:09:38,570 - python27_4 - len(valid_page_ids) = 10
2019-03-24 07:09:38,570 - python27_4 - len(invalid_page_ids) = 0
2019-03-24 07:09:39,583 - python27_4 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```