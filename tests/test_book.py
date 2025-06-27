import unittest
from src.book import Book

class TestBookCreation(unittest.TestCase):
	"""Tests de création de livre"""

	def test_create_valid_book(self):
		"""Test création livre valide"""
		book = Book(title="1984", author="George Orwell", isbn="1234567890123")
		self.assertEqual(book.title, "1984")
		self.assertEqual(book.author, "George Orwell")
		self.assertEqual(book.isbn, "1234567890123")


	def test_create_book_empty_title_raises_error(self):
		"""Test titre vide lève une erreur"""
		with self.assertRaises(ValueError):
			Book(title="", author="George Orwell", isbn="1234567890123")

	def test_create_book_invalid_isbn_raises_error(self):
		"""Test ISBN invalide lève une erreur"""
		with self.assertRaises(ValueError):
			Book(title="1984", author="George Orwell", isbn="123")
		with self.assertRaises(ValueError):
			Book(title="1984", author="George Orwell", isbn="12345678901234")

class TestBookBorrowing(unittest.TestCase):
	"""Tests d'emprunt de livre"""

	def setUp(self):
		"""Fixture : prépare un livre pour chaque test"""
		self.book = Book(title="1984", author="George Orwell", isbn="1234567890123")

	def test_new_book_is_available(self):
		"""Test livre neuf disponible"""
		self.assertTrue(self.book.is_available())

	def test_borrow_available_book_success(self):
		"""Test emprunt livre disponible"""
		self.assertTrue(self.book.borrow())
		self.assertFalse(self.book.is_available())
		self.assertFalse(self.book.is_available())

	def test_borrow_already_borrowed_book_fails(self):
		"""Test emprunt livre déjà emprunté"""
		self.book.borrow()
		self.assertFalse(self.book.borrow())
		self.assertFalse(self.book.is_available())