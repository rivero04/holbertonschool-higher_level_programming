#!/usr/bin/python3
"""Read and print the content of a text file."""


def read_file(filename=""):
    """
    This function opens a file in read mode with UTF-8 encoding,
    reads the entire content, and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
