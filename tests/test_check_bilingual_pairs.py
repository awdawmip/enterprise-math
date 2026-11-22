import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "tools" / "check_bilingual_pairs.py"


class BilingualSelectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        (self.root / "docs").mkdir()
        shutil.copyfile(CHECKER, self.root / "tools" / CHECKER.name)
        pairs = [[f"docs/{name}.en.md", f"docs/{name}.zh-CN.md"]
                 for name in ("alpha", "beta")]
        (self.root / "bilingual_pairs.json").write_text(
            json.dumps({"version": 1, "pairs": pairs}), encoding="utf-8")
        for name in ("alpha", "beta"):
            self.write(f"docs/{name}.en.md", f"# {name}\n\n## Scope\n\nBaseline.\n")
            self.write(f"docs/{name}.zh-CN.md", f"# {name}\n\n## 范围\n\n正文。\n")

    def write(self, path, text):
        (self.root / path).write_text(text, encoding="utf-8")

    def check(self, *arguments):
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / CHECKER.name), *arguments],
            cwd=self.root, text=True, capture_output=True,
        )

    def assert_passes(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_fails(self, result):
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_selected_skips_unrelated_pairs_and_default_audits_them(self):
        self.assert_passes(self.check())
        (self.root / "docs/beta.zh-CN.md").unlink()
        self.write("docs/unregistered.en.md", "# Unregistered\n")
        self.assert_passes(self.check("--paths", "docs/alpha.en.md"))
        self.assert_fails(self.check())

    def test_missing_selected_counterpart_fails(self):
        (self.root / "docs/alpha.zh-CN.md").unlink()
        self.assert_fails(self.check("--paths", "docs/alpha.en.md"))

    def test_unregistered_requested_path_fails(self):
        path = "docs/unregistered.en.md"
        self.write(path, "# Unregistered\n")
        result = self.check("--paths", "docs/alpha.en.md", path)
        self.assert_fails(result)
        self.assertIn(path, result.stdout)

    def test_selected_heading_and_character_checks_remain(self):
        for content in ("# Alpha\n", "# Alpha\n\n## Scope\n\n中文。\n"):
            with self.subTest(content=content):
                self.write("docs/alpha.en.md", content)
                self.assert_fails(self.check("--paths", "docs/alpha.zh-CN.md"))

    def test_all_requested_pairs_are_checked(self):
        self.write("docs/beta.en.md", "# Beta\n\n## Scope\n\n中文。\n")
        self.assert_fails(self.check("--paths", "docs/alpha.en.md", "docs/beta.zh-CN.md"))

    @unittest.skipUnless(shutil.which("git"), "git is required for the comparison test")
    def test_selected_base_check_preserves_same_change_requirement(self):
        def git(*arguments):
            return subprocess.run(
                ["git", "-c", "user.name=Bilingual Test", "-c", "user.email=test@example.invalid",
                 *arguments], cwd=self.root, text=True, capture_output=True, check=True,
            ).stdout.strip()

        git("init", "-q")
        git("add", ".")
        git("commit", "-qm", "initial pair")
        base = git("rev-parse", "HEAD")
        self.write("docs/alpha.en.md", "# Alpha\n\n## Scope\n\nUpdated.\n")
        git("add", ".")
        git("commit", "-qm", "English draft")
        args = ("--base", base, "--paths", "docs/alpha.zh-CN.md")
        self.assert_fails(self.check(*args))
        self.write("docs/alpha.zh-CN.md", "# Alpha\n\n## 范围\n\n修改正文。\n")
        git("add", ".")
        git("commit", "-qm", "paired integration")
        self.assert_passes(self.check(*args))


if __name__ == "__main__":
    unittest.main()
