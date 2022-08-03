#!/usr/bin/python3
""" This module contain a function that return
a lit of a class attributes"""


def lookup(obj):
    """ This fuction returns the list of a class
    attraibutes
    Args:
        obj: A class param
    Return:
        Returns a list of attributes"""
    list_attr = dir(obj)
    return list_attr
