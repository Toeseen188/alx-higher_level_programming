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

    def area(self):
        """return the multiplication of
        width and heigh"""
        return self.__width * self.__height

    def __str__(self):
        """print string"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
