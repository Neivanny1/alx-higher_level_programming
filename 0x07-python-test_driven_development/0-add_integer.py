#!/usr/bin/python3
"""
Module to find the sum of two integers or floats
"""


def add_integer(a, b):
    """
    Function to find and return sum of two integers or floats
    """

    """Checks if first variable is an int or float"""
    if not isinstance(a, int) and not isinstance(a, float) or \
       isinstance(a, bool):
        raise TypeError("a must be an integer")

    """Checks if second variable is an int or float"""
    if not isinstance(b, int) and not isinstance(b, float) or \
       isinstance(b, bool):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
