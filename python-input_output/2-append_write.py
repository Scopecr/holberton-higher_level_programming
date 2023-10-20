#!/usr/bin/python3
"""
function that appends to a file
"""


def append_write(filename="", text=""):
    """
    Filename gets append text with utf-8 encoding
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
