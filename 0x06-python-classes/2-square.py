#!/usr/bin/python3
""" Build a class Square and instantiate with
    an instance """


class Square:
    """ class Square """
    def __int__(self, size=0):
        """
        Args:
            size(int, optional): the size of the square
        Raise:
            TypeError: when value of size in not int
            ValueError: when the value of size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
