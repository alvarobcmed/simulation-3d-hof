# iOS Application

3D Orofacial Harmonization Simulation iOS App built with Swift and ARKit.

## Features

- **3D Capture**: Real-time 3D facial capture using ARKit
- **AR Mirror**: Augmented reality mirror for simulation preview
- **Simulation Engine**: 3D visualization and transformation engine
- **Offline Support**: Core functionality available without network
- **Secure Storage**: HIPAA-compliant local data handling

## Architecture

- **SwiftUI**: Modern declarative UI framework
- **ARKit**: 3D capture and augmented reality
- **Metal**: High-performance 3D rendering
- **Core Data**: Local data persistence
- **Combine**: Reactive programming framework

## Requirements

- iOS 15.0+
- iPhone with TrueDepth camera (iPhone X or newer)
- Xcode 14.0+
- Swift 5.7+

## Development Setup

```bash
# Open project in Xcode
open ios-app.xcodeproj

# Install dependencies (if using Swift Package Manager)
# Dependencies are managed through Xcode
```

## Testing

- Unit tests: Run via Xcode Test Navigator
- UI tests: Automated UI testing with XCUITest
- Coverage target: ≥80% overall, 100% for critical paths

## Security

- All sensitive data encrypted at rest
- Biometric authentication support
- Network communications over TLS 1.3
- Regular security scanning integration