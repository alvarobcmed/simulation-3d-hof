# ADR-003: Development Process and Quality Gates

**Status**: Proposto
**Data**: 2024-09-26
**Revisores**: Technical Team, QA Lead

## Context

O projeto Simulation 3D HOF é um sistema médico crítico que requer:

- **Qualidade Extrema**: Zero defeitos em funcionalidades críticas
- **Compliance**: Rastreabilidade completa RF↔Código↔Teste↔API↔DB
- **Segurança**: SAST/DAST sem vulnerabilidades críticas
- **Performance**: Garantias de SLA (p95 ≤ 30-50ms)
- **Manutenibilidade**: Código limpo, documentado, testável
- **Entrega Contínua**: Deploy frequente com confiança

### Restrições

- **Regulatórias**: Auditoria médica requer documentação completa
- **Equipe**: Desenvolvedores com níveis variados de experiência
- **Timeline**: Pressão por entrega rápida
- **Orçamento**: Ferramentas pagas limitadas

### Problemas a Resolver

- Como garantir qualidade sem sacrificar velocidade?
- Como manter rastreabilidade sem overhead excessivo?
- Como fazer code review efetivo em equipe pequena?
- Como automatizar qualidade sem custo proibitivo?

## Decision

### Git Workflow: GitHub Flow Modificado

```
main branch (production-ready)
├── feature/RF-001-arkit-capture
├── feature/RF-002-toxin-simulation  
├── hotfix/critical-security-patch
└── release/v1.0.0-rc1
```

#### Branch Strategy
```bash
# Feature branches
feature/RF-XXX-short-description    # Requisito funcional
feature/RNF-XXX-short-description   # Requisito não funcional
feature/TECH-XXX-short-description  # Melhorias técnicas

# Release branches
release/vX.Y.Z-rcN                  # Release candidates

# Hotfix branches  
hotfix/critical-description         # Correções críticas
```

#### Commit Convention
```bash
# Formato: type(scope): description [RF-XXX]
feat(capture): implement ARKit LiDAR integration [RF-001]
fix(simulation): resolve FEBio memory leak [RF-005]
docs(adr): add database architecture decision [TECH-002]
test(api): add integration tests for auth flow [RNF-003]
```

### Code Review Process

#### Mandatory Reviewers
```yaml
# .github/CODEOWNERS
# Global rules
* @tech-lead @senior-dev

# Critical paths
/backend/auth/ @security-expert @tech-lead
/ios/capture/ @ios-expert @tech-lead  
/simulation/ @physics-expert @tech-lead
/docs/adrs/ @architect @tech-lead
```

#### Review Checklist
```markdown
## Functional Review
- [ ] Implementa completamente o RF/RNF especificado
- [ ] Testes cobrem todos os cenários (happy path + edge cases)
- [ ] Documentação API atualizada (se aplicável)
- [ ] Performance dentro dos SLAs definidos

## Code Quality
- [ ] Segue padrões de código definidos
- [ ] Nomes descritivos e auto-documentados
- [ ] Funções pequenas e focadas (max 20 linhas)
- [ ] Zero code smells reportados pelo SonarQube

## Security & Compliance  
- [ ] Não expõe dados sensíveis
- [ ] Validação de input adequada
- [ ] Logs de auditoria implementados
- [ ] Sem vulnerabilidades SAST/DAST

## Testing
- [ ] Unit tests ≥ 80% coverage
- [ ] Integration tests para fluxos críticos
- [ ] Performance tests passando
- [ ] Accessibility tests (UI changes)
```

### Automated Quality Gates

#### Pre-commit Hooks (Husky + lint-staged)
```json
{
  "lint-staged": {
    "*.py": ["black", "isort", "flake8", "mypy"],
    "*.ts": ["eslint --fix", "prettier --write"],
    "*.swift": ["swiftlint autocorrect"],
    "*.sql": ["sqlfluff fix"]
  }
}
```

