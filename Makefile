install:
	poetry install

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

help:
	poetry run gendiff --help

.PHONY: install test lint selfcheck check build help