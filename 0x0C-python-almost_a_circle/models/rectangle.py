#!/usr/bin/python3
"""
Module to import class Base
"""
from models.base import Base


class Rectangle(Base):
    """class intialization"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    @property
    def width(self):
        """gets width"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <=0:
            raise ValueError("width must be > 0")
        self.__width = value
    @property
    def height(self):
        """gets height"""

        return self.__height
    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """gets x"""
        return self.__x
    @x.setter
    def x(self, value):
        """sets x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """gets y"""
        return self.__y
    @y.setter
    def y(self, value):
        """sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """return area of rectangle"""
        return (self.__height * self.__width)
    def display(self):
        """Print shape of rectangle with # in stdout"""
        gap_in_btw = " "
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            print(gap_in_btw * self.__x, end="")
            print('#' *  self.__width)
    def __str__(self):
        """ overriding the __str__ method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
    def update(self, *args, **kwargs):
        """ A public method that assigns an argument to each attribute"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

