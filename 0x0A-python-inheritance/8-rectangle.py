#!/usr/bin/python3
"""
Imports class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ initializes class """
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, "width", width):
            self.width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.height = height
