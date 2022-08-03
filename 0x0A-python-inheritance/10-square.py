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
        """init"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("height", height)

    def area(self):
        """return the multiplication of
        width and heigh"""
        return self.__width * self.__height

    def __str__(self):
        """print string"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size):
        """instantiation with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the multiplication of
        width and height"""
        return self.__size * self.__size
