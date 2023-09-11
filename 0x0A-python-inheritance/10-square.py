#!/usr/bin/python3
"""Defines class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from class Rectangle"""
    def __init__(self, size):
        """Initializing a square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
