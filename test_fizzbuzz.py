import pytest
from fizzbuzz import fizzbuzz

def test_fizz_for_multiples_of_3():
  assert fizzbuzz(3) == "Fizz"

def test_buzz_for_multiples_of_5():
  assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz_for_multiples_of_15():
  assert fizzbuzz(15) == "FizzBuzz"

def test_return_number_as_string_for_other_numbers():
  assert fizzbuzz(1) == "1"
  assert fizzbuzz(2) == "2"
  assert fizzbuzz(998) == "997"
  assert fizzbuzz(998) == "998"

