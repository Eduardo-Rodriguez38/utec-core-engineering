#!/usr/bin/env python3
"""Module that defines a Square class with size, position and __str__."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: the length of the square's side (default 0).
            position: tuple (x, y) used to offset the printed square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square drawn with # as a string."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        lines = [""] * y
        lines += [" " * x + "#" * self.__size] * self.__size
        return "\n".join(lines)

    def my_print(self):
        """Print the square with the # character."""
        print(self)
