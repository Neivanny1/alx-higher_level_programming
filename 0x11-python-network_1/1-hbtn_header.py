#!/usr/bin/python3
"""
Module to send request to a url
"""


from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        ans = response.info()
        req = ans.get('X-Request-Id')
        print(req)
