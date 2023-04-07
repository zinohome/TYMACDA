#!/bin/bash
IMGNAME=jointhero/macda
IMGVERSION=ty-v1.0922
docker build --no-cache -t $IMGNAME:$IMGVERSION .
