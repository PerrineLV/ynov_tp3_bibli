import pytest
from src.library import Library
from src.book import Book
from src.user import User

@pytest.fixture
def library_with_books_and_users():
    """Fixture complexe : bibliothèque avec livres et utilisateurs"""
    library = Library(name="Bibliothèque Municipale")
    book1 = Book(title="Livre 1", author="Auteur 1", isbn="1234567890123")
    book2 = Book(title="Livre 2", author="Auteur 2", isbn="1234567890124")
    book3 = Book(title="Livre 3", author="Auteur 3", isbn="1234567890125")
    user1 = User(name="Toto", email="toto@toto.toto")
    user2 = User(name="Titi", email="titi@titi.titi")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    return library, book1, book2, book3, user1, user2

class TestLibraryOperations:
    def test_borrow_flow_success(self, library_with_books_and_users):
        """Test flux complet d'emprunt réussi"""
        library, book1, _, _, user1, _ = library_with_books_and_users
        assert library.borrow_book(user1, "1234567890123")
        assert not book1.is_available()
        assert user1.can_borrow()
        assert len(user1.borrowed_books) == 1
        assert user1.borrowed_books[0].isbn == "1234567890123"

    def test_user_cannot_borrow_more_than_limit(self, library_with_books_and_users):
        """Test limite d'emprunts par utilisateur"""
        library, _, _, _, user1, _ = library_with_books_and_users
        assert library.borrow_book(user1, "1234567890123")
        assert library.borrow_book(user1, "1234567890124")
        assert library.borrow_book(user1, "1234567890125")
        assert not library.borrow_book(user1, "1234567890126")
        assert user1.borrowed_books[0].isbn == "1234567890123"
        assert user1.borrowed_books[1].isbn == "1234567890124"
        assert user1.borrowed_books[2].isbn == "1234567890125"