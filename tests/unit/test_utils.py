"""
Unit tests for utilities.
"""

import pytest

from src.portfolio_tracker.utils import exceptions
from src.portfolio_tracker.utils.helpers import (
    generate_error_response,
    generate_response,
)


class TestHelpers:
    """Tests for helper functions."""

    def test_generate_response(self):
        """Test response generation."""
        result = generate_response(data={"test": "value"}, message="Success")
        assert result["data"] == {"test": "value"}
        assert result["message"] == "Success"
        assert "meta" in result
        assert "timestamp" in result["meta"]

    def test_generate_error_response(self):
        """Test error response generation."""
        result = generate_error_response(
            code="TEST_ERROR", message="Test error message", field="test_field"
        )
        assert result["data"] is None
        assert len(result["errors"]) == 1
        assert result["errors"][0]["code"] == "TEST_ERROR"
        assert result["errors"][0]["field"] == "test_field"


class TestExceptions:
    """Tests for custom exceptions."""

    def test_portfolio_tracker_exception(self):
        """Test base exception."""
        with pytest.raises(exceptions.PortfolioTrackerException):
            raise exceptions.PortfolioTrackerException("Test error")

    def test_validation_exception(self):
        """Test validation exception."""
        with pytest.raises(exceptions.ValidationException):
            raise exceptions.ValidationException("Validation error", field="test_field")