#### CI Pipeline (GitHub Actions)
```yaml
# .github/workflows/quality-gate.yml
name: Quality Gate

on: [push, pull_request]

jobs:
  unit-tests:
    strategy:
      matrix:
        component: [backend, web, ios]
    steps:
      - name: Run Tests
        run: make test-${{ matrix.component }}
      - name: Coverage Report  
        run: make coverage-${{ matrix.component }}

  integration-tests:
    needs: unit-tests
    steps:
      - name: Start Services
        run: docker-compose up -d
      - name: Run Integration Tests
        run: make test-integration
      - name: Performance Tests
        run: make test-performance

  security-scan:
    steps:
      - name: SAST Scan
        run: make security-sast
      - name: Dependency Check
        run: make security-deps
      - name: Container Scan
        run: make security-containers

  quality-check:
    steps:
      - name: Code Quality (SonarQube)
        run: make quality-sonar
      - name: Architecture Tests
        run: make test-architecture
```

### Testing Strategy

#### Pyramid de Testes
```
              ┌─────────────────┐
              │   E2E Tests     │  ← 5% (Críticos)
              │   (Playwright)  │
              └─────────────────┘
            ┌─────────────────────┐
            │ Integration Tests   │  ← 15% (APIs + DB)
            │  (pytest + TestAPI) │
            └─────────────────────┘
        ┌─────────────────────────────┐
        │      Unit Tests             │  ← 80% (Lógica)
        │ (pytest/Jest/XCTest)        │
        └─────────────────────────────┘
```

#### Test Categories
```python
# Unit Tests (80% coverage target)
- Lógica de negócio pura
- Transformações de dados
- Validações e cálculos
- Mocks para dependências externas

# Integration Tests (100% coverage para fluxos críticos)
- API endpoints com database real
- Integrações com serviços externos
- Message queue processing
- File upload/download workflows

# E2E Tests (Cenários críticos apenas)
- Login e autenticação completa
- Captura 3D end-to-end
- Simulação completa (toxina)
- Export de relatórios
```

#### Test Data Management
```yaml
# Estratégia de dados de teste
Development:
  - Fixtures com dados sintéticos
  - Factories para geração automática
  - Reset automático entre testes

Staging:
  - Dados anonimizados de produção
  - Refresh semanal automático
  - Cenários específicos de teste

Production:
  - Smoke tests apenas
  - Dados reais, testes não-destrutivos
  - Monitoring contínuo
```

### Documentation Standards

#### Code Documentation
```python
# Python (Google Style)
def simulate_toxin_injection(
    mesh: Mesh3D, 
    injection_points: List[Point3D],
    dosage: float,
    muscle_groups: List[MuscleGroup]
) -> SimulationResult:
    """Simula injeção de toxina botulínica em malha 3D.
    
    Args:
        mesh: Malha 3D facial normalizada
        injection_points: Pontos de injeção em coordenadas 3D
        dosage: Dosagem em unidades Botox (1-50U)
        muscle_groups: Grupos musculares alvo
        
    Returns:
        Resultado da simulação com mesh modificada e métricas
        
    Raises:
        InvalidDosageError: Se dosagem fora do range seguro
        MeshNotNormalizedError: Se malha não foi normalizada
        
    Example:
        >>> result = simulate_toxin_injection(
        ...     mesh=normalized_face,
        ...     injection_points=[Point3D(10, 20, 5)],
        ...     dosage=25.0,
        ...     muscle_groups=[MuscleGroup.FRONTALIS]
        ... )
        >>> assert result.success
    """
```

#### API Documentation
```yaml
# OpenAPI 3.0 com exemplos completos
paths:
  /api/v1/simulations/toxin:
    post:
      summary: "Simular injeção de toxina botulínica"
      description: |
        Realiza simulação FEM de injeção de toxina botulínica
        considerando biomecânica muscular e difusão.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ToxinSimulationRequest'
            examples:
              frontalis_treatment:
                summary: "Tratamento de rugas frontais"
                value:
                  mesh_id: "mesh_123"
                  injection_points: [{"x": 10, "y": 20, "z": 5}]
                  dosage: 25.0
                  muscle_groups: ["FRONTALIS"]
```

### Performance and Monitoring

#### Performance Testing
```python
# Performance benchmarks
@pytest.mark.performance
def test_mesh_normalization_performance():
    """Normalização deve processar em < 5 segundos."""
    start_time = time.time()
    result = normalize_mesh(large_test_mesh)
    duration = time.time() - start_time
    
    assert duration < 5.0
    assert result.quality_score > 0.95

# Load testing (k6)
export let options = {
  thresholds: {
    http_req_duration: ['p(95)<50'], // 95% < 50ms
    http_req_failed: ['rate<0.01'],  // <1% failures
  }
};
```

