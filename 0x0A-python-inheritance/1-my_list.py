#!/usr/bin/python3
"""
defines class MyList that inherits from list
"""


class MyList(list):
    """ initializes MyList """
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
