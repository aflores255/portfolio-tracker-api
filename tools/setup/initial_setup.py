"""
Initial project setup script.
"""

import sys
from pathlib import Path


def main() -> int:
    """
    Execute initial setup.

    Returns:
        Exit code (0 = success)
    """
    print("🚀 Initial project setup")

    # Create necessary directories
    directories = ["logs", "cache", "data"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Directory created: {directory}")

    print("✨ Initial setup completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
