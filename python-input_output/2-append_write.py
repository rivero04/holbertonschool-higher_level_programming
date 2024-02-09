#!/usr/bin/python3
"""
Append a string at the end of a text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
     This function opens a file in append mode with UTF-8 encoding,
     writes the given text to the end of the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        char_added = file.write(text)
    return char_added
