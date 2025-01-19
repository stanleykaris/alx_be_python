class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f'You have checked out "{self.title}" by {self.author}.'
        return f'"{self.title}" is already checked out.'

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f'You have returned "{self.title}" by {self.author}.'
        return f'"{self.title}" was not checked out.'

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f'Book "{title}" not found in the library.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f'Book "{title}" not found in the library.'

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return "Available books:\n" + "\n".join(available_books)
        return "No books are available."