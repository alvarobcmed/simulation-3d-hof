"""
Logging configuration for the application.
"""

import logging
import logging.config
import sys
from typing import Dict, Any
import structlog
from app.core.config import settings


def setup_logging() -> None:
    """Set up application logging configuration."""
    
    # Configure structlog for structured logging
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer() if settings.ENVIRONMENT == "production" 
            else structlog.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Determine log level
    log_level = "INFO"
    if settings.DEBUG:
        log_level = "DEBUG"
    elif settings.ENVIRONMENT == "production":
        log_level = "WARNING"
    
    # Logging configuration
    config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
            },
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "json" if settings.ENVIRONMENT == "production" else "detailed",
                "stream": sys.stdout,
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "app": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["console"],
                "level": "INFO" if settings.DEBUG else "WARNING",
                "propagate": False,
            },
            "fastapi": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
            "sqlalchemy.engine": {
                "handlers": ["console"],
                "level": "INFO" if settings.DEBUG else "WARNING",
                "propagate": False,
            },
        },
    }
    
    # Apply logging configuration
    logging.config.dictConfig(config)
    
    # Set up audit logging if enabled
    if settings.AUDIT_LOGGING:
        _setup_audit_logging()


def _setup_audit_logging() -> None:
    """Set up audit logging for compliance."""
    audit_logger = logging.getLogger("audit")
    
    # Create audit handler (could be file, syslog, or external service)
    audit_handler = logging.StreamHandler(sys.stdout)
    audit_handler.setLevel(logging.INFO)
    
    # Audit formatter with structured format
    audit_formatter = logging.Formatter(
        '{"timestamp": "%(asctime)s", "audit": true, "level": "%(levelname)s", '
        '"message": "%(message)s", "module": "%(module)s"}'
    )
    audit_handler.setFormatter(audit_formatter)
    
    audit_logger.addHandler(audit_handler)
    audit_logger.setLevel(logging.INFO)
    audit_logger.propagate = False


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Get a configured logger instance."""
    return structlog.get_logger(name)