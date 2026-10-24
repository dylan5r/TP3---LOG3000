
import pytest
from app import app, calculate


# ==================================================
# Tests de calculate()
# ==================================================

#Tests des opérations arithmétiques

def test_calculate_addition():
    """Vérifie le calcul d'une addition."""
    assert calculate("8+2") == 10

def test_calculate_decimal_operands():
    """Vérifie que les opérandes décimaux sont acceptés."""
    assert calculate("2.5+1.5") == 4.0


def test_calculate_subtraction():
    """Vérifie le calcul d'une soustraction."""
    assert calculate("8-2") == 6


def test_calculate_multiplication():
    """Vérifie le calcul d'une multiplication."""
    assert calculate("8*2") == 16


def test_calculate_division_integer():
    """Vérifie une division dont le résultat est entier."""
    assert calculate("8/2") == 4.0


def test_calculate_division_decimal():
    """Vérifie une division dont le résultat est décimal."""
    assert calculate("7/2") == 3.5

def test_calculate_division_by_zero():
    """Vérifie qu'une division par zéro déclenche une exception."""
    with pytest.raises(ZeroDivisionError):
        calculate("5/0")


# Tests des espaces

def test_calculate_with_spaces():
    """Vérifie que les espaces entre les opérandes sont ignorés."""
    assert calculate("8 + 2") == 10


def test_calculate_spaces_around_expression():
    """Vérifie que les espaces au début et à la fin sont ignorés."""
    assert calculate("  8+2  ") == 10


# Tests des nombres négatifs

def test_calculate_negative_first_operand():
    """Vérifie qu'un premier opérande négatif est accepté."""
    assert calculate("-5+3") == -2


def test_calculate_negative_second_operand():
    """Vérifie qu'un deuxième opérande négatif est accepté."""
    assert calculate("5+-3") == 2


def test_calculate_two_negative_operands():
    """Vérifie une addition entre deux nombres négatifs."""
    assert calculate("-5+-3") == -8

# Tests des expressions invalides

def test_calculate_empty_expression():
    """Vérifie qu'une expression vide est refusée."""
    with pytest.raises(ValueError):
        calculate("")


def test_calculate_spaces_only():
    """Vérifie qu'une expression contenant uniquement des espaces est refusée."""
    with pytest.raises(ValueError):
        calculate("   ")


def test_calculate_missing_operator():
    """Vérifie qu'une expression sans opérateur est refusée."""
    with pytest.raises(ValueError):
        calculate("53")


def test_calculate_missing_first_operand():
    """Vérifie qu'une expression sans premier opérande est refusée."""
    with pytest.raises(ValueError):
        calculate("+5")


def test_calculate_missing_operand():
    """Vérifie qu'une expression sans deuxième opérande est refusée."""
    with pytest.raises(ValueError):
        calculate("8+")


def test_calculate_multiple_operators():
    """Vérifie qu'une expression contenant plusieurs opérations est refusée."""
    with pytest.raises(ValueError):
        calculate("8+2*3")


def test_calculate_invalid_first_operand():
    """Vérifie qu'un premier opérande non numérique est refusé."""
    with pytest.raises(ValueError):
        calculate("abc+2")


def test_calculate_invalid_second_operand():
    """Vérifie qu'un deuxième opérande non numérique est refusé."""
    with pytest.raises(ValueError):
        calculate("5+abc")


# Tests des types d'entrées incorrects

def test_calculate_none():
    """Vérifie qu'une valeur None est refusée."""
    with pytest.raises(ValueError):
        calculate(None)


def test_calculate_invalid_type():
    """Vérifie qu'une entrée numérique est refusée."""
    with pytest.raises(ValueError):
        calculate(123)

# ==================================================
# Tests des requêtes HTTP
# ==================================================

# Tests des requêtes GET

def test_index_get():
    """Vérifie que la page principale est accessible."""
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_index_get_display_empty():
    """Vérifie que l'affichage est vide au chargement de la page."""
    client = app.test_client()
    response = client.get("/")

    assert b'value=""' in response.data


# Tests des requêtes POST

def test_index_post_addition():
    """Vérifie que le résultat d'une addition est affiché."""
    client = app.test_client()
    response = client.post("/", data={"display": "8+2"})

    assert response.status_code == 200
    assert b'value="10.0"' in response.data


def test_index_post_empty_expression():
    """Vérifie qu'une expression vide produit un message d'erreur."""
    client = app.test_client()
    response = client.post("/", data={"display": ""})

    assert response.status_code == 200
    assert b"Error:" in response.data


def test_index_post_division_by_zero():
    """Vérifie qu'une division par zéro produit un message d'erreur."""
    client = app.test_client()
    response = client.post("/", data={"display": "5/0"})

    assert response.status_code == 200
    assert b"Error:" in response.data


def test_index_post_missing_display():
    """Vérifie qu'une requête sans champ display produit une erreur."""
    client = app.test_client()
    response = client.post("/", data={})

    assert response.status_code == 200
    assert b"Error:" in response.data