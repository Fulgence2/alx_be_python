class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
        self.books = []

    def __str__(self):
        return f"{self.title} by {self.author}"

    def is_checked_out(self):
        return self.checked_out

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        return False

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return True
        return False
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.check_out():
                print(f"You have checked out '{book.title}'.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.return_book():
                print(f"You have returned '{book.title}'.")
                return
        print(f"'{title}' was not checked out.")
def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()
if __name__ == "__main__":
    main()
# This code defines a simple library management system with classes for Book and Library.