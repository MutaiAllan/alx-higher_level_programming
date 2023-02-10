#!/usr/bin/python3
"""Defines a function that creates an object from json file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename: name of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
