#!/usr/bin/python3
"""
Module to check if object is instance of class inherited from
"""


def is_kind_of_class(obj, a_class):
    """return true if object is instance and false otherwise"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
