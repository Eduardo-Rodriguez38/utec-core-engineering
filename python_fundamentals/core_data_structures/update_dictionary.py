#!/usr/bin/env python3
"""Module that replaces or adds a key/value pair in a dictionary."""


def update_dictionary(a_dictionary, key, value):
    """Replace or add key with value and return the dictionary."""
    a_dictionary[key] = value
    return a_dictionary
