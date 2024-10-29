import pytest
from string_calculator import stringCalculator

# empty 
def test_empty_string_returns_zero():
    calc=stringCalculator()
    assert calc.add("")==0