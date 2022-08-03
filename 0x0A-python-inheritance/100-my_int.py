#!/usr/bin/python3
""" this module contain a class of supercalss int"""


class MyInt(int):
    """ This is a class that inherit from class int"""
    def __init__(self, rebel):
        """instantiation"""
        self.__rebel = rebel

    def __eq__(self, y):
        """check for equality and return not equal"""
        return self.__rebel != y

    def __ne__(self, y):
        """check for inequality and return equal"""
        return self.__rebel == y
