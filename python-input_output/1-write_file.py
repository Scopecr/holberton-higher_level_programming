#!/usr/bin/python3
"""function that writes text file utf-8"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)
