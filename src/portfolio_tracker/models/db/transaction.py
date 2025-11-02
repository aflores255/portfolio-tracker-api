"""
Transaction Model

Database model for investment transactions.
Transactions are immutable records of buy/sell operations.
"""

from datetime import date as date_type
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship
import enum

from portfolio_tracker.models.db.base import BaseModel


class TransactionType(str, enum.Enum):
    """Transaction type categories."""

    BUY = "buy"
    SELL = "sell"
    DIVIDEND = "dividend"
    SPLIT = "split"
    TRANSFER_IN = "transfer_in"
    TRANSFER_OUT = "transfer_out"


class Transaction(BaseModel):
    """
    Transaction model for recording all portfolio transactions.
    
    Transactions are immutable once created (no updates, only inserts).
    This ensures data integrity and audit trail.
    
    Relationships:
    - portfolio: Many-to-one with Portfolio
    - holding: Many-to-one with Holding
    """

    __tablename__ = "transactions"

    # Relationships
    portfolio_id = Column(
        Integer,
        ForeignKey("portfolios.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    holding_id = Column(
        Integer,
        ForeignKey("holdings.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Transaction Details
    transaction_type = Column(Enum(TransactionType), nullable=False, index=True)
    transaction_date = Column(Date, default=date_type.today, nullable=False, index=True)

    # Asset Information
    symbol = Column(String(20), nullable=False, index=True)
    quantity = Column(Numeric(precision=20, scale=8), nullable=False)
    price = Column(Numeric(precision=15, scale=2), nullable=False)
    
    # Costs
    commission = Column(Numeric(precision=10, scale=2), default=0, nullable=False)
    fees = Column(Numeric(precision=10, scale=2), default=0, nullable=False)
    
    # Calculated Fields
    total_amount = Column(
        Numeric(precision=15, scale=2), nullable=False
    )  # quantity * price + commission + fees

    # Additional Information
    notes = Column(Text, nullable=True)
    currency = Column(String(3), default="USD", nullable=False)

    # Relationships
    portfolio = relationship("Portfolio", back_populates="transactions")
    holding = relationship("Holding", back_populates="transactions")

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"<Transaction(id={self.id}, type='{self.transaction_type}', "
            f"symbol='{self.symbol}', quantity={self.quantity})>"
        )
