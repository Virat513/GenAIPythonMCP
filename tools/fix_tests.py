# NOTE FOR AI TOOLS:
# This file is executed programmatically.
# Do NOT suggest running it manually.
# Do NOT repeat CLI commands.

import subprocess
import sys
import re
from pathlib import Path
from typing import List, Dict


PROJECT_ROOT = Path(__file__).resolve().parents[1]

TEST_DIRS = [
    PROJECT_ROOT / "src" / "tests"
]

REPORT_DIR = PROJECT_ROOT / "reports" / "html"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


class PytestResult:
    def __init__(self, returncode: int, output: str):
        self.returncode = returncode
        self.output = output
        self.failed_tests = self._extract_failed_tests()

    def _extract_failed_tests(self) -> Dict[str, List[str]]:
        failures = {}
        pattern = re.compile(r"FAILED\s+(.*)::(.*)")

        for line in self.output.splitlines():
            match = pattern.search(line)
            if match:
                file_path, test_name = match.groups()
                failures.setdefault(file_path, []).append(test_name)

        return failures


class Healer:

    def run_pytest(self, only_files: List[str] | None = None) -> PytestResult:
        """Run pytest with parallel workers and HTML reporting."""

        cmd = [
            sys.executable, "-m", "pytest",
            "-n", "3",
            "-v",
            "--maxfail=0",
            "--disable-warnings",
            f"--html={REPORT_DIR / 'report.html'}",
            "--self-contained-html"
        ]

        if only_files:
            cmd.extend(only_files)
        else:
            for d in TEST_DIRS:
                if d.exists():
                    cmd.append(str(d))

        print("\n▶ Running pytest...\n")

        process = subprocess.Popen(
            cmd,
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            universal_newlines=True
        )

        output_lines = []

        try:
            for line in process.stdout:
                print(line, end="")
                output_lines.append(line)
            process.wait()
        except KeyboardInterrupt:
            print("\n⚠ Test run interrupted by user.")
            process.kill()
            raise

        return PytestResult(process.returncode, "".join(output_lines))

    def heal_failures(self, failures: Dict[str, List[str]]):
        """Apply safe, deterministic fixes to failing tests."""
        print("\n🩺 Healing failed tests...")

        for file_path in failures:
            path = PROJECT_ROOT / file_path
            if not path.exists():
                continue

            content = path.read_text(encoding="utf-8")
            original = content

            # Normalize imports
            content = re.sub(
                r"from\s+pages\.",
                "from src.pages.",
                content
            )

            if content != original:
                path.write_text(content, encoding="utf-8")
                print(f"✔ Healed: {file_path}")
            else:
                print(f"⚠ No safe fix applied: {file_path}")

    def execute(self):
        result = self.run_pytest()

        if result.returncode == 0:
            print("\n✅ All tests passed. No healing required.")
            return

        if not result.failed_tests:
            print("\n❌ Pytest failed but no test failures detected.")
            return

        # Guard against environment-wide failures
        if len(result.failed_tests) > 5:
            print("\n❌ Environment-level failure detected.")
            print("   Skipping healing to avoid unsafe changes.")
            return

        self.heal_failures(result.failed_tests)

        print("\n🔁 Re-running healed tests...")
        rerun_result = self.run_pytest(list(result.failed_tests.keys()))

        print("\n📊 Healing Summary")
        print("----------------------------")
        print(f"Initial Failures: {len(result.failed_tests)}")
        print(
            "Final Status:",
            "✅ PASS" if rerun_result.returncode == 0 else "❌ STILL FAILING"
        )


if __name__ == "__main__":
    print("\n🩺 Healer started")
    print("=" * 40)

    Healer().execute()

    print("\n🩺 Healer finished")
    print("=" * 40)
