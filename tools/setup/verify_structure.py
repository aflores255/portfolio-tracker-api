"""
Script para verificar la estructura del proyecto.
"""

import sys
from pathlib import Path


def verify_structure() -> bool:
    """
    Verificar que la estructura del proyecto sea correcta.
    
    Returns:
        True si la estructura es correcta, False en caso contrario
    """
    required_dirs = [
        "src",
        "tests",
        "docs"
    ]
    
    required_files = [
        "pyproject.toml",
        "README.md",
        ".gitignore"
    ]
    
    errors = []
    
    # Verificar directorios
    for directory in required_dirs:
        if not Path(directory).exists():
            errors.append(f"❌ Directorio faltante: {directory}")
        else:
            print(f"✅ Directorio encontrado: {directory}")
    
    # Verificar archivos
    for file in required_files:
        if not Path(file).exists():
            errors.append(f"❌ Archivo faltante: {file}")
        else:
            print(f"✅ Archivo encontrado: {file}")
    
    if errors:
        print("\n⚠️  Errores encontrados:")
        for error in errors:
            print(f"  {error}")
        return False
    
    print("\n✨ Estructura del proyecto verificada correctamente")
    return True


def main() -> int:
    """
    Función principal del script de verificación.
    
    Returns:
        Código de salida (0 = éxito, 1 = error)
    """
    if verify_structure():
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

