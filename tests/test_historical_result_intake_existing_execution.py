"""Pinned Q24 provenance only: no scientific replay or recovered historical authority."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock

from control_plane import research_historical_result_intake as h
from control_plane import research_result_records_impl as impl

REPO = Path(__file__).resolve().parents[1]
Q24 = "RR-1DE3F3213271AED2625C"
ENUM_ERRORS = ["invalid method_harvest", "invalid independence_status", "invalid source_exposure_status"]


class ExistingCanonicalExecutionEvidenceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.contract = json.loads((REPO / h.CONTRACT).read_text())
        self.target = next(t for t in self.contract["targets"] if t["historical_result_id"] == Q24)
        self.copy_target(self.target)
        self.write(h.CONTRACT, self.contract)
        self.old = self.read(self.target["result_pin"]["path"])
        self.er = self.read(self.target["execution_pin"]["path"])
        self.pub = self.read(self.target["publication_pin"]["path"])

    def copy_target(self, target):
        old = json.loads((REPO / target["result_pin"]["path"]).read_text())
        paths = {target[k]["path"] for k in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin")}
        paths.update(row["path"] for row in old["output_manifest"])
        for rel in paths:
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / rel, path)

    def read(self, rel):
        return json.loads((self.root / rel).read_text())

    def write(self, rel, value):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value) + "\n")

    def inventory(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def evidence(self, *, target=None, er=None, old=None, pub=None):
        return h._execution_evidence(self.root, self.target if target is None else target,
                                    self.old if old is None else old, self.er if er is None else er,
                                    self.pub if pub is None else pub)

    def test_actual_q24_science_uses_exact_existing_er_without_normalization_or_writes(self):
        before = self.inventory()
        target = h._target(self.root, self.target["task_id"], self.target["publication_id"], Q24)
        old, outputs = h._science(self.root, target)
        self.assertEqual(old, self.old)
        self.assertEqual(len(outputs), 4)
        self.assertEqual(impl.execution_map(self.root)[old["execution_record_id"]],
                         {**self.er, "_record_path": target["execution_pin"]["path"]})
        self.assertEqual({e.split(": ", 1)[-1] for e in impl.audit_result_record(old, self.er, self.root)}, set(ENUM_ERRORS))
        self.assertEqual(target["historical_authentication_status"], "UNKNOWN_NO_RECOVERED_AUTHENTICATED_SERVER_ENVELOPES")
        self.assertEqual(self.inventory(), before)
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())
        self.assertFalse((self.root / h.REVIEW_ROOT).exists())

    def test_no_profile_still_rejects_canonical_er_and_no_target_is_not_admitted(self):
        target = copy.deepcopy(self.target)
        target.pop("historical_execution_evidence")
        with self.assertRaisesRegex(h.HistoricalIntakeError, "cannot be imported or aliased"):
            h._science(self.root, target)
        self.contract["targets"].remove(self.target)
        self.write(h.CONTRACT, self.contract)
        with self.assertRaisesRegex(h.HistoricalIntakeError, "no exact Source-approved intake scope"):
            h._target(self.root, target["task_id"], target["publication_id"], Q24)

    def test_missing_field_profile_cannot_describe_this_existing_canonical_er(self):
        legacy = next(t for t in self.contract["targets"] if t["historical_result_id"] == "RR-65F19B398F4D33FEAE9C")
        target = copy.deepcopy(self.target)
        target["historical_execution_evidence"] = legacy["historical_execution_evidence"]
        with self.assertRaisesRegex(h.HistoricalIntakeError, "exact missing execution fields"):
            h._science(self.root, target)

    def test_closed_profile_rejects_unknown_schema_fields_and_changed_binding(self):
        changes = [("schema", "OTHER"), ("historical_identifier_field", "record_id"),
                   ("required_fields", ["execution_record_id"]), ("execution_map_binding", "ANY_RECORD"),
                   ("taskbook_binding_basis", "INFER_FROM_NAME"), ("extra", True)]
        for field, value in changes:
            target = copy.deepcopy(self.target)
            target["historical_execution_evidence"][field] = value
            with self.subTest(field=field), self.assertRaises(h.HistoricalIntakeError):
                self.evidence(target=target)

    def test_authentication_and_alias_flags_require_literal_false(self):
        for field in ("execution_authentication_restored", "canonical_execution_alias_created"):
            for value in (True, 0):
                target = copy.deepcopy(self.target)
                target["historical_execution_evidence"][field] = value
                with self.subTest(field=field, value=value), self.assertRaises(h.HistoricalIntakeError):
                    self.evidence(target=target)
        target = copy.deepcopy(self.target)
        target["historical_authentication_status"] = "AUTHENTICATED"
        with self.assertRaisesRegex(h.HistoricalIntakeError, "cannot restore historical authentication"):
            self.evidence(target=target)

    def test_no_extra_missing_or_duplicate_allowed_fault(self):
        for errors in (ENUM_ERRORS + ["unknown execution record"], ENUM_ERRORS[:-1], ENUM_ERRORS + [ENUM_ERRORS[0]]):
            target = copy.deepcopy(self.target)
            target["allowed_ordinary_audit_errors"] = errors
            with self.subTest(errors=errors), self.assertRaisesRegex(h.HistoricalIntakeError, "only the three exact"):
                h._science(self.root, target)

    def test_wrong_pin_or_scientific_output_drift_is_rejected_before_write(self):
        for field in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin"):
            target = copy.deepcopy(self.target)
            target[field]["sha256"] = "0" * 64
            with self.subTest(field=field), self.assertRaisesRegex(h.HistoricalIntakeError, "byte drift"):
                h._science(self.root, target)
        path = self.root / self.old["return_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(h.HistoricalIntakeError, "byte drift"):
            h._science(self.root, self.target)
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())

    def test_original_er_schema_id_and_required_fields_are_not_inferred(self):
        for field, value in (("record_schema", "OTHER"), ("execution_record_id", "ER-OTHER"),
                             ("taskbook_blob_sha1", ""), ("_record_path", self.target["execution_pin"]["path"]),
                             ("execution_branch_base", "a" * 40)):
            with self.subTest(field=field), self.assertRaises(h.HistoricalIntakeError):
                self.evidence(er={**self.er, field: value})
        for field in ("execution_record_id", "taskbook_blob_sha1"):
            er = copy.deepcopy(self.er)
            er.pop(field)
            with self.subTest(missing=field), self.assertRaises(h.HistoricalIntakeError):
                self.evidence(er=er)

    def test_all_three_taskbook_paths_and_blobs_are_exact(self):
        for which in ("er", "old", "pub"):
            original = getattr(self, which)
            for field, value in (("taskbook_path", "research_tasks/other.md"), ("taskbook_blob_sha1", "sha1:" + "a" * 40)):
                with self.subTest(which=which, field=field), self.assertRaises(h.HistoricalIntakeError):
                    self.evidence(**{which: {**original, field: value}})

    def test_missing_map_entry_wrong_path_and_content_cannot_be_substituted(self):
        exact = {**self.er, "_record_path": self.target["execution_pin"]["path"]}
        cases = [({}, "absent from execution map"),
                 ({self.old["execution_record_id"]: {**exact, "_record_path": "research_execution_records/other.json"}}, "path mismatch"),
                 ({self.old["execution_record_id"]: {**exact, "researcher_id": "EM-OTHER"}}, "content mismatch"),
                 ({self.old["execution_record_id"]: {**exact, "_unexpected_provider_metadata": True}}, "content mismatch")]
        for records, message in cases:
            with self.subTest(message=message), mock.patch.object(impl, "execution_map", return_value=records):
                with self.assertRaisesRegex(h.HistoricalIntakeError, message):
                    h._science(self.root, self.target)

    def test_actual_duplicate_map_id_is_rejected_without_selecting_a_winner(self):
        self.write("research_execution_records/RS-OTHER/duplicate.json", self.er)
        with self.assertRaisesRegex(impl.ResultRecordError, "duplicate execution_record_id"):
            h._science(self.root, self.target)

    def test_new_actual_audit_fault_or_changed_old_diagnosis_is_rejected(self):
        for field, value in (("unresolved_residue", ""), ("method_harvest", "RESULT_ONLY")):
            old = {**self.old, field: value}
            self.write(self.target["result_pin"]["path"], old)
            target = copy.deepcopy(self.target)
            target["result_pin"] = h.pin(self.root, self.target["result_pin"]["path"])
            with self.subTest(field=field), self.assertRaisesRegex(h.HistoricalIntakeError, "unapproved failure or changed diagnosis"):
                h._science(self.root, target)

    def test_claim_author_branch_and_publication_binding_remain_strict(self):
        for field, value in (("task_id", "RS-OTHER"), ("publication_id", "TP2-OTHER"),
                             ("claim_id", "other"), ("researcher_id", "EM-OTHER"), ("execution_branch", "research/other")):
            self.write(self.target["execution_pin"]["path"], {**self.er, field: value})
            target = copy.deepcopy(self.target)
            target["execution_pin"] = h.pin(self.root, self.target["execution_pin"]["path"])
            with self.subTest(field=field), self.assertRaisesRegex(h.HistoricalIntakeError, "historical publication scope mismatch|historical execution-linked field mismatch"):
                h._science(self.root, target)

    def test_existing_three_targets_still_audit_with_no_canonical_alias(self):
        for target in self.contract["targets"]:
            if target["historical_result_id"] == Q24:
                continue
            self.copy_target(target)
            with self.subTest(result=target["historical_result_id"]):
                old, outputs = h._science(self.root, target)
                self.assertEqual(old, self.read(target["result_pin"]["path"]))
                self.assertEqual(len(outputs), len(old["output_manifest"]))
                self.assertNotIn(old["execution_record_id"], impl.execution_map(self.root))


if __name__ == "__main__":
    unittest.main()
