from database import get_database
from pymongo import errors

# Fonction pour insérer un auteur
def insert_author(author):
    db = get_database()
    authors_collection = db['authors']
    try:
        authors_collection.insert_one(author)
        print(f"Auteur '{author['name']}' inseré avec succés.")
    except errors.DuplicateKeyError:
        print(f"L'auteur '{author['name']}' existe déja.")

# Fonction pour modifier un auteur
def update_author(name, new_data):
    db = get_database()
    authors_collection = db['authors']
    result = authors_collection.update_one({"name": name}, {"$set": new_data})
    if result.matched_count > 0:
        print(f"Auteur '{name}' modifié avec succés.")
    else:
        print(f"Auteur '{name}' non trouvé.")

# Fonction pour supprimer un auteur
def delete_author(name):
    db = get_database()
    authors_collection = db['authors']
    result = authors_collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Auteur '{name}' supprimé avec succés.")
    else:
        print(f"Auteur '{name}' non trouvé.")

# Fonction pour trouver un auteur par nom
def find_author_by_name(name):
    db = get_database()
    authors_collection = db['authors']
    author = authors_collection.find_one({"name": name})
    return author