"""
Script de configuración inicial del proyecto.
"""

import sys
from pathlib import Path


def main() -> int:
    """
    Ejecutar configuración inicial.
    
    Returns:
        Código de salida (0 = éxito)
    """
    print("🚀 Configuración inicial del proyecto")
    
    # Crear directorios necesarios
    directories = ["logs", "cache", "data"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directorio creado: {directory}")
    
    print("✨ Configuración inicial completada")
    return 0


if __name__ == "__main__":
    sys.exit(main())

