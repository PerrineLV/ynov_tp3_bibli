class Book:
    """Représente un livre dans la bibliothèque."""

    def __init__(self, title, author, isbn):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Le titre doit être une chaîne non vide.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("L'auteur doit être une chaîne non vide.")
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("L'ISBN doit être une chaîne non vide.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False
        pass

    def is_available(self):
        return not self.borrowed
        pass

    def borrow(self):
        if self.borrowed:
            return False
        self.borrowed = True
        return True
        pass

    def return_book(self):
        if not self.borrowed:
            return False
        self.borrowed = False
        return True
        pass