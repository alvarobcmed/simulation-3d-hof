# ADR-001: Architecture and Technology Stack Decisions

**Status**: Accepted  
**Date**: 2024-09-26  
**Context**: Initial architecture design for 3D Orofacial Harmonization Simulation App  

## Decision

We have decided on the following architectural approach and technology stack for the 3D Orofacial Harmonization Simulation Application.

## Architecture Overview

### Monorepo vs Polyrepo

**Decision**: Monorepo architecture  
**Rationale**: 
- Enables atomic changes across multiple domains (3D/AR, API, UI)
- Simplifies dependency management and versioning
- Better code sharing and reuse across modules
- Unified CI/CD pipeline and quality gates
- Easier maintenance and refactoring

**Trade-offs**:
- ✅ Simplified dependency management
- ✅ Atomic cross-module changes
- ✅ Unified tooling and standards
- ❌ Larger repository size
- ❌ Potential for slower CI/CD on large changes

## Technology Stack Decisions

### 1. iOS Application

**Decision**: Swift + ARKit + Custom 3D Engine  
**Rationale**:
- Native performance required for real-time 3D rendering (SRS Section 2.3.1)
- ARKit provides robust AR capabilities for face tracking (SRS Section 2.2.1)
- Swift ensures optimal iOS integration and performance
- Custom 3D engine allows fine-tuned control for medical visualization

**Alternatives Considered**:
- Unity: Higher overhead, licensing costs
- React Native: Performance limitations for 3D rendering
- Flutter: Limited ARKit integration

### 2. Backend API Services

**Decision**: FastAPI (Python)  
**Rationale**:
- Excellent performance for API services (SRS Section 3.2)
- Strong typing support with Pydantic
- Automatic OpenAPI documentation generation
- Rich ecosystem for ML/3D processing libraries
- Async support for real-time features

**Alternatives Considered**:
- Node.js: Less suitable for 3D/ML processing
- Django: Higher overhead for API-focused services
- .NET Core: Good performance but team expertise considerations

### 3. Database Layer

**Decision**: PostgreSQL  
**Rationale**:
- ACID compliance for patient data integrity (RNF-SEC-01)
- JSON/JSONB support for flexible 3D model metadata
- Strong spatial data support via PostGIS extension
- Excellent performance and scalability
- HIPAA compliance capabilities

**Alternatives Considered**:
- MySQL: Limited JSON support
- MongoDB: ACID compliance concerns for medical data
- SQLServer: Licensing costs and deployment complexity

### 4. Storage Strategy

**Decision**: S3-Compatible Object Storage  
**Rationale**:
- Scalable storage for 3D models and assets (RNF-PER-02)
- CDN integration for global distribution
- Versioning support for model iterations
- Cost-effective for large binary assets
- Standard API compatibility

### 5. Authentication & Authorization

**Decision**: OIDC/JWT with RBAC  
**Rationale**:
- Standards-based approach (RNF-SEC-02)
- Supports multiple user roles (patient, practitioner, admin)
- Token-based architecture supports mobile apps
- Integration with existing medical systems

### 6. Observability Stack

**Decision**: OpenTelemetry + Prometheus + Grafana  
**Rationale**:
- Vendor-neutral observability (RNF-OBS-01)
- Distributed tracing for complex 3D workflows
- Custom metrics for medical application monitoring
- Industry standard tools with strong community support

## Security & Compliance Architecture

### Data Protection
- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Key Management**: Hardware Security Modules (HSM)
- **Data Classification**: Automatic PII/PHI detection and handling

### Compliance Framework
- **LGPD Compliance**: Data subject rights automation
- **HIPAA Readiness**: Audit logging, access controls, data integrity
- **SOC 2 Type II**: Continuous compliance monitoring

## Deployment Strategy

**Decision**: Containerized microservices with Kubernetes  
**Rationale**:
- Service isolation and independent scaling (RNF-PER-01)
- Rolling deployments with zero downtime
- Resource optimization for 3D processing workloads
- Cloud-agnostic deployment options

## Quality Assurance Strategy

### Testing Framework
- **Unit Tests**: pytest (Python), XCTest (iOS) - ≥80% coverage
- **Integration Tests**: TestContainers for database integration
- **E2E Tests**: Appium for iOS, API testing with httpx
- **Performance Tests**: Locust for load testing

### Code Quality Gates
- **SAST**: SonarQube with custom rules for medical applications
- **DAST**: OWASP ZAP automated scanning
- **Dependency Scanning**: Dependabot + Snyk integration
- **License Compliance**: FOSSA scanning

## Migration Strategy

### Phase 1: Foundation (PR1)
- Repository scaffolding and CI/CD setup
- Core service structure without business logic
- Basic authentication and authorization framework

### Phase 2: Core Modules (PR2-4)
- 3D capture and processing engine
- AR mirror functionality
- Simulation composer framework

### Phase 3: Business Logic (PR5-7)
- API development with business rules
- UI/UX implementation
- Integration with external systems

### Phase 4: Hardening (PR8-10)
- Performance optimization
- Security hardening
- Compliance validation

## Consequences

### Positive
- Modular architecture supports iterative development
- Technology choices align with performance requirements
- Strong foundation for regulatory compliance
- Scalable architecture for future enhancements

### Negative
- Initial setup complexity due to multiple technologies
- Team needs training on selected stack
- Higher initial development overhead for proper abstractions

### Risks & Mitigations
- **Risk**: 3D performance on older iOS devices
  - **Mitigation**: Adaptive quality settings, performance profiling
- **Risk**: Complex integration with existing medical systems  
  - **Mitigation**: Standard APIs, comprehensive integration testing
- **Risk**: Compliance validation complexity
  - **Mitigation**: Early engagement with compliance experts, automated testing

## References

- SRS Section 2.2.1: AR Mirror Requirements
- SRS Section 2.3.1: 3D Rendering Performance Requirements  
- RNF-SEC-01: Data Integrity Requirements
- RNF-SEC-02: Authentication Requirements
- RNF-PER-01: Scalability Requirements
- RNF-PER-02: Storage Performance Requirements
- RNF-OBS-01: Observability Requirements