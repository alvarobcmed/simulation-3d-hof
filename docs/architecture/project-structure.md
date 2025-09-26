# Project Structure

Este documento descreve a estrutura organizacional do projeto Simulation 3D HOF.

## Visão Geral

O projeto segue uma arquitetura de **monorepo modular** com separação clara entre frontend, backend, documentação e infraestrutura.

```
simulation-3d-hof/
├── README.md                    # Visão geral do projeto
├── CONTRIBUTING.md              # Guia de contribuição
├── LICENSE                      # Licença do projeto
├── Makefile                     # Comandos de automação
├── docker-compose.yml           # Orquestração local
├── .github/                     # GitHub workflows e templates
│   ├── workflows/              # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/         # Templates de issues
│   └── PULL_REQUEST_TEMPLATE/  # Template de PR
├── docs/                       # Documentação do projeto
│   ├── adrs/                   # Architecture Decision Records
│   ├── api/                    # Documentação da API
│   ├── architecture/           # Documentos arquiteturais
│   └── deployment/             # Guias de deployment
├── ios/                        # Aplicativo iOS nativo
│   ├── SimulationHOF/         # Projeto Xcode principal
│   ├── SimulationHOFTests/    # Testes unitários
│   ├── Frameworks/            # Unity framework integration
│   └── Scripts/               # Scripts de build
├── web/                        # Progressive Web App
│   ├── src/                   # Código fonte React
│   ├── public/                # Assets estáticos
│   ├── tests/                 # Testes frontend
│   └── docs/                  # Documentação específica
├── backend/                    # APIs e serviços Python
│   ├── core/                  # API Gateway (FastAPI)
│   ├── capture/               # Serviço de captura 3D
│   ├── simulation/            # Engine de simulação
│   ├── analytics/             # Serviço de análise
│   ├── integrations/          # Conectores externos
│   ├── shared/                # Utilitários compartilhados
│   ├── tests/                 # Testes backend
│   └── migrations/            # Migrações de banco
├── simulation-engine/          # Microserviço SOFA/FEBio
│   ├── src/                   # Código C++/Python
│   ├── models/                # Modelos biomecânicos
│   ├── solvers/               # Solvers customizados
│   └── tests/                 # Testes específicos
├── database/                   # Scripts de banco
│   ├── migrations/            # Migrações SQL
│   ├── seeds/                 # Dados iniciais
│   └── schemas/               # Definições de schema
├── infrastructure/             # Infraestrutura como código
│   ├── terraform/             # Definições Terraform
│   ├── kubernetes/            # Manifests K8s
│   ├── docker/                # Dockerfiles específicos
│   └── monitoring/            # Configurações de observabilidade
├── tools/                      # Ferramentas e scripts
│   ├── generators/            # Geradores de código
│   ├── validators/            # Validadores customizados
│   └── migration-tools/       # Ferramentas de migração
└── tests/                      # Testes end-to-end
    ├── e2e/                   # Testes Playwright
    ├── load/                  # Testes de carga (k6)
    ├── fixtures/              # Dados de teste
    └── utils/                 # Utilitários de teste
```

## Detalhamento por Módulo

### 📱 iOS App (`/ios/`)

**Estrutura**:
```
ios/
├── SimulationHOF/
│   ├── App/                   # App delegate e configuração
│   ├── Features/              # Features por módulo
│   │   ├── Capture/          # Captura 3D com ARKit
│   │   ├── Simulation/       # Interface de simulação
│   │   ├── Analysis/         # Análise e relatórios
│   │   └── Settings/         # Configurações
│   ├── Shared/               # Componentes compartilhados
│   │   ├── UI/              # UI components
│   │   ├── Services/        # Services layer
│   │   ├── Models/          # Data models
│   │   └── Extensions/      # Swift extensions
│   ├── Resources/            # Assets, strings, etc.
│   └── Unity/               # Integration com Unity
├── Frameworks/               # Unity e frameworks externos
└── Scripts/                  # Build e deployment scripts
```

**Responsabilidades**:
- Captura 3D usando ARKit + LiDAR
- Interface nativa iOS otimizada
- Integração com Unity para renderização
- Sincronização com backend via APIs

### 🌐 Web PWA (`/web/`)

