# Makefile for Python project

install:
	pip install -r requirements.txt

test:
	pytest

coverage:
	pytest --cov=src --cov-report=html

clean:
	rm -rf htmlcov/ .coverage .pytest_cache/
