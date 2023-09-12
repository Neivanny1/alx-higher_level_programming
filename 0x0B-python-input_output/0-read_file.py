#!/usr/bin/python3
"""
Module to read a text file and print to stdout
"""


def read_file(filename=""):
    """ function that reads UTF8 file and prints to stdout """
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            print(line, end="")
