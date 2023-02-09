#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """A rebel with operators == and != inverted."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
