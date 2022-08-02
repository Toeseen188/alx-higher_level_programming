#!/usr/bin/python3
"""module to create a function"""


def class_to_json(obj):
    """ returns a simple data
    structure for json"""
    return obj.__dict__
