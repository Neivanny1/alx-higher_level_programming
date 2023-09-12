#!/usr/bin/python3
"""
Module that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """
    with open(filename, encoding="UTF-8") as a_file:
        return json.load(a_file)
