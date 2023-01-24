#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Representing a square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): Size of the new square.
        Raises:
            TypeError: if size is not integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.size = size

    @property
    def size(self):
        """returns the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current area of the square"""
        return (self.__size * self.__size)
