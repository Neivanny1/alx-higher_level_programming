#!/usr/bin/python3
"""
Defines class Square
"""


class Square:
    """ defines private attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(x is not int for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if all(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    """ prints square with # in stdout """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            x = self.position[0]
            y = self.position[1]
            for i in range(y):
                print("")
            for row in range(self.size):
                for j in range(x):
                    print(" ", end="")
                for col in range(self.size):
                    print("#", end="")
                print()

    """ returns area of the square """
    def area(self):
        return self.size ** 2
