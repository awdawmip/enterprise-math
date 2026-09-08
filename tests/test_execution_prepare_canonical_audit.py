"""Real CLI prepare over exact historical isolation; no claim/runtime grant.

The fixture copies control Python imports and the needed immutable source records
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

from tests.test_research_task_record_compatibility import _write_semantic_fixture

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
FORK_TASK = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
FORK_REGISTRY = "research_task_publication_quarantines.json"
NEW_TASK = "RS-PFSSV-FINITE-WINDOW-NULL-IDENTIFIABILITY"
NEW_PUBLICATION = "TP2-38717785C4ADF3A12A49"


class ExecutionPrepareCanonicalAuditTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="em-execution-prepare-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.source_bytes = {}
        # The real CLI now installs canonical runtime views before prepare.
        # Copy only Python control imports, not the full research source store;
        # data fixtures below still satisfy the actual validators independently.
        code = set(CODE)
        for directory in ("tools", "control_plane"):
            code.update(path.relative_to(REPO).as_posix()
                        for path in REPO.joinpath(directory).glob("*.py"))
        code.update(path.relative_to(REPO).as_posix() for path in REPO.glob("research*.py"))
        for path in sorted(code):
            self.capture(path)
        # Namespace/package behavior follows the repository, not private aliases.
        for path in ("tools/__init__.py", "control_plane/__init__.py"):
            if REPO.joinpath(path).is_file():
                self.capture(path)
        # Bootstrap requires a genuinely invalid, exactly pinned authority row.
        # This retained review fails the unchanged Driver-id syntax gate; no
        # fabricated Driver identity or valid-authority exemption is introduced.
        authority_registry = "research_driver_review_authority_quarantines.json"
        authority_payload = json.loads(self.capture(authority_registry))
        authority_row = next(row for row in authority_payload["entries"]
                             if row["review_id"] == "DR-2F834647FD94CAF46D05")
        self.write(authority_registry, {**authority_payload, "entries": [authority_row]})
        self.capture(authority_row["review_record_path"])
        self.capture("research_driver_authority_contract.json")
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
        _write_semantic_fixture(self.root)
        self.semantic_history = {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in (
                self.root.joinpath("research_task_semantic_integrity_quarantines.json"),
                self.root.joinpath("research_task_records/RS-SEMANTIC-FIXTURE/TP2-SEMANTIC-FIXTURE.json"),
                self.root.joinpath("research_tasks/TP2-SEMANTIC-FIXTURE.md"),
                self.root.joinpath("fixtures/semantic-source.md"),
            )
        }
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

    def prepare(self, entry="module", *, branch="fixture/er-prepare", task_id=TASK,
                prepared_at="2026-09-08T11:00:00+00:00"):
        return self.run_cli(
            entry, "prepare-claim", "--task-id", task_id,
            "--claim-id", "fixture-er-prepare", "--researcher-id", "EM-FIXTURE-0101",
            "--theorem-owner", "fixture/metadata-only",
            "--execution-branch", branch, "--execution-branch-base", "1" * 40,
            "--allowed-outputs-json", '["research_artifacts/ER_PREPARE_FIXTURE/output.json"]',
            "--owner-lease-minutes", "120", "--prepared-at", prepared_at,
        )

    def assert_sources_preserved(self, *, except_paths=()):
        for path, data in self.semantic_history.items():
            self.assertEqual(self.root.joinpath(path).read_bytes(), data, path)
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

    def add_real_unresolved_fork(self):
        payload = json.loads(self.capture(FORK_REGISTRY))
        self.fork_row = next(row for row in payload["quarantines"]
                             if row["task_id"] == FORK_TASK)
        self.assertEqual(3, len(self.fork_row["publication_ids"]))
        self.write(FORK_REGISTRY, {**payload, "quarantines": [self.fork_row]})
        # Keep all generations of this exact retained task, including ancestry
        # needed by a future legitimate lineage-forward representation.
        for path in REPO.joinpath("research_task_records", FORK_TASK).glob("*.json"):
            self.capture_publication(FORK_TASK, path.stem)
        self.capture_publication(NEW_TASK, NEW_PUBLICATION)
        self.history.update({path: self.root.joinpath(path).read_bytes()
                             for path in self.source_bytes})
        self.fork_intents_before = {
            path.name: path.read_bytes()
            for path in self.root.joinpath("research_execution_records", FORK_TASK).glob("*.json")
        }

    def assert_no_new_fork_intent(self):
        self.assertEqual(self.fork_intents_before, {
            path.name: path.read_bytes()
            for path in self.root.joinpath("research_execution_records", FORK_TASK).glob("*.json")
        })

    def check_prepare_over_real_fork(self, entry):
        self.add_real_unresolved_fork()
        run = self.prepare(entry, task_id=NEW_TASK, prepared_at="2026-09-08T13:00:00+00:00")
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        record = json.loads(run.stdout)
        self.assertEqual(record["task_id"], NEW_TASK)
        self.assertEqual(record["publication_id"], NEW_PUBLICATION)
        self.assertEqual(record["record_state"], "CLAIM_INTENT")
        self.assertEqual(record["allowed_outputs"], ["research_artifacts/ER_PREPARE_FIXTURE/output.json"])
        self.assert_no_new_fork_intent()
        self.assert_sources_preserved()

    def test_direct_script_prepare_applies_existing_fork_isolation(self):
        self.check_prepare_over_real_fork("script")

    def test_module_prepare_applies_existing_fork_isolation(self):
        self.check_prepare_over_real_fork("module")

    def test_direct_script_rejects_fork_head_drift_before_write(self):
        self.add_real_unresolved_fork()
        payload = json.loads(self.root.joinpath(FORK_REGISTRY).read_bytes())
        payload["quarantines"][0]["publication_ids"].pop()
        self.write(FORK_REGISTRY, payload)
        run = self.prepare("script", task_id=NEW_TASK)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("quarantine head set drift", run.stdout + run.stderr)
        self.assertNotIn("execution record created but audit failed", run.stdout + run.stderr)
        self.assertFalse(self.root.joinpath("research_execution_records", NEW_TASK).exists())
        self.assert_sources_preserved(except_paths=[FORK_REGISTRY])

    def test_direct_script_cannot_prepare_a_quarantined_task(self):
        self.add_real_unresolved_fork()
        run = self.prepare("script", task_id=FORK_TASK)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("execution intents are required only for immutable registered tasks", run.stdout + run.stderr)
        self.assert_no_new_fork_intent()
        self.assert_sources_preserved()


if __name__ == "__main__":
    unittest.main()
