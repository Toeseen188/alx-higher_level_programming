#!/usr/bin/python3
""" module that print square with # """


def print_square(size=0):
    """ print # in size of a square
    Args:
        size(int): size of the square
    Returns:
        return # size of a square
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print('#', end="")
        print()
