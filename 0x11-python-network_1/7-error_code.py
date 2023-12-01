#!/usr/bin/python3
"""
Module to send request to url
"""
from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
