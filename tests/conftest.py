"""
Configuración pytest (fixtures compartidas).
"""

import pytest


@pytest.fixture
def ejemplo_fixture():
    """Fixture de ejemplo para tests."""
    return {"data": "test"}


@pytest.fixture
def config_mock():
    """Fixture con configuración de ejemplo."""
    return {"setting1": "value1", "setting2": "value2"}
