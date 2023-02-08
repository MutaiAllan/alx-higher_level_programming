#!/usr/bin/python3
"""Defines a class that checks an object."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match.

    Returns:
        True: If obj is an instance or inherited instance of a class.
        False: If obj is not an instance or inherited instance of a class.
    """

    if isinstance(obj, a_class):
        return True
    return False
