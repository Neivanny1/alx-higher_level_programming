#!/usr/bin/python3
"""
Module to write a string to text file
"""


def write_file(filename="", text=""):
    """writes  to textfile and returns no pf characters written"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
