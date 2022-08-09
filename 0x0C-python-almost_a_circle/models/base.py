#!/usr/bin/python3
""" module containing base class """


class Base:
    """ BAse class...... """
    __nb_objects = 0

    def __init__(self, id=None):
        """ intialization on every instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
