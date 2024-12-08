import pytest
import random
from fizzbuzz import fizzbuzz

MULTIPLES_OF_15 = [15 * x for x in range(1, 67)]
MULTIPLES_OF_3 = [3 * x for x in range(1, 334) if 3 * x not in MULTIPLES_OF_15]
MULTIPLES_OF_5 = [5 * x for x in range(1, 201) if 5 * x not in MULTIPLES_OF_15]
EXCLUDED_NUMBERS = set(MULTIPLES_OF_3) | set(MULTIPLES_OF_5) | set(MULTIPLES_OF_15)
OTHER_NUMBERS = list(set(range(1, 1001)) - EXCLUDED_NUMBERS)

def test_fizz_for_multiples_of_3():
  for _ in range(3):
    n = random.choice(MULTIPLES_OF_3)
    print(f"Testing Fizz for: {n}")
    assert fizzbuzz(n) == "Fizz", f"Failed for input: {n}"

def test_buzz_for_multiples_of_5():
  for _ in range(3):
    n = random.choice(MULTIPLES_OF_5)
    print(f"Testing Buzz for: {n}")
    assert fizzbuzz(n) == "Buzz", f"Failed for input: {n}"

def test_fizzbuzz_for_multiples_of_15():
  for _ in range(3):
    n = random.choice(MULTIPLES_OF_15)
    print(f"Testing FizzBuzz for: {n}")
    assert fizzbuzz(n) == "FizzBuzz", f"Failed for input: {n}"

def test_return_number_as_string_for_other_numbers():
  for _ in range(3):
    n = random.choice(OTHER_NUMBERS)
    print(f"Testing Other Number for: {n}")
    assert fizzbuzz(n) == str(n), f"Failed for input: {n}"
