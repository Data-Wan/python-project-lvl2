install:
	poetry install

lint:
	poetry run flake8 calculate_diff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

help:
	poetry run gendiff --help

test:
	poetry run tests --cov=calculate_diff --cov-report xml tests/

.PHONY: install test lint selfcheck check build help