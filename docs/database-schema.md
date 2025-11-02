# Database Schema

## Overview

The Portfolio Tracker API uses PostgreSQL as its primary database with the following entities:

- **Users** - User accounts and authentication
- **Portfolios** - Investment portfolios owned by users
- **Holdings** - Individual asset positions within portfolios
- **Transactions** - Immutable record of all buy/sell operations
- **Market Prices** - Historical price data for assets

---

## Entity Relationship Diagram

```
┌─────────────┐
│    User     │
│─────────────│
│ id (PK)     │
│ email       │◄────────┐
│ password    │         │
│ name        │         │
│ is_active   │         │
└─────────────┘         │
                        │ 1:N
                        │
                ┌───────┴──────────┐
                │    Portfolio     │
                │──────────────────│
                │ id (PK)          │
                │ user_id (FK)     │
                │ name             │
                │ currency         │
                │ risk_profile     │
                │ total_value      │
                └──────┬───────────┘
                       │
            ┌──────────┼──────────┐
            │ 1:N      │ 1:N      │
            │          │          │
    ┌───────▼──────┐   │   ┌──────▼────────┐
    │   Holding    │   │   │  Transaction  │
    │──────────────│   │   │───────────────│
    │ id (PK)      │   │   │ id (PK)       │
    │ portfolio_id │   │   │ portfolio_id  │
    │ symbol       │   │   │ holding_id    │
    │ quantity     │   │   │ type          │
    │ avg_cost     │   │   │ quantity      │
    │ current_price│   │   │ price         │
    └──────┬───────┘   │   │ date          │
           │           │   └───────────────┘
           │ 1:N       │
           └───────────┘

┌─────────────────┐
│  Market Price   │  (Independent table)
│─────────────────│
│ id (PK)         │
│ symbol          │
│ date            │
│ open/high/low   │
│ close           │
│ volume          │
└─────────────────┘
```

---

## Table Definitions

### Users

Stores user account information and authentication data.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Auto-incrementing user ID |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL, INDEX | User email (login) |
| `password_hash` | VARCHAR(255) | NOT NULL | Bcrypt hashed password |
| `name` | VARCHAR(255) | NOT NULL | User full name |
| `avatar_url` | VARCHAR(500) | NULL | Profile picture URL |
| `is_active` | BOOLEAN | NOT NULL, DEFAULT true | Account active status |
| `is_verified` | BOOLEAN | NOT NULL, DEFAULT false | Email verified |
| `is_superuser` | BOOLEAN | NOT NULL, DEFAULT false | Admin privileges |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes:**
- `ix_users_email` on `email`

**Relationships:**
- One-to-many with `portfolios`

---

### Portfolios

Investment portfolios owned by users.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Auto-incrementing portfolio ID |
| `user_id` | INTEGER | FOREIGN KEY, NOT NULL, INDEX | Owner user ID |
| `name` | VARCHAR(255) | NOT NULL | Portfolio name |
| `description` | TEXT | NULL | Portfolio description |
| `currency` | VARCHAR(3) | NOT NULL, DEFAULT 'USD' | ISO 4217 currency code |
| `risk_profile` | ENUM | NOT NULL | conservative, moderate, aggressive |
| `total_value` | NUMERIC(15,2) | NOT NULL, DEFAULT 0 | Current market value |
| `total_cost` | NUMERIC(15,2) | NOT NULL, DEFAULT 0 | Total invested |
| `total_gain_loss` | NUMERIC(15,2) | NOT NULL, DEFAULT 0 | Unrealized P&L |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes:**
- `ix_portfolios_user_id` on `user_id`

**Foreign Keys:**
- `user_id` → `users.id` (CASCADE on delete)

**Relationships:**
- Many-to-one with `users`
- One-to-many with `holdings`
- One-to-many with `transactions`

---

### Holdings

Individual asset positions within portfolios.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Auto-incrementing holding ID |
| `portfolio_id` | INTEGER | FOREIGN KEY, NOT NULL, INDEX | Parent portfolio ID |
| `symbol` | VARCHAR(20) | NOT NULL, INDEX | Asset ticker symbol |
| `name` | VARCHAR(255) | NULL | Full asset name |
| `asset_type` | VARCHAR(50) | NOT NULL, DEFAULT 'stock' | Asset type |
| `quantity` | NUMERIC(20,8) | NOT NULL, DEFAULT 0 | Number of shares/units |
| `average_cost` | NUMERIC(15,2) | NOT NULL, DEFAULT 0 | Avg purchase price |
| `current_price` | NUMERIC(15,2) | NULL | Latest market price |
| `market_value` | NUMERIC(15,2) | NULL | quantity * current_price |
| `total_cost` | NUMERIC(15,2) | NOT NULL, DEFAULT 0 | Total invested |
| `unrealized_gain_loss` | NUMERIC(15,2) | NULL | Current gain/loss |
| `unrealized_gain_loss_percent` | NUMERIC(5,2) | NULL | Gain/loss percentage |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes:**
- `ix_holdings_portfolio_id` on `portfolio_id`
- `ix_holdings_symbol` on `symbol`

**Foreign Keys:**
- `portfolio_id` → `portfolios.id` (CASCADE on delete)

