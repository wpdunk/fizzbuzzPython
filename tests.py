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

# test_capitalize.py

# def capital_case(x):
#     return x.capitalize()
#
# def test_capital_case():
#     assert capital_case('semaphore') == 'Semaphore'


# import pytest
#
# def is_even(input):
#     if input % 2 == 0:
#         return True
#     return False
#
# @pytest.mark.parametrize("input,expected", [
#     (2, True),
#     (3, False),
#     (11, False),
# ])
# def test_is_even(input, expected):
#     assert is_even(input) == expected
