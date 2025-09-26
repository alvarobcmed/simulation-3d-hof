# iOS Application - 3D Orofacial Harmonization Simulation

## Overview

The iOS application provides the primary user interface for the 3D Orofacial Harmonization Simulation system. It leverages ARKit for real-time 3D face capture and provides an intuitive interface for medical professionals.

## Technology Stack

- **Platform**: iOS 16.0+
- **Language**: Swift 5.9+
- **UI Framework**: SwiftUI
- **3D Graphics**: ARKit, Metal, SceneKit
- **Architecture**: MVVM with Combine
- **Dependency Management**: Swift Package Manager

## Project Structure

```
SimulationApp/
├── Core/                    # Core business logic
│   ├── 3DCapture/          # 3D face capture using ARKit
│   ├── ARMirror/           # Real-time AR mirror functionality
│   └── Simulation/         # Simulation engine and processing
├── UI/                     # User interface components
│   ├── Views/              # SwiftUI views
│   ├── ViewModels/         # MVVM view models
│   └── Components/         # Reusable UI components
├── Services/               # External services and APIs
│   ├── API/                # Backend API integration
│   ├── Storage/            # Local data storage
│   └── Network/            # Network layer
└── Utils/                  # Utilities and extensions
    ├── Extensions/         # Swift extensions
    ├── Constants/          # App constants
    └── Helpers/            # Helper functions
```

## Key Features

### 3D Face Capture
- Real-time face detection and tracking
- High-quality 3D mesh generation
- Texture mapping and optimization
- Export capabilities for captured models

### AR Mirror
- Real-time AR overlay on captured face
- Interactive manipulation controls
- Multiple viewing angles
- Simulation preview functionality

### Simulation Engine
- Procedure simulation capabilities
- Before/after comparisons
- Timeline-based playback
- Educational content integration

## Requirements

### Hardware Requirements
- **Device**: iPhone 12 or newer (A14+ chip required)
- **Camera**: TrueDepth camera system
- **Storage**: 2GB free space minimum
- **RAM**: 4GB minimum

### Software Requirements
- **iOS**: 16.0 or later
- **Xcode**: 15.0+ for development
- **Swift**: 5.9+

## Setup Instructions

### Development Environment

1. **Install Xcode 15+** from the App Store

2. **Clone the repository**:
   ```bash
   git clone https://github.com/alvarobcmed/simulation-3d-hof.git
   cd simulation-3d-hof/apps/ios
   ```

3. **Open the project**:
   ```bash
   open SimulationApp.xcodeproj
   ```

4. **Configure signing**:
   - Select your development team in project settings
   - Update bundle identifier if needed

5. **Install dependencies**:
   Dependencies are managed via Swift Package Manager and will be resolved automatically.

### Running the App

1. **Select target device** (iPhone 12+ or simulator)
2. **Build and run** (⌘+R)

Note: AR features require a physical device with TrueDepth camera.

## Testing

### Unit Tests
```bash
# Run from Xcode or command line
xcodebuild test -scheme SimulationApp -destination 'platform=iOS Simulator,name=iPhone 15'
```

### UI Tests
```bash
# Run UI tests
xcodebuild test -scheme SimulationAppUITests -destination 'platform=iOS Simulator,name=iPhone 15'
```

### Performance Tests
```bash
# Run performance tests on device
xcodebuild test -scheme SimulationApp -destination 'platform=iOS,name=Your Device'
```

## Architecture

### MVVM Pattern
- **Models**: Data structures and business logic
- **Views**: SwiftUI views and UI components
- **ViewModels**: Presentation logic and state management

### Dependency Injection
Using a lightweight DI container for:
- API services
- Storage services
- Configuration management

### Reactive Programming
- **Combine**: For reactive data flow
- **ObservableObject**: For SwiftUI state management
- **Publishers**: For event handling

## Performance Considerations

### 3D Rendering Optimization
- **Adaptive Quality**: Automatic quality adjustment based on device capability
- **Level of Detail (LOD)**: Multiple mesh resolutions for optimal performance
- **Culling**: Frustum and occlusion culling for efficient rendering
- **Memory Management**: Proper texture and mesh memory management

### AR Performance
- **Frame Rate**: Target 60 FPS for smooth AR experience
- **Latency**: <50ms for real-time interactions
- **Battery Optimization**: Efficient use of camera and processing resources

## Security Implementation

### Data Protection
- **Keychain**: Secure storage for authentication tokens
- **Encryption**: AES-256 encryption for sensitive local data
- **Biometric Authentication**: Face ID/Touch ID integration

### Privacy Compliance
- **Camera Permissions**: Proper permission handling and user consent
- **Data Minimization**: Only collect necessary data
- **Local Processing**: Process sensitive data locally when possible

## API Integration

### Backend Communication
- **REST API**: HTTP client for backend communication
- **Authentication**: JWT token-based authentication
- **File Upload**: Secure file upload for 3D models
- **Real-time Updates**: WebSocket support for live updates

### Offline Support
- **Local Storage**: Core Data for offline data persistence
- **Sync Management**: Automatic sync when connectivity restored
- **Conflict Resolution**: Merge strategies for conflicting data

## Deployment

### App Store Distribution
1. **Archive build** for release
2. **Code signing** with distribution certificate
3. **Upload to App Store Connect**
4. **Submit for review**

### Enterprise Distribution
1. **Configure enterprise certificate**
2. **Build with enterprise provisioning profile**
3. **Distribute via MDM or direct download**

## Contributing

Please read [CONTRIBUTING.md](../../CONTRIBUTING.md) for development guidelines and standards.

### Code Style
- Follow Swift API Design Guidelines
- Use SwiftLint for style enforcement
- Document public APIs with Swift-DocC

### Testing Requirements
- Unit test coverage ≥80%
- UI tests for critical user flows
- Performance tests for 3D operations

## Troubleshooting

### Common Issues

**AR not working**:
- Ensure device has TrueDepth camera
- Check camera permissions
- Verify iOS version compatibility

**Performance issues**:
- Check device thermal state
- Reduce 3D model complexity
- Enable adaptive quality settings

**Build errors**:
- Clean build folder (⌘+Shift+K)
- Reset package dependencies
- Verify Xcode version compatibility

### Debug Tools
- **Xcode Instruments**: Performance profiling
- **Console.app**: System-level logging
- **AR Debug Options**: ARKit debugging features

## License

This project is proprietary software. All rights reserved.