# Name: Madison Lovett
# Student number: A01292253


def my_sum(x: float, y: float) -> float:
    """A wrapper for adding two numbers.

    :param x: First addend
    :param y: Second addend
    :returns: The sum

    >>> val = my_sum(16.0, 4.0)
    >>> print(val)
    20.0
    """
    return x + y


def my_multiply(x: float, y: float) -> float:
    """A wrapper for multiplying two numbers.

    :param x: First factor
    :param y: Second factor
    :returns: The product

    >>> val = my_multiply(16.0, 4.0)
    >>> print(val)
    64.0
    """
    return x * y


def my_divide(x: float, y: float) -> float:
    """A wrapper for dividing two numbers.

    :param x: A dividend
    :param y: A divisor
    :returns: The quotient

    >>> val = my_divide(16.0, 4.0)
    >>> print(val)
    4.0
    """
    return x / y


def my_subtract(x: float, y: float) -> float:
    """A wrapper for subtracting one number with another.

    :param x: A minuend
    :param y: A subtrahend
    :returns: The difference

    >>> val = my_subtract(16.0, 4.0)
    >>> print(val)
    12.0
    """
    return x - y


def main():
    """Entry point for app."""
    first_value = float(input("enter first number: "))
    second_value = float(input("enter second number: "))

    print("1 to add\n2 to subtract\n3 to multiply\n4 to divide")
    response = int(input())

    if response == 1:
        return print(my_sum(first_value, second_value))

    elif response == 2:
        return print(my_subtract(first_value, second_value))

    elif response == 3:
        return print(my_multiply(first_value, second_value))

    elif response == 4:
        return print(my_divide(first_value, second_value))

    else:
        print("Invalid choice, please choose between 1 and 4.")


if __name__ == '__main__':
    main()
