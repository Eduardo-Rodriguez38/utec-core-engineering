#!/usr/bin/env python3
"""Módulo con la función safe_print_integer."""


def safe_print_integer(value):
    """Imprime value si es entero y devuelve True, si no devuelve False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
