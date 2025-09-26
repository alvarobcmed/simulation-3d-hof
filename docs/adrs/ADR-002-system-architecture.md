# ADR-002: System Architecture Overview

**Status**: Proposto
**Data**: 2024-09-26
**Revisores**: Technical Team, Medical Advisory Board

## Context

O sistema Simulation 3D HOF requer uma arquitetura que suporte:

- **Escalabilidade**: Múltiplos usuários simultâneos realizando captura 3D e simulações
- **Performance**: Renderização interativa < 50ms, simulações FEM em tempo aceitável
- **Segurança**: Dados médicos sensíveis, compliance LGPD/GDPR
- **Confiabilidade**: Disponibilidade 99.9%, recuperação de falhas
- **Extensibilidade**: Adição de novos tipos de simulação e integrações
- **Observabilidade**: Rastreabilidade completa para auditoria médica

### Restrições Arquiteturais

- **Regulatórias**: Compliance médico, auditoria completa
- **Performance**: Tempo real para renderização, batch para simulações complexas
- **Recursos**: Equipe pequena, orçamento limitado inicial
- **Tecnológicas**: Integração com Unity (iOS), WebGPU (Web), SOFA/FEBio

### Alternativas Consideradas

**Arquiteturais**:
1. **Monolito**: Simples mas não escalável
2. **Microserviços**: Complexo mas escalável
3. **Modular Monolito**: Compromisso entre simplicidade e escalabilidade

**Deployment**:
1. **Single Cloud**: Vendor lock-in mas simples
2. **Multi-Cloud**: Resiliente mas complexo
3. **Hybrid**: On-premise + Cloud para dados sensíveis

**Data Architecture**:
1. **CRUD Simples**: Fácil mas limitado
2. **Event Sourcing**: Auditoria completa mas complexo
3. **CQRS**: Separação leitura/escrita, performance

## Decision

### Arquitetura Geral: Modular Monolito com Microserviços Seletivos

```
┌─────────────────────────────────────────────────────────────────┐
│                        Presentation Layer                       │
├─────────────────┬─────────────────┬─────────────────┬───────────┤
│   iOS App       │   Web PWA       │  Admin Panel    │ Public API│
│ (Swift/Unity)   │(React/WebGPU)   │  (React/TS)     │ (REST)    │
└─────────────────┴─────────────────┴─────────────────┴───────────┘
         │                 │                 │             │
         └─────────────────┼─────────────────┼─────────────┘
                           │                 │
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway Layer                          │
│                  (FastAPI + Nginx + Auth)                      │
└─────────────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────────┐
│                     Business Logic Layer                        │
├───────────────┬─────────────┬─────────────┬─────────────────────┤
│ 3D Capture    │ Simulation  │ Analytics   │ Integration         │
│ Service       │ Engine      │ Service     │ Service             │
│ (Modular)     │(Microservice│ (Modular)   │ (Modular)           │
└───────────────┴─────────────┴─────────────┴─────────────────────┘
                           │
┌─────────────────────────────────────────────────────────────────┐
│                        Data Layer                               │
├─────────────────┬─────────────┬─────────────┬─────────────────┤
│ PostgreSQL      │ MinIO       │ Redis       │ Message Queue    │
│ (Primary Data)  │ (Objects)   │ (Cache)     │ (RabbitMQ)      │
└─────────────────┴─────────────┴─────────────┴─────────────────┘
```

### Core Services Design

#### 1. API Gateway (FastAPI Core)
```python
# Responsabilidades:
- Authentication/Authorization (JWT + FIDO2)
- Rate limiting e throttling
- Request/Response logging
- OpenAPI documentation
- CORS e Security headers
```

#### 2. 3D Capture Service (Modular)
```
Módulos:
├── ARKit Integration
├── Photogrammetry Fallback  
├── Mesh Normalization
├── DICOM Export
└── Quality Validation
```

#### 3. Simulation Engine (Microservice)
```
Componentes:
├── SOFA/FEBio Interface
├── Simulation Queue Management
├── Result Caching
├── Progress Tracking
└── Resource Management
```

#### 4. Analytics Service (Modular)
```
Features:
├── Facial Analysis
├── Symmetry Calculation
├── Before/After Comparison
├── Report Generation
└── Export Utilities
```

#### 5. Integration Service (Modular)
```
Integrações:
├── CRM/EMR Connectors
├── PACS/DICOM Interface
├── External APIs
├── Data Synchronization
└── Audit Logging
```

### Data Architecture

