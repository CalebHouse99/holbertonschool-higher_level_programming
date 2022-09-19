#!/usr/bin/python3
"""Writes to file and returns number of letters
"""


def write_file(filename="", text=""):
    """Writes to file and returns number of letters"""
    with open(filename, "w", encoding="utf-8") as file:
        content = file.write(text)
        count = 0
        for letter in text:
            count += 1
        return count
