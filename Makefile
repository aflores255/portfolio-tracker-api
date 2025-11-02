.PHONY: install test lint format build clean setup verify run dev migrate create-migration rollback docker-up docker-down docker-logs docker-build

# Instalación
install:
	poetry install
	poetry run pre-commit install

# Setup inicial
setup:
	poetry run portfolio-tracker-setup

# Verificación
verify:
	poetry run portfolio-tracker-verify

# Desarrollo - FastAPI
dev:
	poetry run uvicorn src.portfolio_tracker.main:app --reload --host 0.0.0.0 --port 8000

run: dev

# Testing
test:
	poetry run pytest tests/ -v --cov=src/portfolio_tracker --cov-report=html --cov-report=term-missing

test-unit:
	poetry run pytest tests/unit/ -v

test-integration:
	poetry run pytest tests/integration/ -v

test-e2e:
	poetry run pytest tests/e2e/ -v

test-watch:
	poetry run ptw tests/ -- -v

# Code Quality
lint:
	poetry run black --check src/ tests/
	poetry run isort --check-only src/ tests/
	poetry run flake8 src/ tests/
	poetry run mypy src/
	poetry run pylint src/
	poetry run bandit -r src/

lint-fast:
	poetry run black --check src/ tests/
	poetry run isort --check-only src/ tests/
	poetry run flake8 src/ tests/

format:
	poetry run black src/ tests/
	poetry run isort src/ tests/

# Database - Alembic Migrations
migrate:
	poetry run alembic upgrade head

create-migration:
	@read -p "Enter migration message: " msg; \
	poetry run alembic revision --autogenerate -m "$$msg"

rollback:
	poetry run alembic downgrade -1

migration-history:
	poetry run alembic history

# Docker
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-build:
	docker-compose build

docker-restart:
	docker-compose restart

# Limpieza
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf logs/
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete

# Build
build:
	poetry build

# Export requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	poetry export -f requirements.txt --output requirements-dev.txt --with dev --without-hashes

# Help
help:
	@echo "Portfolio Tracker API - Makefile Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install          - Install dependencies and setup pre-commit"
	@echo "  make setup            - Run initial project setup"
	@echo ""
	@echo "Development:"
	@echo "  make dev              - Start FastAPI development server"
	@echo "  make run              - Alias for 'make dev'"
	@echo ""
	@echo "Testing:"
	@echo "  make test             - Run all tests with coverage"
	@echo "  make test-unit        - Run unit tests only"
	@echo "  make test-integration - Run integration tests only"
	@echo "  make test-e2e         - Run end-to-end tests only"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint             - Run all linters (check only)"
	@echo "  make format           - Format code with black and isort"
	@echo ""
	@echo "Database:"
	@echo "  make migrate          - Apply database migrations"
	@echo "  make create-migration - Create new migration"
	@echo "  make rollback         - Rollback last migration"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-up        - Start all Docker services"
	@echo "  make docker-down      - Stop all Docker services"
	@echo "  make docker-logs      - View Docker logs"
	@echo "  make docker-build     - Build Docker images"
	@echo ""
	@echo "Other:"
	@echo "  make clean            - Remove build artifacts and cache"
	@echo "  make build            - Build package"
	@echo "  make requirements     - Export requirements.txt files"

