#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """ initializes class """
    def __init__(self):
        pass

    """ public instance method area """
    def area(self):
        raise Exception("area() is not implemented")

    """ public instance method integer_validator """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
