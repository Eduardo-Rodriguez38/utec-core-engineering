#!/usr/bin/env python3
"""Módulo con una función para escribir en un archivo de texto."""


def write_file(filename="", text=""):
    """Escribe text en un archivo UTF-8 y devuelve los caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
