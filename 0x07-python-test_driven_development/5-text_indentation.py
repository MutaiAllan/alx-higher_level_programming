#!/usr/bin/python3
"""Defines a function that prints a test."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' or ':'.

    Args:
        text: string of text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count += 1
        count += 1
