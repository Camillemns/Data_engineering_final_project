#!/bin/sh
while :; do
  curl -sS --fail -o /dev/null "http://localhost:8000/" && break
  sleep 1
done