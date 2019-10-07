#!/bin/bash -e

host="0.0.0.0"
port=8081

docker run --rm -e HOST=$host -e PORT=$port -p $port:$port mccutchen/go-httpbin:v2.1.3