#### Observability
```yaml
# Métricas obrigatórias
Business Metrics:
  - Simulações por dia/hora
  - Taxa de sucesso de captura 3D
  - Tempo médio de processamento
  - Usuários ativos (DAU/MAU)

Technical Metrics:
  - Response time p50/p95/p99
  - Error rate por endpoint
  - Database connection pool
  - Memory/CPU utilization

# Alertas críticos
alerts:
  - API response time p95 > 100ms
  - Error rate > 1%
  - Database connections > 80%
  - Failed simulations > 5%
```

### Release Process

#### Semantic Versioning
```
vMAJOR.MINOR.PATCH[-PRERELEASE]

Examples:
v1.0.0        # Initial release
v1.1.0        # New features (RF-006, RF-007)
v1.1.1        # Bug fixes
v1.2.0-rc.1   # Release candidate
v2.0.0        # Breaking changes
```

#### Release Checklist
```markdown
## Pre-Release
- [ ] All tests passing (unit + integration + E2E)
- [ ] Performance tests within SLAs
- [ ] Security scan clean (SAST/DAST)
- [ ] Documentation updated
- [ ] Migration scripts tested
- [ ] Rollback plan prepared

## Release
- [ ] Tag created with release notes
- [ ] Deployed to staging first
- [ ] Smoke tests on staging passed
- [ ] Database migrations applied
- [ ] Production deployment
- [ ] Post-deployment verification

## Post-Release
- [ ] Monitoring dashboards checked
- [ ] Error rates within normal range
- [ ] Performance metrics stable
- [ ] User acceptance confirmed
- [ ] Hotfix plan activated if needed
```

## Consequences

### Positivas

**Qualidade**:
- Múltiplas camadas de validação previnem defeitos
- Rastreabilidade completa facilita auditoria
- Automated testing reduz regression bugs
- Code review compartilha conhecimento

**Velocidade**:
- CI/CD permite deploy frequente
- Automated quality gates reduzem overhead manual
- Parallel testing acelera feedback
- Feature flags permitem releases incrementais

**Compliance**:
- Documentação automática mantém-se atualizada
- Audit trail completo para reguladores
- Security scanning contínuo previne vulnerabilidades
- Performance monitoring garante SLAs

### Negativas

**Overhead Inicial**:
- Setup de ferramentas demanda tempo
- Learning curve para processo novo
- Infraestrutura de CI/CD complexa
- Necessidade de treinamento da equipe

**Rigidez**:
- Processo pode ser visto como burocrático
- Emergências podem ser dificultadas
- Experimentos rápidos desencorajados
- Overhead para mudanças pequenas

**Custo de Tooling**:
- SonarQube Professional (~$15k/ano)
- GitHub Actions minutes
- Monitoring tools (Datadog/NewRelic)
- Security scanning tools

## Implementation Notes

### Fase 1: Básico (Semana 1)
```bash
# Setup inicial
- Configure pre-commit hooks
- Setup GitHub Actions básico
- Implement branch protection rules
- Create PR templates
```

### Fase 2: Qualidade (Semana 2)
```bash
# Automated quality
- Integrate SonarQube
- Setup SAST scanning
- Implement coverage reporting
- Add performance tests
```

### Fase 3: Observabilidade (Semana 3)
```bash
# Monitoring & alerts
- Setup application monitoring
- Implement custom metrics
- Configure alerting rules
- Create dashboards
```

### Tooling Budget (Anual)
```yaml
Required:
  - GitHub Pro: $4/user/month
  - SonarQube: $15,000/year
  - Monitoring: $5,000/year
  
Optional:
  - Snyk Security: $5,000/year
  - Performance Tools: $3,000/year
  
Total: ~$30,000/year
```

## References

- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [SonarQube Quality Gates](https://docs.sonarqube.org/latest/user-guide/quality-gates/)
- [Medical Software Quality Standards](https://www.fda.gov/medical-devices/software-medical-device-samd/software-medical-device-quality-management-system)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)