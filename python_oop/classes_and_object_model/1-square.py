#!/usr/bin/env python3
"""Module that defines a Square class with a private size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of the square's side.
        """
        self.__size = size
