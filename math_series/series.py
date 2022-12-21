import pytest
import pytest_watch


# def test():
#     return "hello"


def fibonacci(n):
    """
    takes in a number n, returns the nth value in the fibonacci sequence of numbers
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    takes in a number n, returns the nth value in the lucas sequence of numbers
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
