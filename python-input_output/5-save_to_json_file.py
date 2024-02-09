#!/usr/bin/python3
"""
Write an object to a text.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a string representation.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
