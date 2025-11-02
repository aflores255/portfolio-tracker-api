-- Portfolio Tracker API - Database Initialization Script
-- This script runs automatically when the PostgreSQL container starts for the first time

-- Ensure the database exists (already created by POSTGRES_DB env var)
-- This is just for documentation and future extensions

-- Create extensions if needed in the future
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
-- CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Log initialization
DO $$
BEGIN
    RAISE NOTICE 'Portfolio Tracker database initialized successfully!';
END $$;
