# ADR-002: Monorepo vs Polyrepo Approach

## Status

Accepted

## Context

The 3D Orofacial Harmonization Simulation App consists of multiple modular domains:
- iOS Application (3D/AR, UI/UX)
- Backend APIs (FastAPI services)
- Shared Libraries/Packages
- Infrastructure as Code
- Documentation
- CI/CD configurations

We need to decide between a monorepo approach (single repository) vs polyrepo approach (multiple repositories) for organizing these components.

## Decision

**Monorepo Approach** - All components will be maintained in a single repository with the following structure:

```
/
├── apps/
│   ├── ios-app/                 # iOS Swift application
│   └── admin-dashboard/         # Optional web dashboard
├── services/
│   ├── api-gateway/            # API Gateway service
│   ├── simulation-service/     # 3D simulation processing
│   ├── crm-integration/        # CRM/EMR integration
│   └── auth-service/           # Authentication service
├── packages/
│   ├── shared-types/           # Shared TypeScript/Swift types
│   ├── common-utils/           # Utility functions
│   └── sdk/                    # Client SDKs
├── infrastructure/
│   ├── terraform/              # Infrastructure as Code
│   ├── kubernetes/             # K8s manifests
│   └── docker/                 # Docker configurations
├── docs/                       # Documentation
├── .github/                    # CI/CD workflows
└── tools/                      # Development tools
```

## Consequences

### Positive
- **Simplified dependency management**: All packages versions managed centrally
- **Atomic changes**: Cross-component changes in single commits/PRs
- **Unified CI/CD**: Single pipeline for all components with shared quality gates
- **Code sharing**: Easy sharing of types, utilities, and configurations
- **Simplified developer onboarding**: Single repository to clone and understand
- **Consistent tooling**: Unified linting, testing, and build processes
- **Better traceability**: Requirements can be traced across all components
- **Reduced repository overhead**: Single set of issues, PRs, and releases

### Negative
- **Repository size**: May become large over time with 3D assets and models
- **Build complexity**: Need selective builds to avoid rebuilding unchanged components
- **Access control limitations**: Cannot restrict access to specific components easily
- **Potential merge conflicts**: More developers working in same repository
- **Tool limitations**: Some tools may not handle large monorepos efficiently

### Neutral
- **Team coordination**: Requires good communication but facilitates collaboration
- **Release management**: Can do unified or component-specific releases
- **CI/CD resource usage**: May require optimization for build times

## Implementation Strategy

1. **Workspace Management**: Use package managers with workspace support
2. **Selective Building**: Implement build systems that only rebuild changed components
3. **Code Organization**: Clear separation of concerns through directory structure
4. **Access Patterns**: Use GitHub's CODEOWNERS for component ownership
5. **Build Optimization**: Cache strategies and parallel builds
6. **Documentation**: Clear guidelines for cross-component dependencies

## Alternatives Considered

### Polyrepo Approach
- **Pros**: Independent versioning, smaller repositories, fine-grained access control
- **Cons**: Complex dependency management, difficult atomic changes, CI/CD duplication
- **Rejected because**: The tight integration between iOS app and backend services requires frequent cross-component changes

### Hybrid Approach
- **Pros**: Core components in monorepo, auxiliary services separate
- **Cons**: Complexity of managing both approaches, unclear boundaries
- **Rejected because**: Adds unnecessary complexity for initial development phase

## References

- SRS/PRD Section: Modular Architecture Requirements
- SRS/PRD Section: Development Team Structure
- Monorepo best practices documentation
- Team collaboration requirements