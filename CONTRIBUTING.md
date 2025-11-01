# Contributing to [Nombre del Proyecto]

¡Gracias por tu interés en contribuir a este proyecto! Este documento proporciona guías para contribuir.

## 📋 Cómo Contribuir

### 1. Fork del Repositorio
1. Haz fork del repositorio en GitHub
2. Clona tu fork localmente:
   ```bash
   git clone https://github.com/tu-usuario/[nombre-proyecto].git
   cd [nombre-proyecto]
   ```

### 2. Configurar Entorno de Desarrollo
```bash
# Instalar dependencias
make install

# Configurar pre-commit hooks
pre-commit install

# Configurar variables de entorno
cp env.template .env
# Editar .env con tu configuración
```

### 3. Crear una Rama
```bash
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

### 4. Hacer Cambios
- Sigue los estándares de código del proyecto
- Añade tests para nueva funcionalidad
- Actualiza documentación si es necesario
- Ejecuta tests antes de commitear:
  ```bash
  make test
  make lint
  ```

### 5. Commit
```bash
git add .
git commit -m "feat: añadir nueva funcionalidad"
```

Usa [Conventional Commits](https://www.conventionalcommits.org/) para mensajes de commit.

### 6. Push y Pull Request
```bash
git push origin feature/nueva-funcionalidad
```

Luego crea un Pull Request en GitHub.

## 📝 Estándares de Código

### Python
- Seguir PEP 8
- Usar type hints
- Documentar funciones y clases
- Cobertura de tests mínima: 80%

### Commits
- Usar Conventional Commits
- Mensajes claros y descriptivos
- Un commit por cambio lógico

### Tests
- Tests unitarios para nueva funcionalidad
- Tests de integración cuando sea apropiado
- Mantener cobertura de código

## 🐛 Reportar Bugs

1. Verificar que el bug no haya sido reportado
2. Crear un issue con:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Información del entorno

## 💡 Solicitar Funcionalidades

1. Verificar que la funcionalidad no haya sido solicitada
2. Crear un issue con:
   - Descripción detallada de la funcionalidad
   - Casos de uso
   - Justificación del valor

## 📚 Documentación

- Actualizar README.md si es necesario
- Documentar APIs públicas
- Añadir ejemplos de uso
- Actualizar CHANGELOG.md

## 🤝 Proceso de Review

1. Todos los PRs requieren review
2. Tests deben pasar
3. Código debe seguir estándares
4. Documentación debe estar actualizada

## 📞 Soporte

- Crear un issue para preguntas
- Revisar documentación existente
- Consultar ejemplos en el repositorio

