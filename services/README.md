# Backend Services

This directory contains the microservices that power the 3D Orofacial Harmonization Simulation platform.

## Services

### API Gateway (`api-gateway/`)
- Central entry point for all API requests
- Authentication and authorization
- Rate limiting and request routing
- API versioning and documentation

### Simulation Service (`simulation-service/`)
- 3D model processing and transformation
- Simulation algorithm implementations
- Real-time processing capabilities
- Integration with rendering pipeline

### CRM Integration (`crm-integration/`)
- Integration with external CRM/EMR systems
- Data synchronization and mapping
- FHIR compliance for medical data
- Audit logging and compliance

### Auth Service (`auth-service/`)
- User authentication and authorization
- OIDC/OAuth 2.0 implementation
- Role-based access control (RBAC)
- Session management and JWT handling

## Architecture

All services are built with:
- **FastAPI**: High-performance Python web framework
- **PostgreSQL**: Primary database
- **Redis**: Caching and session storage
- **Docker**: Containerization
- **OpenTelemetry**: Observability and tracing

## Development

Each service can be developed and deployed independently. See individual service README files for specific setup instructions.

## Security

- All services require authentication
- Inter-service communication secured with mTLS
- Regular security scanning and updates
- LGPD and HIPAA compliance built-in