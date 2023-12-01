#!/usr/bin/python3
"""
Module to return json
"""
from sys import argv
import requests


if __name__ == '__main__':
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data={'q': arg})
        r_json = r.json()
        if r_json:
            print('[{}] {}'.format(r_json.get('id'), r_json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
