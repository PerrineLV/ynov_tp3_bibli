import pytest
from src.book import Book

@pytest.fixture
def book():
    """Fixture : prépare un livre pour chaque test"""
    return Book(title="1984", author="George Orwell", isbn="1234567890123")

class TestBookCreation:
    """Tests de création de livre"""

    def test_create_valid_book(self):
        """Test création livre valide"""
        book = Book(title="1984", author="George Orwell", isbn="1234567890123")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.isbn == "1234567890123"

    def test_create_book_empty_title(self):
        """Test titre vide lève une erreur"""
        with pytest.raises(ValueError):
            Book(title="", author="George Orwell", isbn="1234567890123")

    def test_create_book_invalid_isbn_raises_error(self):
        """Test ISBN invalide lève une erreur"""
        with pytest.raises(ValueError):
            Book(title="1984", author="George Orwell", isbn="123")
        with pytest.raises(ValueError):
            Book(title="1984", author="George Orwell", isbn="12345678901234")

class TestBookBorrowing:
    """Tests d'emprunt de livre"""

    def test_new_book_is_available(self, book):
        """Test livre neuf disponible"""
        assert book.is_available()

    def test_borrow_available_book_success(self, book):
        """Test emprunt livre disponible"""
        assert book.borrow()
        assert not book.is_available()
        assert not book.is_available()

    def test_borrow_already_borrowed_book_fails(self, book):
        """Test emprunt livre déjà emprunté"""
        book.borrow()
        assert not book.borrow()
        assert not book.is_available()

    def test_return_book_not_borrowed_fails(self, book):
        """Test retour livre non emprunté"""
        assert not book.return_book()
        assert book.is_available()

    def test_return_borrowed_book_success(self, book):
        """Test retour livre emprunté"""
        book.borrow()
        assert book.return_book()
        assert book.is_available()