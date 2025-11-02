# Contributing to Portfolio Tracker API

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## 📋 How to Contribute

### 1. Fork the Repository
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/portfolio-tracker-api.git
   cd portfolio-tracker-api
   ```

### 2. Setup Development Environment
```bash
# Install dependencies
make install

# Setup environment variables
cp env.template .env
# Edit .env with your configuration

# Run initial setup
make setup

# Verify installation
make test
```

### 3. Create a Branch
```bash
git checkout -b feature/new-feature
# or
git checkout -b fix/bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions/updates

### 4. Make Changes
- Follow project code standards
- Add tests for new functionality
- Update documentation as needed
- Run tests before committing:
  ```bash
  make test
  make format
  make lint-fast
  ```

### 5. Commit
```bash
git add .
git commit -m "feat: add new feature"
```

Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Test additions/updates
- `chore:` - Maintenance tasks

### 6. Push and Pull Request
```bash
git push origin feature/new-feature
```

Then create a Pull Request on GitHub with:
- Clear description of changes
- Reference to related issues
- Screenshots (if UI changes)
- Test results

## 📝 Code Standards

### Python
- Follow PEP 8 style guide
- Use type hints for all function signatures
- Document all public functions and classes (Google style docstrings)
- Minimum test coverage: 80%
- Line length: 88 characters (Black default)

### Code Structure
- **Repository Pattern**: Data access layer
- **Service Layer**: Business logic
- **API Routes**: HTTP endpoints (FastAPI)
- **Models**: Database models (SQLAlchemy) and schemas (Pydantic)

### Naming Conventions
- Files: `snake_case.py`
- Classes: `PascalCase`
- Functions/Variables: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private methods: `_leading_underscore`

### Example Code

```python
"""
Module docstring explaining purpose.
"""

from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    """
    User data schema.
    
    Attributes:
        email: User email address
        username: Unique username
    """
    
    email: str
    username: str
    is_active: bool = True


async def get_user_by_id(user_id: int) -> Optional[UserSchema]:
    """
    Retrieve user by ID.
    
    Args:
        user_id: Unique user identifier
        
    Returns:
        User object if found, None otherwise
        
    Raises:
        UserNotFoundException: If user does not exist
    """
    # Implementation here
    pass
```

### Commits
- Use Conventional Commits format
- Clear and descriptive messages
- One logical change per commit
- Reference issues when applicable

### Tests
- Unit tests for all new functionality
- Integration tests for API endpoints
- Use pytest fixtures for test data
- Follow AAA pattern (Arrange, Act, Assert)
- Mock external dependencies

Example test:
```python
def test_should_create_user_when_valid_data():
    """Test user creation with valid data."""
    # Arrange
    user_data = {"email": "test@example.com", "username": "testuser"}
    
    # Act
    result = create_user(user_data)
    
    # Assert
    assert result.email == user_data["email"]
    assert result.is_active is True
```

## 🐛 Reporting Bugs

1. Check if bug has already been reported
2. Create an issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment information (OS, Python version, etc.)
   - Error messages and stack traces
   - Screenshots if applicable

## 💡 Requesting Features

1. Check if feature has already been requested
2. Create an issue with:
   - Detailed feature description
   - Use cases and examples
   - Value proposition
   - Potential implementation approach (optional)

## 📚 Documentation

- Update README.md if needed
- Document all public APIs
- Add usage examples
- Update CHANGELOG.md for notable changes
- Keep docstrings up to date
- Update relevant `.md` files in `docs/` directory

## 🧪 Testing

### Running Tests

```bash
# All tests with coverage
make test

# Unit tests only
make test-unit

# Integration tests only
make test-integration

# Watch mode (runs on file changes)
make test-watch
```

### Coverage Requirements

- Minimum 80% coverage for new code
- All new features must have tests
- Critical paths should have 100% coverage

## 🤝 Review Process

1. All PRs require review before merging
2. All tests must pass (CI/CD)
3. Code must follow project standards
4. Documentation must be updated
5. No merge conflicts
6. At least one approval from maintainer

### Review Checklist

- [ ] Code follows style guidelines
- [ ] Tests are included and passing
- [ ] Documentation is updated
- [ ] No security vulnerabilities introduced
- [ ] Performance impact considered
- [ ] Breaking changes documented

## 🔒 Security

- Never commit secrets, API keys, or passwords
- Use environment variables for sensitive data
- Report security vulnerabilities privately
- Follow security best practices

## 📞 Support

- Create an issue for questions
- Review existing documentation
- Check examples in the repository
- Join community discussions

## 🎉 Recognition

Contributors will be recognized in:
- CHANGELOG.md for notable contributions
- README.md contributors section
- GitHub contributor graph

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

---

Thank you for contributing to Portfolio Tracker API! 🚀

