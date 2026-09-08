"""Fresh public CLI processes must consume exact, validated isolation."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

from tools import research_taskbook


ROOT = Path(__file__).resolve().parents[1]
FORK_TASK = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
FIXTURE_TASK = "TST-PUBLICATION-CLI-CANONICAL"
BOOK = "research_tasks/CLI_CANONICAL_PUBLICATION_FIXTURE.md"
QUARANTINES = "research_task_publication_quarantines.json"


class PublicationCliCanonicalBootstrapTests(unittest.TestCase):
    """Use one disposable source snapshot; never mutate the checkout records."""

    @classmethod
    def _run(cls, arguments):
        argv = [sys.executable, "-B", "-X", "utf8", *arguments]
        start = time.perf_counter()
        result = subprocess.run(argv, cwd=cls.root, capture_output=True, timeout=75)
        cls.runs.append({
            "argv": argv, "cwd": str(cls.root), "returncode": result.returncode,
            "elapsed_seconds": round(time.perf_counter() - start, 6),
            "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(),
            "stderr_sha256": hashlib.sha256(result.stderr).hexdigest(),
            "stdout": result.stdout.decode("utf-8"),
            "stderr": result.stderr.decode("utf-8"),
        })
        return result

    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="em-publication-cli-bootstrap-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name).joinpath("repo")
        cls.runs = []
        # Copy tracked source once so the real bootstrap sees every existing
        # source pin. This is a test fixture, not a replacement policy registry.
        paths = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
        for name in paths.decode("utf-8").split("\0"):
            if name:
                target = cls.root.joinpath(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT.joinpath(name), target)
        cls.facade_sha256 = hashlib.sha256(
            cls.root.joinpath("tools/research_task_records.py").read_bytes()
        ).hexdigest()
        source_book = ROOT.joinpath(
            "research_tasks/LEGACY_CONTROL_MIGRATION_RS_A3_A4_GENERATED_SUPPORT_20260902.md"
        )
        meta, body = research_taskbook.split_taskbook(source_book.read_text(encoding="utf-8"))
        meta.update(task_id=FIXTURE_TASK, registry_key=FIXTURE_TASK,
                    title="Disposable publication CLI fixture")
        cls.root.joinpath(BOOK).write_bytes(
            research_taskbook.render_taskbook(meta, body).encode("utf-8")
        )
        prepared = cls._run([
            "tools/research_task_records.py", "prepare", "--taskbook", BOOK,
            "--publisher-role", "RESEARCH_DRIVER", "--parent-objective-id",
            meta["parent_objective_id"],
        ])
        if prepared.returncode:
            raise AssertionError(prepared.stdout.decode() + prepared.stderr.decode())
        cls.prepared_book = cls.root.joinpath(BOOK).read_bytes()
        cls.quarantine_bytes = cls.root.joinpath(QUARANTINES).read_bytes()
        payload = json.loads(cls.quarantine_bytes)
        row = next(row for row in payload["quarantines"] if row["task_id"] == FORK_TASK)
        pub_path = f"research_task_records/{FORK_TASK}/{row['publication_ids'][0]}.json"
        record = json.loads(cls.root.joinpath(pub_path).read_bytes())
        cls.pinned_book = record["taskbook_path"]
        cls.pinned_book_bytes = cls.root.joinpath(cls.pinned_book).read_bytes()

    @classmethod
    def tearDownClass(cls):
        output = os.environ.get("EM_PUBLICATION_CLI_TEST_RECEIPT")
        if output:
            Path(output).write_bytes((json.dumps({
                "facade_sha256": cls.facade_sha256, "runs": cls.runs,
            }, indent=2) + "\n").encode("utf-8"))

    def setUp(self):
        # A prepared taskbook is intentionally not yet a published task. Do not
        # inject this unrelated orphan into an audit-only import-order case.
        self.root.joinpath(BOOK).unlink(missing_ok=True)
        self.addCleanup(self._restore_fixture)

    def _restore_fixture(self):
        self.root.joinpath(BOOK).unlink(missing_ok=True)
        self.root.joinpath(QUARANTINES).write_bytes(self.quarantine_bytes)
        self.root.joinpath(self.pinned_book).write_bytes(self.pinned_book_bytes)
        directory = self.root.joinpath("research_task_records", FIXTURE_TASK)
        self.assertTrue(directory.resolve().is_relative_to(self.root.resolve()))
        if directory.exists():
            for record in directory.iterdir():
                self.assertTrue(record.is_file())
                record.unlink()
            directory.rmdir()

    def _publish(self):
        if not self.root.joinpath(BOOK).exists():
            self.root.joinpath(BOOK).write_bytes(self.prepared_book)
        return self._run([
            "tools/research_task_records.py", "publish", "--taskbook", BOOK,
            "--publisher-role", "RESEARCH_DRIVER", "--publisher-id", "TEST-CLI",
            "--research-value", "Disposable CLI integration fixture only.",
            "--published-at", "2026-09-08T00:15:00+00:00",
        ])

    def assert_success(self, result):
        self.assertEqual(0, result.returncode,
                         result.stdout.decode("utf-8") + result.stderr.decode("utf-8"))
        self.assertEqual(b"", result.stderr)

    def test_fresh_import_orders_keep_canonical_audit_and_strict_handle(self):
        code = """
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().joinpath('tools')))
order = sys.argv[1]
if order == 'bare-first':
    import research_task_records as bare
