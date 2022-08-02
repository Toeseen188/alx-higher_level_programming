#!/usr/bin/python3
""" This is a python fuction
that read a file """


def read_file(filename=""):
    """ This function takes a filename(string)
    as an argument, create a file with the name
    and read the content stored in it
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
