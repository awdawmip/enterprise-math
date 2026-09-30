"""Stdlib-only tests for the conversation runner, not the repository's full suite."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("conversation_validation", ROOT / "scripts/run_conversation_validation.py")
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class ConversationValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.repo = self.base / "repo"
        (self.repo / "scripts").mkdir(parents=True)
        shutil.copytree(ROOT / ".github/workflows", self.repo / ".github/workflows")
        self.manifest = self.repo / "scripts/conversation_validation_contract.json"
        shutil.copyfile(ROOT / "scripts/conversation_validation_contract.json", self.manifest)
        self.contract = runner.load_contract(self.repo, self.manifest)

    def write(self, relative, content):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    def run_main(self, *args):
        output = self.base / "evidence"
        with contextlib.redirect_stdout(io.StringIO()):
            code = runner.main(["--repo", str(self.repo), "--output", str(output), *args])
        return code, json.loads((output / "receipt.json").read_text())

    def test_all_reference_commands_covered_in_order(self):
        expected = self.contract["workflows"][".github/workflows/reference-integrity.yml"]["run_commands"]
        plan = runner.plan_commands(self.contract, list(runner.STAGES), {"base": None})
        self.assertEqual([row["command"] for row in plan if row["stage"] == "reference-integrity"], expected)
        self.assertEqual(len(expected), 34)
        self.assertEqual(len(plan), 36)
        self.assertIn("apply_registered_json_migration.py", expected[13])
        self.assertIn("research_cohort_runtime", expected[-1])

    def test_quality_preserves_mixed_runner_and_heavy_file(self):
        plan = runner.plan_commands(self.contract, ["quality"], None)
        self.assertEqual(plan[0]["command"], "python scripts/run_unittest_shard.py --index 0 --count 1")
        self.assertEqual(plan[0]["env"], {"PYTHONPATH": "src"})
        self.assertNotIn("unittest discover", plan[0]["command"])
        self.assertNotIn("rm ", plan[0]["command"])

    def test_workflow_hash_mismatch_blocks(self):
        with (self.repo / ".github/workflows/quality.yml").open("a") as file:
            file.write("\n# changed\n")
        with self.assertRaisesRegex(runner.ContractError, "workflow contract changed"):
            runner.load_contract(self.repo, self.manifest)

    def test_missing_workflow_blocks(self):
        (self.repo / ".github/workflows/quality.yml").unlink()
        with self.assertRaisesRegex(runner.ContractError, "missing/unreadable"):
            runner.load_contract(self.repo, self.manifest)

    def test_malformed_manifest_blocks(self):
        for value in ("not json", "[]", '{"schema_version":1}', '{"schema_version":1,"workflows":null}'):
            self.manifest.write_text(value)
            with self.subTest(value=value), self.assertRaises(runner.ContractError):
                runner.load_contract(self.repo, self.manifest)

    def test_command_omission_even_with_correct_workflow_hash_blocks(self):
        self.contract["workflows"][".github/workflows/reference-integrity.yml"]["run_commands"].pop()
        self.manifest.write_text(json.dumps(self.contract))
        with self.assertRaisesRegex(runner.ContractError, "command parity"):
            runner.load_contract(self.repo, self.manifest)

    def test_folded_and_literal_scalars(self):
        text = "jobs:\n  one:\n    steps:\n      - name: x\n        run: >-\n          python a.py\n          --x two\n      - run: |\n          python b.py\n          python c.py\n"
        self.assertEqual(runner.workflow_commands(text), ["python a.py --x two", "python b.py\npython c.py"])

    def test_reference_failfast_and_independent_stages_continue(self):
        plan = runner.plan_commands(self.contract, list(runner.STAGES), {"base": None})
        calls = []
        def execute(argv, **kwargs):
            calls.append(argv)
            kwargs["stdout"].write(b"captured output\n")
            return SimpleNamespace(returncode=7 if len(calls) == 2 else 0)
        output = self.base / "logs"
        output.mkdir()
        rows = runner.execute_plan(self.repo, output, plan, 30, execute)
        self.assertEqual(len(calls), 3)
        self.assertEqual(rows[1]["exit_code"], 7)
        self.assertEqual(rows[1]["status"], "FAIL")
        self.assertTrue(all(row["status"] == "NOT_RUN_DEPENDENCY_FAILED" for row in rows[2:-1]))
        self.assertEqual(rows[-1]["status"], "PASS")
        self.assertEqual(rows[1]["log_sha256"], runner.digest(b"captured output\n"))

    def test_timeout_never_passes(self):
        def execute(*args, **kwargs):
            raise subprocess.TimeoutExpired(args[0], 1)
        output = self.base / "logs"
        output.mkdir()
        rows = runner.execute_plan(self.repo, output, runner.plan_commands(self.contract, ["quality"], None), 1, execute)
        self.assertEqual(rows[0]["status"], "TIMEOUT")
        self.assertIsNone(rows[0]["exit_code"])

    def test_bilingual_never_silently_falls_back(self):
        for mode, base in ((None, None), ("base", None), ("base", "missing"), ("base", "0" * 40), ("full-snapshot", "a" * 40)):
            with self.subTest(mode=mode, base=base), self.assertRaises(runner.ContractError):
                runner.bilingual_provenance(self.repo, mode, base)
        with self.assertRaises(runner.ContractError):
            runner.bilingual_provenance(self.repo, "base", "a" * 40)

    def test_dirty_base_is_rejected(self):
        outputs = [str(self.repo), "a" * 40, "b" * 40, " M docs/example.en.md"]
        with mock.patch.object(runner, "git_output", side_effect=outputs):
            with self.assertRaisesRegex(runner.ContractError, "clean committed candidate"):
                runner.bilingual_provenance(self.repo, "base", "a" * 40)

    def test_full_snapshot_is_honest_and_emits_evidence(self):
        self.write("tools/check_bilingual_pairs.py", "print('synthetic structural test')\n")
        code, receipt = self.run_main("--stages", "bilingual", "--full-snapshot")
        self.assertEqual(code, 0)
        self.assertEqual(receipt["status"], "LOCAL_SELECTED_SCOPE_PASS")
        self.assertFalse(receipt["bilingual"]["same_change_pairing_verified"])
        self.assertFalse(receipt["github_checks_updated"])
        self.assertTrue(receipt["source_unchanged"])
        self.assertEqual(len(receipt["workflow_sha256"]), 3)
        self.assertEqual(receipt["results"][0]["exit_code"], 0)

    def test_missing_script_blocks_before_execution(self):
        code, receipt = self.run_main("--stages", "quality")
        self.assertEqual(code, 2)
        self.assertEqual(receipt["status"], "BLOCKED")
        self.assertEqual(receipt["results"], [])

    def test_reference_subset_records_real_failure(self):
        self.write("control_plane/apply_registered_json_migration.py", "import sys\nprint('synthetic migration failure')\nsys.exit(9)\n")
        code, receipt = self.run_main("--stages", "reference-integrity", "--reference-step", "14")
        self.assertEqual(code, 1)
        self.assertEqual(receipt["reference_subset"], [14])
        self.assertEqual(len(receipt["results"]), 1)
        self.assertEqual(receipt["results"][0]["exit_code"], 9)
        self.assertIn("subset only", receipt["coverage"])

    def test_source_change_prevents_pass(self):
        self.write("tools/check_bilingual_pairs.py", "from pathlib import Path\nPath('changed.txt').write_text('mutation')\n")
        code, receipt = self.run_main("--stages", "bilingual", "--full-snapshot")
        self.assertEqual(code, 1)
        self.assertFalse(receipt["source_unchanged"])
        self.assertEqual(receipt["results"][0]["status"], "PASS")
        self.assertEqual(receipt["status"], "FAIL")

    def test_path_traversal_source_blocked(self):
        with self.assertRaises(runner.ContractError):
            runner.read_source(self.repo, "../outside")

    def test_quality_rejects_connector_only_tree(self):
        self.write("scripts/run_unittest_shard.py", "print('not a complete suite')\n")
        self.write("tests/test_p017_mirror_cross.py", "# synthetic fixture\n")
        with self.assertRaises(runner.ContractError):
            runner.quality_source_provenance(self.repo)

    def test_quality_rejects_sparse_checkout(self):
        outputs = [str(self.repo), "b" * 40, "true", "S tests/hidden.py\0"]
        with mock.patch.object(runner, "git_output", side_effect=outputs):
            with self.assertRaisesRegex(runner.ContractError, "sparse"):
                runner.quality_source_provenance(self.repo)

    def test_quality_rejects_missing_head_file(self):
        outputs = [str(self.repo), "b" * 40, "false", "H scripts/run_unittest_shard.py\0", "scripts/run_unittest_shard.py\0tests/test_p017_mirror_cross.py\0src/missing.py\0"]
        with mock.patch.object(runner, "git_output", side_effect=outputs):
            with self.assertRaisesRegex(runner.ContractError, "missing/unreadable"):
                runner.quality_source_provenance(self.repo)


if __name__ == "__main__":
    unittest.main()
