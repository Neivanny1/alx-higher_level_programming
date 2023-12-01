#!/usr/bin/env python3
"""
Module that fetches a url
"""

import urllib.request
import urllib.parse


def fetch_url():
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('UTF-8'))


if __name__ == "__main__":
    fetch_url()
