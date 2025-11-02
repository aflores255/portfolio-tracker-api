# 🚀 Quick Start Guide

## 📋 Introduction

This guide will help you get started with Portfolio Tracker API.

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- Poetry
- Git
- PostgreSQL 14+
- Redis (optional, for caching)

### Quick Installation

```bash
# Clone repository
git clone https://github.com/aflores255/portfolio-tracker-api.git
cd portfolio-tracker-api

# Install dependencies
make install

# Setup environment
cp env.template .env
# Edit .env with your configuration

# Run initial setup
make setup

# Run tests
make test
```

## 🚀 Basic Usage

### Starting the API Server

```bash
# Development mode with hot reload
make dev

# Or using uvicorn directly
poetry run uvicorn src.portfolio_tracker.main:app --reload
```

The API will be available at: `http://localhost:8000`

- **API Documentation (Swagger)**: `http://localhost:8000/docs`
- **Alternative Documentation (ReDoc)**: `http://localhost:8000/redoc`

### Example API Usage

```python
# Example: Using the API with requests
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Create a portfolio (authentication required)
headers = {"Authorization": "Bearer YOUR_TOKEN"}
data = {
    "name": "My Investment Portfolio",
    "description": "Long-term investments"
}
response = requests.post(
    "http://localhost:8000/api/v1/portfolios",
    json=data,
    headers=headers
)
print(response.json())
```

### Using Helper Functions

```python
# Example: Using utility functions
from src.portfolio_tracker.utils.helpers import generate_response, paginate_query

# Generate API response
response = generate_response(
    data={"message": "Success"},
    message="Operation completed"
)

# Calculate pagination
offset, limit = paginate_query(page=1, page_size=10)
```

## 🗄️ Database Setup

```bash
# Run migrations
make migrate

# Create a new migration
make create-migration

# Rollback last migration
make rollback
```

## 🐳 Using Docker

```bash
# Start all services (API, PostgreSQL, Redis)
make docker-up

# View logs
make docker-logs

# Stop services
make docker-down
```

## 🧪 Running Tests

```bash
# Run all tests with coverage
make test

# Run only unit tests
make test-unit

# Run only integration tests
make test-integration
```

## 📚 Additional Documentation

- [API Reference](api-reference.md)
- [Database Schema](database-schema.md)
- [Architecture](architecture.md)
- [Deployment Guide](deployment.md)
- [Contributing](../CONTRIBUTING.md)

## 🆘 Troubleshooting

### Common Issues

**Port 8000 already in use:**
```bash
# Change port in command
poetry run uvicorn src.portfolio_tracker.main:app --reload --port 8001
```

**Database connection error:**
- Verify PostgreSQL is running
- Check credentials in `.env` file
- Ensure database exists

**Import errors:**
- Run `poetry install` again
- Verify you're using the correct Python version (3.11+)

## 📞 Support

- Create an issue on GitHub for bugs
- Check existing documentation
- Review examples in the repository

