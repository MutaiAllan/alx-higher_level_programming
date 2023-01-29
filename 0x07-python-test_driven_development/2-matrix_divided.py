#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Devides all elements of a matrix by div.

    Args:
        matrix: A list of lists of ints/floats.
        div: divisor of the matrix.

    Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If matrix contains rows of different size.
        TypeError: If div is not an int or float.

    Returns:
        A new matrix showing the result of division.
    """
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                             "integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