**Relationships:**
- Many-to-one with `portfolios`
- One-to-many with `transactions`

---

### Transactions

Immutable record of all portfolio transactions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Auto-incrementing transaction ID |
| `portfolio_id` | INTEGER | FOREIGN KEY, NOT NULL, INDEX | Parent portfolio ID |
| `holding_id` | INTEGER | FOREIGN KEY, NOT NULL, INDEX | Related holding ID |
| `transaction_type` | ENUM | NOT NULL, INDEX | buy, sell, dividend, split, transfer_in, transfer_out |
| `transaction_date` | DATE | NOT NULL, INDEX | Transaction date |
| `symbol` | VARCHAR(20) | NOT NULL, INDEX | Asset ticker |
| `quantity` | NUMERIC(20,8) | NOT NULL | Number of shares/units |
| `price` | NUMERIC(15,2) | NOT NULL | Price per unit |
| `commission` | NUMERIC(10,2) | NOT NULL, DEFAULT 0 | Broker commission |
| `fees` | NUMERIC(10,2) | NOT NULL, DEFAULT 0 | Other fees |
| `total_amount` | NUMERIC(15,2) | NOT NULL | Total transaction value |
| `notes` | TEXT | NULL | Additional notes |
| `currency` | VARCHAR(3) | NOT NULL, DEFAULT 'USD' | Currency code |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes:**
- `ix_transactions_portfolio_id` on `portfolio_id`
- `ix_transactions_holding_id` on `holding_id`
- `ix_transactions_transaction_type` on `transaction_type`
- `ix_transactions_transaction_date` on `transaction_date`
- `ix_transactions_symbol` on `symbol`

**Foreign Keys:**
- `portfolio_id` → `portfolios.id` (CASCADE on delete)
- `holding_id` → `holdings.id` (CASCADE on delete)

**Relationships:**
- Many-to-one with `portfolios`
- Many-to-one with `holdings`

**Important:** Transactions are **immutable**. No updates allowed, only inserts.

---

### Market Prices

Historical market price data for assets (updated by Airflow).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Auto-incrementing price ID |
| `symbol` | VARCHAR(20) | NOT NULL, INDEX | Asset ticker symbol |
| `date` | DATE | NOT NULL, INDEX | Price date |
| `open` | NUMERIC(15,2) | NULL | Opening price |
| `high` | NUMERIC(15,2) | NULL | Highest price |
| `low` | NUMERIC(15,2) | NULL | Lowest price |
| `close` | NUMERIC(15,2) | NOT NULL | Closing price |
| `volume` | NUMERIC(20,0) | NULL | Trading volume |
| `adjusted_close` | NUMERIC(15,2) | NULL | Adjusted close price |
| `source` | VARCHAR(50) | NOT NULL, DEFAULT 'yahoo' | Data source |
| `created_at` | TIMESTAMP | NOT NULL | Record creation time |
| `updated_at` | TIMESTAMP | NOT NULL | Last update time |

**Indexes:**
- `ix_market_prices_symbol` on `symbol`
- `ix_market_prices_date` on `date`
- `ix_market_prices_symbol_date` UNIQUE on `(symbol, date)`

**Relationships:**
- Independent table (no foreign keys)

---

## Data Types

### Enums

**RiskProfile:**
- `conservative` - Low risk tolerance
- `moderate` - Medium risk tolerance
- `aggressive` - High risk tolerance

**TransactionType:**
- `buy` - Purchase of assets
- `sell` - Sale of assets
- `dividend` - Dividend payment
- `split` - Stock split
- `transfer_in` - Transfer into portfolio
- `transfer_out` - Transfer out of portfolio

---

## Cascading Deletes

- Deleting a **User** → Deletes all their **Portfolios**
- Deleting a **Portfolio** → Deletes all its **Holdings** and **Transactions**
- Deleting a **Holding** → Deletes all its **Transactions**

---

## Migrations

Managed with Alembic. To create a new migration:

```bash
# Generate migration automatically
alembic revision --autogenerate -m "Description of changes"

# Review generated migration in migrations/versions/

# Apply migration
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

---

## Sample Queries

### Get all portfolios for a user with total value

```sql
SELECT 
    p.id,
    p.name,
    p.currency,
    p.total_value,
    COUNT(h.id) as holding_count
FROM portfolios p
LEFT JOIN holdings h ON h.portfolio_id = p.id
WHERE p.user_id = 1
GROUP BY p.id;
```

### Get portfolio performance

```sql
SELECT 
    p.name,
    p.total_value,
    p.total_cost,
    p.total_gain_loss,
    (p.total_gain_loss / NULLIF(p.total_cost, 0) * 100) as roi_percent
FROM portfolios p
WHERE p.user_id = 1;
```

### Get transaction history for a portfolio

```sql
SELECT 
    t.transaction_date,
    t.symbol,
    t.transaction_type,
    t.quantity,
    t.price,
    t.total_amount
FROM transactions t
WHERE t.portfolio_id = 1
ORDER BY t.transaction_date DESC
LIMIT 50;
```

---

## Next Steps

- [ ] Add indexes for performance optimization
- [ ] Implement database views for complex queries
- [ ] Add triggers for automatic calculations
- [ ] Setup backup and restore procedures
- [ ] Implement audit logging
