"""
Application configuration settings.
"""

from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn, RedisDsn
from typing import List, Optional
import secrets


class Settings(BaseSettings):
    """Application settings."""
    
    # API Settings
    API_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "3D Orofacial Harmonization Simulation API"
    
    # Environment
    ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
    DEBUG: bool = Field(default=False, env="DEBUG")
    
    # Security
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_urlsafe(32), env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 8, env="ACCESS_TOKEN_EXPIRE_MINUTES")  # 8 days
    REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 30, env="REFRESH_TOKEN_EXPIRE_MINUTES")  # 30 days
    
    # CORS
    ALLOWED_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8080"],
        env="ALLOWED_ORIGINS"
    )
    ALLOWED_HOSTS: List[str] = Field(
        default=["localhost", "127.0.0.1"],
        env="ALLOWED_HOSTS"
    )
    
    # Database
    DATABASE_URL: Optional[PostgresDsn] = Field(
        default=None,
        env="DATABASE_URL"
    )
    
    # Redis
    REDIS_URL: Optional[RedisDsn] = Field(
        default=None,
        env="REDIS_URL"
    )
    
    # File Storage (S3-compatible)
    MINIO_ENDPOINT: str = Field(default="localhost:9000", env="MINIO_ENDPOINT")
    MINIO_ACCESS_KEY: str = Field(default="minioadmin", env="MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY: str = Field(default="minioadmin123", env="MINIO_SECRET_KEY")
    MINIO_SECURE: bool = Field(default=False, env="MINIO_SECURE")
    MINIO_BUCKET: str = Field(default="simulation-data", env="MINIO_BUCKET")
    
    # Encryption
    ENCRYPTION_KEY: Optional[str] = Field(default=None, env="ENCRYPTION_KEY")
    
    # Observability
    ENABLE_METRICS: bool = Field(default=True, env="ENABLE_METRICS")
    ENABLE_TRACING: bool = Field(default=True, env="ENABLE_TRACING")
    OTEL_EXPORTER_OTLP_ENDPOINT: Optional[str] = Field(default=None, env="OTEL_EXPORTER_OTLP_ENDPOINT")
    
    # Medical/Compliance Settings
    HIPAA_MODE: bool = Field(default=True, env="HIPAA_MODE")
    AUDIT_LOGGING: bool = Field(default=True, env="AUDIT_LOGGING")
    DATA_RETENTION_DAYS: int = Field(default=2555, env="DATA_RETENTION_DAYS")  # 7 years default
    
    # Performance Settings
    MAX_UPLOAD_SIZE: int = Field(default=100 * 1024 * 1024, env="MAX_UPLOAD_SIZE")  # 100MB
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, env="RATE_LIMIT_PER_MINUTE")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create global settings instance
settings = Settings()