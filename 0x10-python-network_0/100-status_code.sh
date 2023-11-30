#!/bin/bash
# Displays all HTTP methods the URL's server will accept
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
