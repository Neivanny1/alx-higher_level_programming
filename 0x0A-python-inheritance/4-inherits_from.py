#!/usr/bin/python3
"""
Module to check if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
    return true if object is instance of class else false
    """
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
