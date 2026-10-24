import pytest
from operators import add, subtract, multiply, divide

# ==================================================
# Tests d'addition
# ==================================================

def test_add_positive_numbers():
    """Vérifie l'addition de deux nombres positifs."""
    assert add(5, 3) == 8


def test_add_negative_numbers():
    """Vérifie l'addition de deux nombres négatifs."""
    assert add(-5, -3) == -8


def test_add_positive_and_negative():
    """Vérifie l'addition d'un nombre positif et d'un nombre négatif."""
    assert add(5, -3) == 2


def test_add_with_zero():
    """Vérifie que l'addition avec zéro conserve le nombre initial."""
    assert add(5, 0) == 5


def test_add_decimal_numbers():
    """Vérifie l'addition de deux nombres décimaux."""
    assert add(2.5, 1.5) == 4.0


def test_add_small_decimals():
    """Vérifie l'addition de petits nombres décimaux avec une tolérance."""
    assert add(0.001, 0.002) == pytest.approx(0.003)


# ==================================================
# Tests de soustraction
# ==================================================

def test_subtract_positive_numbers():
    """Vérifie la soustraction de deux nombres positifs."""
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    """Vérifie la soustraction de deux nombres négatifs."""
    assert subtract(-5, -3) == -2


def test_subtract_positive_and_negative():
    """Vérifie la soustraction d'un nombre négatif à un nombre positif."""
    assert subtract(5, -3) == 8


def test_subtract_negative_and_positive():
    """Vérifie la soustraction d'un nombre positif à un nombre négatif."""
    assert subtract(-5, 3) == -8


def test_subtract_from_zero():
    """Vérifie la soustraction d'un nombre positif à zéro."""
    assert subtract(0, 5) == -5


def test_subtract_decimal_numbers():
    """Vérifie la soustraction de deux nombres décimaux."""
    assert subtract(5.5, 2.5) == 3.0


# ==================================================
# Tests de multiplication
# ==================================================

def test_multiply_positive_numbers():
    """Vérifie la multiplication de deux nombres positifs."""
    assert multiply(5, 3) == 15


def test_multiply_negative_numbers():
    """Vérifie la multiplication de deux nombres négatifs."""
    assert multiply(-5, -3) == 15


def test_multiply_positive_and_negative():
    """Vérifie la multiplication d'un nombre positif et d'un nombre négatif."""
    assert multiply(5, -3) == -15


def test_multiply_by_zero():
    """Vérifie que la multiplication par zéro donne zéro."""
    assert multiply(5, 0) == 0


def test_multiply_by_one():
    """Vérifie que la multiplication par un conserve le nombre initial."""
    assert multiply(5, 1) == 5


def test_multiply_decimal_numbers():
    """Vérifie la multiplication de deux nombres décimaux."""
    assert multiply(2.5, 1.5) == 3.75


# ==================================================
# Tests de division
# ==================================================

def test_divide_positive_numbers():
    """Vérifie la division de deux nombres positifs."""
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    """Vérifie la division de deux nombres négatifs."""
    assert divide(-6, -3) == 2


def test_divide_positive_and_negative():
    """Vérifie la division d'un nombre positif par un nombre négatif."""
    assert divide(6, -3) == -2


def test_divide_decimal_result():
    """Vérifie une division dont le résultat est décimal."""
    assert divide(7, 2) == 3.5


def test_divide_smaller_by_larger():
    """Vérifie la division d'un nombre plus petit par un nombre plus grand."""
    assert divide(2, 5) == 0.4


def test_divide_zero_by_number():
    """Vérifie que zéro divisé par un nombre non nul donne zéro."""
    assert divide(0, 5) == 0


def test_divide_by_zero():
    """Vérifie qu'une division par zéro déclenche une ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)