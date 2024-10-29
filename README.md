# String Calculator

A Python implementation of the String Calculator Kata, following Test-Driven Development (TDD) principles. This project calculates the sum of numbers in a string format, supporting multiple and custom delimiters, as well as error handling for negative numbers.

## Features

- **Basic Sum Calculation**: Adds up numbers separated by commas or newlines
- **Custom Delimiters**: Supports single and multiple custom delimiters, including delimiters with varied lengths
- **Negative Number Handling**: Raises an error if negative numbers are present
- **Number Filtering**: Ignores numbers greater than 1000 in the sum

## Requirements

- Python 3.6 or higher
- `pytest` for running tests

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd string-calculator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The `StringCalculator` class provides an `add()` method that takes a string and returns the sum of numbers within it.

### Examples

```python
from string_calculator import StringCalculator

calc = StringCalculator()

# Basic usage with commas
print(calc.add("1,2,3"))  # Output: 6

# Using newline as delimiter
print(calc.add("3\n4,5"))  # Output: 12

# Custom delimiter
print(calc.add("//;\n1;2"))  # Output: 3

# Multiple custom delimiters
print(calc.add("//[*][%]\n1*2%3"))  # Output: 6

# Custom delimiters with different lengths
print(calc.add("//[***][%%]\n1***2%%3"))  # Output: 6

# Handling negative numbers (raises ValueError)
try:
    print(calc.add("1,-1,2,-3"))
except ValueError as e:
    print(e)  # Output: Negatives not allowed: -1,-3
```

## Tests

The project includes a comprehensive suite of tests that can be run with `pytest`. These tests cover all features and edge cases.

1. Run Tests:

   ```bash
   pytest
   ```

2. Test Coverage:
   The tests include cases for:
   - Empty and single-number inputs
   - Basic comma and newline delimiters
   - Custom and multiple delimiters of varied lengths
   - Negative number handling
   - Ignoring numbers greater than 1000

### Example Test Cases

You can find the test cases in `tests/test_string_calculator.py`. Below are a few examples of the tests included:

```python
def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.add("") == 0

def test_single_number():
    calc = StringCalculator()
    assert calc.add("5") == 5

def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3

def test_negative_numbers():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: -1,-3"):
        calc.add("1,-1,2,-3")
```

## License

This project is licensed under the MIT License.

### AUTHOR

Ashok
