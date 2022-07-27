#!/usr/bin/python3
""" module doc"""


class Square:
    """ class square """
    def __init__(self, size=0):
        """
        Args:
            size: int args
        Raises:
            TypeError: raised if size is not int
            ValueError: raised if size is less than 0
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
