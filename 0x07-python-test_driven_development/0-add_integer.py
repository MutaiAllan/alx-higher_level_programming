#!/usr/bin/python3
"""Defines a function that adds integers."""


def add_integer(a, b=98):
    """Returns the sum of a and b.

    Args:
        a: first integer.
        b: second integer.
    Raises:
        TypeError: If a or b is not integer/float.
    Returns:
        Sum of a and b.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
