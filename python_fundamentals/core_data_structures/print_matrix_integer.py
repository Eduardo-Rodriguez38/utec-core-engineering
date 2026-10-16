#!/usr/bin/env python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print each row of matrix on its own line, values separated by spaces."""
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()
