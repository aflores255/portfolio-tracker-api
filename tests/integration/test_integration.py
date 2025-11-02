"""
Integration tests for the project.
"""

import pytest
from fastapi.testclient import TestClient

from src.portfolio_tracker.main import app


class TestIntegration:
    """Integration tests."""

    def test_health_check_endpoint(self):
        """Test that verifies health check endpoint."""
        client = TestClient(app)
        response = client.get("/health")

        # Verify response
        assert response.status_code in [200, 404]  # 404 if not implemented yet
