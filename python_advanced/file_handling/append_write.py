#!/usr/bin/env python3
"""Módulo con una función para añadir texto a un archivo."""


def append_write(filename="", text=""):
    """Añade text al final de un archivo UTF-8 y devuelve los caracteres."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
