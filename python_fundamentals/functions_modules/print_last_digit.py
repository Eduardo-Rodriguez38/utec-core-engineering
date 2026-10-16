#!/usr/bin/env python3
"""Module that prints and returns the last digit of a number."""


def print_last_digit(number):
    """Print the last digit of number and return it."""
    last = abs(number) % 10
    print("{}".format(last), end="")
    return last
