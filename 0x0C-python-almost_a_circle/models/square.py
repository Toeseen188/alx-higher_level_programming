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

    def update(self, *args, **kwargs):
        """assigns properties to a list of args"""
        if (args):
            if len(args) > 0:
                for i in range(len(args)):
                    if i == 0:
                        self.id = args[0]
                    if i == 1:
                        self.size = args[1]
                    if i == 2:
                        self.x = args[2]
                    if i == 3:
                        self.y = args[3]

        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "size":
                        self.size = kwargs["size"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """ this returns the dictionary representation of
        square with it attributes"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
