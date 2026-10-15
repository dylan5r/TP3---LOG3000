# static

Ce dossier contient les fichiers que Flask envoie tels quels au navigateur, sans les modifier. Dans ce projet, il y a seulement le fichier de style de la calculatrice.

## Fichiers

- `style.css` définit l'apparence de la calculatrice. Il centre la calculatrice dans la page, met l'affichage en haut avec le texte aligné à droite, place les boutons dans une grille de 4 colonnes et met les opérateurs et le bouton = en orange.

## Dépendances et hypothèses

- `style.css` est chargé par `templates/index.html`
- Le CSS utilise les classes et l'id de `index.html` (`.calculator`, `.buttons`, `.btn`, `.operator` et `#display`). Si on change un de ces noms dans le HTML, il faut aussi le changer ici.
