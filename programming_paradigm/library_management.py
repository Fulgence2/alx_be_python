class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
    def _is_checked_out(self):
        return hasattr(self, 'checked_out') and self.checked_out
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_available_books(self):
        """List all available books in the library."""
        for book in self.books:
            if not book._is_checked_out():
                print(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.books:
            if book.title == title and not book._is_checked_out():
                book.checked_out = True
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self.books:
            if book.title == title and book._is_checked_out():
                del book.checked_out
                print(f"Returned: {book}")
                return
        print(f"Book '{title}' was not checked out.")
# This code defines a simple library management system with classes for Book and Library.