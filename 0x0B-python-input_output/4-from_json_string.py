#!/usr/bin/python3
""" Module to load from json obj"""
import json


def from_json_string(my_str):
    """ this function load string
    into obj with json"""
    json_load = json.loads(my_str)
    return json_load
