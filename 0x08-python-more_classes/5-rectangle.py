#!/usr/bin/python3
"""Define rectangle Class """


class Rectangle:
    """Rectangle created with width and height
    with area and perimeter calculated"""
    def __init__(self, width=0, height=0):
        """Initializes rectangle features
        Args:
            width: this is an int instance variable
            height: this is an int instance variable"""
        self.__height = height
        self.__width = width

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        """instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width settter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ hight setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculate and return the
        area of a rectangule i.e height * width """
        return(self.__height * self.__width)

    def perimeter(self):
        """ calculate and return perimeter of a rectangle
        i.e 2*width + 2*height """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """ printing using str()"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')
            if i != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)

    def __rep__(self):
        """ return a representative instance of string to be
        to use eval """
        return "Rectangle({self.__width}, {self.__height})"
