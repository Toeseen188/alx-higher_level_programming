#!/usr/bin/python3
""" module containing base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert list of dictionary to Json"""
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this method writes the JSON string representation of list_objs
        to a file"""
        filename = cls.__name__ + ".json"

        with open(filename, "w") as json_file:
            if list_objs is None or []:
                json_file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dicts))
