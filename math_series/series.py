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


def sum_series(n, opt1=0, opt2=1):
    """
    takes in a number n, and 2 optional arguments opt1 & opt2. If no optional parameters are entered,
    it will return the nth value of the fibonacci sequence of numbers. If optional parameters are 2 & 1,
    it will return the nth value of the lucas sequence of numbers.
    """
    if n == 0:
        return opt1
    elif n == 1:
        return opt2
    else:
        return sum_series(n-1, opt1, opt2) + sum_series(n-2, opt1, opt2)


