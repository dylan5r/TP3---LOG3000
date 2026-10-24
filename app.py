"""Serveur Flask de la calculatrice.

Ce fichier crée l'application web. Il reçoit l'expression envoyée par la page,
fait le calcul avec les fonctions de operators.py et renvoie le résultat à la page.
Pour lancer le serveur, il faut exécuter python app.py.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Chaque symbole de la calculatrice est relié à sa fonction dans operators.py
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Calcule le résultat d'une expression simple comme "8+2".

    L'expression doit contenir deux nombres et un seul opérateur (+, -, * ou /).

    Entrées
        expr (str) l'expression à calculer, les espaces sont permis

    Sortie
        float, le résultat du calcul

    Erreurs
        ValueError si l'expression est vide, s'il y a plus d'un opérateur,
        s'il manque l'opérateur ou un des deux nombres, ou si un des deux
        côtés n'est pas un nombre
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # On enlève les espaces pour que "8 + 2" donne le même résultat que "8+2"
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # La calculatrice fait une seule opération à la fois, donc on refuse un deuxième opérateur
    for i, ch in enumerate(s):
        t=str(ch)
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch
   
    # Il faut au moins un caractère de chaque côté de l'opérateur
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format"+t)
    
    left = s[:op_pos]
    right = s[op_pos+1:]

    # On utilise float pour accepter aussi les nombres décimaux comme 2.5
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et calcule le résultat quand on appuie sur =.

    Entrées
        Aucun paramètre. Pour une requête POST, l'expression est lue dans
        le champ "display" du formulaire.

    Sortie
        La page index.html avec le résultat du calcul, un message d'erreur
        ou un affichage vide si c'est une requête GET
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On affiche l'erreur dans la calculatrice au lieu de faire planter la page
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # debug=True recharge le serveur à chaque modification, c'est seulement pour le développement
    app.run(debug=True)
