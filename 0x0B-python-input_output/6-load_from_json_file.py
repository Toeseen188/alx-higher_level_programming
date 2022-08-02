#!/usr/bin/python3
""" THis program create an object from
json file"""
import json


def load_from_json_file(filename):

    """" a function that create an obj from
    a json file"""
    with open(filename, encoding='utf-8') as f:
        json_str = f.read()
        json_obj = json.loads(json_str)
        return json_obj
