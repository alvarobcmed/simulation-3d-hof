# Shared Packages

This directory contains shared packages and libraries used across the application.

## Package Overview

### UI Components (`ui/`)
Shared user interface components:
- Design system and theme
- Reusable UI components
- Icons and assets
- Style utilities

**Technology**: TypeScript, CSS-in-JS, Component library

### 3D Engine (`3d-engine/`)
Core 3D rendering and processing utilities:
- 3D math utilities
- Mesh processing algorithms
- Rendering helpers
- Performance optimization tools

**Technology**: TypeScript, WebGL, Three.js, Math libraries

### Utils (`utils/`)
Common utilities and helpers:
- Data validation
- Type definitions
- Configuration helpers
- Common algorithms

**Technology**: TypeScript, Utility libraries

## Development Setup

Install dependencies for all packages:
```bash
# From root directory
npm install
```

Build all packages:
```bash
npm run build:packages
```

Test all packages:
```bash
npm run test:packages
```

## Package Architecture

### Monorepo Structure
- Each package is a separate npm workspace
- Shared dependencies at root level
- Independent versioning and publishing
- Cross-package dependencies managed

### TypeScript Configuration
- Strict TypeScript configuration
- Shared tsconfig for consistency
- Path mapping for clean imports
- Declaration file generation

### Build System
- Rollup for package bundling
- TypeScript compilation
- Tree-shaking optimization
- Multiple output formats (ESM, CJS)

## Usage in Applications

### Import Patterns
```typescript
// UI components
import { Button, Input } from '@simulation/ui';

// 3D utilities
import { MeshProcessor, Vector3D } from '@simulation/3d-engine';

// Common utilities
import { validateEmail, formatDate } from '@simulation/utils';
```

### Package Dependencies
```json
{
  "dependencies": {
    "@simulation/ui": "workspace:*",
    "@simulation/3d-engine": "workspace:*", 
    "@simulation/utils": "workspace:*"
  }
}
```

## Development Guidelines

### Code Standards
- Follow shared ESLint configuration
- Use Prettier for code formatting
- Write comprehensive unit tests
- Document all public APIs

### Testing
- Jest for unit testing
- React Testing Library for UI tests
- Coverage requirements: ≥80%
- Snapshot testing for components

### Documentation
- JSDoc for all public APIs
- README for each package
- Storybook for UI components
- Type definitions as documentation

## Package Management

### Adding New Packages
1. Create package directory
2. Add package.json with workspace config
3. Implement package functionality
4. Add tests and documentation
5. Update root package.json workspace list

### Versioning Strategy
- Semantic versioning (semver)
- Independent package versioning
- Automated changelog generation
- Release coordination across packages

### Publishing
- Private npm registry for internal packages
- Automated publishing via CI/CD
- Version bump automation
- Release notes generation

## Quality Gates

All packages must pass:
- TypeScript compilation
- Linting (ESLint)
- Unit tests (Jest)
- Coverage thresholds
- Bundle size analysis
- Security audit

## Performance

### Bundle Optimization
- Tree-shaking enabled
- Dynamic imports where applicable
- Minimal external dependencies
- Bundle size monitoring

### Runtime Performance
- Efficient algorithms
- Memory usage optimization
- Lazy loading patterns
- Performance monitoring

## Security

### Dependency Management
- Regular dependency updates
- Vulnerability scanning
- License compliance checking
- Supply chain security

### Code Security
- Input validation utilities
- Secure coding practices  
- Static analysis scanning
- Security-focused code reviews

## Migration Guide

When breaking changes are needed:
1. Deprecate old APIs with warnings
2. Provide migration utilities
3. Update all consuming applications
4. Remove deprecated APIs in next major version

## Support

For questions about shared packages:
- Check package README files
- Review API documentation
- Create GitHub issues with `packages` label
- Contact package maintainers