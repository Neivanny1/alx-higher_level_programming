#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """ Rectangle class intialisation """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """returns the rectangle area"""
    def area(self):
        return (self.__height * self.__width)

    """ returns the rectangle perimeter"""
    def perimeter(self):
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

    """ print shape of rectangle with #"""
    def __str__(self):
        rectangle = []
        if (self.__width == 0) or (self.__height == 0):
            return ""
        else:
            for heighti in range(self.__height):
                for widthi in range(self.__width):
                    rectangle.append("#")
                if heighti < self.__height - 1:
                    rectangle.append("\n")
            rectangle = "".join(rectangle)
            return rectangle

    """returns string representation of the rectangle"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
