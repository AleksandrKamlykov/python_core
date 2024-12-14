import json
from typing import List

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class BookController:

    __filename = "books.json"

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        self.save_books()

    def list_books(self):
        return self.books

    def find_index_by_title(self, title):
        for index, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                return index
        return -1

    def find_index_by_author(self, author):
        for index, book in enumerate(self.books):
            if book.author.lower() == author.lower():
                return index
        return -1


    def find_book_by_name(self, title):
        idx = self.find_index_by_title(title)
        if idx == -1:
            return None

        return self.books[idx]

    def find_book_by_author(self, author):
        idx = self.find_index_by_author(author)
        if idx == -1:
            return None

        return self.books[idx]

    def remove_book(self, title):

        idx = self.find_index_by_title(title)
        if idx == -1:
            return None

        self.save_books()

        return self.books.pop(idx)


    def save_books(self):
        with open(self.__filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def load_books(self):
        try:
            with open(self.__filename, 'r') as file:
                books_data = json.load(file)
                self.books = [Book(**data) for data in books_data]
        except FileNotFoundError:
            self.books = []



class BookView:
    def __init__(self, controller:BookController):
        self.controller = controller
        self.controller.load_books()

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        self.controller.add_book(title, author)

    def list_books(self):
        books = self.controller.list_books()
        for book in books:
            print(book)

    def find_book_by_name(self):
        title = input("Enter the title of the book: ")
        book = self.controller.find_book_by_name(title)
        if book:
            print(book)
        else:
            print("Book not found")

    def find_book_by_author(self):
        author = input("Enter the author of the book: ")
        book = self.controller.find_book_by_author(author)
        if book:
            print(book)
        else:
            print("Book not found")

    def remove_book(self):
        title = input("Enter the title of the book: ")
        book = self.controller.remove_book(title)
        if book:
            print(f"Removed book: {book}")
        else:
            print("Book not found")

    def run(self):

        while True:
            print("1. Add book")
            print("2. List books")
            print("3. Find book by name")
            print("4. Find book by author")
            print("5. Remove book")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.list_books()
            elif choice == "3":
                self.find_book_by_name()
            elif choice == "4":
                self.find_book_by_author()
            elif choice == "5":
                self.remove_book()
            elif choice == "6":
                break
            else:
                print("Invalid choice")

                
controller = BookController()
view = BookView(controller)
view.run()
