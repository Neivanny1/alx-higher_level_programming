#!/usr/bin/python3
"""
Imports class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ initializes class """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
    """ public instance method area """
    def area(self):
        return self.__size ** 2