**Estrutura**:
```
web/
├── src/
│   ├── components/           # Componentes React reutilizáveis
│   │   ├── ui/              # Componentes básicos de UI
│   │   ├── forms/           # Formulários e inputs
│   │   └── 3d/              # Componentes 3D (Three.js)
│   ├── pages/               # Páginas da aplicação
│   │   ├── Dashboard/       # Dashboard principal
│   │   ├── Capture/         # Captura via fotogrametria
│   │   ├── Simulation/      # Interface de simulação
│   │   └── Reports/         # Relatórios e análises
│   ├── services/            # Services para APIs
│   ├── hooks/               # Custom React hooks
│   ├── store/               # Estado global (Redux/Zustand)
│   ├── utils/               # Utilitários
│   └── types/               # TypeScript definitions
├── public/                  # Assets estáticos
├── tests/                   # Testes Jest/RTL
└── docs/                    # Documentação específica
```

**Responsabilidades**:
- Interface web responsiva
- Captura via fotogrametria (fallback)
- Visualização 3D com WebGPU/WebGL
- PWA capabilities (offline, push notifications)

### 🔧 Backend (`/backend/`)

**Estrutura**:
```
backend/
├── core/                    # API Gateway principal
│   ├── main.py             # FastAPI app
│   ├── routers/            # Route handlers
│   ├── middleware/         # Middleware customizado
│   ├── auth/               # Autenticação e autorização
│   └── config/             # Configurações
├── capture/                # Serviço de captura 3D
│   ├── processors/         # Processamento de mesh
│   ├── validators/         # Validação de qualidade
│   └── exporters/          # Export para DICOM
├── simulation/             # Interface com simulation engine
│   ├── toxin/              # Simulações de toxina
│   ├── fillers/            # Simulações de fillers
│   ├── pdo/                # Simulações de fios PDO
│   └── energy/             # Tecnologias de energia
├── analytics/              # Análise e métricas
│   ├── facial/             # Análise facial
│   ├── symmetry/           # Cálculo de simetria
│   └── reports/            # Geração de relatórios
├── integrations/           # Integrações externas
│   ├── crm/                # Conectores CRM
│   ├── emr/                # Conectores EMR
│   └── pacs/               # Interface PACS/DICOM
├── shared/                 # Código compartilhado
│   ├── models/             # Pydantic models
│   ├── database/           # Database utilities
│   ├── security/           # Security utilities
│   └── exceptions/         # Exception handlers
└── tests/                  # Testes backend
    ├── unit/               # Testes unitários
    ├── integration/        # Testes de integração
    └── fixtures/           # Fixtures de teste
```

**Responsabilidades**:
- APIs RESTful com FastAPI
- Orquestração de serviços
- Autenticação e autorização
- Integração com sistemas externos

### 🧮 Simulation Engine (`/simulation-engine/`)

**Estrutura**:
```
simulation-engine/
├── src/
│   ├── core/               # Core simulation logic
│   ├── solvers/            # Custom FEM solvers
│   ├── materials/          # Material properties
│   ├── meshes/             # Mesh processing
│   └── api/                # REST API interface
├── models/                 # Biomechanical models
│   ├── facial/             # Facial anatomy models
│   ├── muscles/            # Muscle group definitions
│   └── tissues/            # Tissue property definitions
├── config/                 # SOFA scene configurations
└── tests/                  # Simulation tests
```

**Responsabilidades**:
- Simulações FEM com SOFA/FEBio
- Cálculos biomecânicos
- Processamento de alta performance
- API para comunicação com backend

### 🗄️ Database (`/database/`)

**Estrutura**:
```
database/
├── migrations/             # Migrações Alembic
│   ├── versions/          # Arquivos de migração
│   └── alembic.ini        # Configuração Alembic
├── seeds/                 # Dados iniciais
│   ├── dev/               # Dados de desenvolvimento
│   ├── staging/           # Dados de staging
│   └── production/        # Dados mínimos de produção
├── schemas/               # Definições de schema
│   ├── user.sql           # Schema de usuários
│   ├── simulation.sql     # Schema de simulações
│   └── audit.sql          # Schema de auditoria
└── scripts/               # Scripts utilitários
    ├── backup.sh          # Script de backup
    └── restore.sh         # Script de restore
```

**Responsabilidades**:
- Estrutura de dados relacional
- Versionamento de schema
- Scripts de manutenção
- Dados de teste e produção

### 🏗️ Infrastructure (`/infrastructure/`)

