#!/usr/bin/python3
"""
Module to append a string and end of text file
"""


def append_write(filename="", text=""):
    """Appends strings to end of file and return characters added"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
