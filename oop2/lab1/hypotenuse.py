# Name: Madison Lovett
# Student number: A01292253

"""Module for calculating the hypotenuse of a right triangle."""

import math


def hypotenuse(length: float, height: float) -> float:
    """Calculate the hypotenuse of a right triangle.

    :param length: The length of one leg of the triangle
    :param height: The height (other leg) of the triangle
    :returns: The hypotenuse of the right triangle

    >>> val = hypotenuse(3.0, 4.0)
    >>> print(val)
    5.0
    """
    return math.sqrt(length ** 2 + height ** 2)


if __name__ == "__main__":
    result = hypotenuse(3, 4)
    print(result)
