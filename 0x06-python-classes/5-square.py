#!/usr/bin/python3
""" Documentation of class Square """


class Square:
    """ this class prints square with #
    """
    def __init__(self, size=0):
        """initialise"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be > 0")

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

    @property
    def size(self):
        """return self.__size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"setter method"""
        self.__size = value

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be > 0")
