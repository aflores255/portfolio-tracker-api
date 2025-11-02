# 💼 Portfolio Tracker API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

RESTful API for investment portfolio management and analysis, built with FastAPI, PostgreSQL, Redis, and Apache Airflow.

---

## 📋 Description

Portfolio Tracker API is a robust backend platform that allows users to manage their investment portfolios, track holdings, record transactions, and analyze investment performance with updated market data.

### ✨ Key Features

- 🔐 **JWT Authentication** - Secure token-based authentication system
- 💰 **Portfolio Management** - Complete CRUD for investment portfolios
- 📊 **Holdings Tracking** - Detailed tracking of positions and assets
- 💸 **Transaction Recording** - Immutable transaction history
- 📈 **Real-Time Analytics** - Performance metrics and risk analysis
- 🔄 **Automatic Updates** - Market prices updated via Airflow
- ⚡ **Performance** - Redis caching for fast queries
- 🐳 **Containerized** - Deployment with Docker and Kubernetes

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | FastAPI 0.104+ |
| **Database** | PostgreSQL 16 |
| **ORM** | SQLAlchemy 2.0 (async) |
| **Migrations** | Alembic |
| **Cache** | Redis 7 |
| **Orchestration** | Apache Airflow |
| **Authentication** | JWT (PyJWT) |
| **Validation** | Pydantic 2.5+ |
| **Testing** | pytest + pytest-asyncio |
| **Code Quality** | black, isort, flake8, mypy |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Poetry** (dependency manager)
- **PostgreSQL 16** (local or Docker)
- **Redis** (optional, for caching)
- **Git**

### Installation

```bash
# 1. Clone repository
git clone https://github.com/aflores255/portfolio-tracker-api.git
cd portfolio-tracker-api

# 2. Install dependencies
make install
# Or manually: poetry install

# 3. Configure environment variables
cp env.template .env
# Edit .env with your configuration

# 4. Start PostgreSQL (with Docker - optional)
docker run --name portfolio-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=portfolio_tracker \
  -p 5432:5432 \
  -d postgres:16

# 5. Apply migrations (once created - Step 2)
make migrate

# 6. Start development server
make dev
```

### Verify Installation

```bash
# Health check
curl http://localhost:8000/health

# Interactive documentation (Swagger)
# Open in browser: http://localhost:8000/api/v1/docs

# Alternative documentation (ReDoc)
# Open in browser: http://localhost:8000/api/v1/redoc
```

---

## 📖 Usage

### API Structure

```
/api/v1/
├── /auth           - Authentication (login, register)
├── /users          - User management
├── /portfolios     - Portfolio CRUD
├── /holdings       - Position management
├── /transactions   - Transaction recording
└── /analytics      - Metrics and analysis
```

### Usage Example

```python
import httpx

# Create client
client = httpx.AsyncClient(base_url="http://localhost:8000/api/v1")

# Register user
response = await client.post("/auth/register", json={
    "email": "user@example.com",
    "password": "secure_password",
    "name": "John Doe"
})

# Login and get token
response = await client.post("/auth/login", json={
    "email": "user@example.com",
    "password": "secure_password"
})
token = response.json()["access_token"]

# Create portfolio (authenticated)
headers = {"Authorization": f"Bearer {token}"}
response = await client.post("/portfolios", headers=headers, json={
    "name": "My Portfolio",
    "description": "Long-term investments",
    "currency": "USD"
})
```

---

## 🛠️ Available Commands

### Development

```bash
make dev              # Start FastAPI server (localhost:8000)
make run              # Alias for 'make dev'
make help             # View all available commands
```

### Testing

```bash
make test             # Run all tests with coverage
make test-unit        # Unit tests only
make test-integration # Integration tests only
make test-e2e         # End-to-end tests only
```

### Code Quality

```bash
make format           # Format code (black + isort)
make lint             # Check linting (black, isort, flake8, mypy)
```

### Database

```bash
make migrate          # Apply pending migrations
make create-migration # Create new migration
make rollback         # Rollback last migration
```

### Docker

```bash
make docker-up        # Start all services
make docker-down      # Stop all services
make docker-logs      # View logs in real-time
make docker-build     # Build images
```

