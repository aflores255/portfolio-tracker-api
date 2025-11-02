"""
Logging Configuration

Centralized logging setup for the application.
"""

import logging
import sys
from typing import Any, Dict

from portfolio_tracker.config.settings import get_settings

settings = get_settings()


def setup_logging() -> None:
    """
    Configure application logging.

    Sets up formatters, handlers, and log levels based on environment.
    """
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # Set specific log levels for third-party libraries
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.INFO if settings.DATABASE_ECHO else logging.WARNING
    )


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.

    Args:
        name: Logger name (usually __name__)

    Returns:
        logging.Logger: Configured logger instance
    """
    return logging.getLogger(name)


class LogContext:
    """
    Context manager for adding context to log messages.

    Example:
        with LogContext(user_id=123, request_id="abc"):
            logger.info("Processing request")
            # Log will include user_id and request_id
    """

    def __init__(self, **context: Any) -> None:
        """Initialize log context."""
        self.context = context
        self.old_factory = logging.getLogRecordFactory()

    def __enter__(self) -> "LogContext":
        """Enter context manager."""

        def record_factory(*args: Any, **kwargs: Any) -> logging.LogRecord:
            record = self.old_factory(*args, **kwargs)
            for key, value in self.context.items():
                setattr(record, key, value)
            return record

        logging.setLogRecordFactory(record_factory)
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit context manager."""
        logging.setLogRecordFactory(self.old_factory)
