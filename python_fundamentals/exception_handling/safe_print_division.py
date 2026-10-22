#!/usr/bin/env python3
"""Módulo con la función safe_print_division."""


def safe_print_division(a, b):
    """Divide a entre b y siempre imprime el resultado dentro de finally."""
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
