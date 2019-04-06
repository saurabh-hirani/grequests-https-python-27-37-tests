#!/bin/bash -e

module_path=$(python /app/get_module_path.py 'gevent_openssl.SSL' | sed 's/\.pyc/\.py/g')
patch -R $module_path < /patches/gevent_openssl_ssl.patch
