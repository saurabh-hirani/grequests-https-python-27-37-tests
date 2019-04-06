Table of Contents
=================

   * [Stage 3: Python 2.7](#stage-3-python-27)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 3: Python 2.7

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
./docker-exec.sh test_grequests_python27_3 \
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
+ docker exec -it test_grequests_python27_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 06:40:09,187 - python27_3 - START
2019-03-24 06:40:10,256 - python27_3 - len(all_page_ids) = 10
2019-03-24 06:40:10,257 - python27_3 - len(valid_page_ids) = 10
2019-03-24 06:40:10,257 - python27_3 - len(invalid_page_ids) = 0
2019-03-24 06:40:10,260 - python27_3 - total_time=0:00:01.078878
2019-03-24 06:40:10,260 - python27_3 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python27_3 \
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
+ docker exec -it test_grequests_python27_3 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 06:40:40,079 - python27_3 - START
2019-03-24 06:40:40,087 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,093 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,096 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,099 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,102 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,105 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,107 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,109 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,111 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:40,113 - python27_3 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 06:40:41,137 - python27_3 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 06:40:41,140 - python27_3 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 06:40:41,141 - python27_3 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 06:40:41,142 - python27_3 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 06:40:41,143 - python27_3 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 06:40:41,144 - python27_3 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 06:40:41,145 - python27_3 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 06:40:41,146 - python27_3 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 06:40:41,147 - python27_3 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 06:40:41,147 - python27_3 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 06:40:41,148 - python27_3 - len(all_page_ids) = 10
2019-03-24 06:40:41,148 - python27_3 - len(valid_page_ids) = 10
2019-03-24 06:40:41,149 - python27_3 - len(invalid_page_ids) = 0
2019-03-24 06:40:41,150 - python27_3 - total_time=0:00:01.077381
2019-03-24 06:40:41,150 - python27_3 - END
+ set +x
================================
```

## Profile code

- Command:

```
./docker-exec.sh test_grequests_python27_3 \
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
+ docker exec -it test_grequests_python27_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 06:41:32,826 - python27_3 - START
2019-03-24 06:41:34,239 - python27_3 - len(all_page_ids) = 10
2019-03-24 06:41:34,239 - python27_3 - len(valid_page_ids) = 10
2019-03-24 06:41:34,239 - python27_3 - len(invalid_page_ids) = 0
         23615 function calls (23164 primitive calls) in 1.409 seconds

   Ordered by: cumulative time
   List reduced from 535 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.410    1.410 /usr/local/lib/python2.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000    1.409    1.409 /usr/local/lib/python2.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.409    1.409 /usr/local/lib/python2.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000    1.380    1.380 /usr/local/lib/python2.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.378    1.378 /usr/local/lib/python2.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.367    1.367 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.364    1.364 /usr/local/lib/python2.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.364    1.364 /usr/local/lib/python2.7/httplib.py:1084(getresponse)
     10/1    0.001    0.000    1.364    1.364 /usr/local/lib/python2.7/httplib.py:431(begin)
     70/7    0.006    0.000    1.362    0.195 /usr/local/lib/python2.7/socket.py:410(readline)
     10/1    0.001    0.000    1.362    1.362 /usr/local/lib/python2.7/httplib.py:392(_read_status)
     10/1    0.000    0.000    1.362    1.362 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:271(recv)
     10/1    0.000    0.000    1.343    1.343 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:61(recv)
     30/1    0.984    0.033    1.343    1.343 /usr/local/lib/python2.7/site-packages/gevent_openssl/SSL.py:24(__iowait)
       10    0.002    0.000    0.099    0.010 /usr/local/lib/python2.7/site-packages/requests/sessions.py:426(prepare_request)
     10/1    0.001    0.000    0.075    0.075 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:382(_resolve_addr)
     20/1    0.001    0.000    0.075    0.075 /usr/local/lib/python2.7/site-packages/gevent/_socketcommon.py:179(getaddrinfo)
       10    0.001    0.000    0.051    0.005 /usr/local/lib/python2.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
       10    0.000    0.000    0.047    0.005 /usr/local/lib/python2.7/site-packages/requests/adapters.py:292(get_connection)
       10    0.000    0.000    0.045    0.004 /usr/local/lib/python2.7/site-packages/urllib3/contrib/pyopenssl.py:418(set_ciphers)



2019-03-24 06:41:34,248 - python27_3 - total_time=0:00:01.430398
2019-03-24 06:41:34,248 - python27_3 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python27_3 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python27_3 \
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
+ docker exec -it test_grequests_python27_3 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 06:43:11,637 - python27_3 - START
2019-03-24 06:43:12,682 - python27_3 - len(all_page_ids) = 10
2019-03-24 06:43:12,682 - python27_3 - len(valid_page_ids) = 10
2019-03-24 06:43:12,682 - python27_3 - len(invalid_page_ids) = 0
2019-03-24 06:43:13,696 - python27_3 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```