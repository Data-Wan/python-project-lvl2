install:
	poetry install

lint:
	poetry run flake8 calculate_diff

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

help:
	poetry run gendiff --help

test:
	poetry run pytest calculate_diff tests --cov=calculate_diff --cov-report xml

.PHONY: install test lint selfcheck check build help