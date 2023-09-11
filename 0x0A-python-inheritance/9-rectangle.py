#!/usr/bin/python3
"""
Imports class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ initializes class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """ public instance method area """
    def area(self):
        return self.__width * self.__height
    """ prints rectangle description """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
