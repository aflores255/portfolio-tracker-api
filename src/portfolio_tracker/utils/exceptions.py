"""
Custom Exceptions

Centralized exception definitions for the application.
All custom exceptions inherit from base exceptions and include
proper HTTP status codes for API responses.
"""

from typing import Any, Dict, Optional


class PortfolioTrackerException(Exception):
    """Base exception for Portfolio Tracker API."""

    def __init__(
        self,
        message: str,
        code: str = "INTERNAL_ERROR",
        status_code: int = 500,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize exception.
        
        Args:
            message: Human-readable error message
            code: Machine-readable error code
            status_code: HTTP status code
            details: Additional error details
        """
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)


# ============================================================================
# Authentication & Authorization Exceptions
# ============================================================================


class AuthenticationException(PortfolioTrackerException):
    """Base exception for authentication errors."""

    def __init__(
        self,
        message: str = "Authentication failed",
        code: str = "AUTH_FAILED",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, code, 401, details)


class InvalidCredentialsException(AuthenticationException):
    """Raised when credentials are invalid."""

    def __init__(
        self,
        message: str = "Invalid email or password",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, "INVALID_CREDENTIALS", details)


class TokenExpiredException(AuthenticationException):
    """Raised when JWT token has expired."""

    def __init__(
        self,
        message: str = "Token has expired",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, "TOKEN_EXPIRED", details)


class InvalidTokenException(AuthenticationException):
    """Raised when JWT token is invalid."""

    def __init__(
        self,
        message: str = "Invalid token",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, "INVALID_TOKEN", details)


class UnauthorizedException(PortfolioTrackerException):
    """Raised when user lacks required permissions."""

    def __init__(
        self,
        message: str = "Insufficient permissions",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, "UNAUTHORIZED", 403, details)


# ============================================================================
# Resource Not Found Exceptions
# ============================================================================


class NotFoundException(PortfolioTrackerException):
    """Base exception for resource not found errors."""

    def __init__(
        self,
        message: str = "Resource not found",
        code: str = "NOT_FOUND",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, code, 404, details)


class UserNotFoundException(NotFoundException):
    """Raised when user is not found."""

    def __init__(
        self, user_id: Any, details: Optional[Dict[str, Any]] = None
    ) -> None:
        message = f"User with ID {user_id} not found"
        super().__init__(message, "USER_NOT_FOUND", details)


class PortfolioNotFoundException(NotFoundException):
    """Raised when portfolio is not found."""

    def __init__(
        self, portfolio_id: Any, details: Optional[Dict[str, Any]] = None
    ) -> None:
        message = f"Portfolio with ID {portfolio_id} not found"
        super().__init__(message, "PORTFOLIO_NOT_FOUND", details)


class HoldingNotFoundException(NotFoundException):
    """Raised when holding is not found."""

    def __init__(
        self, holding_id: Any, details: Optional[Dict[str, Any]] = None
    ) -> None:
        message = f"Holding with ID {holding_id} not found"
        super().__init__(message, "HOLDING_NOT_FOUND", details)


class TransactionNotFoundException(NotFoundException):
    """Raised when transaction is not found."""

    def __init__(
        self, transaction_id: Any, details: Optional[Dict[str, Any]] = None
    ) -> None:
        message = f"Transaction with ID {transaction_id} not found"
        super().__init__(message, "TRANSACTION_NOT_FOUND", details)


# ============================================================================
# Validation Exceptions
# ============================================================================


class ValidationException(PortfolioTrackerException):
    """Raised when input validation fails."""

    def __init__(
        self,
        message: str = "Validation error",
        field: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        if field and details is None:
            details = {"field": field}
        super().__init__(message, "VALIDATION_ERROR", 422, details)


class DuplicateResourceException(PortfolioTrackerException):
    """Raised when attempting to create duplicate resource."""

    def __init__(
        self,
        message: str = "Resource already exists",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, "DUPLICATE_RESOURCE", 409, details)


# ============================================================================
# Business Logic Exceptions
# ============================================================================


class BusinessLogicException(PortfolioTrackerException):
    """Base exception for business logic errors."""

    def __init__(
        self,
        message: str,
        code: str = "BUSINESS_LOGIC_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, code, 400, details)


class InsufficientFundsException(BusinessLogicException):
    """Raised when user has insufficient funds."""

    def __init__(
        self,
        required: float,
        available: float,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        message = (
            f"Insufficient funds: required {required}, available {available}"
        )
        super().__init__(message, "INSUFFICIENT_FUNDS", details)


class InvalidTransactionException(BusinessLogicException):
    """Raised when transaction is invalid."""

    def __init__(
        self, message: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        super().__init__(message, "INVALID_TRANSACTION", details)


# ============================================================================
# External Service Exceptions
# ============================================================================


class ExternalServiceException(PortfolioTrackerException):
    """Base exception for external service errors."""

    def __init__(
        self,
        message: str = "External service error",
        code: str = "EXTERNAL_SERVICE_ERROR",
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, code, 503, details)


class MarketDataUnavailableException(ExternalServiceException):
    """Raised when market data is unavailable."""

    def __init__(
        self, symbol: str, details: Optional[Dict[str, Any]] = None
    ) -> None:
        message = f"Market data unavailable for symbol: {symbol}"
        super().__init__(message, "MARKET_DATA_UNAVAILABLE", details)
