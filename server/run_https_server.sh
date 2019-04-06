#!/bin/bash -e

cn=${1:-example.com}
host="0.0.0.0"
port=8082

docker run --rm -e HTTPS_CERT_FILE='/tmp/server.crt' -e HTTPS_KEY_FILE='/tmp/server.key' -e PORT=$port -p $port:$port -v /tmp:/tmp mccutchen/go-httpbin:v2.1.1
