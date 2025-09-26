# Makefile for 3D Orofacial Harmonization Simulation Project

.PHONY: help setup clean build test lint security deploy

# Default target
help:
	@echo "Available targets:"
	@echo "  setup          - Set up development environment"
	@echo "  clean          - Clean build artifacts and dependencies"
	@echo "  build          - Build all services and applications"
	@echo "  test           - Run all tests"
	@echo "  lint           - Run linting and code quality checks"
	@echo "  security       - Run security scans"
	@echo "  deploy-local   - Deploy to local development environment"
	@echo "  deploy-staging - Deploy to staging environment"
	@echo "  docs           - Generate documentation"

# Environment setup
setup:
	@echo "Setting up development environment..."
	@echo "Installing Node.js dependencies..."
	npm install
	@echo "Setting up Python environments..."
	cd services/api && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt
	@echo "Starting development services..."
	docker-compose up -d postgres redis minio
	@echo "Setup complete! Run 'make build' to build all components."

# Clean up
clean:
	@echo "Cleaning build artifacts..."
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null || true
	rm -rf node_modules packages/*/node_modules packages/*/dist
	rm -rf services/api/build services/api/dist
	rm -rf apps/ios/build apps/ios/DerivedData
	docker-compose down --volumes --remove-orphans

# Build all components
build: build-packages build-api build-ios

build-packages:
	@echo "Building shared packages..."
	npm run build:packages

build-api:
	@echo "Building API service..."
	cd services/api && python -m pip install -e .

build-ios:
	@echo "Building iOS application..."
	cd apps/ios && xcodebuild -scheme SimulationApp -destination 'platform=iOS Simulator,name=iPhone 15' build

# Testing
test: test-packages test-api test-ios

test-packages:
	@echo "Testing shared packages..."
	npm run test:packages

test-api:
	@echo "Testing API service..."
	cd services/api && python -m pytest tests/ --cov=app --cov-report=term-missing

test-ios:
	@echo "Testing iOS application..."
	cd apps/ios && xcodebuild test -scheme SimulationApp -destination 'platform=iOS Simulator,name=iPhone 15'

# Integration tests
test-integration:
	@echo "Running integration tests..."
	docker-compose up -d postgres redis minio
	cd services/api && python -m pytest tests/integration/ -v
	docker-compose down

# Linting and code quality
lint: lint-python lint-javascript lint-swift

lint-python:
	@echo "Linting Python code..."
	cd services/api && black --check . && isort --check-only . && flake8 . && mypy .

lint-javascript:
	@echo "Linting JavaScript/TypeScript code..."
	npm run lint

lint-swift:
	@echo "Linting Swift code..."
	cd apps/ios && swiftlint

# Fix linting issues
lint-fix:
	@echo "Fixing linting issues..."
	cd services/api && black . && isort .
	npm run lint:fix

# Security scanning
security: security-python security-javascript security-docker

security-python:
	@echo "Running Python security scans..."
	cd services/api && bandit -r app/ && safety check

security-javascript:
	@echo "Running JavaScript security scans..."
	npm audit --audit-level high

security-docker:
	@echo "Scanning Docker images..."
	docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image simulation-api:latest

# Local development deployment
deploy-local:
	@echo "Deploying to local environment..."
	docker-compose up -d
	@echo "Services available at:"
	@echo "  API: http://localhost:8000"
	@echo "  Docs: http://localhost:8000/docs"
	@echo "  PostgreSQL: localhost:5432"
	@echo "  Redis: localhost:6379"
	@echo "  MinIO: http://localhost:9001"
	@echo "  Grafana: http://localhost:3000"
	@echo "  Prometheus: http://localhost:9090"

# Staging deployment
deploy-staging:
	@echo "Deploying to staging environment..."
	kubectl apply -f infrastructure/kubernetes/staging/
	kubectl rollout status deployment/api-deployment -n staging

# Production deployment
deploy-production:
	@echo "Deploying to production environment..."
	kubectl apply -f infrastructure/kubernetes/production/
	kubectl rollout status deployment/api-deployment -n production

# Database operations
db-migrate:
	@echo "Running database migrations..."
	cd services/api && alembic upgrade head

db-rollback:
	@echo "Rolling back database migration..."
	cd services/api && alembic downgrade -1

db-reset:
	@echo "Resetting database..."
	docker-compose down postgres
	docker volume rm simulation-3d-hof_postgres_data
	docker-compose up -d postgres
	sleep 10
	$(MAKE) db-migrate

# Documentation
docs:
	@echo "Generating documentation..."
	@echo "API documentation available at http://localhost:8000/docs when API is running"

# Development helpers
dev-api:
	@echo "Starting API in development mode..."
	cd services/api && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-ios:
	@echo "Opening iOS project..."
	cd apps/ios && open SimulationApp.xcodeproj

# Monitoring
logs:
	@echo "Showing service logs..."
	docker-compose logs -f

logs-api:
	@echo "Showing API logs..."
	docker-compose logs -f api

# Health checks
health:
	@echo "Checking service health..."
	curl -f http://localhost:8000/health || echo "API service not responding"

# Performance testing
perf-test:
	@echo "Running performance tests..."
	cd services/api && locust -f tests/performance/locustfile.py --headless -u 10 -r 2 -t 60s --host http://localhost:8000

# Code coverage
coverage:
	@echo "Generating coverage reports..."
	cd services/api && python -m pytest tests/ --cov=app --cov-report=html --cov-report=term
	npm run coverage --workspaces --if-present

# Git hooks
install-hooks:
	@echo "Installing Git hooks..."
	cp scripts/git-hooks/* .git/hooks/
	chmod +x .git/hooks/*

# Docker operations
docker-build:
	@echo "Building Docker images..."
	docker build -t simulation-api:latest services/api/

docker-push:
	@echo "Pushing Docker images..."
	docker tag simulation-api:latest ghcr.io/alvarobcmed/simulation-3d-hof/api:latest
	docker push ghcr.io/alvarobcmed/simulation-3d-hof/api:latest

# Utilities
check-deps:
	@echo "Checking for dependency updates..."
	cd services/api && pip list --outdated
	npm outdated