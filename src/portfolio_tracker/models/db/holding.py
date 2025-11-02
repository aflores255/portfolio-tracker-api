"""
Holding Model

Database model for portfolio holdings (positions).
"""

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from portfolio_tracker.models.db.base import BaseModel


class Holding(BaseModel):
    """
    Holding model for tracking investment positions.
    
    A holding represents a specific asset held in a portfolio.
    
    Relationships:
    - portfolio: Many-to-one with Portfolio
    - transactions: One-to-many with Transaction
    """

    __tablename__ = "holdings"

    # Relationships
    portfolio_id = Column(
        Integer,
        ForeignKey("portfolios.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Asset Information
    symbol = Column(String(20), nullable=False, index=True)  # Ticker symbol
    name = Column(String(255), nullable=True)  # Full asset name
    asset_type = Column(
        String(50), default="stock", nullable=False
    )  # stock, crypto, etf, bond, etc.

    # Position Details
    quantity = Column(Numeric(precision=20, scale=8), default=0, nullable=False)
    average_cost = Column(
        Numeric(precision=15, scale=2), default=0, nullable=False
    )  # Average purchase price
    
    # Current Market Data (updated by workers)
    current_price = Column(Numeric(precision=15, scale=2), nullable=True)
    market_value = Column(Numeric(precision=15, scale=2), nullable=True)
    
    # Performance Metrics
    total_cost = Column(Numeric(precision=15, scale=2), default=0, nullable=False)
    unrealized_gain_loss = Column(Numeric(precision=15, scale=2), default=0, nullable=True)
    unrealized_gain_loss_percent = Column(Numeric(precision=5, scale=2), default=0, nullable=True)

    # Relationships
    portfolio = relationship("Portfolio", back_populates="holdings")
    transactions = relationship(
        "Transaction",
        back_populates="holding",
        cascade="all, delete-orphan",
        lazy="select",
    )

    def __repr__(self) -> str:
        """String representation."""
        return f"<Holding(id={self.id}, symbol='{self.symbol}', quantity={self.quantity})>"
