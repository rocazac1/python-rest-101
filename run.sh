#!/bin/bash
set -e
docker run --rm -p 5000:5000 -e LOG_DIR=/var/log -v $(pwd)/log:/var/log rocazac1/python-rest-101 