from tools import research_task_records as canonical
from control_plane import research_task_records_impl as core
strict = canonical._STRICT_AUDIT
raw = strict(Path.cwd())
assert any('publication fork for RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE' in e for e in raw), raw
if order == 'bootstrap-first':
    from control_plane import research_control_bootstrap
    research_control_bootstrap.install(Path.cwd())
if order != 'bare-first':
    import research_task_records as bare
entry = canonical if order == 'canonical-first' else bare
previous_audit, previous_writer = core.audit, core.build_record
sys.argv = ['tools/research_task_records.py', 'audit']
assert entry.main() == 0
assert canonical._STRICT_AUDIT is strict
assert core._immutable_history_original_audit is strict
assert core.audit is previous_audit and core.build_record is previous_writer
assert 'RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE' not in canonical.current_records(Path.cwd())
print('PASS: strict pre-bootstrap fork retained; canonical CLI and alias order agree')
"""
        for order in ("bare-first", "canonical-first", "bootstrap-first"):
            with self.subTest(order=order):
                self.assert_success(self._run(["-c", code, order]))

    def test_unrelated_publication_survives_existing_exact_quarantine(self):
        result = self._publish()
        self.assert_success(result)
        record = json.loads(result.stdout)
        self.assertEqual(FIXTURE_TASK, record["task_id"])
        self.assertEqual(1, record["publication_generation"])
        self.assertFalse(record["working_truth_granted"])
        self.assertFalse(record["canonical_promotion_granted"])
        self.assertEqual(self.quarantine_bytes, self.root.joinpath(QUARANTINES).read_bytes())
        # A defect on this newly written, unrelated record is not an allowed
        # historical suppression, even while the old fork remains quarantined.
        path = self.root.joinpath(record["record_path"])
        stored = json.loads(path.read_bytes())
        stored["working_truth_granted"] = True
        path.write_bytes((json.dumps(stored, indent=2) + "\n").encode("utf-8"))
        rejected = self._run(["tools/research_task_records.py", "audit"])
        self.assertNotEqual(0, rejected.returncode)
        self.assertIn(b"publication cannot grant Working Truth", rejected.stdout + rejected.stderr)

    def test_fork_without_exact_quarantine_still_rejects(self):
        payload = json.loads(self.quarantine_bytes)
        payload["quarantines"] = [row for row in payload["quarantines"]
                                  if row["task_id"] != FORK_TASK]
        self.root.joinpath(QUARANTINES).write_bytes(
            (json.dumps(payload, indent=2) + "\n").encode("utf-8")
        )
        result = self._run(["tools/research_task_records.py", "audit"])
        self.assertNotEqual(0, result.returncode)
        self.assertIn(f"publication fork for {FORK_TASK}".encode(), result.stdout + result.stderr)

    def test_bad_new_taskbook_is_not_published(self):
        text = self.prepared_book.decode("utf-8")
        heading = "## Frozen inputs and scope"
        self.assertIn(heading, text)
        self.root.joinpath(BOOK).write_bytes(text.replace(heading, "## Removed fixture section").encode("utf-8"))
        result = self._publish()
        self.assertNotEqual(0, result.returncode)
        self.assertIn(b"mandatory body section is missing or empty: Frozen inputs and scope", result.stdout + result.stderr)
        self.assertFalse(self.root.joinpath("research_task_records", FIXTURE_TASK).exists())

    def test_pin_drift_on_quarantined_history_still_rejects(self):
        self.root.joinpath(self.pinned_book).write_bytes(self.pinned_book_bytes + b"\n")
        result = self._run(["tools/research_task_records.py", "audit"])
        self.assertNotEqual(0, result.returncode)
        self.assertIn(b"taskbook blob", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
