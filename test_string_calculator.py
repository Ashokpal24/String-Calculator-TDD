import pytest
from string_calculator import stringCalculator


def test_empty_string_returns_zero():
    calc = stringCalculator()
    assert calc.add("") == 0


def test_single_number():
    calc = stringCalculator()
    assert calc.add("5") == 5
