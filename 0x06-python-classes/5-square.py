#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Represents a square"""
    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the #."""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            print("#" * self.__size)
