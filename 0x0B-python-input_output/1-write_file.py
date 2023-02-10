#!/usr/bin/python3
"""Defines a function that adds a string in a file.."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to teh file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
