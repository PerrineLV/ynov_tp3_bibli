from .book import Book
from .user import User

class Library:
    """Gestionnaire de bibliothèque"""
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def borrow_book(self, user, isbn):
        """Gère l'emprunt d'un livre par un utilisateur."""
        book = self.find_book_by_isbn(isbn)
        if not book:
            return False  # Livre non trouvé
        if not user.can_borrow():
            return False  # Limite d'emprunt atteinte
        if not book.is_available():
            return False  # Livre déjà emprunté
        if book.borrow():
            user.add_borrowed_book(book)
            return True
        return False

