#!/bin/env python3
"""
Module that fetches a url
"""

import urllib.request

def fetch_url():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode()))


if __name__ == "__main__":
    fetch_url()
