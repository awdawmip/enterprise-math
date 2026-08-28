import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ResearchCommonSurfaceGateTests(unittest.TestCase):
    def test_shared_surface_integrity_checker_passes(self) -> None:
        # The production reference-integrity route installs the canonical
        # fault-isolated runtime view before evaluating the shared surface.  The
        # regression must exercise that same control boundary rather than a raw
        # internal helper that intentionally remains strict/bootstrap-free.
        code = (
            "from control_plane import research_control_bootstrap as b; "
            "b.install(); "
            "from tools import check_research_common_surface as c; "
            "c.check()"
        )
        result = subprocess.run(
            [sys.executable, "-c", code],
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
