class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

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
