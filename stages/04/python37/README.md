Table of Contents
=================

   * [Stage 4: Python 3.7](#stage-4-python-37)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs before patching](#fetch-urls-before-patching)
      * [Fetch URLs with DEBUG logs before patching](#fetch-urls-with-debug-logs-before-patching)
      * [Patch gevent_openssl](#patch-gevent_openssl)
      * [Fetch URLs after patching](#fetch-urls-after-patching)
      * [Fetch URLs with DEBUG logs after patching](#fetch-urls-with-debug-logs-after-patching)
      * [Toggle patch to verify](#toggle-patch-to-verify)
      * [Profile code after patching](#profile-code-after-patching)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 4: Python 3.7

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

## Fetch URLs before patching

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:30:17,574 - python37_4 - START
2019-03-24 07:30:27,618 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:30:27,618 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:30:27,618 - python37_4 - len(invalid_page_ids) = 0
2019-03-24 07:30:27,620 - python37_4 - total_time=0:00:10.052055
2019-03-24 07:30:27,620 - python37_4 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs before patching

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:31:47,838 - python37_4 - START
2019-03-24 07:31:47,846 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,854 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,856 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,858 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,861 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,862 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,867 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,869 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,873 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:47,875 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:31:48,870 - python37_4 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 07:31:49,878 - python37_4 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 07:31:50,880 - python37_4 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 07:31:51,887 - python37_4 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 07:31:52,894 - python37_4 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 07:31:53,899 - python37_4 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 07:31:54,906 - python37_4 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 07:31:55,914 - python37_4 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 07:31:56,916 - python37_4 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 07:31:57,922 - python37_4 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 07:31:57,923 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:31:57,923 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:31:57,923 - python37_4 - len(invalid_page_ids) = 0
2019-03-24 07:31:57,925 - python37_4 - total_time=0:00:10.095101
2019-03-24 07:31:57,925 - python37_4 - END
+ set +x
================================
```

## Patch gevent_openssl

- Command:

```
./docker-exec-patch-action.sh test_grequests_python37_4 apply
```

- Sample output:

```
+ docker exec -it test_grequests_python37_4 /bin/bash /patches/apply_patch.sh
patching file /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py
+ set +x
```

## Fetch URLs after patching

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:35:15,051 - python37_4 - START
2019-03-24 07:35:16,110 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:35:16,110 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:35:16,110 - python37_4 - len(invalid_page_ids) = 0
2019-03-24 07:35:16,111 - python37_4 - total_time=0:00:01.069503
2019-03-24 07:35:16,112 - python37_4 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs after patching

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 07:34:17,336 - python37_4 - START
2019-03-24 07:34:17,340 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,344 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,347 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,350 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,353 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,355 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,356 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,358 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,359 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:17,360 - python37_4 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 07:34:18,374 - python37_4 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 07:34:18,377 - python37_4 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 07:34:18,378 - python37_4 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 07:34:18,378 - python37_4 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 07:34:18,380 - python37_4 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 07:34:18,382 - python37_4 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 07:34:18,383 - python37_4 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 07:34:18,383 - python37_4 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 07:34:18,384 - python37_4 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 07:34:18,385 - python37_4 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 07:34:18,385 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:34:18,385 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:34:18,385 - python37_4 - len(invalid_page_ids) = 0
2019-03-24 07:34:18,388 - python37_4 - total_time=0:00:01.057208
2019-03-24 07:34:18,388 - python37_4 - END
+ set +x
================================
```

## Toggle patch to verify 

- Commands:

```
./docker-exec-patch-action.sh test_grequests_python37_4 apply
```

```
./docker-exec-patch-action.sh test_grequests_python37_4 revert
```

## Profile code after patching

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 07:37:01,504 - python37_4 - START
2019-03-24 07:37:03,012 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:37:03,012 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:37:03,012 - python37_4 - len(invalid_page_ids) = 0
         30140 function calls (29692 primitive calls) in 1.505 seconds

   Ordered by: cumulative time
   List reduced from 709 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.507    1.507 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.001    0.000    1.506    1.506 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.506    1.506 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.001    0.000    1.481    1.481 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.479    1.479 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.472    1.472 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.470    1.470 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.469    1.469 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
     10/1    0.001    0.000    1.469    1.469 /usr/local/lib/python3.7/http/client.py:289(begin)
     10/1    0.001    0.000    1.465    1.465 /usr/local/lib/python3.7/http/client.py:256(_read_status)
     70/7    0.001    0.000    1.465    0.209 {method 'readline' of '_io.BufferedReader' objects}
     10/1    0.001    0.000    1.465    1.465 /usr/local/lib/python3.7/socket.py:575(readinto)
     10/1    0.001    0.000    1.435    1.435 /usr/local/lib/python3.7/site-packages/urllib3/contrib/pyopenssl.py:292(recv_into)
     10/1    0.001    0.000    1.435    1.435 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:76(recv_into)
     30/1    0.980    0.033    1.435    1.435 /usr/local/lib/python3.7/site-packages/gevent_openssl/SSL.py:24(__iowait)
       10    0.001    0.000    0.092    0.009 /usr/local/lib/python3.7/site-packages/requests/sessions.py:426(prepare_request)
       10    0.001    0.000    0.080    0.008 /usr/local/lib/python3.7/site-packages/requests/sessions.py:690(merge_environment_settings)
       10    0.000    0.000    0.074    0.007 /usr/local/lib/python3.7/site-packages/requests/utils.py:755(get_environ_proxies)
       10    0.001    0.000    0.066    0.007 /usr/local/lib/python3.7/site-packages/urllib3/util/ssl_.py:229(create_urllib3_context)
      560    0.014    0.000    0.064    0.000 /usr/local/lib/python3.7/_collections_abc.py:742(__iter__)



2019-03-24 07:37:03,022 - python37_4 - total_time=0:00:01.524109
2019-03-24 07:37:03,022 - python37_4 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python37_4 \
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
+ docker exec -it test_grequests_python37_4 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 07:38:08,698 - python37_4 - START
2019-03-24 07:38:09,747 - python37_4 - len(all_page_ids) = 10
2019-03-24 07:38:09,748 - python37_4 - len(valid_page_ids) = 10
2019-03-24 07:38:09,748 - python37_4 - len(invalid_page_ids) = 0
2019-03-24 07:38:10,765 - python37_4 - socket_class = <class 'urllib3.contrib.pyopenssl.WrappedSocket'>
+ set +x
================================
```