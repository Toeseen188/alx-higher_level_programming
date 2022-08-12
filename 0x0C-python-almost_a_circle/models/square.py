#!/usr/bin/python3
"""This module contains class Square
that inherited from class REctangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size"""
        self.width = value

    def __str__(self):
        """ return string"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
