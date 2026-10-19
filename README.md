# Calculatrice Flask

Projet fait dans le cadre du TP3 du cours LOG3000.

## Équipe

Groupe 18

- Lune-Ève Orius
- Dylan Rakoto
- Ethan Van Gelder

## Description du projet

C'est une calculatrice web faite en Python avec Flask. On entre une opération avec les boutons de la page, par exemple 8+2, et le serveur calcule le résultat avant de l'afficher.

La calculatrice fait une seule opération à la fois entre deux nombres. Les opérations possibles sont l'addition, la soustraction, la multiplication et la division. Elle ne gère pas les calculs avec plusieurs opérateurs comme 2+3*4, les parenthèses ou les nombres négatifs.

L'objectif est d'avoir une calculatrice fiable et un projet bien organisé. Pour ça, on documente le code, on ajoute des tests et on corrige les bogues en suivant un processus clair avec des branches, des issues et des pull requests.

## Structure du projet

- `app.py` lance le serveur Flask, lit l'expression envoyée par la page et fait le calcul
- `operators.py` contient les fonctions des quatre opérations
- `templates/` contient la page HTML de la calculatrice (voir [templates/README.md](templates/README.md))
- `static/` contient le fichier CSS (voir [static/README.md](static/README.md))

## Installation

Il faut avoir Python 3.9 ou plus récent, pip et Git.

1. Cloner le dépôt avec `git clone https://github.com/dylan5r/TP3---LOG3000.git`
2. Aller dans le dossier du projet avec `cd TP3---LOG3000`
3. Installer Flask avec `python -m pip install flask`

## Utilisation

1. Dans le dossier du projet, lancer le serveur avec `python app.py`
2. Ouvrir http://127.0.0.1:5000 dans un navigateur
3. Cliquer sur un premier nombre, un opérateur (+, -, *, /), puis un deuxième nombre
4. Appuyer sur = pour voir le résultat dans l'affichage
5. Appuyer sur C pour vider l'affichage et commencer un nouveau calcul

Si le calcul n'est pas valide, par exemple 8+ ou 8+2+3, un message qui commence par Error s'affiche à la place du résultat.

Pour arrêter le serveur, il faut faire Ctrl+C dans le terminal.

## Tests

Les tests seront dans le dossier `tests/`.

1. Installer pytest avec `python -m pip install pytest`
2. À la racine du projet, lancer les tests avec `python -m pytest`

## Flux de contribution

On ne travaille jamais directement sur `main`. Chaque changement passe par une issue, une branche et une pull request.

1. Issue. Chaque bogue ou tâche est décrit dans une issue GitHub avec les étapes pour le reproduire. L'issue est assignée à un membre de l'équipe.
2. Branche. On crée une branche pour chaque issue à partir de `main` à jour, avec `git checkout main`, `git pull` puis `git checkout -b fix/nom-du-bogue`. On utilise `fix/` pour un bogue et `docs/` pour de la documentation.
3. Commits. Les messages de commit expliquent clairement ce qui a été changé et pourquoi.
4. Pull request. On ouvre une pull request vers main et on lie l'issue correspondante dans la description. Un autre membre relit le code et vérifie que les tests passent avant de fusionner.
