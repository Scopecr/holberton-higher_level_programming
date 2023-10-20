#!/usr/bin/python3
"""Module that creates a Object from a json file"""
import json


def load_from_json_file(filename):
    """Creates an Object"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