**Estrutura**:
```
infrastructure/
├── terraform/
│   ├── aws/               # Recursos AWS
│   ├── azure/             # Recursos Azure
│   ├── modules/           # Módulos reutilizáveis
│   └── environments/      # Configurações por ambiente
├── kubernetes/
│   ├── base/              # Manifests base
│   ├── overlays/          # Kustomize overlays
│   └── operators/         # Custom operators
├── docker/
│   ├── Dockerfile.backend # Backend container
│   ├── Dockerfile.web     # Web container
│   └── Dockerfile.simulation # Simulation engine
└── monitoring/
    ├── prometheus/        # Configuração Prometheus
    ├── grafana/           # Dashboards Grafana
    └── alertmanager/      # Regras de alerta
```

**Responsabilidades**:
- Infraestrutura como código
- Orquestração de containers
- Monitoring e observabilidade
- Deployment automatizado

### 🔧 Tools (`/tools/`)

**Estrutura**:
```
tools/
├── generators/
│   ├── api-client.py      # Gerador de client APIs
│   ├── migration.py       # Gerador de migrações
│   └── component.js       # Gerador de componentes React
├── validators/
│   ├── mesh-quality.py    # Validador de qualidade de mesh
│   ├── api-compliance.py  # Validador de compliance API
│   └── security-scan.py   # Scanner de segurança
└── migration-tools/
    ├── data-migration.py  # Ferramenta de migração de dados
    └── version-upgrade.py # Ferramenta de upgrade de versão
```

**Responsabilidades**:
- Automação de tarefas repetitivas
- Validação de qualidade
- Ferramentas de desenvolvimento
- Scripts de migração

### 🧪 Tests (`/tests/`)

**Estrutura**:
```
tests/
├── e2e/                   # Testes end-to-end
│   ├── user-flows/       # Fluxos de usuário
│   ├── api-integration/  # Testes de integração API
│   └── performance/      # Testes de performance
├── load/                 # Testes de carga
│   ├── scenarios/        # Cenários de teste
│   └── results/          # Resultados históricos
├── fixtures/             # Dados de teste
│   ├── meshes/           # Modelos 3D de teste
│   ├── users/            # Dados de usuário
│   └── simulations/      # Resultados de simulação
└── utils/                # Utilitários de teste
    ├── helpers.py        # Funções auxiliares
    └── assertions.py     # Assertions customizadas
```

**Responsabilidades**:
- Testes de integração completa
- Validação de performance
- Dados de teste padronizados
- Utilitários de teste compartilhados

## Convenções de Nomenclatura

### Diretórios
- **kebab-case**: `simulation-engine`, `api-gateway`
- **Singular**: `user`, `simulation` (não `users`, `simulations`)
- **Descritivo**: Nomes que descrevem claramente o propósito

### Arquivos
- **Python**: `snake_case.py`
- **JavaScript/TypeScript**: `camelCase.ts`, `PascalCase.tsx` (componentes)
- **Swift**: `PascalCase.swift`
- **Configuration**: `kebab-case.yml`, `lowercase.json`

### Código
- **Classes**: `PascalCase`
- **Functions/Methods**: `camelCase` (JS/TS), `snake_case` (Python)
- **Constants**: `UPPER_SNAKE_CASE`
- **Variables**: `camelCase` (JS/TS), `snake_case` (Python)

## Dependências Compartilhadas

### Development
```json
{
  "tools": [
    "pre-commit",
    "husky", 
    "lint-staged",
    "commitizen"
  ],
  "testing": [
    "jest",
    "pytest", 
    "playwright",
    "k6"
  ],
  "quality": [
    "eslint",
    "prettier",
    "black",
    "mypy",
    "sonarqube"
  ]
}
```

### Runtime
```yaml
Backend:
  - FastAPI 0.104+
  - PostgreSQL 15+
  - Redis 7+
  - Celery 5+

Frontend:
  - React 18+
  - TypeScript 5+
  - Three.js/Babylon.js
  - Material-UI

Mobile:
  - Swift 5.9+
  - ARKit 6.0+
  - Unity 2023.2 LTS

Infrastructure:
  - Docker & Docker Compose
  - Terraform
  - Kubernetes (optional)
  - Prometheus & Grafana
```

## Próximos Passos

1. **PR 1**: Implementar scaffold básico desta estrutura
2. **PR 2**: Configurar CI/CD pipelines
3. **PR 3**: Setup de desenvolvimento local
4. **PR 4**: Implementar primeiro módulo (captura 3D)

Para detalhes específicos de implementação, consulte os ADRs em `/docs/adrs/`.