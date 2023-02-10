#!/usr/bin/python3
"""Defines a function that writes an Object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file suing JSON representation.

    Args:
        my_obj: The Object to be converted.
        filename: name of the text file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
