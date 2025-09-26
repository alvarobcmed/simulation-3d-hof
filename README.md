# 3D Orofacial Harmonization Simulation App

A real-time 3D simulation application for educational purposes in orofacial harmonization, combining AR/3D technology with CRM/EMR integration and advanced visualization capabilities.

## 🏗️ Architecture

This project follows a monorepo architecture with modular domains:

- **[`apps/`](./apps/)** - Client applications (iOS, Admin Dashboard)
- **[`services/`](./services/)** - Backend microservices (API, Simulation, CRM, Auth)
- **[`packages/`](./packages/)** - Shared libraries and utilities
- **[`infrastructure/`](./infrastructure/)** - Infrastructure as Code and deployment
- **[`docs/`](./docs/)** - Documentation and Architecture Decision Records

## 🚀 Quick Start

### Prerequisites

- **iOS Development**: Xcode 14.0+, iOS 15.0+, iPhone with TrueDepth camera
- **Backend Development**: Python 3.9+, Docker, PostgreSQL
- **Infrastructure**: Terraform, Kubernetes CLI

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/alvarobcmed/simulation-3d-hof.git
   cd simulation-3d-hof
   ```

2. **iOS Application**
   ```bash
   cd apps/ios-app
   open ios-app.xcodeproj
   # Build and run in Xcode
   ```

3. **Backend Services**
   ```bash
   cd services
   docker-compose up -d
   # Services will be available at http://localhost:8000
   ```

4. **Infrastructure**
   ```bash
   cd infrastructure/terraform
   terraform init
   terraform plan
   # Follow infrastructure setup guide
   ```

## 🏛️ Technology Stack

### iOS Application
- **Swift** - Primary development language
- **ARKit** - 3D capture and AR functionality
- **Metal** - High-performance 3D rendering
- **SwiftUI/UIKit** - User interface framework

### Backend Services
- **FastAPI** - High-performance API framework
- **PostgreSQL** - Primary database
- **Redis** - Caching and session management
- **MinIO/S3** - Object storage for 3D assets

### Infrastructure & DevOps
- **Docker** - Containerization
- **Kubernetes** - Container orchestration
- **Terraform** - Infrastructure as Code
- **GitHub Actions** - CI/CD pipelines

### Security & Compliance
- **OAuth 2.0/OIDC** - Authentication and authorization
- **TLS 1.3** - Encryption in transit
- **AES-256** - Encryption at rest
- **LGPD/HIPAA** - Compliance framework

## 📋 Development Phases

### Phase 1: Foundation (PR1)
- [x] Repository setup and architecture decisions
- [ ] CI/CD pipeline configuration
- [ ] Quality gates implementation
- [ ] Basic scaffolding for all components

### Phase 2: Core Modules (PR2-4)
- [ ] 3D capture implementation (ARKit)
- [ ] AR mirror functionality
- [ ] 3D composer and simulation engine
- [ ] Basic API endpoints

### Phase 3: Advanced Features (PR5-7)
- [ ] Advanced simulation algorithms
- [ ] UI/UX implementation
- [ ] CRM/EMR integration
- [ ] Real-time processing optimization

### Phase 4: Integration & Testing (PR8-9)
- [ ] End-to-end integration
- [ ] Performance optimization
- [ ] Security hardening
- [ ] Compliance validation

### Phase 5: Production Readiness (PR10)
- [ ] Production deployment
- [ ] Monitoring and alerting
- [ ] Documentation completion
- [ ] User acceptance testing

## 🔒 Security & Compliance

This application is designed with security and compliance as first-class concerns:

- **LGPD Compliance**: Privacy by design, data minimization, consent management
- **HIPAA Readiness**: Encryption, access controls, audit logging
- **Security Controls**: Regular SAST/DAST scanning, dependency management
- **Access Control**: Role-based permissions with OIDC authentication

## 📊 Quality Gates

All code changes must pass:
- **Test Coverage**: ≥80% overall, 100% for critical paths
- **Security Scanning**: No HIGH/CRITICAL findings in SAST/DAST
- **Code Quality**: SonarQube quality gate passed
- **Dependencies**: Up-to-date with automated security updates

## 🔍 Monitoring & Observability

- **OpenTelemetry**: Distributed tracing and metrics
- **Prometheus**: Metrics collection and alerting
- **Grafana**: Visualization and dashboards
- **Structured Logging**: Centralized log management

## 📖 Documentation

- **[Architecture Decisions](./docs/adr/)** - Technical decision records
- **[API Documentation](./docs/api/)** - REST API specifications
- **[Development Guide](./docs/development.md)** - Setup and contribution guide
- **[Security Guide](./docs/security.md)** - Security practices and compliance

## 🤝 Contributing

1. Review the [Development Guide](./docs/development.md)
2. Follow the established coding standards and practices
3. Ensure all quality gates pass before submitting PRs
4. Update documentation for any architectural changes

## 📄 License

This project is proprietary and confidential. All rights reserved.

## 🆘 Support

For development support and questions:
- Create an issue in this repository
- Consult the documentation in the `docs/` directory
- Follow the troubleshooting guides for each component