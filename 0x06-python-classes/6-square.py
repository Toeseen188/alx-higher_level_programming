#!/usr/bin/python3
""" Documentation of class Square """


class Square:
    """ this class prints square with #
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialise"""
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be > 0")
        elif not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or \
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area"""
        return self.__size * self.__size

    def my_print(self):
        """print #"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(' ', end='')
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

    @property
    def position(self):
        """ get method returns self.__position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set the value of postion"""
        self.__postion = value

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
