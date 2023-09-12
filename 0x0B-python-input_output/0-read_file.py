#!/usr/bin/python3
"""
Module to read a text file and print to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")
