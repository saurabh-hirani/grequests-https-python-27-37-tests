#!/bin/bash -e

cn=${1:-example.com}
host="0.0.0.0"
port=8082

docker run --rm -e HTTPS_CERT_FILE='/tmp/example.com.crt' -e HTTPS_KEY_FILE='/tmp/example.com.key' -e PORT=$port -p $port:$port -v /tmp:/tmp mccutchen/go-httpbin:v2.1.3
