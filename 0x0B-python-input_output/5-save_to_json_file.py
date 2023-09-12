#!/usr/bin/python3
"""
Module to save object to a text file with JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """"saves obj to txt file with JSON rep"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
