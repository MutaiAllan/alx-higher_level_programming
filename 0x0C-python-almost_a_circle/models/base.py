#!/usr/bin/python3
"""Defines a base class for all other tasks."""
import json
import csv
import turtle


class Base:
    """Base of all other classes in the project.

    Private Class Attributes:
        __nb_object (int): Number of bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): The identity of the enw Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
