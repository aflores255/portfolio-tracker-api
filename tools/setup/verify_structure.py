"""
Script to verify project structure.
"""

import sys
from pathlib import Path


def verify_structure() -> bool:
    """
    Verify that the project structure is correct.

    Returns:
        True if structure is correct, False otherwise
    """
    required_dirs = [
        "src",
        "tests",
        "docs"
    ]

    required_files = [
        "pyproject.toml",
        "README.md",
        ".gitignore"
    ]

    errors = []

    # Verify directories
    for directory in required_dirs:
        if not Path(directory).exists():
            errors.append(f"❌ Missing directory: {directory}")
        else:
            print(f"✅ Directory found: {directory}")

    # Verify files
    for file in required_files:
        if not Path(file).exists():
            errors.append(f"❌ Missing file: {file}")
        else:
            print(f"✅ File found: {file}")

    if errors:
        print("\n⚠️  Errors found:")
        for error in errors:
            print(f"  {error}")
        return False

    print("\n✨ Project structure verified successfully")
    return True


def main() -> int:
    """
    Main function for verification script.

    Returns:
        Exit code (0 = success, 1 = error)
    """
    if verify_structure():
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
