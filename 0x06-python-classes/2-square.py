#!/usr/bin/python3
"""
Defines a class Square with a size attribute
"""


class Square:
    """ A square class with optional  private size attribute """
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
