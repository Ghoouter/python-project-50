install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml
