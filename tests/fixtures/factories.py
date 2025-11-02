"""
Factories para crear objetos de prueba.
"""

from typing import Any, Dict


def create_test_config(**overrides: Any) -> Dict[str, Any]:
    """
    Crear configuración de prueba.

    Args:
        **overrides: Valores a sobrescribir

    Returns:
        Diccionario de configuración
    """
    default = {"setting1": "default_value1", "setting2": "default_value2"}
    default.update(overrides)
    return default
