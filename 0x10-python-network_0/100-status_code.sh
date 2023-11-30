#!/bin/bash
# Sends a GET request and displays body of the response
curl -s -o /dev/null -w '%{http_code}' "$1"
