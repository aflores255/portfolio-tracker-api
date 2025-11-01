"""
Helper Utilities

Reusable helper functions for common operations.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Optional
from uuid import UUID


def generate_response(
    data: Any = None,
    message: Optional[str] = None,
    meta: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Generate standardized API response.
    
    Args:
        data: Response data
        message: Optional message
        meta: Optional metadata
        
    Returns:
        Dict: Standardized response format
    """
    response: Dict[str, Any] = {
        "data": data,
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "version": "v1",
            **(meta or {}),
        },
    }

    if message:
        response["message"] = message

    return response


def generate_error_response(
    code: str,
    message: str,
    field: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Generate standardized error response.
    
    Args:
        code: Error code
        message: Error message
        field: Optional field that caused error
        details: Additional error details
        
    Returns:
        Dict: Standardized error response format
    """
    error: Dict[str, Any] = {
        "code": code,
        "message": message,
    }

    if field:
        error["field"] = field

    if details:
        error["details"] = details

    return {
        "data": None,
        "errors": [error],
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "version": "v1",
        },
    }


def to_dict(obj: Any, exclude: Optional[list[str]] = None) -> Dict[str, Any]:
    """
    Convert SQLAlchemy model to dictionary.
    
    Args:
        obj: SQLAlchemy model instance
        exclude: List of fields to exclude
        
    Returns:
        Dict: Model as dictionary
    """
    if exclude is None:
        exclude = []

    result = {}
    for column in obj.__table__.columns:
        if column.name not in exclude:
            value = getattr(obj, column.name)
            # Convert UUID to string
            if isinstance(value, UUID):
                value = str(value)
            # Convert datetime to ISO format
            elif isinstance(value, datetime):
                value = value.isoformat()
            result[column.name] = value

    return result


def paginate_query(
    page: int = 1,
    page_size: int = 10,
    max_page_size: int = 100,
) -> tuple[int, int]:
    """
    Calculate pagination offset and limit.
    
    Args:
        page: Page number (1-indexed)
        page_size: Items per page
        max_page_size: Maximum allowed page size
        
    Returns:
        Tuple[int, int]: (offset, limit)
    """
    # Validate and constrain page size
    page_size = min(max(1, page_size), max_page_size)

    # Validate page number
    page = max(1, page)

    # Calculate offset
    offset = (page - 1) * page_size

    return offset, page_size


def generate_pagination_meta(
    page: int,
    page_size: int,
    total_items: int,
) -> Dict[str, Any]:
    """
    Generate pagination metadata.
    
    Args:
        page: Current page number
        page_size: Items per page
        total_items: Total number of items
        
    Returns:
        Dict: Pagination metadata
    """
    total_pages = (total_items + page_size - 1) // page_size

    return {
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_previous": page > 1,
    }
