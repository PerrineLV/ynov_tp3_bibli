import pytest
from src.book import Book

class TestBookCreation:
    """Tests de création de livre"""

    def test_create_valid_book(self):
        """Test création livre valide"""
        book = Book(title="1984", author="George Orwell", isbn="1234567890123")
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.isbn == "1234567890123"

    def test_create_book_empty_title_raises_error(self):
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

    def setup_method(self):
        """Fixture : prépare un livre pour chaque test"""
        self.book = Book(title="1984", author="George Orwell", isbn="1234567890123")

    def test_new_book_is_available(self):
        """Test livre neuf disponible"""
        assert self.book.is_available()

    def test_borrow_available_book_success(self):
        """Test emprunt livre disponible"""
        assert self.book.borrow()
        assert not self.book.is_available()
        assert not self.book.is_available()

    def test_borrow_already_borrowed_book_fails(self):
        """Test emprunt livre déjà emprunté"""
        self.book.borrow()
        assert not self.book.borrow()
        assert not self.book.is_available()