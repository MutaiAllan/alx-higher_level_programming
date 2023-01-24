#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes anew square.

        Args:
            size (int): size of the new square.
            position (int, int): position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the size of the new square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size * self.__size)

    def posn(self):
        """Returns the position in spaces"""
        pos = ''
        if self.size == 0:
            return "\n"
        for i in range(self.position[1]):
            pos += "\n"
        for i in range(self.size):
            for i in range(self.position[0]):
                pos += ' '
            for j in range(self.size):
                pos += '#'
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square in position."""
        print(self.posn(), end='')
