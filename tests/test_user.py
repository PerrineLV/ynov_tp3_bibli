import pytest
from src.user import User

@pytest.fixture
def valid_user():
    return User("Alice", "alice@example.com")

@pytest.fixture
def user_with_books():
    user = User("Bob", "bob@example.com")
    user.borrowed_books = [1, 2]
    return user

# Test de la création d'un utilisateur valide
def test_user_creation_valid(valid_user):
    assert valid_user.name == "Alice"
    assert valid_user.email == "alice@example.com"
    assert valid_user.borrowed_books == []

# Test de la création d'un utilisateur avec un nom vide
def test_user_creation_empty_name():
    with pytest.raises(ValueError):
        User("", "alice@example.com")
    with pytest.raises(ValueError):
        User(None, "alice@example.com")
    with pytest.raises(ValueError):
        User("   ", "alice@example.com")

# Test de la création d'un utilisateur avec un email invalide
def test_user_creation_invalid_email():
    with pytest.raises(ValueError):
        User("Alice", "aliceexample.com")
    with pytest.raises(ValueError):
        User("Alice", "")
    with pytest.raises(ValueError):
        User("Alice", None)
    with pytest.raises(ValueError):
        User("Alice", "   ")

# Test de la méthode can_borrow
def test_can_borrow(user_with_books):
    assert user_with_books.can_borrow() is True
    user_with_books.borrowed_books = [1, 2, 3]
    assert user_with_books.can_borrow() is False
    user_with_books.borrowed_books = [1, 2]
    assert user_with_books.can_borrow() is True

# Test de l'ajout d'un livre emprunté
def test_add_borrowed_book(valid_user):
    valid_user.add_borrowed_book("Book1")
    assert "Book1" in valid_user.borrowed_books
    valid_user.add_borrowed_book
    user = User("Dan", "dan@example.com")
    user.add_borrowed_book("Book1")
    user.add_borrowed_book("Book2")
    user.remove_borrowed_book("Book1")
    assert "Book1" not in user.borrowed_books
    user.remove_borrowed_book("Book3")  # Ne doit rien faire si le livre n'est pas emprunté
    assert "Book2" in user.borrowed_books
