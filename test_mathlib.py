# test_math_utils.py
import pytest
from mathlib import square, factorial, is_prime, gcd, lcm

def test_square():
    assert square(5) == 25
    assert square(-3) == 9
    assert square(0) == 0

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert not is_prime(1)

def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5

def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(7, 13) == 91
    assert lcm(0, 5) == 0