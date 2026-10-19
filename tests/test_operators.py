import pytest
from operators import add, subtract, multiply, divide

# ==================================================
# Tests d'addition
# ==================================================


def test_add_positive_numbers():
    assert add(5, 3) == 8


def test_add_negative_numbers():
    assert add(-5, -3) == -8


def test_add_positive_and_negative():
    assert add(5, -3) == 2


def test_add_with_zero():
    assert add(5, 0) == 5


def test_add_decimal_numbers():
    assert add(2.5, 1.5) == 4.0


def test_add_small_decimals():
    assert add(0.001, 0.002) == pytest.approx(0.003)



# ==================================================
# Tests de soustraction
# ==================================================

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_positive_and_negative():
    assert subtract(5, -3) == 8


def test_subtract_negative_and_positive():
    assert subtract(-5, 3) == -8


def test_subtract_from_zero():
    assert subtract(0, 5) == -5


def test_subtract_decimal_numbers():
    assert subtract(5.5, 2.5) == 3.0




# ==================================================
# Tests de multiplication
# ==================================================

def test_multiply_positive_numbers():
    assert multiply(5, 3) == 15


def test_multiply_negative_numbers():
    assert multiply(-5, -3) == 15


def test_multiply_positive_and_negative():
    assert multiply(5, -3) == -15


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_by_one():
    assert multiply(5, 1) == 5


def test_multiply_decimal_numbers():
    assert multiply(2.5, 1.5) == 3.75



# ==================================================
# Tests de division
# ==================================================

def test_divide_positive_numbers():
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    assert divide(-6, -3) == 2


def test_divide_positive_and_negative():
    assert divide(6, -3) == -2


def test_divide_decimal_result():
    assert divide(7, 2) == 3.5


def test_divide_smaller_by_larger():
    assert divide(2, 5) == 0.4


def test_divide_zero_by_number():
    assert divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
