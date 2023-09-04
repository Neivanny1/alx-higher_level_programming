#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """ Rectangle class intialisation """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    rectangle.append(str(self.print_symbol))
                if heighti < self.__height - 1:
                    rectangle.append("\n")
            rectangle = "".join(rectangle)
            return rectangle

    """returns string representation of the rectangle"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    """deleting the list rectangle"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """static mothod that returns the biggest rectangle based on area"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
