#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('UTF-8'))
