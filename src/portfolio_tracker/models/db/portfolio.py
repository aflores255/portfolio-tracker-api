"""
Portfolio Model

Database model for investment portfolios.
"""

from sqlalchemy import Column, Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship
import enum

from portfolio_tracker.models.db.base import BaseModel


class RiskProfile(str, enum.Enum):
    """Risk profile categories."""

    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"


class Portfolio(BaseModel):
    """
    Portfolio model for managing investment portfolios.
    
    Relationships:
    - user: Many-to-one with User
    - holdings: One-to-many with Holding
    - transactions: One-to-many with Transaction
    """

    __tablename__ = "portfolios"

    # Relationships
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )

    # Basic Information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    currency = Column(String(3), default="USD", nullable=False)  # ISO 4217

    # Configuration
    risk_profile = Column(
        Enum(RiskProfile), default=RiskProfile.MODERATE, nullable=False
    )
    
    # Cached Values (updated by analytics)
    total_value = Column(Numeric(precision=15, scale=2), default=0, nullable=False)
    total_cost = Column(Numeric(precision=15, scale=2), default=0, nullable=False)
    total_gain_loss = Column(Numeric(precision=15, scale=2), default=0, nullable=False)

    # Relationships
    user = relationship("User", back_populates="portfolios")
    holdings = relationship(
        "Holding",
        back_populates="portfolio",
        cascade="all, delete-orphan",
        lazy="select",
    )
    transactions = relationship(
        "Transaction",
        back_populates="portfolio",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def __repr__(self) -> str:
        """String representation."""
        return f"<Portfolio(id={self.id}, name='{self.name}', user_id={self.user_id})>"
