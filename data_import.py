import json
import os
from database import get_database
from pymongo import MongoClient, errors
from config import MONGO_URI, DATABASE_NAME

def create_collections_with_validation():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # Validateur pour la collection authors
    author_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "birth"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "birth": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                }
            }
        }
    }

    # Validateur pour la collection books
    book_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["title", "author", "year"],
            "properties": {
                "title": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "author": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "year": {
                    "bsonType": "int",
                    "description": "must be an integer and is required"
                }
            }
        }
    }

    # Crée la collection avec le validateur si elle n'existe pas
    if "authors" not in db.list_collection_names():
        db.create_collection("authors", validator=author_validator)
        db["authors"].create_index("name", unique=True)
    else:
        db.command("collMod", "authors", validator=author_validator)

    if "books" not in db.list_collection_names():
        db.create_collection("books", validator=book_validator)
    else:
        db.command("collMod", "books", validator=book_validator)

def import_data():
    create_collections_with_validation()
    db = get_database()
    books_collection = db['books']
    authors_collection = db['authors']

    # Construction du chemin du fichier JSON
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'ressources', 'tp3_library_data_en.json')

    # Ouverture du fichier JSON avec encodage UTF-8
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Insertion dans la base de données
    books_collection.insert_many(data['books'])
    try:
        authors_collection.insert_many(data['authors'])
    except errors.BulkWriteError as bwe:
        for error in bwe.details['writeErrors']:
            if error['code'] == 11000:  # Duplicate key error
                print(f"Duplicate author found: {error['errmsg']}")
    print("Data importées avec succès.")

if __name__ == "__main__":
    import_data()