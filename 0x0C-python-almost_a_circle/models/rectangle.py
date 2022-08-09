#!/usr/bin/python3
""" this module contain a class Rectangle
that inherit from class Base"""

from models.base import Base


class Rectangle(Base):
    """ This class inherit the attributes
    from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing rectangle class """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter method for width"""
        self.__width = width

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def set_height(self, height):
        """setter for method for height"""
        self.__height = height

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ setter method for x"""
        self.__x = x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        self.__y = y
