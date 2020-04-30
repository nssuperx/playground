#!/bin/sh
LOCALIP=$(ifconfig en1 | grep inet | awk '$1=="inet" {print $2}')
echo $LOCALIP
