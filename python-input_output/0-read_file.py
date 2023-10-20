#!/usr/bin/python3
"""
function that reads file that does not exist
"""


def read_file(filename=""):
    """
    using with to open file: "" wit utf-8 encoding
    as file and print the read
    """
    with open("", mode="r", encoding="UTF-8") as file:
        print(file.read(), end="")
