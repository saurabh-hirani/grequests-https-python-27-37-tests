Table of Contents
=================

   * [Stage 1: Python 3.7](#stage-1-python-37)
      * [Check installed modules](#check-installed-modules)
      * [Fetch URLs](#fetch-urls)
      * [Fetch URLs with DEBUG logs](#fetch-urls-with-debug-logs)
      * [Profile code](#profile-code)
      * [Trace code](#trace-code)
      * [Get socket class](#get-socket-class)

# Stage 1: Python 3.7

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
./docker-exec.sh test_grequests_python37_1 \
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
+ docker exec -it test_grequests_python37_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 04:50:45,188 - python37_1 - START
2019-03-24 04:50:46,240 - python37_1 - len(all_page_ids) = 10
2019-03-24 04:50:46,240 - python37_1 - len(valid_page_ids) = 10
2019-03-24 04:50:46,240 - python37_1 - len(invalid_page_ids) = 0
2019-03-24 04:50:46,241 - python37_1 - total_time=0:00:01.059414
2019-03-24 04:50:46,242 - python37_1 - END
+ set +x
================================
```

## Fetch URLs with DEBUG logs

- Command:

```
./docker-exec.sh test_grequests_python37_1 \
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
+ docker exec -it test_grequests_python37_1 /usr/local/bin/python /app/test_grequests_v2.py --log-level DEBUG --url https://https_server:8081/delay/1 --url-count 10
2019-03-24 05:09:13,967 - python37_1 - START
2019-03-24 05:09:13,976 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,981 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,982 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,984 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,985 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,986 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,987 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,988 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,994 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:13,996 - python37_1 - Starting new HTTPS connection (1): https_server:8081
2019-03-24 05:09:15,028 - python37_1 - https://https_server:8081 "GET /delay/1?page=1 HTTP/1.1" 200 308
2019-03-24 05:09:15,030 - python37_1 - https://https_server:8081 "GET /delay/1?page=7 HTTP/1.1" 200 308
2019-03-24 05:09:15,031 - python37_1 - https://https_server:8081 "GET /delay/1?page=5 HTTP/1.1" 200 308
2019-03-24 05:09:15,032 - python37_1 - https://https_server:8081 "GET /delay/1?page=0 HTTP/1.1" 200 308
2019-03-24 05:09:15,033 - python37_1 - https://https_server:8081 "GET /delay/1?page=3 HTTP/1.1" 200 308
2019-03-24 05:09:15,034 - python37_1 - https://https_server:8081 "GET /delay/1?page=9 HTTP/1.1" 200 308
2019-03-24 05:09:15,035 - python37_1 - https://https_server:8081 "GET /delay/1?page=2 HTTP/1.1" 200 308
2019-03-24 05:09:15,035 - python37_1 - https://https_server:8081 "GET /delay/1?page=4 HTTP/1.1" 200 308
2019-03-24 05:09:15,036 - python37_1 - https://https_server:8081 "GET /delay/1?page=8 HTTP/1.1" 200 308
2019-03-24 05:09:15,037 - python37_1 - https://https_server:8081 "GET /delay/1?page=6 HTTP/1.1" 200 308
2019-03-24 05:09:15,038 - python37_1 - len(all_page_ids) = 10
2019-03-24 05:09:15,038 - python37_1 - len(valid_page_ids) = 10
2019-03-24 05:09:15,038 - python37_1 - len(invalid_page_ids) = 0
2019-03-24 05:09:15,040 - python37_1 - total_time=0:00:01.079346
2019-03-24 05:09:15,040 - python37_1 - END
+ set +x
================================
```


## Profile code

- Command:

```
./docker-exec.sh test_grequests_python37_1 \
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
+ docker exec -it test_grequests_python37_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --profile-code --profile-stats-count 20
2019-03-24 04:51:04,899 - python37_1 - START
2019-03-24 04:51:06,288 - python37_1 - len(all_page_ids) = 10
2019-03-24 04:51:06,288 - python37_1 - len(valid_page_ids) = 10
2019-03-24 04:51:06,288 - python37_1 - len(invalid_page_ids) = 0
         25194 function calls (24776 primitive calls) in 1.385 seconds

   Ordered by: cumulative time
   List reduced from 657 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.387    1.387 /usr/local/lib/python3.7/site-packages/grequests.py:103(map)
     10/1    0.000    0.000    1.386    1.386 /usr/local/lib/python3.7/site-packages/grequests.py:60(send)
     10/1    0.001    0.000    1.386    1.386 /usr/local/lib/python3.7/site-packages/requests/sessions.py:466(request)
     10/1    0.002    0.000    1.353    1.353 /usr/local/lib/python3.7/site-packages/requests/sessions.py:617(send)
     10/1    0.001    0.000    1.351    1.351 /usr/local/lib/python3.7/site-packages/requests/adapters.py:394(send)
     10/1    0.001    0.000    1.344    1.344 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:446(urlopen)
     10/1    0.001    0.000    1.342    1.342 /usr/local/lib/python3.7/site-packages/urllib3/connectionpool.py:319(_make_request)
     10/1    0.000    0.000    1.341    1.341 /usr/local/lib/python3.7/http/client.py:1277(getresponse)
     10/1    0.001    0.000    1.341    1.341 /usr/local/lib/python3.7/http/client.py:289(begin)
     10/1    0.001    0.000    1.337    1.337 /usr/local/lib/python3.7/http/client.py:256(_read_status)
     70/7    0.001    0.000    1.337    0.191 {method 'readline' of '_io.BufferedReader' objects}
     10/1    0.000    0.000    1.337    1.337 /usr/local/lib/python3.7/socket.py:575(readinto)
     10/1    0.000    0.000    1.303    1.303 /usr/local/lib/python3.7/site-packages/gevent/_ssl3.py:494(recv_into)
     10/1    0.964    0.096    1.303    1.303 /usr/local/lib/python3.7/site-packages/gevent/_ssl3.py:312(read)
       10    0.001    0.000    0.088    0.009 /usr/local/lib/python3.7/site-packages/requests/sessions.py:426(prepare_request)
       10    0.001    0.000    0.066    0.007 /usr/local/lib/python3.7/site-packages/requests/sessions.py:690(merge_environment_settings)
       10    0.000    0.000    0.061    0.006 /usr/local/lib/python3.7/site-packages/requests/utils.py:755(get_environ_proxies)
      560    0.012    0.000    0.055    0.000 /usr/local/lib/python3.7/_collections_abc.py:742(__iter__)
       20    0.005    0.000    0.053    0.003 /usr/local/lib/python3.7/urllib/request.py:2456(getproxies_environment)
     10/3    0.001    0.000    0.047    0.016 <frozen importlib._bootstrap>:978(_find_and_load)



2019-03-24 04:51:06,297 - python37_1 - total_time=0:00:01.408052
2019-03-24 04:51:06,297 - python37_1 - END
+ set +x
================================
```

## Trace code

- Command:

```
./docker-exec.sh test_grequests_python37_1 \
 /usr/local/bin/python /app/test_grequests_v2.py \
 --url https://https_server:8081/delay/1 --url-count 10 \
 --trace-calls > trace.out
```

## Get socket class

- Command:

```
./docker-exec.sh test_grequests_python37_1 \
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
+ docker exec -it test_grequests_python37_1 /usr/local/bin/python /app/test_grequests_v2.py --url https://https_server:8081/delay/1 --url-count 10 --socket-class
2019-03-24 04:51:41,567 - python37_1 - START
2019-03-24 04:51:42,614 - python37_1 - len(all_page_ids) = 10
2019-03-24 04:51:42,614 - python37_1 - len(valid_page_ids) = 10
2019-03-24 04:51:42,614 - python37_1 - len(invalid_page_ids) = 0
2019-03-24 04:51:43,629 - python37_1 - socket_class = <class 'gevent._ssl3.SSLSocket'>
+ set +x
================================
```