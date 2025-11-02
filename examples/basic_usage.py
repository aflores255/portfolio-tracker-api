#!/usr/bin/env python3
"""
Basic usage example for Portfolio Tracker API.

This script demonstrates basic usage of main functionalities.
"""

import asyncio
from src.portfolio_tracker.utils.helpers import generate_response, generate_error_response


async def main():
    """Main function for the example."""
    print("🚀 Portfolio Tracker API - Basic Usage Example")

    # Generate a standard API response
    response = generate_response(
        data={"message": "Hello from Portfolio Tracker!"},
        message="Success"
    )
    print(f"✅ Response: {response}")

    # Generate an error response
    error_response = generate_error_response(
        code="EXAMPLE_ERROR",
        message="This is an example error",
        field="example_field"
    )
    print(f"❌ Error Response: {error_response}")

    print("\n� For more examples, check the documentation at /docs")


if __name__ == "__main__":
    asyncio.run(main())
