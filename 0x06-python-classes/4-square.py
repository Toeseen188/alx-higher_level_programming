#!/usr/bin/python3
"""class Square"""


class Square:
    """ class """
    def __init__(self, size=0):
        """ initialize class attribute"""
        self.__size = size

        if size < 0:
            raise ValueError("size must be > 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the size * size"""
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
