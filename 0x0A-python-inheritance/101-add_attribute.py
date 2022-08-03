#!/usr/bin/python3
""" this module contain a function"""


def add_attribute(obj, name, value):
    """ add attribute if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
