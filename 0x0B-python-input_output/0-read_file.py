#!/usr/bin/python3
"""Reads text and outputs it
"""


def read_file(filename=""):
    """Reads text and outputs it"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
