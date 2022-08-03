#!/usr/bin/python3
""" A module containing an empty class"""


class BaseGeometry:
    """ This is an empty class"""
    def __init__(self):
        """ init"""
        pass

    def area(self):
        """ This method raises an exceptions"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public method to validate name and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ This is class Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
