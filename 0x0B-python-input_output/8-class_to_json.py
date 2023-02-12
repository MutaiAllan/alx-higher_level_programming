#!/usr/bin/python3
"""Defines a function that returns the dictionary description
with simple data structure for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    return obj.__dict__
