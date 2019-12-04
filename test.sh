#!/bin/sh
#
#
curl -X POST -H "Content-Type: application/json" -d '{"timestamp": "2019/12/04 14:44:31","value": {"humidity": 65.56496528572518,"temperature": 24.28290226596475}}' localhost:8080/m2x