### Other

```bash
make clean            # Clean temporary files and cache
make build            # Build package
make requirements     # Export requirements.txt
```

---

## 🧪 Testing

The project maintains a minimum coverage of 80% and follows the AAA pattern (Arrange, Act, Assert).

```bash
# Run all tests
poetry run pytest

# With coverage report
poetry run pytest --cov=src/portfolio_tracker --cov-report=html

# View HTML report
open htmlcov/index.html  # macOS/Linux
start htmlcov/index.html # Windows
```

**Test Structure:**
- `tests/unit/` - Unit tests (isolated logic, mocks)
- `tests/integration/` - Integration tests (real DB, APIs)
- `tests/e2e/` - End-to-end tests (complete workflows)

---

## 📚 Documentation

- 📘 [Architecture](docs/architecture.md) - System design and technical decisions
- 📗 [API Reference](docs/api-reference.md) - Endpoint documentation
- 📙 [Database Schema](docs/database-schema.md) - Database schema
- 📕 [Development Guide](docs/development.md) - Development guide
- 📓 [Deployment](docs/deployment.md) - Deployment instructions
- 📔 [Getting Started](docs/getting-started.md) - Beginner tutorial

---

## 🏛️ Architecture

The project follows a **layered architecture** with separation of concerns:

```
┌─────────────────────────────────────────┐
│         API Layer (FastAPI)             │  ← Routers, endpoints
├─────────────────────────────────────────┤
│       Service Layer (Business Logic)    │  ← Business logic
├─────────────────────────────────────────┤
│    Repository Layer (Data Access)       │  ← Data access
├─────────────────────────────────────────┤
│         Models (Domain + ORM)           │  ← Models and schemas
├─────────────────────────────────────────┤
│      Database (PostgreSQL + Redis)      │  ← Persistence
└─────────────────────────────────────────┘
```

**Principles:**
- ✅ **DRY** (Don't Repeat Yourself)
- ✅ **SOLID** principles
- ✅ **Repository Pattern** for data access
- ✅ **Dependency Injection** for testing
- ✅ **Async/Await** for I/O operations

---

## 🔐 Security

- 🔒 JWT tokens for authentication
- 🔑 Passwords hashed with bcrypt
- 🛡️ Rate limiting on public endpoints
- 🌐 CORS properly configured
- 🚫 SQL injection prevention (ORM)
- ✅ Input validation with Pydantic

---

## 🚢 Deployment

### Docker Compose (Local/Staging)

```bash
docker-compose up -d
```

### Kubernetes (Production)

```bash
kubectl apply -f deploy/k8s/
```

See [docs/deployment.md](docs/deployment.md) for more details.

---

## 🤝 Contributing

Contributions are welcome. Please:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

### Code Conventions

- **Formatting**: `black` (line length 88)
- **Import sorting**: `isort` (profile black)
- **Type hints**: Mandatory (mypy strict)
- **Docstrings**: Google style
- **Tests**: Minimum 80% coverage

---

## 📋 Roadmap

### Phase 1 - MVP (Current)
- [x] Base project structure
- [x] FastAPI + SQLAlchemy setup
- [ ] Database models
- [ ] JWT authentication system
- [ ] Basic CRUD (users, portfolios, holdings, transactions)
- [ ] Unit and integration tests
- [ ] Docker Compose

### Phase 2 - Features
- [ ] Airflow for price updates
- [ ] Advanced analytics
- [ ] Redis caching
- [ ] Rate limiting
- [ ] Email notifications
- [ ] CI/CD with GitHub Actions

### Phase 3 - Production
- [ ] Kubernetes deployment
- [ ] Monitoring (Prometheus/Grafana)
- [ ] Centralized logging
- [ ] Performance optimization
- [ ] Complete documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **aflores255** - *Initial work* - [aflores255](https://github.com/aflores255)

---

## 📞 Support

Need help? 

- 🐛 [Report a bug](https://github.com/aflores255/portfolio-tracker-api/issues)
- 💡 [Request a feature](https://github.com/aflores255/portfolio-tracker-api/issues)
- 📖 [Read the documentation](docs/)

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations

---

**⭐ If you like this project, give it a star on GitHub!**
