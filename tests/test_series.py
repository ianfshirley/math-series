import pytest
import pytest_watch
from math_series.series import fibonacci, lucas, sum_series


# def test_hello():
#     assert test() == "hello"


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(6) == 8


def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(6) == 18


def test_sum():
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(3) == 2
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(3, 2, 1) == 4

