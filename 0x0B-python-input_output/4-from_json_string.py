#!/usr/bin/python3
"""Defines a function that returns an object represented be a JSON string."""
import json


def from_json_string(my_str):
    """Returns thepyhton object representation of a JSON string.

    Args:
        my_str (str): JSON STRING
    """
    return json.loads(my_str)
