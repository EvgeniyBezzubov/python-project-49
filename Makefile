install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build
brain-games:
    poetry run brain-games
.PHONY: install test lint selfcheck check build