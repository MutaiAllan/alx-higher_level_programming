#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])."""

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_ordered_list(self):
        """Tests an oredered lsit of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Tests an unordered list of integers."""
        unordered = [3, 4, 2, 1]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_bginning(self):
        """Tests a list with maximum vlue at beginning."""
        max_at_beginning = [4, 3,  2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_element(self):
        """Tests a list with a single element."""
        one_element = [2]
        self.assertEqual(max_integer(one_element), 2)

    def test_float_list(self):
        """Tests a list of floats."""
        floats = [1.43, 4.3, 7.34, 5.33]
        self.assertEqual(max_integer(floats), 7.34)

    def test_intfloat_list(self):
        """Tests a list of integers and floats."""
        int_floats = [5, 5.1, 2, 3.6]
        self.assertEqual(max_integer(int_floats), 5.1)

    def test_string(self):
        """Tests a string."""
        string = "Africa"
        self.assertEqual(max_integer(string), 'r')

    def test_strings(self):
        """Tests a list of strings."""
        strings = ["I", "a", "student", "at", "alx"]
        self.assertEqual(max_integer(strings), "student")

    def test_empty_string(self):
        """Tests an empty string."""
        string = ""
        self.assertEqual(max_integer(string), None)

if __name__ == '__main__':
    unittest.main()
