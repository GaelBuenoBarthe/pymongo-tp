# DigiLibrairie

DigiLibrairie est une application Python pour gérer une bibliothèque numérique. Elle permet aux utilisateurs d'effectuer diverses opérations sur les auteurs et les livres, telles que la création, la mise à jour, la suppression et la recherche.

## Prérequis

- Python 3.x
- `pip` (gestionnaire de paquets Python)
- MongoDB

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/GaelBuenoBarthe/pymongo-tp.git
    cd pymongo
    ```

2. Créez un environnement virtuel :
    ```sh
    python -m venv .venv
    ```

3. Activez l'environnement virtuel :
    - Sur Windows :
        ```sh
        .venv\Scripts\activate
        ```
    - Sur macOS/Linux :
        ```sh
        source .venv/bin/activate
        ```

4. Installez les paquets requis :
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Mettez à jour la configuration MongoDB dans `config.py` :
```python
# Configuration de la base de données
MONGO_URI = 'mongodb://localhost:27017/'
DATABASE_NAME = 'library'
```

## Utilisation
Executez l'application principale :
```sh
python main.py
```
## Fonctionnalitées
Opérations sur les auteurs :  
Créer un auteur
Modifier un auteur
Supprimer un auteur
Trouver un auteur par nom
Opérations sur les livres :  
Créer un livre
Modifier un livre
Supprimer un livre
Trouver des livres par auteur
Trouver des livres publiés après une certaine année
Trouver des livres par mot-clé
Opérations d'agrégation :  
Compter les livres par catégorie
Calculer le prix moyen par catégorie
Compter les livres par année
Trouver la catégorie avec le prix moyen le plus élevé
Compter les livres par auteur