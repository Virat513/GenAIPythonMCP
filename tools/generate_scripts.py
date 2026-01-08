from typing import Dict, List
from pathlib import Path
import os

from mcp.server.fastmcp import FastMCP


# -------------------------------------------------
# MCP SERVER SETUP
# -------------------------------------------------

mcp = FastMCP("playwright-python-test-generator")


# -------------------------------------------------
# PROJECT STRUCTURE
# -------------------------------------------------

PROJECT_ROOT = Path.cwd()

SRC_DIR = PROJECT_ROOT / "src"
PAGES_DIR = SRC_DIR / "pages"
TESTS_DIR = SRC_DIR / "tests"
UTILS_DIR = SRC_DIR / "utils"
CONSTANTS_DIR = SRC_DIR / "constants"

# Ensure required directories exist
for directory in [PAGES_DIR, TESTS_DIR, UTILS_DIR, CONSTANTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------
# INTERNAL HELPERS (REUSE & SAFETY)
# -------------------------------------------------

def scan_existing_code() -> Dict[str, List[Path]]:
    """
    Scan existing src/ directories to detect reusable files.
    """
    index = {
        "pages": [],
        "tests": [],
        "utils": [],
        "constants": []
    }

    for root, _, files in os.walk(SRC_DIR):
        for file in files:
            if not file.endswith(".py"):
                continue

            path = Path(root) / file

            if PAGES_DIR in path.parents:
                index["pages"].append(path)
            elif TESTS_DIR in path.parents:
                index["tests"].append(path)
            elif UTILS_DIR in path.parents:
                index["utils"].append(path)
            elif CONSTANTS_DIR in path.parents:
                index["constants"].append(path)

    return index


def is_inside_src(path: Path) -> bool:
    """
    Ensure writes are restricted to src/ only.
    """
    return path.resolve().as_posix().startswith(
        SRC_DIR.resolve().as_posix()
    )


# -------------------------------------------------
# MCP TOOL: FILE GENERATION
# -------------------------------------------------

@mcp.tool()
def generator_write_file(
    relative_path: str,
    content: str
) -> Dict[str, str]:
    """
    Write a generated Python file to disk with strict
    duplication-prevention and reuse enforcement.

    Args:
        relative_path: File path relative to project root
                       (e.g. src/tests/test_login_valid.py)
        content: Complete Python source code

    Returns:
        Status message with generated file path
    """

    # ----------------------------
    # Basic validation
    # ----------------------------

    if not relative_path or not relative_path.strip():
        raise ValueError("relative_path must not be empty")

    if not content or not content.strip():
        raise ValueError("content must not be empty")

    file_path = PROJECT_ROOT / relative_path

    # ----------------------------
    # Safety: restrict writes
    # ----------------------------

    if not is_inside_src(file_path):
        raise ValueError(
            "Generator can write files ONLY inside src/ directory"
        )

    # ----------------------------
    # Scan existing codebase
    # ----------------------------

    existing_code = scan_existing_code()

    # ----------------------------
    # Hard duplication prevention
    # ----------------------------

    if file_path.exists():
        raise ValueError(
            f"File already exists: {relative_path}. "
            "Generator MUST reuse or extend existing code."
        )

    # Prevent duplicate Page Objects
    if PAGES_DIR in file_path.parents:
        for page in existing_code["pages"]:
            if page.name == file_path.name:
                raise ValueError(
                    f"Page Object already exists: {page.name}. "
                    "Reuse or extend the existing Page Object."
                )

    # Prevent duplicate Utils
    if UTILS_DIR in file_path.parents:
        for util in existing_code["utils"]:
            if util.name == file_path.name:
                raise ValueError(
                    f"Utility file already exists: {util.name}. "
                    "Reuse existing utilities instead of duplicating."
                )

    # Prevent duplicate Constants
    if CONSTANTS_DIR in file_path.parents:
        for const in existing_code["constants"]:
            if const.name == file_path.name:
                raise ValueError(
                    f"Constants file already exists: {const.name}. "
                    "Reuse existing constants."
                )

    # ----------------------------
    # Write file
    # ----------------------------

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")

    return {
        "status": "success",
        "message": "File generated successfully",
        "file": str(file_path.resolve())
    }


# -------------------------------------------------
# SERVER ENTRYPOINT
# -------------------------------------------------

if __name__ == "__main__":
    mcp.run()
else:
    __all__ = ["generator_write_file"]
