#!/usr/bin/env python3
"""
Ejemplo básico de uso de nombre-proyecto.

Este script demuestra el uso básico de las funcionalidades principales.
"""

from src.nombre_paquete import ClasePrincipal, utilidad_principal


def main():
    """Función principal del ejemplo."""
    print("🚀 Ejemplo básico de nombre-proyecto")
    
    # Crear instancia de la clase principal
    instancia = ClasePrincipal()
    
    # Usar funcionalidad principal
    resultado = instancia.metodo_principal()
    print(f"✅ Resultado: {resultado}")
    
    # Configurar instancia
    instancia.configurar({"ejemplo": "configuracion"})
    print(f"📋 Configuración: {instancia.obtener_configuracion()}")
    
    # Usar función de utilidad
    resultado_utilidad = utilidad_principal("test")
    print(f"🔧 Utilidad: {resultado_utilidad}")


if __name__ == "__main__":
    main()

