#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, att, value):
    """Adda a new attribute to an object.

    Args
        obj (any): Object to add an attribute to.
        att (str): Name of the attribute to add to object.
        value (any): The value of attribute.

    Raises:
        TypeError: If the attributes cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
