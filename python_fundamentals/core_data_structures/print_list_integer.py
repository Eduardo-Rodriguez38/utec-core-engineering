#!/usr/bin/env python3
"""Module that prints all integers of a list."""


def print_list_integer(my_list=[]):
    """Print each integer of my_list, one per line."""
    for number in my_list:
        print("{:d}".format(number))
