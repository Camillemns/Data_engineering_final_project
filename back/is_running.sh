#!/bin/sh

while true ; do
  curl -sS --fail "http://localhost:8000/" && break
  sleep 1
done
