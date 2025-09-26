# ADR-001: Technology Stack Selection

**Status**: Proposto
**Data**: 2024-09-26
**Revisores**: Technical Team

## Context

O projeto Simulation 3D HOF requer um espelho inteligente 3D para simulação em tempo real de procedimentos de harmonização orofacial. As principais necessidades técnicas incluem:

- Captura 3D de alta qualidade em tempo real
- Renderização 3D interativa com performance ≤ 50ms (p95)
- Simulações científicas complexas (FEM, biomecânica)
- Integração com sistemas médicos (PACS/DICOM, CRM/EMR)
- Compliance médico (LGPD/GDPR, rastreabilidade completa)
- Escalabilidade para múltiplos usuários simultâneos
- Disponibilidade multiplataforma (iOS, Web, Desktop)

### Restrições
- Foco inicial em iOS (ARKit + LiDAR disponível)
- Orçamento limitado para infraestrutura
- Equipe pequena com expertise em Python/JavaScript
- Timeline agressivo (6 meses para MVP)

### Alternativas Consideradas

**Mobile Development**:
- Swift + ARKit vs React Native vs Flutter vs Unity
- Native iOS escolhido para máxima performance em captura 3D

**Backend/API**:
- FastAPI vs Django REST vs Node.js vs Go
- FastAPI escolhido pela documentação automática e performance

**3D Rendering**:
- Unity vs Unreal vs Three.js vs WebGPU nativo
- Híbrido: Unity para iOS, WebGPU para Web

**Database**:
- PostgreSQL vs MongoDB vs MySQL
- PostgreSQL escolhido por suporte JSONB e compliance médico

**Scientific Computing**:
- SOFA vs FEBio vs Custom solution
- SOFA/FEBio escolhidos por serem padrão médico

## Decision

### Core Stack

**Frontend**:
- **iOS App**: Swift 5.9+ com ARKit 6.0, Unity 2023.2 LTS para renderização 3D
- **Web PWA**: React 18+ com TypeScript, WebGPU via three.js/babylon.js
- **Admin Panel**: React + Material-UI para gestão

**Backend**:
- **API Layer**: FastAPI 0.104+ com Python 3.11+
- **Scientific Computing**: SOFA Framework + FEBio para simulações FEM
- **Task Queue**: Celery com Redis para processamento assíncrono

**Data**:
- **Primary DB**: PostgreSQL 15+ com extensões PostGIS e pgcrypto
- **Object Storage**: MinIO (S3-compatible) para modelos 3D e texturas  
- **Cache**: Redis 7+ para sessões e cache de resultados
- **Search**: PostgreSQL Full-Text Search (inicialmente)

**Infrastructure**:
- **Containerization**: Docker + Docker Compose
- **Orchestration**: Kubernetes (futuro) ou Docker Swarm (MVP)
- **IaC**: Terraform para AWS/Azure
- **Monitoring**: OpenTelemetry + Prometheus + Grafana
- **CI/CD**: GitHub Actions

**Development Tools**:
- **Code Quality**: ESLint, Prettier, Black, mypy, SwiftLint
- **Testing**: pytest, Jest, XCTest, Playwright para E2E
- **Documentation**: Sphinx para Python, Typedoc para TS, Jazzy para Swift

## Consequences

### Positivas

**Performance e Qualidade**:
- ARKit + Unity fornece captura 3D e renderização de classe mundial
- FastAPI oferece performance excelente com documentação automática
- PostgreSQL garante ACID compliance necessário para dados médicos
- Stack moderna com forte ecossistema de ferramentas

**Desenvolvimento**:
- TypeScript reduz bugs em produção 
- Tooling robusto acelera desenvolvimento
- Hot reload e debugging eficiente
- Reutilização de código entre Web e Admin

**Compliance e Segurança**:
- PostgreSQL + pgcrypto facilita criptografia de dados
- OpenTelemetry fornece rastreabilidade completa
- Stack bem documentada facilita auditorias

### Negativas

**Complexidade**:
- Stack heterogênea requer expertise em múltiplas tecnologias
- Unity adiciona complexidade de build e deployment
- SOFA/FEBio têm curva de aprendizado íngreme

**Vendor Lock-in**:
- ARKit limita a iOS (mitigado por fallback fotogrametria)
- Unity requer licença Pro para features avançadas
- Cloud provider lock-in (mitigado por Terraform)

**Performance Trade-offs**:
- WebGPU ainda em desenvolvimento, fallback para WebGL
- Python pode ser limitante para cálculos intensivos (mitigado por SOFA/FEBio)

## Implementation Notes

### Fase 1: Scaffold e Infraestrutura
1. Setup repositório com estrutura monorepo
2. Configurar Docker e Docker Compose
3. Setup CI/CD básico com GitHub Actions
4. Implementar FastAPI com PostgreSQL básico

### Fase 2: Core Services
1. Implementar serviço de captura 3D (iOS)
2. Implementar APIs básicas (CRUD)
3. Setup Redis para cache
4. Implementar autenticação JWT

### Fase 3: Advanced Features
1. Integrar SOFA/FEBio
2. Implementar WebGPU rendering
3. Setup MinIO para storage
4. Implementar integração DICOM

### Cronograma Estimado
- Scaffold: 2 semanas
- Core Services: 4 semanas  
- Advanced Features: 8 semanas
- Polish & Hardening: 4 semanas

## References

- [ARKit Documentation](https://developer.apple.com/documentation/arkit/)
- [FastAPI Performance Benchmarks](https://fastapi.tiangolo.com/benchmarks/)
- [PostgreSQL in Medical Applications](https://www.postgresql.org/about/success-stories/hipaa/)
- [SOFA Framework](https://www.sofa-framework.org/)
- [WebGPU Specification](https://www.w3.org/TR/webgpu/)
- [Unity for iOS Best Practices](https://docs.unity3d.com/Manual/ios-best-practice.html)