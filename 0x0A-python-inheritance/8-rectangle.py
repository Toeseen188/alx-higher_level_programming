#!/usr/bin/python3
""" A module containing an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is class Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
