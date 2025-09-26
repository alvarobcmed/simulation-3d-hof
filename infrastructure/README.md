# Infrastructure

This directory contains Infrastructure as Code (IaC) and deployment configurations for the 3D Orofacial Harmonization Simulation application.

## Infrastructure Overview

### Kubernetes Deployment (`kubernetes/`)
Production-ready Kubernetes manifests:
- Application deployments
- Service configurations
- Ingress controllers
- ConfigMaps and Secrets management

### Terraform Configuration (`terraform/`)
Cloud infrastructure provisioning:
- Cloud resources (AWS/Azure/GCP)
- Networking and security groups
- Database and storage setup
- Monitoring and logging infrastructure

### Helm Charts (`helm/`)
Kubernetes package management:
- Application charts
- Dependency management
- Environment-specific values
- Release management

### Monitoring (`monitoring/`)
Observability stack configuration:
- Prometheus setup
- Grafana dashboards
- Alert rules
- Log aggregation (ELK stack)

## Deployment Environments

### Development
- Single-node Kubernetes cluster (minikube/kind)
- Local PostgreSQL and Redis
- Development SSL certificates
- Debug logging enabled

### Staging
- Multi-node Kubernetes cluster
- Cloud-managed databases
- Staging SSL certificates
- Production-like configuration

### Production
- High-availability Kubernetes cluster
- Multi-region deployment
- Production SSL certificates
- Optimized for performance and security

## Infrastructure Components

### Container Registry
- Private Docker registry
- Vulnerability scanning
- Image signing and verification
- Automated cleanup policies

### Databases
- PostgreSQL primary/replica setup
- Automated backups and point-in-time recovery
- Connection pooling
- Performance monitoring

### Message Queues
- Redis for caching and pub/sub
- Message durability and persistence
- Cluster setup for high availability
- Monitoring and alerting

### Object Storage
- S3-compatible storage (MinIO/AWS S3)
- Versioning and lifecycle policies
- Encryption at rest
- Cross-region replication

### Load Balancing
- Application Load Balancer (ALB)
- SSL termination
- Health checks
- Auto-scaling integration

### Monitoring Stack
- **Metrics**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger/Zipkin
- **Alerting**: AlertManager + PagerDuty

## Security Configuration

### Network Security
- VPC with private subnets
- Security groups with least privilege
- WAF (Web Application Firewall)
- DDoS protection

### Identity and Access Management
- RBAC for Kubernetes
- Service accounts with minimal permissions
- Secrets management (Vault/AWS Secrets Manager)
- Certificate management (cert-manager)

### Compliance
- HIPAA-compliant infrastructure
- LGPD compliance configurations
- Audit logging and retention
- Encryption in transit and at rest

## Development Workflow

### Local Development
```bash
# Start local infrastructure
docker-compose up -d

# Deploy to local Kubernetes
make deploy-local

# Port forward for debugging
kubectl port-forward svc/api-service 8000:8000
```

### Staging Deployment
```bash
# Deploy to staging
make deploy-staging

# Run smoke tests
make test-staging

# Promote to production
make promote-production
```

### Production Deployment
```bash
# Deploy with blue-green strategy
make deploy-production-blue-green

# Canary deployment
make deploy-production-canary

# Rollback if needed
make rollback-production
```

## Scaling Configuration

### Horizontal Pod Autoscaler (HPA)
- CPU and memory-based scaling
- Custom metrics scaling
- Predictive scaling policies
- Scale-down stabilization

### Vertical Pod Autoscaler (VPA)
- Resource request optimization
- Memory and CPU recommendations
- Automatic resource adjustment
- Policy-based constraints

### Cluster Autoscaler
- Node pool auto-scaling
- Cost optimization
- Multi-zone distribution
- Spot instance integration

## Disaster Recovery

### Backup Strategy
- Automated database backups
- Cross-region backup replication
- Point-in-time recovery capability
- Backup verification and testing

### Recovery Procedures
- RTO (Recovery Time Objective): 4 hours
- RPO (Recovery Point Objective): 1 hour
- Automated failover procedures
- Regular disaster recovery testing

## Cost Optimization

### Resource Optimization
- Right-sizing recommendations
- Unused resource cleanup
- Reserved instance planning
- Spot instance utilization

### Monitoring and Alerting
- Cost monitoring dashboards
- Budget alerts and limits
- Resource utilization tracking
- Optimization recommendations

## Compliance and Auditing

### HIPAA Compliance
- Encrypted storage and transmission
- Access logging and monitoring
- Audit trail maintenance
- Risk assessment documentation

### LGPD Compliance
- Data location restrictions
- Data subject rights automation
- Consent management
- Data retention policies

## Troubleshooting

### Common Issues
- Pod startup failures
- Database connection issues
- Storage provisioning problems
- Network connectivity issues

### Debugging Tools
- kubectl for cluster inspection
- Logs aggregation and search
- Distributed tracing
- Performance profiling

### Support Procedures
- Escalation matrix
- On-call procedures
- Incident response playbooks
- Post-mortem analysis

## Documentation

### Runbooks
- Deployment procedures
- Troubleshooting guides
- Emergency response procedures
- Maintenance tasks

### Architecture Diagrams
- Infrastructure overview
- Network topology
- Data flow diagrams
- Security architecture

For detailed setup instructions, see the README files in each subdirectory.