import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ToolboxLogicClosureTests(unittest.TestCase):
    def test_toolbox_logic_closure_checker_passes(self):
        result = subprocess.run(
            [sys.executable, "tools/check_toolbox_logic_closure.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=(
                "toolbox logic closure checker failed\n"
                f"stdout:\n{result.stdout}\n"
                f"stderr:\n{result.stderr}"
            ),
        )
        self.assertIn("toolbox logic closure: OK", result.stdout)


if __name__ == "__main__":
    unittest.main()
