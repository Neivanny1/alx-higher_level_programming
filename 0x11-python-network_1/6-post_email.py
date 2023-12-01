#!/usr/bin/python3
"""
Module to send emails
"""
from sys import argv
import requests


if __name__ == '__main__':
    creds = {'email': argv[2]}
    r = requests.post(argv[1], creds)
    print(r.text)
