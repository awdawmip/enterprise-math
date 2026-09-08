"""Real CLI prepare over exact historical isolation; no claim/runtime grant.

The fixture copies the small Python import closure and immutable source records
into TEMP, so script and module entrypoints have genuine local ROOT defaults.
No bootstrap, reader, builder, audit, or permission validator is mocked. The ER
CI checker itself uses the strict audit plus its existing exact nonlive registry;
this test does not replace that chain with a different startup/audit layer.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
REGISTRY = "research_execution_record_audit_quarantines.json"
TASK = "RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION"
PUBLICATION = "TP2-2029B5CCC5EEC5F0132C"
CODE = (
    "tools/research_execution_records.py",
    "tools/research_identity.py",
    "tools/research_task_records.py",
    "tools/research_taskbook.py",
    "research_execution_cohorts.py",
    "control_plane/research_task_records_impl.py",
    "control_plane/research_execution_record_audit_fault_isolation.py",
)


class ExecutionPrepareCanonicalAuditTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="em-execution-prepare-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.source_bytes = {}
        for path in CODE:
            self.capture(path)
        # Namespace/package behavior follows the repository, not private aliases.
        for path in ("tools/__init__.py", "control_plane/__init__.py"):
            if REPO.joinpath(path).is_file():
                self.capture(path)
        registry = json.loads(REPO.joinpath(REGISTRY).read_bytes())
        self.row = copy.deepcopy(next(
            row for row in registry["quarantines"]
            if row["nonlive_basis"] == "TERMINAL_EXECUTION_STATE"
        ))
        self.registry = {**registry, "quarantines": [self.row]}
        self.write(REGISTRY, self.registry)
        self.capture(self.row["record_path"])
        self.capture_publication(self.row["task_id"], self.row["publication_id"])
        # Copy a fixed admitted publication and its ancestor chain, rather than
        # selecting whichever future main generation happens to be current.
        publication_id = PUBLICATION
        seen = set()
        while publication_id:
            self.assertNotIn(publication_id, seen)
            seen.add(publication_id)
            record = self.capture_publication(TASK, publication_id)
            publication_id = record.get("supersedes_publication_id")
        self.history = {path: self.root.joinpath(path).read_bytes()
                        for path in self.source_bytes}
        self.intent_dir = self.root.joinpath("research_execution_records", TASK)

    def capture(self, relative):
        data = REPO.joinpath(relative).read_bytes()
        self.source_bytes[relative] = data
        path = self.root.joinpath(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return data

    def capture_publication(self, task_id, publication_id):
        relative = f"research_task_records/{task_id}/{publication_id}.json"
        record = json.loads(self.capture(relative))
        self.capture(record["taskbook_path"])
        return record

    def write(self, relative, value):
        path = self.root.joinpath(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        return path

    def run_cli(self, entry, *arguments):
        prefix = (["tools/research_execution_records.py"] if entry == "script"
                  else ["-m", "tools.research_execution_records"] if entry == "module"
                  else ["control_plane/research_execution_record_audit_fault_isolation.py"])
        argv = [sys.executable, "-B", "-X", "utf8", *prefix, *arguments]
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        run = subprocess.run(argv, cwd=self.root, env=environment, capture_output=True,
                             text=True, encoding="utf-8", timeout=30)
        print(json.dumps({"test": self._testMethodName, "entry": entry,
                          "argv": argv, "cwd": str(self.root), "exit": run.returncode,
                          "stdout": run.stdout, "stderr": run.stderr}, ensure_ascii=False))
        return run

    def prepare(self, entry="module", *, branch="fixture/er-prepare"):
        return self.run_cli(
            entry, "prepare-claim", "--task-id", TASK,
            "--claim-id", "fixture-er-prepare", "--researcher-id", "EM-FIXTURE-0101",
            "--theorem-owner", "fixture/metadata-only",
            "--execution-branch", branch, "--execution-branch-base", "1" * 40,
            "--allowed-outputs-json", '["research_artifacts/ER_PREPARE_FIXTURE/output.json"]',
            "--owner-lease-minutes", "120", "--prepared-at", "2026-09-08T11:00:00+00:00",
        )

    def assert_sources_preserved(self, *, except_paths=()):
        for path, data in self.history.items():
            if path not in except_paths:
                self.assertEqual(self.root.joinpath(path).read_bytes(), data, path)
            self.assertEqual(REPO.joinpath(path).read_bytes(), self.source_bytes[path], path)

    def assert_failure_leaves_new_intent(self, run, message):
        self.assertNotEqual(run.returncode, 0, run.stdout)
        self.assertIn("execution record created but audit failed", run.stdout + run.stderr)
        self.assertIn(message, run.stdout + run.stderr)
        rows = list(self.intent_dir.glob("*.json"))
        self.assertEqual(len(rows), 1)
        row = json.loads(rows[0].read_bytes())
        self.assertEqual(row["record_state"], "CLAIM_INTENT")
        self.assertEqual(row["publication_id"], PUBLICATION)

    def check_success_and_raw_boundary(self, entry):
        run = self.prepare(entry)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        record = json.loads(run.stdout)
        path = self.root.joinpath(record["record_path"])
        stored = json.loads(path.read_bytes())
        self.assertEqual(stored, {key: value for key, value in record.items() if key != "record_path"})
        self.assertEqual(stored["publication_id"], PUBLICATION)
        self.assertEqual(stored["record_state"], "CLAIM_INTENT")
        raw = self.run_cli(entry, "audit")
        self.assertEqual(raw.returncode, 1, raw.stdout + raw.stderr)
        expected = [f"ERROR: {self.row['record_path']}: {error}"
                    for error in self.row["allowed_execution_record_audit_errors"]]
        self.assertEqual(raw.stdout.splitlines(), expected)
        canonical = self.run_cli("checker")
        self.assertEqual(canonical.returncode, 0, canonical.stdout + canonical.stderr)
        self.assertIn("no runtime authority granted", canonical.stdout)
        self.assert_sources_preserved()

    def test_script_prepare_uses_exact_gate_and_retains_raw_diagnostics(self):
        self.check_success_and_raw_boundary("script")

    def test_module_prepare_uses_exact_gate_and_retains_raw_diagnostics(self):
        self.check_success_and_raw_boundary("module")

    def test_existing_pin_drift_rejects_after_write_without_deleting_intent(self):
        path = self.root.joinpath(self.row["record_path"])
        path.write_bytes(path.read_bytes() + b"\n")
        self.assert_failure_leaves_new_intent(self.prepare(), "execution record blob drift")
        self.assert_sources_preserved(except_paths=[self.row["record_path"]])

    def test_stale_declared_error_cannot_turn_into_a_prepare_exemption(self):
        self.row["allowed_execution_record_audit_errors"].append("unobserved fixture error")
        self.write(REGISTRY, self.registry)
        self.assert_failure_leaves_new_intent(self.prepare(), "stale or unused suppression")
        self.assert_sources_preserved()

    def test_same_suffix_at_an_unregistered_path_is_not_suppressed(self):
        extra = json.loads(self.root.joinpath(self.row["record_path"]).read_bytes())
        extra.update(execution_record_id="ER-UNREGISTERED-FIXTURE", claim_id="fixture-extra-claim")
        relative = f"research_execution_records/{extra['task_id']}/{extra['execution_record_id']}.json"
        self.write(relative, extra)
        error = self.row["allowed_execution_record_audit_errors"][0]
        self.assert_failure_leaves_new_intent(self.prepare(), relative + ": " + error)
        self.assert_sources_preserved()

    def test_a_repinned_live_record_cannot_use_the_terminal_basis(self):
        relative = self.row["record_path"]
        record = json.loads(self.root.joinpath(relative).read_bytes())
        record["record_state"] = "CLAIM_INTENT"
        path = self.write(relative, record)
        data = path.read_bytes()
        self.row["record_blob_sha1"] = "sha1:" + hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        self.write(REGISTRY, self.registry)
        self.assert_failure_leaves_new_intent(self.prepare(), "not TERMINAL_EXECUTION")
        self.assert_sources_preserved(except_paths=[relative])

    def test_new_intent_duplicate_claim_is_strictly_rejected_after_write(self):
        first = self.prepare(branch="fixture/first-branch")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        prior_path = self.root.joinpath(json.loads(first.stdout)["record_path"])
        prior = prior_path.read_bytes()
        second = self.prepare(branch="fixture/second-branch")
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("duplicate execution claim within owner scope", second.stdout + second.stderr)
        self.assertEqual(len(list(self.intent_dir.glob("*.json"))), 2)
        self.assertEqual(prior_path.read_bytes(), prior)
        self.assert_sources_preserved()

    def test_repeated_prepare_does_not_overwrite_existing_intent(self):
        first = self.prepare()
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        path = self.root.joinpath(json.loads(first.stdout)["record_path"])
        before = path.read_bytes()
        again = self.prepare()
        self.assertNotEqual(again.returncode, 0)
        self.assertIn("already exists", again.stdout + again.stderr)
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(len(list(self.intent_dir.glob("*.json"))), 1)
        self.assert_sources_preserved()


if __name__ == "__main__":
    unittest.main()
