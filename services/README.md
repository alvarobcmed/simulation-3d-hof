# Backend Services

This directory contains the backend services for the 3D Orofacial Harmonization Simulation application.

## Services Overview

### API Service (`api/`)
Main REST API service providing:
- Patient data management
- User authentication and authorization
- File upload and management
- Simulation data processing
- Integration with external systems

**Technology**: FastAPI (Python), PostgreSQL, Redis

### Simulation Service (`simulation/`)
Specialized service for 3D processing:
- 3D model processing and optimization
- Simulation calculations and rendering
- Mesh analysis and validation
- Educational content management

**Technology**: Python, NumPy, Open3D, Medical imaging libraries

### Integration Service (`integration/`)
External system integration service:
- CRM/EMR system integration
- FHIR-compliant data exchange
- Third-party API integrations
- Data synchronization

**Technology**: FastAPI (Python), FHIR libraries, Message queues

## Development Setup

1. **Start dependencies**:
   ```bash
   docker-compose up -d postgres redis minio
   ```

2. **Set up each service**:
   ```bash
   # API Service
   cd api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   
   # Simulation Service
   cd ../simulation
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m app.main
   
   # Integration Service
   cd ../integration
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python -m app.main
   ```

## Architecture

All services follow similar patterns:
- **FastAPI** for HTTP APIs
- **Pydantic** for data validation
- **SQLAlchemy** for database ORM
- **Alembic** for database migrations
- **OpenTelemetry** for observability
- **Structured logging** with audit trails

## Service Communication

Services communicate via:
- **HTTP APIs** for synchronous operations
- **Redis Pub/Sub** for real-time events
- **Message queues** for asynchronous processing
- **Shared database** for critical data consistency

## Security

All services implement:
- JWT-based authentication
- RBAC authorization
- Input validation and sanitization
- Rate limiting and DDoS protection
- Audit logging for compliance
- Encryption for sensitive data

## Testing

Each service includes:
- Unit tests (≥80% coverage)
- Integration tests
- API contract tests
- Performance tests
- Security tests

Run tests for all services:
```bash
# From root directory  
make test-services
```

## Monitoring

Services are monitored via:
- **Health checks** at `/health`
- **Metrics** at `/metrics` (Prometheus format)
- **Distributed tracing** via OpenTelemetry
- **Structured logs** with correlation IDs

## Deployment

Services are containerized and deployed via:
- **Docker** containers
- **Kubernetes** orchestration
- **Helm** charts for configuration
- **GitOps** for continuous deployment

See [deployment documentation](../docs/deployment/) for details.