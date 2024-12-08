import pytest
from fizzbuzz import fizzbuzz

def test_fizz_for_multiples_of_3():
  assert fizzbuzz(3) == "Fizz"
