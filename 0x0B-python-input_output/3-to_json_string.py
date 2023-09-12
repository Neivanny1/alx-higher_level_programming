#!/usr/bin/python3
import json
"""
Module to print JSON representation of object
"""


def to_json_string(my_obj):
    """returns  the JSON representation of an object (string):"""
    return json.dumps(my_obj)
