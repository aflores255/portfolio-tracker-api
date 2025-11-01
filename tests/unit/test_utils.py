"""
Tests unitarios para utilidades.
"""

import pytest
from src.nombre_paquete.utils import exceptions
from src.nombre_paquete.utils.helpers import (
    chunk_list,
    merge_dicts,
    sanitize_string
)


class TestHelpers:
    """Tests para funciones auxiliares."""
    
    def test_sanitize_string(self):
        """Test sanitización de strings."""
        assert sanitize_string("  test  ") == "test"
    
    def test_merge_dicts(self):
        """Test combinación de diccionarios."""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3}
        result = merge_dicts(dict1, dict2)
        assert result == {"a": 1, "b": 2, "c": 3}
    
    def test_chunk_list(self):
        """Test división de lista en chunks."""
        items = [1, 2, 3, 4, 5]
        chunks = chunk_list(items, 2)
        assert chunks == [[1, 2], [3, 4], [5]]


class TestExceptions:
    """Tests para excepciones personalizadas."""
    
    def test_nombre_proyecto_error(self):
        """Test excepción base."""
        with pytest.raises(exceptions.NombreProyectoError):
            raise exceptions.NombreProyectoError("Test error")
    
    def test_configuracion_error(self):
        """Test excepción de configuración."""
        with pytest.raises(exceptions.ConfiguracionError):
            raise exceptions.ConfiguracionError("Config error")

