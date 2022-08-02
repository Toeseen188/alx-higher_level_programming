#!/usr/bin/python3
"""This module create a file
and append a file to it. It creates
new file not already existed"""


def append_write(filename="", text=""):
    """ this function create append texts
    to a existed file or create a new file
    if not already existed"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f_append = f.write(text)
    return (f_append)
