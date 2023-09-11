#!/usr/bin/python3
"""
Defines a class Mylist that inherits from lists
"""


class MyList(list):
    """MyList initialization"""
    def __init__(self):
        pass

    """prints sorted list"""
    def print_sorted(self):
        print(sorted(self))
