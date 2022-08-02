#!/usr/bin/python3
""" This module gives the json
representation of an object"""
import json


def to_json_string(my_obj):
    """ This fuction return the json reprensentation
    of the object"""
    d = json.dumps(my_obj)
    return d
