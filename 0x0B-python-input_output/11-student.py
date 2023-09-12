#!/usr/bin/python3
"""Defines ``Student`` class"""


class Student:
    """
    """
    def __init__(self, first_name, last_name, age):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        """
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            name = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    name[key] = value
            return name

    def reload_from_json(self, json):
        """
        """

        for i, j in json.items():
            self.__dict__[i] = j
