# Contributing to Simulation 3D HOF

Obrigado por contribuir com o projeto Simulation 3D HOF! Este documento descreve o processo de desenvolvimento e as diretrizes para contribuições.

## 🚀 Getting Started

### Prerequisites
- **iOS Development**: Xcode 15+, Swift 5.9+
- **Backend**: Python 3.11+, FastAPI, PostgreSQL 15+
- **Web**: Node.js 18+, React 18+, TypeScript 5+
- **Tools**: Docker, Git, Make

### Local Setup
```bash
# Clone repository
git clone https://github.com/alvarobcmed/simulation-3d-hof.git
cd simulation-3d-hof

# Setup environment
make setup-dev

# Start services
make dev-up

# Run tests
make test-all
```

## 📋 Development Process

### 1. Issue Creation
- Use templates em `.github/ISSUE_TEMPLATE/`
- Link para Requisitos Funcionais (RF-XXX)
- Inclua critérios de aceitação claros
- Adicione labels apropriadas

### 2. Branch Strategy
```bash
# Feature branches
git checkout -b feature/RF-001-arkit-capture
git checkout -b feature/RNF-003-performance-optimization

# Bug fixes
git checkout -b fix/simulation-memory-leak

# Documentation
git checkout -b docs/update-api-examples
```

### 3. Commit Convention
```bash
# Formato: type(scope): description [RF-XXX]
git commit -m "feat(capture): implement ARKit LiDAR integration [RF-001]"
git commit -m "fix(api): resolve authentication timeout [RNF-002]"
git commit -m "docs(adr): add security architecture decision"
```

**Tipos de commit**:
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação (sem mudança de lógica)
- `refactor`: Refatoração sem mudança de funcionalidade
- `test`: Adição/modificação de testes
- `chore`: Tarefas de manutenção

### 4. Pull Request Process

#### Antes de criar PR
```bash
# Certifique-se de que está atualizado
git pull origin main
git rebase main

# Execute todos os testes
make test-all

# Execute linters
make lint-all

# Execute security scan
make security-scan
```

#### PR Checklist
- [ ] Título descritivo incluindo RF/RNF
- [ ] Descrição completa com contexto
- [ ] Screenshots/GIFs para mudanças de UI
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Performance impact considerado
- [ ] Security review quando necessário

#### PR Template
```markdown
## Descrição
Breve descrição das mudanças implementadas.

## Tipo de Mudança
- [ ] Bug fix (mudança que corrige um problema)
- [ ] New feature (mudança que adiciona funcionalidade)
- [ ] Breaking change (mudança que quebra compatibilidade)
- [ ] Documentation update

## Requisitos Relacionados
- RF-XXX: [Descrição do requisito funcional]
- RNF-XXX: [Descrição do requisito não funcional]

## Como Testar
1. Passos para testar localmente
2. Dados de teste necessários
3. Cenários de edge case

## Checklist
- [ ] Meu código segue as diretrizes de estilo
- [ ] Fiz uma auto-revisão do meu código
- [ ] Comentei o código em partes complexas
- [ ] Mudanças geram warnings ou erros
- [ ] Adicionei testes que provam que minha correção é efetiva
- [ ] Testes unitários novos e existentes passam
- [ ] Mudanças requerem atualização de documentação
- [ ] Atualizei a documentação
```

## 🧪 Testing Guidelines

### Test Coverage Requirements
- **Unit Tests**: ≥ 80% coverage geral
- **Critical Paths**: 100% coverage (auth, payment, medical data)
- **Integration Tests**: Todos os endpoints da API
- **E2E Tests**: Fluxos críticos de usuário

### Test Structure
```python
# Python - pytest
def test_should_normalize_3d_mesh_successfully():
    """Test that 3D mesh normalization produces valid output."""
    # Given
    raw_mesh = create_test_mesh()
    
    # When
    normalized = normalize_mesh(raw_mesh)
    
    # Then
    assert normalized.is_valid()
    assert normalized.vertex_count > 0
    assert normalized.quality_score > 0.8
```

```typescript
// TypeScript - Jest
describe('MeshNormalization', () => {
  it('should normalize 3D mesh successfully', () => {
    // Given
    const rawMesh = createTestMesh();
    
    // When
    const normalized = normalizeMesh(rawMesh);
    
    // Then
    expect(normalized.isValid()).toBe(true);
    expect(normalized.vertexCount).toBeGreaterThan(0);
    expect(normalized.qualityScore).toBeGreaterThan(0.8);
  });
});
```

### Performance Testing
```python
@pytest.mark.performance
def test_mesh_processing_performance():
    """Mesh processing should complete within 5 seconds."""
    mesh = create_large_test_mesh()
    
    start_time = time.time()
    result = process_mesh(mesh)
    duration = time.time() - start_time
    
    assert duration < 5.0
    assert result.success
```

## 📝 Code Style Guidelines

### Python (Black + isort + flake8)
```python
# Good
def calculate_facial_symmetry(
    left_landmarks: List[Point3D],
    right_landmarks: List[Point3D],
    tolerance: float = 0.1,
) -> SymmetryScore:
    """Calculate facial symmetry score from landmarks."""
    if not left_landmarks or not right_landmarks:
        raise ValueError("Landmarks cannot be empty")
    
    # Calculate distances and compare
    score = compute_symmetry_metric(left_landmarks, right_landmarks)
    return SymmetryScore(value=score, tolerance=tolerance)
```

