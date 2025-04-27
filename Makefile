install:
	uv sync

package:
	uv tool install dist/*.whl

run:
	uv run hexlet-gendiff

test:
	uv run pytest

lint:
	uv run ruff check

build:
	uv build

