.PHONY: install db-up db-down run test lint format typecheck check

install:
	uv sync

db-up:
	docker compose up -d db

db-down:
	docker compose down

run:
	uv run uvicorn handa.api.main:app --reload

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src

check: lint typecheck test
