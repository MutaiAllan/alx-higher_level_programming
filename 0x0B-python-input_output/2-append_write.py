#!/usr/bin/python3
"""Defines a functio that appends a string at the end of a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a utf-8 file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
