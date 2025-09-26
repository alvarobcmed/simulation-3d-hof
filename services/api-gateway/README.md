# API Gateway Service

Central entry point and routing service for the 3D Orofacial Harmonization Simulation platform.

## Features

- **Request Routing**: Intelligent routing to backend services
- **Authentication**: OIDC/JWT token validation and management
- **Rate Limiting**: Configurable rate limiting per user/endpoint
- **API Versioning**: Support for multiple API versions
- **Request/Response Transformation**: Data format standardization
- **Monitoring**: Comprehensive metrics and tracing

## Architecture

- **Framework**: FastAPI for high-performance async processing
- **Authentication**: JWT validation with OIDC compliance
- **Database**: PostgreSQL for configuration and user management
- **Caching**: Redis for session management and rate limiting
- **Monitoring**: OpenTelemetry for distributed tracing

## Configuration

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/api_gateway
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET_KEY=your-secret-key
OIDC_DISCOVERY_URL=https://auth.example.com/.well-known/openid_configuration

# Service Discovery
SIMULATION_SERVICE_URL=http://simulation-service:8001
CRM_INTEGRATION_URL=http://crm-integration:8002
AUTH_SERVICE_URL=http://auth-service:8003

# Monitoring
OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4317
OTEL_SERVICE_NAME=api-gateway
```

## Development Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

2. **Database Setup**
   ```bash
   alembic upgrade head
   ```

3. **Run Development Server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Documentation

Once running, API documentation is available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_auth.py -v
```

## Security

- All endpoints require authentication except health checks
- Rate limiting applied per user and IP address
- Input validation using Pydantic models
- SQL injection protection through SQLAlchemy ORM
- CORS policy configured for frontend domains only

## Monitoring

The service exposes metrics at `/metrics` in Prometheus format:
- Request duration and count
- Authentication success/failure rates
- Database connection pool status
- Cache hit/miss ratios
- Error rates by endpoint

## Deployment

See the main [infrastructure documentation](../../infrastructure/README.md) for deployment instructions.