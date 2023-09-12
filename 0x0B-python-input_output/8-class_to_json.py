#!/usr/bin/python3
"""
Module that returns the dictionary description with simple data
structure for JSON serialization of an object
"""


def class_to_json(obj):
    """returns dictionary description with simple
    data structure for JSON serialization of an object """
    return obj.__dict__
