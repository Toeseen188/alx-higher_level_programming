#!/usr/bin/python3
""" This module contains a fuction that checks
if obj is a subclass of a_class"""


def inherits_from(obj, a_class):
    """ Return True if obj is a subclass of a_class
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        False
