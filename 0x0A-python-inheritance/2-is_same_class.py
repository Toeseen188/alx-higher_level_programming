#!/usr/bin/python3
""" This module contain fuction that
checks if object is contained in a class
"""


def is_same_class(obj, a_class):
    """ this function returns True if obj
    is instance of a_class, otherwise, false
    Args:
        obj: object of a class, argument
        a_class: a class as args
    Return:
        returns True if obj is instance of a_class
        and False if  not
        """
    if type(obj) is a_class:
        return True
    else:
        return False
