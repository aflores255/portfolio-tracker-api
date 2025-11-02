# 🚀 Deployment Guide

## Prerequisites

- Python 3.11+
- Poetry
- PostgreSQL 14+
- Redis (for caching)
- Kubernetes cluster (for K8s deployment)
- Docker & Docker Compose
- Access to deployment server

## Production Installation

### 1. Prepare Environment

```bash
# Clone repository
git clone https://github.com/aflores255/portfolio-tracker-api.git
cd portfolio-tracker-api

# Install dependencies (production only)
poetry install --no-dev

# Setup environment variables
cp env.template .env
# Edit .env with production configuration
```

### 2. Configure Application

#### Environment Variables

Create a `.env` file with production settings:

```env
# Application
APP_ENV=production
DEBUG=False
LOG_LEVEL=INFO

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_tracker
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=10

# Redis Cache
REDIS_URL=redis://localhost:6379/0
CACHE_TTL=3600

# Security
SECRET_KEY=your-super-secret-key-change-this
JWT_SECRET_KEY=your-jwt-secret-key-change-this
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API
API_V1_PREFIX=/api/v1
CORS_ORIGINS=["https://yourdomain.com"]

# External Services
MARKET_DATA_API_KEY=your-api-key
```

#### Database Setup

```bash
# Run migrations
poetry run alembic upgrade head

# Verify database connection
poetry run python -c "from src.portfolio_tracker.config.database import engine; print('DB OK')"
```

### 3. Deploy with Docker

#### Build Docker Image

```bash
# Build production image
docker build -t portfolio-tracker-api:latest .

# Or using docker-compose
docker-compose -f docker-compose.prod.yml build
```

#### Run with Docker Compose

```bash
# Start all services
docker-compose -f docker-compose.prod.yml up -d

# Check logs
docker-compose -f docker-compose.prod.yml logs -f api

# Check health
curl http://localhost:8000/health
```

### 4. Deploy to Kubernetes

#### Prepare Kubernetes Resources

```bash
# Create namespace
kubectl create namespace portfolio-tracker

# Create secrets
kubectl create secret generic portfolio-tracker-secrets \
  --from-env-file=.env.production \
  -n portfolio-tracker

# Apply configurations
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

#### Verify Deployment

```bash
# Check pods
kubectl get pods -n portfolio-tracker

# Check logs
kubectl logs -f deployment/portfolio-tracker-api -n portfolio-tracker

# Check services
kubectl get svc -n portfolio-tracker
```

## Production Configuration

### Important Environment Variables

- `APP_ENV`: Application environment (production, staging, development)
- `DEBUG`: Debug mode (False for production)
- `LOG_LEVEL`: Logging level (INFO, WARNING, ERROR)
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `SECRET_KEY`: Application secret key
- `JWT_SECRET_KEY`: JWT token secret
- `CORS_ORIGINS`: Allowed CORS origins
- `API_V1_PREFIX`: API version prefix

### Security Considerations

1. **Never commit secrets** to version control
2. **Use strong secret keys** (generate with `openssl rand -hex 32`)
3. **Enable HTTPS** in production
4. **Configure CORS** properly
5. **Set rate limiting** on public endpoints
6. **Use secure headers** (configured in middleware)
7. **Keep dependencies updated**

## Database Migrations

```bash
# Run pending migrations
poetry run alembic upgrade head

# Rollback one migration
poetry run alembic downgrade -1

# Check migration history
poetry run alembic history

# Create new migration
poetry run alembic revision --autogenerate -m "Description"
```

## Monitoring & Logging

### Logs

```bash
# View application logs
tail -f logs/app.log

# View error logs
tail -f logs/error.log

# Docker logs
docker-compose logs -f api

# Kubernetes logs
kubectl logs -f deployment/portfolio-tracker-api -n portfolio-tracker
```

### Health Checks

```bash
# API health check
curl http://localhost:8000/health

# Database health check
curl http://localhost:8000/health/db

# Redis health check
curl http://localhost:8000/health/redis
```

### Monitoring Setup

- Configure APM tools (e.g., New Relic, Datadog)
- Set up alerts for:
  - High error rates
  - Slow response times
  - Database connection issues
  - High memory/CPU usage
- Monitor Airflow DAGs for market data updates

## Airflow Workers (Market Data)

### Setup Airflow

```bash
# Initialize Airflow database
poetry run airflow db init

# Create admin user
poetry run airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

# Start webserver
poetry run airflow webserver -p 8080

# Start scheduler
poetry run airflow scheduler
```

### Deploy DAGs

```bash
# Copy DAGs to Airflow directory
cp -r workers/dags/* $AIRFLOW_HOME/dags/

# Trigger manual run
poetry run airflow dags trigger market_data_update
```

## Backup & Recovery

### Database Backup

```bash
# Create backup
pg_dump -h localhost -U user portfolio_tracker > backup_$(date +%Y%m%d).sql

# Restore from backup
psql -h localhost -U user portfolio_tracker < backup_20251102.sql
```

### Automated Backups

Set up cron job for daily backups:
```bash
0 2 * * * pg_dump -h localhost -U user portfolio_tracker > /backups/portfolio_$(date +\%Y\%m\%d).sql
```

## Scaling

### Horizontal Scaling (Kubernetes)

```bash
# Scale API pods
kubectl scale deployment/portfolio-tracker-api --replicas=5 -n portfolio-tracker

# Auto-scaling
kubectl autoscale deployment/portfolio-tracker-api \
  --cpu-percent=70 \
  --min=2 \
  --max=10 \
  -n portfolio-tracker
```

### Database Connection Pooling

Configure in `.env`:
```env
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=10
```

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Change port in deployment
uvicorn src.portfolio_tracker.main:app --host 0.0.0.0 --port 8001
```

**Database connection issues:**
- Check PostgreSQL is running
- Verify credentials
- Check network connectivity
- Review connection pool settings

**High memory usage:**
- Adjust worker processes
- Review database query efficiency
- Check for memory leaks

## Rollback

```bash
# Docker deployment
docker-compose down
docker-compose up -d --build

# Kubernetes deployment
kubectl rollout undo deployment/portfolio-tracker-api -n portfolio-tracker

# Database rollback
poetry run alembic downgrade -1
```

## Support

- Check logs for errors
- Review documentation
- Create GitHub issue
- Contact DevOps team

