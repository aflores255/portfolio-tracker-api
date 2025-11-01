# 🚀 Guía de Despliegue

## Requisitos Previos

- Python 3.11+
- Poetry
- Acceso al servidor de despliegue

## Instalación en Producción

### 1. Preparar Entorno

```bash
# Clonar repositorio
git clone <repository-url>
cd nombre-proyecto

# Instalar dependencias
poetry install --no-dev

# Configurar variables de entorno
cp env.template .env
# Editar .env con configuración de producción
```

### 2. Configurar Aplicación

```bash
# Ejecutar migraciones si aplica
poetry run nombre-proyecto-migrate --run

# Verificar estructura
poetry run nombre-proyecto-verify
```

### 3. Desplegar

```bash
# Construir paquete
poetry build

# O usar Docker si está configurado
make docker-prod
```

## Configuración de Producción

### Variables de Entorno Importantes

- `LOG_LEVEL`: Nivel de logging (INFO, WARNING, ERROR)
- Configuraciones específicas según el proyecto

## Monitoreo

- Revisar logs regularmente
- Configurar alertas según necesidades
- Monitorear métricas de rendimiento

