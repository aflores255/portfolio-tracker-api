"""
Unit tests for main module.
"""

import pytest

from src.portfolio_tracker.main import app


class TestApp:
    """Tests for FastAPI application."""

    def test_app_creation(self):
        """Test that verifies app instance creation."""
        assert app is not None
        assert app.title == "Portfolio Tracker API"

    def test_app_version(self):
        """Test that verifies app version."""
        assert app.version == "1.0.0"

    def test_app_has_routes(self):
        """Test that verifies app has routes configured."""
        routes = [route.path for route in app.routes]
        assert "/docs" in routes
        assert "/openapi.json" in routes
