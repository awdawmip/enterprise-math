"""A misplaced frozen payload can withhold authority without creating identity."""
from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_authority_fault_isolation as isolation
from control_plane import research_result_records_impl as impl
from tools import research_result_records as results
from test_research_task_record_compatibility import _write_semantic_fixture

ROOT = Path(__file__).resolve().parents[1]
RID = "RR-F97259D79B7E7EF3F69F"


def setUpModule():
    bootstrap.install(ROOT)


class FlatFrozenResultAuthorityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.row = copy.deepcopy(isolation.quarantine_rows(ROOT)[RID])
        for pin in self.row["dependency_pins"]:
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / pin["path"], destination)
        _write_semantic_fixture(self.root)
        self.save_registry()
        self.before = {pin["path"]: (self.root / pin["path"]).read_bytes()
                       for pin in self.row["dependency_pins"]}

    def save_registry(self):
        (self.root / isolation.QUARANTINE_FILE).write_text(json.dumps({
            "schema": isolation.SCHEMA, "status": "ACTIVE", "entries": [self.row],
        }, indent=2) + "\n", encoding="utf-8")

    def load(self, path):
        return json.loads((self.root / path).read_bytes())

    def repin(self, path, value, primary_field):
        raw = (json.dumps(value, indent=2) + "\n").encode()
        (self.root / path).write_bytes(raw)
        blob, sha = isolation._digests(raw)
        self.row[primary_field] = blob
        for pin in self.row["dependency_pins"]:
            if pin["path"] == path:
                pin.update(git_blob_sha1=blob, sha256=sha)
        self.save_registry()

    def test_withholding_does_not_index_execution_or_create_terminal_result(self):
        self.assertIn(RID, isolation.validated_rows(self.root))
        self.assertNotIn(self.row["execution_record_id"], impl.execution_map(self.root))
        self.assertEqual([], results.iter_results(self.root))
        self.assertEqual([], results.iter_reviews(self.root))
        state = results.task_result_state(self.row["task_id"], self.root, self.row["publication_id"])
        self.assertEqual(isolation.STATE, state["state"])
        self.assertFalse(state["terminal"])
        self.assertIsNone(state["result"])
        self.assertIsNone(state["review"])
        self.assertEqual(self.before, {p: (self.root / p).read_bytes() for p in self.before})

    def test_new_canonical_alias_invalidates_the_flat_basis(self):
        path = self.root / "research_execution_records" / self.row["task_id"] / (self.row["execution_record_id"] + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((self.root / self.row["execution_record_path"]).read_bytes())
        with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "remain absent from canonical map"):
            isolation.validated_rows(self.root)

    def test_frozen_manifest_must_bind_both_original_execution_digests(self):
        original = self.load(self.row["record_path"])
        for mutation in ("remove", "duplicate", "blob", "sha256"):
            with self.subTest(mutation=mutation):
                value = copy.deepcopy(original)
                rows = value["output_manifest"]
                item = next(row for row in rows if row["path"] == self.row["execution_record_path"])
                if mutation == "remove":
                    rows.remove(item)
                elif mutation == "duplicate":
                    rows.append(copy.deepcopy(item))
                elif mutation == "blob":
                    item["git_blob_sha1"] = "sha1:" + "0" * 40
                else:
                    item["sha256"] = "sha256:" + "0" * 64
                self.repin(self.row["record_path"], value, "record_blob_sha1")
                with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "frozen manifest lacks exact flat execution bytes"):
                    isolation.validated_rows(self.root)

    def test_flat_path_and_execution_identity_cannot_be_general_aliases(self):
        original = copy.deepcopy(self.row)
        self.row["execution_record_path"] = "research_execution_records/other.json"
        self.save_registry()
        with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "execution_record_path identity mismatch"):
            isolation.validated_rows(self.root)
        self.row = original
        self.save_registry()
        execution = self.load(self.row["execution_record_path"])
        execution["execution_record_id"] = "ER-OTHER"
        self.repin(self.row["execution_record_path"], execution, "execution_record_blob_sha1")
        with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "identity/schema mismatch"):
            isolation.validated_rows(self.root)

    def test_exact_raw_errors_and_bound_diagnostics_remain_separate(self):
        self.assertIn("unknown execution record", self.row["allowed_result_audit_errors"])
        self.assertNotIn("unknown execution record", self.row["bound_legacy_diagnostic_errors"])
        for field in ("allowed_result_audit_errors", "bound_legacy_diagnostic_errors"):
            original = list(self.row[field])
            self.row[field] = original[:-1]
            self.save_registry()
            with self.assertRaisesRegex(isolation.ResultAuthorityIsolationError, "error set drift|diagnostic set drift"):
                isolation.validated_rows(self.root)
            self.row[field] = original
            self.save_registry()


if __name__ == "__main__":
    unittest.main()
