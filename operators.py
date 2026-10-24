"""Opérations de base de la calculatrice.

Chaque fonction prend deux nombres et retourne le résultat d'une opération.
Ces fonctions sont utilisées par app.py pour faire le calcul.
"""


def add(a,b):
    """Additionne deux nombres.

    Entrées
        a (float) le premier nombre
        b (float) le deuxième nombre

    Sortie
        float, la somme a + b
    """
    return a + b

def subtract(a,b):
    """Soustrait le deuxième nombre du premier.

    Entrées
        a (float) le premier nombre
        b (float) le nombre à enlever de a

    Sortie
        float, la différence a - b
    """
    return a - b

def multiply(a,b):
    """Multiplie deux nombres.

    Entrées
        a (float) le premier nombre
        b (float) le deuxième nombre

    Sortie
        float, le produit a * b
    """
    return a * b

def divide(a,b):
    """Divise le premier nombre par le deuxième.

    Entrées
        a (float) le nombre à diviser
        b (float) le diviseur, il ne doit pas être 0

    Sortie
        float, le résultat de la division a / b
    """
    return a / b