#### Primary Data (PostgreSQL)
```sql
-- Core Entities
Users (patients, doctors, admins)
Sessions (capture + simulation sessions)
Models3D (mesh data metadata)
Simulations (parameters + results)
Procedures (medical procedure definitions)
Audit_Log (compliance tracking)
```

#### Object Storage (MinIO)
```
Structure:
├── raw-captures/          # Original 3D captures
├── normalized-models/     # Processed meshes
├── simulation-results/    # FEM outputs
├── textures/             # UV maps and materials
└── exports/              # DICOM and reports
```

#### Cache Layer (Redis)
```
Usage:
├── Session management
├── Simulation results cache
├── API response cache
├── Real-time progress tracking
└── Rate limiting data
```

### Security Architecture

#### Authentication Flow
```
1. User → Login Request
2. API Gateway → Validate Credentials
3. Generate JWT + Refresh Token
4. Optional: FIDO2 Challenge
5. Return Authenticated Session
```

#### Data Protection
```
├── Encryption at Rest (AES-256)
├── Encryption in Transit (TLS 1.3)
├── Field-level encryption (PII)
├── Database row-level security
└── Object storage access control
```

#### Audit System
```
Rastreabilidade:
├── Every API call logged
├── Data changes tracked
├── User actions recorded
├── System events captured
└── Compliance reports automated
```

## Consequences

### Positivas

**Escalabilidade**:
- Simulation Engine como microserviço permite scaling independente
- Modular monolito reduz complexidade inicial
- Cache agressivo melhora performance
- Message queue permite processamento assíncrono

**Segurança**:
- Arquitetura de camadas facilita controle de acesso
- Audit logging garante compliance
- Criptografia em múltiplas camadas
- Isolamento de dados sensíveis

**Manutenibilidade**:
- Separação clara de responsabilidades
- APIs bem definidas entre módulos
- Documentação automática com OpenAPI
- Observabilidade integrada

**Performance**:
- Cache em múltiplas camadas
- Processamento assíncrono para operações pesadas
- CDN para assets estáticos
- Database optimization com índices adequados

### Negativas

**Complexidade Operacional**:
- Múltiplos componentes para monitorar
- Configuração de networking complexa
- Backup e recovery mais sofisticado
- Debugging distribuído

**Latência de Rede**:
- Comunicação entre serviços adiciona latência
- Serialização/deserialização overhead
- Possível single point of failure no API Gateway

**Desenvolvimento Inicial**:
- Setup mais complexo
- Necessidade de mocking para desenvolvimento
- Testes de integração mais elaborados

## Implementation Notes

### Fase 1: Monolito Modular (Semanas 1-4)
```bash
# Estrutura inicial
simulation-3d-hof/
├── backend/
│   ├── core/           # API Gateway
│   ├── capture/        # 3D Capture Service
│   ├── analytics/      # Analytics Service
│   └── integrations/   # Integration Service
├── database/
│   ├── migrations/
│   └── seeds/
└── docker-compose.yml
```

### Fase 2: Microserviço de Simulação (Semanas 5-8)
```bash
# Separar simulation engine
├── simulation-service/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
└── docker-compose.yml  # Updated
```

### Fase 3: Hardening e Observabilidade (Semanas 9-12)
```bash
# Adicionar infraestrutura
├── monitoring/
│   ├── prometheus/
│   ├── grafana/
│   └── jaeger/
├── nginx/
│   └── nginx.conf
└── terraform/
    ├── aws/
    └── azure/
```

### Deployment Strategy

#### Development
```yaml
# docker-compose.dev.yml
- Hot reload habilitado
- Debug logging
- Seed data
- Local storage
```

#### Staging  
```yaml
# docker-compose.staging.yml
- Production-like environment
- Real integrations (sandbox)
- Performance testing
- Security scanning
```

#### Production
```yaml
# kubernetes ou docker-compose.prod.yml
- High availability
- Auto-scaling
- Monitoring completo
- Backup automatizado
```

## References

- [Modular Monolith Architecture](https://www.kamilgrzybek.com/design/modular-monolith-primer/)
- [FastAPI Production Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [PostgreSQL High Performance](https://postgresql.org/docs/current/performance-tips.html)
- [MinIO Production Deployment](https://docs.min.io/minio/baremetal/installation/deployment-and-management.html)
- [SOFA Framework Architecture](https://www.sofa-framework.org/community/doc/main-principles/architecture/)
- [Medical Data Security Standards](https://www.hhs.gov/hipaa/for-professionals/security/index.html)