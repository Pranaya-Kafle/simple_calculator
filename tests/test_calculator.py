import pytest
from calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    calculate_hypotenuse,
    calculate_power,
    calculate_remainder
)

# --- Tests for the Professor's 4 Functions ---

@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (5, 25)
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 3),
    (3, 6)
])
def test_triNums(n, expected):
    assert triNums(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 2),
    (2, 4),
    (3, 7)
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected

@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, 5),
    (3, 15)
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


# --- Tests for your 3 New Functions ---

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 5.0),
    (5, 12, 13.0),
    (8, 15, 17.0)
])
def test_calculate_hypotenuse(a, b, expected):
    assert calculate_hypotenuse(a, b) == expected

@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 2, 25),
    (10, 0, 1)
])
def test_calculate_power(base, exponent, expected):
    assert calculate_power(base, exponent) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (15, 4, 3),
    (20, 5, 0)
])
def test_calculate_remainder(a, b, expected):
    assert calculate_remainder(a, b) == expected