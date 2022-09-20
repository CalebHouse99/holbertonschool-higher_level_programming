#!/usr/bin/python3
"""Append to the end of file
"""


def append_write(filename="", text=""):
    """Append to end of a file"""
    with open(filename, "a") as file:
        file.write(text)
        return len(text)
