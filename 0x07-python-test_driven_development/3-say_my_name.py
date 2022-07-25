#!/usr/bin/python3
""" A doc """
def say_my_name(first_name, last_name=""):
    """ this function print first_name and last_name 
    as strings only.
    it gives an error if any other type is supplied 
    as arguments.

    Args:
        first_name: must be string, otherwise error
        last_name: must be string, otherwise error
    Returns:
        Prints first_name and last_name if successful
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
