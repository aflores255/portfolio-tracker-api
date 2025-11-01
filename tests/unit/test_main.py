"""
Tests unitarios para el módulo principal.
"""

import pytest
from src.nombre_paquete import ClasePrincipal, utilidad_principal


class TestClasePrincipal:
    """Tests para ClasePrincipal."""
    
    def test_creacion_instancia(self):
        """Test que verifica la creación de instancia."""
        instancia = ClasePrincipal()
        assert instancia is not None
    
    def test_metodo_principal(self):
        """Test que verifica el método principal."""
        instancia = ClasePrincipal()
        resultado = instancia.metodo_principal()
        assert resultado == "Funcionalidad principal ejecutada correctamente"
    
    def test_configurar(self):
        """Test que verifica la configuración."""
        instancia = ClasePrincipal()
        config = {"key": "value"}
        instancia.configurar(config)
        assert instancia.obtener_configuracion() == config


class TestUtilidadPrincipal:
    """Tests para utilidad_principal."""
    
    def test_utilidad_principal_exitoso(self):
        """Test que verifica el procesamiento exitoso."""
        resultado = utilidad_principal("test")
        assert resultado == "Procesado: test"
    
    def test_utilidad_principal_parametro_vacio(self):
        """Test que verifica el error con parámetro vacío."""
        with pytest.raises(ValueError):
            utilidad_principal("")

