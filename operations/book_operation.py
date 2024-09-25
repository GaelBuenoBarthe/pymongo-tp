from database import get_database

# Fonction pour insérer un livre
def insert_book(book):
    db = get_database()
    books_collection = db['books']
    books_collection.insert_one(book)
    print(f"Livre '{book['title']}' crée avec succés.")

# Fonction pour modifier un livre
def update_book(title, new_data):
    db = get_database()
    books_collection = db['books']
    result = books_collection.update_one({"title": title}, {"$set": new_data})
    if result.matched_count > 0:
        print(f"Livre '{title}' modifié avec succés.")
    else:
        print(f"Livre '{title}' non trouvé.")

# Fonction pour supprimer un livre
def delete_book(title):
    db = get_database()
    books_collection = db['books']
    result = books_collection.delete_one({"title": title})
    if result.deleted_count > 0:
        print(f"Livre '{title}' supprimé avec succés.")
    else:
        print(f"Livre '{title}' non trouvé.")

# Fonction pour trouver un livre par auteur
def find_books_by_author(author):
    db = get_database()
    books_collection = db['books']
    books = books_collection.find({"author": author})
    return list(books)

# Fonction pour insérer un auteur
def find_books_published_after(year):
    db = get_database()
    books_collection = db['books']
    books = books_collection.find({"year": {"$gt": year}})
    return list(books)

# Fonction pour trouver un livre par mot-clé
def find_books_by_keyword(keyword):
    db = get_database()
    books_collection = db['books']
    books = books_collection.find({"title": {"$regex": keyword, "$options": "i"}})
    return list(books)