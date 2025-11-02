"""
User Model

Database model for user accounts.
"""

from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from portfolio_tracker.models.db.base import BaseModel


class User(BaseModel):
    """
    User model for authentication and profile management.
    
    Relationships:
    - portfolios: One-to-many with Portfolio
    """

    __tablename__ = "users"

    # Authentication
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)

    # Profile
    name = Column(String(255), nullable=False)
    avatar_url = Column(String(500), nullable=True)

    # Status
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)

    # Relationships
    portfolios = relationship(
        "Portfolio",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def __repr__(self) -> str:
        """String representation."""
        return f"<User(id={self.id}, email='{self.email}')>"
