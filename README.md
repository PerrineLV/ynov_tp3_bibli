# Projet Bibliothèque

## Installation

Pour installer les dépendances nécessaires, utilisez le Makefile ou pip :

```bash
make install
```
Ou directement :
```bash
pip install -r requirements.txt
```

## Tests

Pour lancer les tests unitaires avec pytest :

```bash
make test
```
Ou directement :
```bash
pytest
```

## Couverture

Pour générer un rapport de couverture de code (HTML) :

```bash
make coverage
```
Le rapport sera disponible dans le dossier `htmlcov/` (ouvrez `htmlcov/index.html` dans votre navigateur).

## Structure

- `src/` : Contient le code source du projet
  - `book.py` : Classe représentant un livre
  - `user.py` : Classe représentant un utilisateur
  - `library.py` : Classe gérant la bibliothèque (livres, utilisateurs, emprunts)
- `tests/` : Contient les tests unitaires pour chaque module
- `requirements.txt` : Dépendances Python du projet
- `Makefile` : Commandes pour installer, tester, générer la couverture, nettoyer
- `htmlcov/` : Rapport de couverture généré automatiquement

Chaque module est testé séparément dans le dossier `tests/`.