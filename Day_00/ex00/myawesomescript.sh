#!/bin/sh

curl -s -I  $1 | grep Location | cut -d " " -f2
