install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff --fix

test:
	uv run pytest

test-cov:
	uv run pytest --cov

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
