#!/usr/bin/python3
"""Defines a function that inserts line of text."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text to a file, after each line containing specific string.

    Args:
        filename (str): Name of the file.
        search_string (str): String to be searched.
        new_string (str): String to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
