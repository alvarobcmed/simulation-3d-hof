# App de Simulação 3D em Tempo Real para Harmonização Orofacial

## Overview

This repository contains the implementation of a 3D real-time simulation application for orofacial harmonization, combining 3D/AR simulation, CRM/EMR integration, and advanced visualization for educational purposes.

## Architecture

The project follows a monorepo architecture to support modular development across multiple domains:

- **3D/AR Simulation**: Core 3D rendering and AR capabilities
- **iOS Application**: Native iOS app using Swift and ARKit
- **API Services**: Backend services for data management and processing
- **UI/UX Components**: Shared design system and user interface components
- **Integration Modules**: CRM/EMR and external system integrations

## Technology Stack

### Frontend/Mobile
- **iOS**: Swift, ARKit, potentially Unity/Metal for 3D rendering
- **UI Framework**: SwiftUI with custom 3D components

### Backend
- **API**: FastAPI (Python) or Node.js with TypeScript
- **Database**: PostgreSQL for structured data
- **Storage**: S3-compatible storage for 3D models and assets
- **Authentication**: OIDC/JWT-based auth with RBAC

### Infrastructure & Observability
- **Observability**: OpenTelemetry for metrics, logs, and tracing
- **CI/CD**: GitHub Actions with automated testing and deployment
- **Security**: SAST/DAST scanning, dependency management

## Repository Structure

```
.
├── apps/                    # Applications
│   ├── ios/                # iOS application
│   └── web/                # Web interface (if needed)
├── services/               # Backend services
│   ├── api/                # Main API service
│   ├── simulation/         # 3D simulation service
│   └── integration/        # CRM/EMR integration service
├── packages/               # Shared packages
│   ├── ui/                 # UI component library
│   ├── 3d-engine/          # 3D rendering engine
│   └── utils/              # Shared utilities
├── docs/                   # Documentation
│   ├── adr/                # Architecture Decision Records
│   ├── api/                # API documentation
│   └── deployment/         # Deployment guides
├── infrastructure/         # Infrastructure as Code
└── .github/                # GitHub workflows and templates
```

## Getting Started

### Prerequisites

- **iOS Development**: Xcode 15+, iOS 16+ target
- **Backend Development**: Python 3.11+ or Node.js 18+
- **Database**: PostgreSQL 15+
- **Tools**: Docker, git

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alvarobcmed/simulation-3d-hof.git
   cd simulation-3d-hof
   ```

2. **Set up backend services**:
   ```bash
   cd services/api
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up iOS development**:
   ```bash
   cd apps/ios
   open SimulationApp.xcodeproj
   ```

4. **Run local development environment**:
   ```bash
   docker-compose up -d  # Start PostgreSQL and other services
   ```

### Development Workflow

1. Create feature branches from `main`
2. Implement changes with appropriate tests
3. Run quality gates locally before pushing
4. Create pull request with proper documentation
5. Ensure all CI/CD checks pass
6. Obtain required code reviews

## Quality Gates

### Testing Requirements
- **Unit Tests**: ≥80% coverage required
- **Critical Paths**: 100% coverage required
- **Integration Tests**: All API endpoints covered
- **E2E Tests**: Core user workflows covered

### Security Requirements
- **SAST/DAST**: No HIGH/CRITICAL findings allowed
- **Dependency Scanning**: Regular updates via Dependabot
- **Secrets Management**: No hardcoded secrets in code

### Compliance
- **LGPD**: Data privacy and protection compliance
- **HIPAA**: Healthcare data handling readiness
- **Encryption**: All data encrypted in transit and at rest

## Contributing

Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

### Code Review Process
- All changes require peer review
- Maintainer approval required for merging
- Automated quality gates must pass

## Documentation

- [Architecture Decision Records](docs/adr/)
- [API Documentation](docs/api/)
- [Deployment Guide](docs/deployment/)
- [Traceability Matrix](docs/traceability-matrix.md)

## License

This project is proprietary software. All rights reserved.

## Support

For support and questions, please create an issue using our [issue templates](.github/ISSUE_TEMPLATE/).