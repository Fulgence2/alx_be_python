class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize the book's title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly string that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (you can comment this out for unit testing or production)
if __name__ == "__main__":
    b = Book("1984", "George Orwell", 1949)
    print(str(b))   # Output: 1984 by George Orwell, published in 1949
    print(repr(b))  # Output: Book('1984', 'George Orwell', 1949)
    del b           # Output: Deleting 1984