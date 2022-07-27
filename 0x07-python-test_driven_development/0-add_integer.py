#!/usr/bin/python3
""" A module about a function that adds integer"""


def add_integer(a, b=98):
    """ A function that add
    two integer or two float and raise TypeError
    if they are not

    Args:
        a: must be int or float, raises a TypeError,
            if not
        b: must be int or float, raises a TypeError,
            if not
    Returns:
        Returns the additon of a and b after casting
        into an int

    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
