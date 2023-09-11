#!/usr/bin/python3
"""
Adds a new attribute to an object if it possible
"""


def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__') or \
            (hasattr(type(obj), '__slots__') and attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
