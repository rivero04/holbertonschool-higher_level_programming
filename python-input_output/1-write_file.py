#!/usr/bin/python3
"""
Write a string to a text file and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function opens a file in write mode with
    UTF-8 encoding,writes the given text to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        char_written = file.write(text)
    return char_written
