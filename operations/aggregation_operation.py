from database import get_database

# Fonction pour compter les livres par catégorie
def count_books_by_category():
    db = get_database()
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$category", "total_books": {"$sum": 1}}}
    ]
    return list(books_collection.aggregate(pipeline))

# Fonction pour calculer le prix moyen par catégorie
def average_price_by_category():
    db = get_database()
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$category", "average_price": {"$avg": "$price"}}}
    ]
    return list(books_collection.aggregate(pipeline))

# Fonction pour compter les livres par année
def count_books_by_year():
    db = get_database()
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$year", "total_books": {"$sum": 1}}},
        {"$sort": {"_id": -1}}
    ]
    return list(books_collection.aggregate(pipeline))

# Fonction pour trouver la catégorie avec le prix moyen le plus élevé
def category_with_highest_average_price():
    db = get_database()
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$category", "average_price": {"$avg": "$price"}}},
        {"$sort": {"average_price": -1}},
        {"$limit": 1}
    ]
    return list(books_collection.aggregate(pipeline))

# Fonction pour compter les livres par auteur
def count_books_by_author():
    db = get_database()
    books_collection = db['books']
    pipeline = [
        {"$group": {"_id": "$author", "total_books": {"$sum": 1}}},
        {"$sort": {"total_books": -1}}
    ]
    return list(books_collection.aggregate(pipeline))