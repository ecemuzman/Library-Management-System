class Library:

    def list_books(self):
        with open("books.txt", "a+") as file:
            file.seek(0)
            books = file.read().splitlines()

        if not books:
            print("There is no book in the list.")
        else:
            for book in books:
                print(book)

    def add_book(self):
        name = input("Book Name: ")
        author = input("Author: ")
        year = input("Release Year: ")
        pages = input("Pages: ")

        with open("books.txt", "a") as file:
            file.write(f"{name}, {author}, {year}, {pages}\n")

    def remove_book(self):
        name = input("Book Name: ")

        with open("books.txt", "r") as file:
            books = file.read().splitlines()

        new_books = []
        removed = False

        for book in books:
            book_name = book.split(",")[0].strip()
            if book_name.lower() != name.lower():
                new_books.append(book)
            else:
                removed = True

        with open("books.txt", "w") as file:
            for book in new_books:
                file.write(book + "\n")

        if removed:
            print(f"Book '{name}' removed successfully.")
        else:
            print(f"Book '{name}' not found.")
