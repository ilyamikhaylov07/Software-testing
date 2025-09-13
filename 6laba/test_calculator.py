import pytest
from calculator import Calculator

calc = Calculator()

# --- add ---
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 5, 4),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add(a, b, expected):
    assert calc.add(a, b) == expected


# --- divide ---
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (-15, -3, 5),
    (7, 2, 3.5)
])
def test_divide(a, b, expected):
    assert calc.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


# --- is_prime_number ---
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (1, False),
    (0, False),
    (-5, False)
])
def test_is_prime_number(n, expected):
    assert calc.is_prime_number(n) == expected
