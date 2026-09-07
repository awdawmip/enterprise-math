"""Exact history containment must preserve direct publication lineage and errors."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_result_record_audit_fault_isolation as isolation
from control_plane import research_result_records_impl as results
from control_plane import research_task_records_impl as tasks

REPO = Path(__file__).resolve().parents[1]
RESULT_ID = "RR-68BA014D54542DA7221C"


class SupersededResultAuditBoundaryTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        payload = json.loads((REPO / isolation.QUARANTINE_FILE).read_text(encoding="utf-8"))
        self.row = next(row for row in payload["entries"] if row["result_id"] == RESULT_ID)
        self.payload = {**payload, "entries": [copy.deepcopy(self.row)]}
        record_path = self.row["record_path"]
        target = self.root / record_path
        target.parent.mkdir(parents=True)
        target.write_bytes((REPO / record_path).read_bytes())
        self.result = {**json.loads(target.read_text(encoding="utf-8")), "_record_path": record_path}
        self.publications = []
        for publication_id in (self.row["publication_id"], self.row["superseding_publication_id"]):
            relative = f"research_task_records/{self.row['task_id']}/{publication_id}.json"
            self.publications.append(json.loads((REPO / relative).read_text(encoding="utf-8")))
        self.write_registry()
        history = mock.patch.object(
            results, "_history_original_iter_results", return_value=[self.result], create=True
        )
        publication_history = mock.patch.object(tasks, "iter_records", return_value=self.publications)
        history.start()
        publication_history.start()
        self.addCleanup(history.stop)
        self.addCleanup(publication_history.stop)

    def write_registry(self):
        (self.root / isolation.QUARANTINE_FILE).write_text(json.dumps(self.payload), encoding="utf-8")

    def errors(self):
        return [f"{self.row['record_path']}: {suffix}" for suffix in self.row["allowed_result_audit_errors"]]

    def test_real_direct_newer_publication_accepts_only_exact_errors(self):
        original = (self.root / self.row["record_path"]).read_bytes()
        self.assertEqual({RESULT_ID}, set(isolation.validated_rows(self.root)))
        self.assertEqual([], isolation.audit_against(self.errors(), self.root))
        self.assertEqual(original, (self.root / self.row["record_path"]).read_bytes())

    def test_new_error_is_not_hidden(self):
        for additional in ("unrelated record: unexpected defect", f"{self.row['record_path']}: return artifact missing"):
            with self.subTest(additional=additional):
                self.assertEqual([additional], isolation.audit_against(self.errors() + [additional], self.root))

    def test_each_missing_registered_error_is_stale(self):
        for omitted in self.errors():
            with self.subTest(omitted=omitted):
                actual = isolation.audit_against([error for error in self.errors() if error != omitted], self.root)
                self.assertEqual(1, len(actual))
                self.assertIn("stale or unused suppression", actual[0])
                self.assertIn(omitted, actual[0])

    def test_drifted_immutable_result_rejects_even_if_id_is_unchanged(self):
        path = self.root / self.row["record_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(isolation.ResultAuditIsolationError, "record blob drift"):
            isolation.validated_rows(self.root)

    def test_other_task_or_indirect_or_nonincreasing_successor_rejects(self):
        cases = [
            ("task_id", "RS-UNRELATED", "lineage task mismatch"),
            ("supersedes_publication_id", "TP2-UNRELATED", "successor is not direct"),
            ("publication_generation", self.publications[0]["publication_generation"], "not newer"),
        ]
        for field, changed, message in cases:
            with self.subTest(field=field):
                original = self.publications[1][field]
                self.publications[1][field] = changed
                try:
                    with self.assertRaisesRegex(isolation.ResultAuditIsolationError, message):
                        isolation.validated_rows(self.root)
                finally:
                    self.publications[1][field] = original

    def test_record_identity_mismatch_is_not_an_audit_waiver(self):
        self.result["publication_id"] = "TP2-UNRELATED"
        with self.assertRaisesRegex(isolation.ResultAuditIsolationError, "result identity mismatch"):
            isolation.validated_rows(self.root)


if __name__ == "__main__":
    unittest.main()
