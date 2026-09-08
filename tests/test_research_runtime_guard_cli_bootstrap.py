"""The public runtime guard must start without an inherited repository path."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RuntimeGuardCliBootstrapTests(unittest.TestCase):
    def _assert_help(self, arguments: list[str]) -> None:
        env = dict(os.environ)
        env.pop("PYTHONPATH", None)
        result = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", *arguments, "--help"],
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Enterprise Math repository-backed runtime guard", result.stdout)
        for command in (
            "authorize", "pre-final", "terminal", "adopt",
            "pre-math-stamp", "raw-freeze", "source-expose",
        ):
            self.assertIn(command, result.stdout)

    def test_direct_script_help_without_pythonpath(self) -> None:
        self._assert_help(["tools/research_runtime_guard.py"])

    def test_module_help_without_pythonpath(self) -> None:
        self._assert_help(["-m", "tools.research_runtime_guard"])

    def test_driver_queue_import_bootstrap_outside_repository(self) -> None:
        # Run the actual facade without __main__: this verifies import setup,
        # not the expensive current-store queue or any authority operation.
        script = ROOT.joinpath("tools/research_driver_queue.py")
        probe = (
            "import runpy; "
            f"runpy.run_path({str(script)!r}, run_name='probe'); "
            "import control_plane.research_control_bootstrap; "
            "print('QUEUE_IMPORT_BOOTSTRAP_OK')"
        )
        env = dict(os.environ)
        env.pop("PYTHONPATH", None)
        with tempfile.TemporaryDirectory(prefix="em-queue-import-bootstrap-") as cwd:
            result = subprocess.run(
                [sys.executable, "-B", "-X", "utf8", "-c", probe],
                cwd=cwd,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=30,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "QUEUE_IMPORT_BOOTSTRAP_OK")


if __name__ == "__main__":
    unittest.main()
