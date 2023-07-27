class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Available books in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Matching books:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. {book}")
        else:
            print("No matching books found.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            print("Books by the author:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. {book}")
        else:
            print("No books by the author found.")


def main():
    library = Library()

    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book3 = Book("1984", "George Orwell", 1949)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Welcome to the Digital Library!")

    while True:
        print("\nMenu:")
        print("1. Display all books")
        print("2. Search books by title")
        print("3. Search books by author")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title to search: ")
            library.search_by_title(title)
        elif choice == "3":
            author = input("Enter the author's name to search: ")
            library.search_by_author(author)
        elif choice == "4":
            print("Goodbye! Exiting the Digital Library.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
