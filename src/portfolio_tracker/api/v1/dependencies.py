"""
FastAPI Dependencies

Reusable dependencies for dependency injection.
"""

from typing import AsyncGenerator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from portfolio_tracker.config.database import get_db
from portfolio_tracker.config.settings import get_settings

settings = get_settings()

# Security scheme for JWT tokens
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> dict:
    """
    Get current authenticated user from JWT token.

    Args:
        credentials: HTTP Bearer credentials (JWT token)
        db: Database session

    Returns:
        dict: Current user data

    Raises:
        HTTPException: If token is invalid or user not found

    TODO: Implement actual JWT validation and user lookup
    """
    # Placeholder - will be implemented with authentication system
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Authentication not yet implemented",
    )


async def get_optional_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(
        HTTPBearer(auto_error=False)
    ),
    db: AsyncSession = Depends(get_db),
) -> Optional[dict]:
    """
    Get current user if authenticated, None otherwise.

    Args:
        credentials: Optional HTTP Bearer credentials
        db: Database session

    Returns:
        Optional[dict]: Current user data or None
    """
    if credentials is None:
        return None

    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None


def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    """
    Require current user to be an admin.

    Args:
        current_user: Current authenticated user

    Returns:
        dict: Current user data

    Raises:
        HTTPException: If user is not an admin

    TODO: Implement actual role checking
    """
    # Placeholder - will be implemented with user roles
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
    return current_user


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Alias for get_db for cleaner dependency injection.

    Yields:
        AsyncSession: Database session
    """
    async for session in get_db():
        yield session
