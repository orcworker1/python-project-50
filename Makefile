install:
	uv sync

run:
	uv run hexlet-gendiff

test:
	uv run pytest

lint:
	uv run ruff check

build:
	uv build
