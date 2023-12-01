#!/usr/bin/python3
"""
Module to send email
"""
from sys import argv
import urllib.parse
import urllib.request


if __name__ == "__main__":
    creds = {'email': argv[2]}
    msg = urllib.parse.urlencode(creds)
    msg = msg.encode('ascii')
    req = urllib.request.Request(argv[1], msg)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
