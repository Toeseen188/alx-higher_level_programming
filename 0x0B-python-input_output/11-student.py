#!/usr/bin/python3
"""A class Student"""


class Student:
    """ create a class student and initialize"""
    def __init__(self, first_name, last_name, age):
        """ initialize public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ etrieves a dictionary representation of a Student instance
        """
        if not isinstance(attrs, list):
            return self.__dict__
        for var in attrs:
            if not isinstance(var, str):
                return self.__dict__

        string_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                string_dict[string] = self.__dict__[string]
        return string_dict

    def reload_from_json(self, json):
        """ replaces the attributes in the instance"""
        keys = list(json.keys())
        for key in keys:
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]
