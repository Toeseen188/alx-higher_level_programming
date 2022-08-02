#!/usr/bin/python3
"""A class Student"""


class Student:
    """ create a class student and initialize"""
    def __init__(self, first_name, last_name, age):
        """ initialize public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ etrieves a dictionary representation of a Student instance
        """
        return self.__dict__
