#!/usr/bin/python3
""" This module create a file
and save json obj into it"""
import json


def save_to_json_file(my_obj, filename):
    """ create a file with filename, and save obj in
    it"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
