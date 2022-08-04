#!/usr/bin/python3
"""inserts a line of text to a file,after eachline containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """define a text file insertion
            """
    text = ""
    with open(filename, "r", encoding='utf-8') as myF:
        for line in myF:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding='utf-8') as newF:
        newF.write(text)
