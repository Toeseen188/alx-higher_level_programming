#!/usr/bin/python3
""" locked class """


class LockedClass():
    """ this __slot__ prevent dynamic creation of 
    instances """

    __slots__ = ['first_name']

    def __init__(self):
        """ instantiation """
        pass
