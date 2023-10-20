#!/usr/bin/python3
"""Module that creates a Object from a json file"""
import json


def load_from_json_file(filename):
    """Creates an Object"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
