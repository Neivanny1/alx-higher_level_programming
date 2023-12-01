#!/usr/bin/python3
"""
Module to send request to url
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
