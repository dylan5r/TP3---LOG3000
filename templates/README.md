# templates

Ce dossier contient les pages HTML de l'application. C'est la partie que l'utilisateur voit dans son navigateur. Flask utilise ces fichiers pour construire la page qu'il renvoie à chaque requête.

## Fichiers

- `index.html` est la seule page de l'application. Elle contient l'affichage en haut, les boutons des chiffres de 0 à 9, les opérateurs (+, -, *, /), le bouton . pour les nombres décimaux, le bouton C pour effacer et le bouton = pour calculer. Elle contient aussi deux fonctions JavaScript, `appendToDisplay` qui ajoute le caractère d'un bouton à l'affichage et `clearDisplay` qui vide l'affichage. Si on clique sur un chiffre juste après =, `appendToDisplay` vide d'abord l'affichage pour commencer un nouveau calcul.

Quand on appuie sur =, le formulaire envoie l'expression au serveur avec une requête POST. Le serveur fait le calcul et renvoie la même page avec le résultat dans l'affichage.

## Dépendances et hypothèses

- La page est affichée par la fonction `index()` de `app.py`, qui lui envoie les variables `result` et `equals_pressed`.
- Le champ de l'affichage doit garder le nom `display`, parce que `app.py` lit l'expression avec ce nom.
- Le style vient de `static/style.css`.
