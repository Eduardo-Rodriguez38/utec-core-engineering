#!/usr/bin/env python3
"""Módulo con la función safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Imprime solo los enteros de los primeros x elementos de my_list."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
