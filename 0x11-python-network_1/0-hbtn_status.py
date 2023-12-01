#!/bin/env python3
"""
Module that fetches a url
"""


def fetch_url():

    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as rp:
        response = rp.read()
        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode()}")


if __name__ == "__main__":
    fetch_url()
