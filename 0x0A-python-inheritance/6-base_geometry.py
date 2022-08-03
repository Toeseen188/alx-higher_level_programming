#!/usr/bin/python3
""" A module containing an empty class"""


class BaseGeometry:
    """ This is an empty class"""
    def __init__(self):
        """ init"""
        pass

    def area(self):
        """ This method raises an exceptions"""
        raise Exception("area() is not implemented")
