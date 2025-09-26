# Applications

This directory contains the client applications for the 3D Orofacial Harmonization Simulation system.

## Applications Overview

### iOS Application (`ios/`)
Native iOS application providing:
- 3D face capture using ARKit
- Real-time AR mirror functionality
- Simulation visualization and interaction
- Offline-capable design with sync

**Technology**: Swift, SwiftUI, ARKit, Metal

### Web Application (`web/`) - Future Release
Web-based administration interface:
- Patient data management
- Simulation review and analysis
- Educational content management
- System administration

**Technology**: React, TypeScript, WebGL (planned)

## Development Setup

### iOS Development
Requirements:
- macOS 13.0+ with Xcode 15+
- iOS 16.0+ target device or simulator
- Apple Developer account for device testing

Setup:
```bash
cd ios
open SimulationApp.xcodeproj
```

### Web Development (Planned)
Requirements:
- Node.js 18+
- Modern web browser with WebGL support

Setup:
```bash
cd web
npm install
npm run dev
```

## Architecture

### Shared Architecture Principles
- Clean Architecture with clear separation of concerns
- Dependency injection for testability
- Reactive programming patterns
- Offline-first design with synchronization

### Data Flow
1. **Local Data**: Core app functionality works offline
2. **Synchronization**: Background sync with backend services
3. **Real-time Updates**: Live updates for collaborative features
4. **Conflict Resolution**: Automatic merge strategies for conflicts

### Security
- Biometric authentication (Face ID/Touch ID)
- Secure token storage in Keychain
- Certificate pinning for API communication
- Local data encryption

## Testing Strategy

### iOS Testing
- Unit tests for business logic (≥80% coverage)
- UI tests for critical user flows
- Performance tests for 3D operations
- Accessibility tests for WCAG compliance

### Integration Testing
- API integration tests
- End-to-end user workflow tests
- Cross-platform compatibility tests
- Performance benchmarking

## Deployment

### iOS Deployment
- App Store distribution for public release
- TestFlight for beta testing
- Enterprise distribution for internal use
- Over-the-air updates for configuration

### Distribution Strategy
- Staged rollout for new features
- A/B testing for UI improvements
- Feature flags for gradual rollout
- Rollback procedures for issues

## Platform-Specific Features

### iOS Unique Features
- ARKit integration for 3D capture
- Face ID/Touch ID authentication
- Native performance for 3D rendering
- iOS-specific UI patterns and conventions

### Web Unique Features (Planned)
- Administrative dashboards
- Bulk data operations  
- Advanced reporting and analytics
- Multi-tenant organization management

## Performance Requirements

### iOS Performance Targets
- App launch time: <3 seconds
- 3D rendering: ≥30 FPS
- AR mirror latency: <50ms
- Memory usage: <200MB baseline

### Monitoring
- Real-time performance monitoring
- Crash reporting and analysis
- User analytics (privacy-compliant)
- Performance regression detection

## Accessibility

Both applications implement:
- WCAG 2.1 AA compliance
- VoiceOver support (iOS)
- High contrast mode support
- Large text support
- Keyboard navigation (web)

## Internationalization

Support for:
- Multiple languages (starting with English/Portuguese)
- Right-to-left languages
- Cultural formatting (dates, numbers)
- Localized medical terminology

## Offline Capabilities

### Data Synchronization
- Offline-first architecture
- Background sync when online
- Conflict resolution strategies
- Partial sync for large datasets

### Local Storage
- Core Data for structured data (iOS)
- Secure file storage for 3D models
- Encrypted sensitive data
- Storage optimization and cleanup

## Development Guidelines

### Code Quality
- Follow platform-specific style guides
- Comprehensive unit test coverage
- Regular code reviews
- Static analysis and linting

### Documentation
- Inline code documentation
- Architecture decision records
- User guides and tutorials
- API integration guides

For detailed setup and development instructions, see the README in each application directory.