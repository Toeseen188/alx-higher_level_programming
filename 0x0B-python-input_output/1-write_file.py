#!/usr/bin/python3
""" This module create a file
and write to it"""


def write_file(filename="", text=""):
    """takes the name of the file and the tesxt
    as arguments"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
