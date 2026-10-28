#!/usr/bin/env python3
"""Módulo que define la clase Rectangle completa."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectángulo definido por su ancho y su altura."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando width y height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripción del rectángulo."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
