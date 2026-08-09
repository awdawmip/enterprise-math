import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ResearchCommonSurfaceGateTests(unittest.TestCase):
    def test_shared_surface_integrity_checker_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "tools/check_research_common_surface.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=(
                "shared research surface checker failed\n"
                f"stdout:\n{result.stdout}\n"
                f"stderr:\n{result.stderr}"
            ),
        )
        self.assertIn("research common surface: OK", result.stdout)


if __name__ == "__main__":
    unittest.main()
