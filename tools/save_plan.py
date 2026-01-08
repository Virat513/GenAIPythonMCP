from typing import Dict
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("playwright-python-test-planner")

PROJECT_ROOT = Path.cwd()
BASE_DIR = PROJECT_ROOT / "instructions" / "test-plans"
BASE_DIR.mkdir(parents=True, exist_ok=True)


@mcp.tool()
def planner_save_plan(
    plan_name: str,
    content: str
) -> Dict[str, str]:
    """
    Save a manual test plan as a Markdown (.md) file.

    Args:
        plan_name: Name of the test plan file without extension
        content: Complete Markdown-formatted test plan content

    Returns:
        Confirmation message with file path
    """

    if not plan_name.strip():
        raise ValueError("plan_name must not be empty")

    if not content.strip():
        raise ValueError("content must not be empty")

    file_path = (BASE_DIR / f"{plan_name}.md").resolve()

    if not file_path.as_posix().startswith(BASE_DIR.resolve().as_posix()):
        raise ValueError("Test plans must be saved inside instructions/test-plans/")

    file_path.write_text(content, encoding="utf-8")

    return {
        "status": "success",
        "message": "Test plan saved successfully",
        "file": str(file_path)
    }


if __name__ == "__main__":
    mcp.run()
else:
    __all__ = ["planner_save_plan"]
