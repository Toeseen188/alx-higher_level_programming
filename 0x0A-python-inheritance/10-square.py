#!/usr/bin/python3
""" This module contains class Square
that inherit from Rectangle which also inherit
from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the multiplication of
        width and height"""
        return self.__size * self.__size
