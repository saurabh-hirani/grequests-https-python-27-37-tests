#!/bin/bash -e

cn=${1:-example.com}

openssl genrsa -out /tmp/$cn.key 2048
openssl req -new -x509 -sha256 -key /tmp/$cn.key -out /tmp/$cn.crt -days 3650 \
            -subj "/CN=$cn\/emailAddress=admin@$cn/C=US/ST=Ohio/L=Columbus/O=Widgets Inc/OU=Some Unit"
