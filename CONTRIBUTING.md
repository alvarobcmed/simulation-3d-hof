# Contributing to 3D Orofacial Harmonization Simulation App

Thank you for your interest in contributing to this project! This guide will help you understand our development process and standards.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Development Process](#development-process)
- [Getting Started](#getting-started)
- [Making Changes](#making-changes)
- [Quality Standards](#quality-standards)
- [Review Process](#review-process)
- [Security Guidelines](#security-guidelines)

## Code of Conduct

This project adheres to a code of conduct that promotes respect, inclusivity, and collaborative development. All contributors are expected to:

- Be respectful and inclusive in all interactions
- Focus on constructive feedback and solutions
- Respect different viewpoints and experiences
- Report any unacceptable behavior to project maintainers

## Development Process

### Branch Strategy

We use a Git Flow-based branching strategy:

- **`main`**: Production-ready code, protected branch
- **`develop`**: Integration branch for development
- **`feature/*`**: Feature development branches
- **`hotfix/*`**: Critical production fixes
- **`release/*`**: Release preparation branches

### Workflow

1. **Create Feature Branch**: Branch from `develop`
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. **Implement Changes**: Follow coding standards and add tests

3. **Local Testing**: Run all tests and quality checks
   ```bash
   # Run all tests
   npm test
   python -m pytest services/api/tests/
   
   # Run quality checks
   npm run lint
   black services/api/
   ```

4. **Push and Create PR**: Push branch and create pull request to `develop`

5. **Code Review**: Address feedback and ensure CI passes

6. **Merge**: Maintainer merges after approval

## Getting Started

### Prerequisites

- **iOS Development**: Xcode 15+, iOS 16+ simulator
- **Backend Development**: Python 3.11+, Node.js 18+
- **Database**: PostgreSQL 15+ (or Docker)
- **Tools**: Docker, git, make

### Local Setup

1. **Clone Repository**:
   ```bash
   git clone https://github.com/alvarobcmed/simulation-3d-hof.git
   cd simulation-3d-hof
   ```

2. **Start Development Services**:
   ```bash
   docker-compose up -d postgres redis minio
   ```

3. **Set Up Python Environment**:
   ```bash
   cd services/api
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set Up Node.js Environment**:
   ```bash
   npm install
   ```

5. **Set Up iOS Development**:
   ```bash
   cd apps/ios
   open SimulationApp.xcodeproj
   ```

### Environment Configuration

Create `.env` files for each service:

**`services/api/.env`**:
```env
DATABASE_URL=postgresql://postgres:devpassword@localhost:5432/simulation_dev
REDIS_URL=redis://localhost:6379
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin123
ENVIRONMENT=development
SECRET_KEY=your-secret-key-here
```

## Making Changes

### Commit Standards

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks

**Examples**:
```
feat(api): add patient authentication endpoint
fix(ios): resolve AR camera initialization issue
docs(readme): update setup instructions
test(api): add integration tests for simulation endpoints
```

### Code Organization

#### Python (Backend Services)
```
services/api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── core/                # Core functionality
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   ├── api/                 # API routes
│   │   ├── v1/
│   │   └── dependencies.py
│   ├── models/              # Database models
│   ├── schemas/             # Pydantic schemas
│   └── services/            # Business logic
├── tests/                   # Test suite
└── alembic/                 # Database migrations
```

#### Swift (iOS Application)
```
apps/ios/
├── SimulationApp/
│   ├── Core/                # Core functionality
│   │   ├── 3DCapture/
│   │   ├── ARMirror/
│   │   └── Simulation/
│   ├── UI/                  # User interface
│   ├── Services/            # API and data services
│   └── Utils/               # Utilities
├── SimulationAppTests/      # Unit tests
└── SimulationAppUITests/    # UI tests
```

### Testing Requirements

#### Test Coverage Standards
- **Unit Tests**: ≥80% line coverage
- **Critical Paths**: 100% coverage required
- **Integration Tests**: All API endpoints
- **E2E Tests**: Core user workflows

#### Python Testing
```bash
# Run unit tests
pytest tests/unit/ -v

# Run integration tests
pytest tests/integration/ -v

# Run with coverage
pytest --cov=app --cov-report=html tests/
```

#### iOS Testing
```bash
# Run unit tests
xcodebuild test -scheme SimulationApp -destination 'platform=iOS Simulator,name=iPhone 15'

# Run UI tests
xcodebuild test -scheme SimulationAppUITests -destination 'platform=iOS Simulator,name=iPhone 15'
```

## Quality Standards

### Code Style

#### Python
- **Formatter**: Black (line length: 88)
- **Import Sorting**: isort
- **Linting**: flake8, mypy
- **Documentation**: Google-style docstrings

```bash
# Format code
black services/api/
isort services/api/

# Lint code
flake8 services/api/
mypy services/api/
```

#### Swift
- **Style Guide**: Apple Swift Style Guide
- **Linting**: SwiftLint
- **Documentation**: Swift-DocC format

#### TypeScript/JavaScript
- **Formatter**: Prettier
- **Linting**: ESLint with TypeScript rules
- **Style**: Airbnb style guide

### Performance Standards

- **API Response Time**: <200ms (95th percentile)
- **Database Query Time**: <50ms (95th percentile)
- **iOS 3D Rendering**: ≥30 FPS
- **Memory Usage**: iOS app <200MB baseline

### Security Standards

- **SAST**: No HIGH/CRITICAL findings
- **Dependency Scanning**: No known vulnerabilities
- **Secrets**: No hardcoded secrets in code
- **Authentication**: Proper JWT validation
- **Authorization**: RBAC enforcement

## Review Process

### Pull Request Requirements

Before creating a PR, ensure:
- [ ] All tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] Security scan passes
- [ ] Performance impact assessed

### PR Template

Use this template for pull requests:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings introduced
```

### Review Criteria

Reviewers will check:
- **Functionality**: Code works as intended
- **Security**: No security vulnerabilities
- **Performance**: No performance regressions
- **Maintainability**: Code is readable and maintainable
- **Testing**: Adequate test coverage
- **Documentation**: Clear and accurate

### Approval Process

- **Feature PRs**: Require 2 approvals (1 maintainer + 1 peer)
- **Bug Fixes**: Require 1 maintainer approval
- **Hotfixes**: Can be fast-tracked with 1 approval
- **Documentation**: Require 1 approval

## Security Guidelines

### Sensitive Data Handling

- **Never commit secrets** to version control
- **Use environment variables** for configuration
- **Encrypt sensitive data** at rest and in transit
- **Implement proper access controls**

### Vulnerability Reporting

If you discover a security vulnerability:
1. **Do not** create a public issue
2. **Email** the maintainers directly
3. **Provide** detailed reproduction steps
4. **Allow** reasonable time for fix before disclosure

### Security Review

Security-sensitive changes require:
- Security team review
- Penetration testing (if applicable)
- Compliance validation
- Additional approval from security officer

## Getting Help

### Communication Channels

- **General Questions**: Create GitHub issue with `question` label
- **Bug Reports**: Create GitHub issue with `bug` label
- **Feature Requests**: Create GitHub issue with `enhancement` label
- **Security Issues**: Email maintainers directly

### Documentation

- **API Documentation**: [docs/api/](docs/api/)
- **Deployment Guides**: [docs/deployment/](docs/deployment/)
- **Architecture Decisions**: [docs/adr/](docs/adr/)

### Mentorship

New contributors can request mentorship for:
- Understanding the codebase
- Learning development practices
- Guidance on first contributions

## Recognition

We value all contributions and recognize contributors through:
- GitHub contributor statistics
- Mention in release notes
- Optional contributor spotlight in documentation

Thank you for contributing to making this project better!