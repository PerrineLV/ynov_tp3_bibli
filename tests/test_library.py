import pytest
from src.library import Library
from src.book import Book
from src.user import User

class TestLibraryOperations:
	def setup_method(self):
		"""Fixture complexe : bibliothèque avec livres et utilisateurs"""
		self.library = Library(name="Bibliothèque Municipale")
		self.book1 = Book(title="Livre 1", author="Auteur 1", isbn="1234567890123")
		self.book2 = Book(title="Livre 2", author="Auteur 2", isbn="1234567890124")
		self.book3 = Book(title="Livre 3", author="Auteur 3", isbn="1234567890125")
		self.user1 = User(name="Toto", email="toto@toto.toto")
		self.user2 = User(name="Titi", email="titi@titi.titi")
		self.library.add_book(self.book1)
		self.library.add_book(self.book2)
		self.library.add_book(self.book3)
		pass

	def test_borrow_flow_success(self):
		"""Test flux complet d'emprunt réussi"""
		# Empruntez un livre
		assert self.library.borrow_book(self.user1, "1234567890123")
		# Vérifiez tous les changements d'état
		assert not self.book1.is_available()
		assert self.user1.can_borrow()
		assert len(self.user1.borrowed_books) == 1
		assert self.user1.borrowed_books[0].isbn == "1234567890123"

	def test_user_cannot_borrow_more_than_limit(self):
		"""Test limite d'emprunts par utilisateur"""
		# Faites emprunter 3 livres (limite)
		assert self.library.borrow_book(self.user1, "1234567890123")
		assert self.library.borrow_book(self.user1, "1234567890124")
		assert self.library.borrow_book(self.user1, "1234567890125")
		# Tentez un 4ème emprunt
		assert not self.library.borrow_book(self.user1, "1234567890126")
		# Vérifiez que c'est refusé
		assert self.user1.borrowed_books[0].isbn == "1234567890123"
		assert self.user1.borrowed_books[1].isbn == "1234567890124"
		assert self.user1.borrowed_books[2].isbn == "1234567890125"