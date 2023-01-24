#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size: size of new square
        Raise:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >=0')
        self.__size = size

    def area(self):
        """Returns the ares of the new square"""
        return (self.__size * self.__size)
