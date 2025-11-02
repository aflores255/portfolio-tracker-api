"""
FastAPI Application Entry Point

This module initializes the FastAPI application with all necessary
configurations, middleware, and routers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from portfolio_tracker.config.settings import get_settings

# Initialize settings
settings = get_settings()

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version="0.1.0",
    docs_url=f"{settings.API_V1_PREFIX}/docs",
    redoc_url=f"{settings.API_V1_PREFIX}/redoc",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)


@app.get("/")
async def root() -> JSONResponse:
    """Root endpoint - Health check."""
    return JSONResponse(
        content={
            "message": "Portfolio Tracker API",
            "version": "0.1.0",
            "status": "operational",
            "docs": f"{settings.API_V1_PREFIX}/docs",
        }
    )


@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse(
        content={
            "status": "healthy",
            "environment": settings.APP_ENV,
        }
    )


# TODO: Add routers when created
# from portfolio_tracker.api.v1.routers import users, portfolios, holdings, transactions, analytics
# app.include_router(users.router, prefix=f"{settings.API_V1_PREFIX}/users", tags=["users"])
# app.include_router(portfolios.router, prefix=f"{settings.API_V1_PREFIX}/portfolios", tags=["portfolios"])