### TypeScript (ESLint + Prettier)
```typescript
// Good
interface MeshProcessingOptions {
  quality: 'low' | 'medium' | 'high';
  smoothing: boolean;
  decimation?: number;
}

export const processMesh = async (
  mesh: Mesh3D,
  options: MeshProcessingOptions
): Promise<ProcessedMesh> => {
  if (!mesh.isValid()) {
    throw new Error('Invalid mesh provided');
  }

  const processor = new MeshProcessor(options);
  return await processor.process(mesh);
};
```

### Swift (SwiftLint)
```swift
// Good
struct CaptureConfiguration {
    let quality: ARWorldTrackingConfiguration.FrameSemantics
    let enableLiDAR: Bool
    let maxDuration: TimeInterval
    
    static let standard = CaptureConfiguration(
        quality: .sceneDepth,
        enableLiDAR: true,
        maxDuration: 30.0
    )
}

protocol MeshCaptureDelegate: AnyObject {
    func captureDidComplete(_ mesh: ARMeshGeometry)
    func captureDidFail(error: CaptureError)
}
```

## 🔒 Security Guidelines

### Sensitive Data Handling
```python
# ❌ Never do this
def process_patient_data(patient_id: str):
    logger.info(f"Processing patient {patient_id}")  # Logs PII!

# ✅ Do this instead  
def process_patient_data(patient_id: str):
    logger.info("Processing patient data", extra={
        "patient_id_hash": hash_patient_id(patient_id)
    })
```

### API Security
```python
# Always validate input
from pydantic import BaseModel, validator

class SimulationRequest(BaseModel):
    dosage: float
    injection_points: List[Point3D]
    
    @validator('dosage')
    def validate_dosage(cls, v):
        if not 1.0 <= v <= 50.0:
            raise ValueError('Dosage must be between 1.0 and 50.0 units')
        return v
```

### Authentication
```python
# Always use dependency injection for auth
from fastapi import Depends, HTTPException
from .auth import get_current_user

@router.post("/simulations")
async def create_simulation(
    request: SimulationRequest,
    current_user: User = Depends(get_current_user)
):
    if not current_user.can_create_simulations():
        raise HTTPException(status_code=403, detail="Insufficient permissions")
```

## 📚 Documentation Standards

### Code Documentation
- **Functions**: Docstrings com exemplos
- **Classes**: Purpose e usage examples
- **APIs**: OpenAPI/Swagger specs completos
- **Architecture**: ADRs para decisões importantes

### API Documentation
```python
@router.post("/simulations/toxin", response_model=SimulationResult)
async def simulate_toxin_injection(
    request: ToxinSimulationRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Simulate botulinum toxin injection on 3D facial mesh.
    
    This endpoint performs finite element method (FEM) simulation
    to predict muscle relaxation effects from botulinum toxin injection.
    
    Args:
        request: Simulation parameters including mesh, injection points,
                dosage, and target muscle groups
        current_user: Authenticated user performing the simulation
        
    Returns:
        Simulation result with modified mesh and analysis metrics
        
    Raises:
        ValidationError: Invalid simulation parameters  
        InsufficientPermissionsError: User lacks simulation permissions
        ProcessingError: Simulation processing failed
        
    Example:
        ```python
        result = await simulate_toxin_injection(
            ToxinSimulationRequest(
                mesh_id="mesh_123",
                injection_points=[Point3D(x=10, y=20, z=5)],
                dosage=25.0,
                muscle_groups=[MuscleGroup.FRONTALIS]
            )
        )
        ```
    """
```

## 🐛 Debugging & Troubleshooting

### Local Development Issues
```bash
# Container issues
make dev-down && make dev-up

# Database issues  
make db-reset

# Cache issues
make cache-clear

# Full reset
make clean && make setup-dev
```

### Common Problems

**"Tests failing locally but passing in CI"**
- Ensure you're using the same Python/Node versions
- Check for race conditions in async tests
- Verify test isolation

**"Performance tests failing"**
- Run on the same hardware as CI
- Check for background processes
- Profile the slow operations

**"Docker build issues"**
- Clear Docker cache: `docker system prune -a`
- Check available disk space
- Verify Docker daemon is running

## 📞 Getting Help

### Team Communication
- **General Questions**: GitHub Discussions
- **Bug Reports**: GitHub Issues
- **Security Issues**: Email security@simulation3dhof.com
- **Architecture Decisions**: ADR discussions in PRs

### Code Review Process
1. **Self Review**: Review your own PR first
2. **Automated Checks**: Ensure all CI checks pass
3. **Peer Review**: Request review from appropriate team members
4. **Technical Review**: Senior dev approval for architectural changes
5. **Security Review**: Security team approval for auth/data changes

### Escalation Path
1. Team member → Tech Lead
2. Tech Lead → Engineering Manager  
3. Engineering Manager → CTO
4. For medical/regulatory: → Medical Advisory Board

---

**Obrigado por contribuir para o futuro da harmonização orofacial! 🚀**