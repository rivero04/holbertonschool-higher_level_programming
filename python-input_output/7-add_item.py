#!/usr/bin/python3
"""
Script that adds all arguments to a Python list.
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except Exception:
    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[1])
    save_to_json_file(my_list, filename)
