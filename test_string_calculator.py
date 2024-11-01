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


def test_custom_delimiter():
    calc = stringCalculator()
    assert calc.add("//;\n1;2") == 3


def test_negative_numbers():
    calc = stringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: -1,-3"):
        calc.add("1,-1,2,-3")


def test_ignore_number_greater_than_1000():
    calc = stringCalculator()
    assert calc.add("2000,2") == 2
    assert calc.add("2,1001") == 2


def test_more_len_delimiter():
    calc = stringCalculator()
    assert calc.add("//[***]\n1***2***3") == 6


def test_diff_delimiter():
    calc = stringCalculator()
    assert calc.add("//[*][%]\n1*2%3") == 6


def test_diff_delimiter_with_varied_len():
    calc = stringCalculator()
    assert calc.add("//[****][%]\n17****10%3") == 30


def test_only_negative_numbers():
    calc = stringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: -1,-2"):
        calc.add("-1,-2")


def test_multiple_delimiters_no_numbers():
    calc = stringCalculator()
    assert calc.add("//[*][%]\n") == 0


def test_mixed_large_and_small_numbers():
    calc = stringCalculator()
    assert calc.add("1000,1001,2") == 1002
