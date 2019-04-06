Table of Contents
=================

  * [Pre-requisites](#pre-requisites)
  * [Stages](#stages)

These are the different stages which show varying runtime depending on the
Python modules installed.

## Pre-requisites

- Run ```docker-compose``` from the project dir.

```
docker-compose --project-name test_grequests up \
               --build --force-recreate
```

## Stages

* [00](./00) - local non-virtualenv setup 
  - Python2 runs **slow**, Python3 runs fast

* [01](./01) - virtualenv setup without **pyopenssl**
  - Python2 runs fast, Python3 runs fast
  
* [02](./02) - virtualenv setup with **pyopenssl**
  - Python2 runs **slow**, Python3 runs **slow**

* [03](./03) - virtualenv setup with **pyopenssl**, **gevent-openssl**
  - Python2 runs fast, Python3 runs **slow**

* [04](./04) - virtualenv setup with **pyopenssl**, **gevent-openssl** and Python3 patch
  - Python2 runs fast, Python3 runs fast