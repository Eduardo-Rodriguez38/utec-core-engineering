#!/usr/bin/env python3
"""Módulo que define la clase Square."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Cuadrado: un rectángulo con ancho y altura iguales."""

    def __init__(self, size):
        """Inicializa el cuadrado validando size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
