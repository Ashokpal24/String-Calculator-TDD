import pytest
from string_calculator import stringCalculator


def test_empty_string_returns_zero():
    calc = stringCalculator()
    assert calc.add("") == 0


def test_single_number():
    calc = stringCalculator()
    assert calc.add("5") == 5


def test_two_number():
    calc = stringCalculator()
    assert calc.add("1,2") == 3


def test_newline_delimiter():
    calc = stringCalculator()
    assert calc.add("3\n4,5") == 12
