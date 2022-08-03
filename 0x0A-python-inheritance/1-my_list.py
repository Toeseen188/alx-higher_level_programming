#!/usr/bin/python3
""" This module contain class Mylist
"""


class MyList(list):
    """ this class inherit from class list"""
    def __init__(self):
        """init"""
        pass

    def print_sorted(self):
        """ sort list"""
        print(sorted(self))
