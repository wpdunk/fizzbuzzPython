import pytest

import fizzbuzz

def test_hello_world():
    assert fizzbuzz.hello_world() == 'hello world'

@pytest.mark.parametrize("input1, input2 ,expected", [
    (5, 5, True),
    (5, 6, False),
])

def test_divisible(input1, input2, expected):
    assert fizzbuzz.divisible(input1, input2) == expected

@pytest.mark.parametrize("input1 ,expected", [
    (30, True),
    (20, False),
])

def test_divisibleByFifteen(input1, expected):
    assert fizzbuzz.divisibleByFifteen(input1) == expected
