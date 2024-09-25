from operations.aggregation_operation import find_author_with_books, count_books_by_category, average_price_by_category, \
    count_books_by_year, category_with_highest_average_price, count_books_by_author
from operations.author_operation import insert_author, update_author, delete_author
from operations.book_operation import insert_book, update_book, delete_book, find_books_by_author, \
    find_books_published_after, find_books_by_keyword


def main():
    while True:
        print("DigiLibrairie")
        print("1. Créer un auteur")
        print("2. Modifier un auteur")
        print("3. Supprimer un auteur")
        print("4. Trouver un auteur par nom")
        print("5. Créer un livre")
        print("6. Modifier un livre")
        print("7. Supprimer un livre")
        print("8. Trouver un livre par auteur")
        print("9. Trouver les livres publiés après une année")
        print("10. Trouver un livre par mot-clé")
        print("11. Compter les livres par catégorie")
        print("12. Prix moyen par catégorie")
        print("13. Compter les livres par année")
        print("14. Catégorie avec le prix moyen le plus élevé")
        print("15. Compter les livres par auteur")
        print("16. Sortir")

        choice = input("Entrez votre choix: ")

        if choice == '1':
            while True:
                try:
                    name = input("Entrez le nom de l'auteur: ")
                    birth = input("Entrez sa date de naissance: ")
                    country = input("Entrez son pays: ")
                    insert_author({"name": name, "birth": birth, "country": country})
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '2':
            while True:
                try:
                    name = input("Entrez le nom de l'auteur à modifier: ")
                    new_data = {}
                    new_name = input("Entrez un nouveau nom (laissez vide pour passer à l'étape suivante): ")
                    if new_name:
                        new_data["name"] = new_name
                    new_birth = input("Entrez une nouvelle date de naissance (laissez vide pour passer à l'étape suivante): ")
                    if new_birth:
                        new_data["birth"] = new_birth
                    new_country = input("Entrez un nouveau pays (laissez vide pour passer à l'étape suivante): ")
                    if new_country:
                        new_data["country"] = new_country
                    update_author(name, new_data)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '3':
            while True:
                try:
                    name = input("Entrez le nom de l'auteur à supprimer: ")
                    delete_author(name)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '4':
            while True:
                try:
                    name = input("Entrez le nom de l'auteur que vous recherchez: ")
                    author_with_books = find_author_with_books(name)
                    print(author_with_books)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '5':
            while True:
                try:
                    title = input("Entrez le titre du livre: ")
                    author = input("Entrez l'auteur du livre: ")
                    year = int(input("Entrez l'année du livre: "))
                    category = input("Entrez la categorie du livre: ")
                    price = float(input("Entrez le prix du livre: "))
                    insert_book({"title": title, "author": author, "year": year, "category": category, "price": price})
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '6':
            while True:
                try:
                    title = input("Entrez le titre du livre à modifier: ")
                    new_data = {}
                    new_title = input("Entrez le nouveau titre (laissez vide pour passer à l'étape suivante): ")
                    if new_title:
                        new_data["title"] = new_title
                    new_author = input("Entrez le nouvel auteur (laissez vide pour passer à l'étape suivante): ")
                    if new_author:
                        new_data["author"] = new_author
                    new_year = input("Entrez la nouvelle année (laissez vide pour passer à l'étape suivante): ")
                    if new_year:
                        new_data["year"] = new_year
                    new_category = input("Entrez la nouvelle categorie (laissez vide pour passer à l'étape suivante): ")
                    if new_category:
                        new_data["category"] = new_category
                    new_price = input("Entrez le nouveau prix (laissez vide pour passer à l'étape suivante): ")
                    if new_price:
                        new_data["price"] = float(new_price)
                    update_book(title, new_data)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '7':
            while True:
                try:
                    title = input("Entrez le titre du livre à supprimer: ")
                    delete_book(title)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '8':
            while True:
                try:
                    author = input("Entrez le nom de l'auteur pour trouver les livres qu'il a écrits: ")
                    books = find_books_by_author(author)
                    for book in books:
                        print(book)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '9':
            while True:
                try:
                    year = int(input("Entrez l'année minimale de sortie des livres que vous cherchez: "))
                    books = find_books_published_after(year)
                    for book in books:
                        print(book)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '10':
            while True:
                try:
                    keyword = input("Entrez un mot-clé du livre que vous cherchez: ")
                    books = find_books_by_keyword(keyword)
                    for book in books:
                        print(book)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '11':
            while True:
                try:
                    categories = count_books_by_category()
                    for category in categories:
                        print(category)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '12':
            while True:
                try:
                    avg_prices = average_price_by_category()
                    for avg_price in avg_prices:
                        print(avg_price)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '13':
            while True:
                try:
                    years = count_books_by_year()
                    for year in years:
                        print(year)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '14':
            while True:
                try:
                    highest_avg_price = category_with_highest_average_price()
                    for category in highest_avg_price:
                        print(category)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '15':
            while True:
                try:
                    authors = count_books_by_author()
                    for author in authors:
                        print(author)
                    break
                except Exception as e:
                    print(f"Erreur: {e}. Veuillez réessayer.")
        elif choice == '16':
            break
        else:
            print("Choix invalide. Veuillez recommencer")

if __name__ == "__main__":
    main()