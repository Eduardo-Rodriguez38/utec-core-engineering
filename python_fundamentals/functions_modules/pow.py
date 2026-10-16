#!/usr/bin/env python3
"""Module that computes a raised to the power of b."""


def pow(a, b):
    """Return a to the power of b without using **."""
    result = 1
    for i in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
