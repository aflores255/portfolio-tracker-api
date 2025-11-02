"""
Market Price Model

Database model for historical market prices.
Updated daily by Airflow workers.
"""

from datetime import date as date_type
from sqlalchemy import Column, Date, Index, Numeric, String

from portfolio_tracker.models.db.base import BaseModel


class MarketPrice(BaseModel):
    """
    MarketPrice model for storing historical price data.
    
    This table is populated by Airflow workers that fetch data from
    external APIs (Yahoo Finance, Alpha Vantage, etc.).
    """

    __tablename__ = "market_prices"

    # Asset Information
    symbol = Column(String(20), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)

    # OHLCV Data
    open = Column(Numeric(precision=15, scale=2), nullable=True)
    high = Column(Numeric(precision=15, scale=2), nullable=True)
    low = Column(Numeric(precision=15, scale=2), nullable=True)
    close = Column(Numeric(precision=15, scale=2), nullable=False)
    volume = Column(Numeric(precision=20, scale=0), nullable=True)

    # Additional Metrics
    adjusted_close = Column(Numeric(precision=15, scale=2), nullable=True)
    
    # Metadata
    source = Column(String(50), default="yahoo", nullable=False)  # Data source

    # Composite unique constraint: one price per symbol per date
    __table_args__ = (
        Index("ix_market_prices_symbol_date", "symbol", "date", unique=True),
    )

    def __repr__(self) -> str:
        """String representation."""
        return f"<MarketPrice(symbol='{self.symbol}', date={self.date}, close={self.close})>"
