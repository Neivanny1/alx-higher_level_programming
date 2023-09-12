#!/usr/bin/python3
"""
Module to print JSON representation of object
"""
import json


def from_json_string(my_str):
    """returns  the JSON representation of an object (string):"""
    return json.loads(my_str)
