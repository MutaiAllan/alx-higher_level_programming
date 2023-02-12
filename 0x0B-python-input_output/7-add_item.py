#!/usr/bin/python3
"""Defines a function that adds all arguments and save them in a file."""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        arg_lst = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_lst = []

    i = 1

    while i < len(sys.argv):
        arg_lst.append(sys.argv[i])
        i += 1

    save_to_json_file(arg_lst, "add_item.json")
