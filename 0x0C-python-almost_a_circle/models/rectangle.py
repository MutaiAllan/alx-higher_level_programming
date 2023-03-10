#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the new rectangle.
            x (int): The x co-ordinate of the rectangle.
            y (int): The y co-ordinate of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x co-ordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y co-ordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle with #"""
        i = 0
        print("\n" * self.__y, end="")
        while i < self.height:
            j = 0
            print(" " * self.__x, end="")
            while j < self.width:
                print("#", end="")
                j += 1
            print()
            i += 1

        def __str__(self):
            """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                           self.y, self.width,
                                                           self.height)
