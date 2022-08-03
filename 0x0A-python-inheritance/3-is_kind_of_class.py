#!/usr/bin/python3
""" This module contains a function that
checks if a class or obj is a subclass of another
"""


def is_kind_of_class(obj, a_class):
    """ This function returns True if obj is a subclass
    of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
