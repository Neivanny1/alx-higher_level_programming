#!/usr/bin/env python3
"""
Module to send request to a url
"""


import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
