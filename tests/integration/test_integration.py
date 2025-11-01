"""
Tests de integración para el proyecto.
"""

import pytest
from src.nombre_paquete import ClasePrincipal


class TestIntegration:
    """Tests de integración."""
    
    def test_flujo_completo(self):
        """Test que verifica un flujo completo de uso."""
        instancia = ClasePrincipal()
        
        # Configurar
        instancia.configurar({"setting1": "value1"})
        
        # Ejecutar método principal
        resultado = instancia.metodo_principal()
        
        # Verificar
        assert resultado is not None
        assert instancia.obtener_configuracion()["setting1"] == "value1"

