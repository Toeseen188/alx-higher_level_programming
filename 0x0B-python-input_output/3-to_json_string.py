#!/usr/bin/python3
import json


""" This module gives the json
representation of an object"""

def to_json_string(my_obj):
    """ This fuction return the json reprensentation
    of the object"""
    d = json.dumps(my_obj)
    return d
