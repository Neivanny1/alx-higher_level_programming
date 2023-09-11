#!/usr/bin/python3
"""
Module to check  if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    if object is isntance return true and false if otherwise
    """

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
