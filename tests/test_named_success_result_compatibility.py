"""A declared historical success spelling is not a new completion authority."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from tools import research_result_records as records
from control_plane import research_result_records_compat_runtime as compatibility
import research_driver_followup as followup

REPO = Path(__file__).resolve().parents[1]
RID = "RR-566554389F6F36576DE2"
TASK = "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION"
PID = "TP2-ADD82532ACD19FC01D53"
NAME = "R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED"


class NamedSuccessCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        config = json.loads((REPO / compatibility.COMPATIBILITY_FILE).read_bytes())
        self.row = copy.deepcopy(next(r for r in config["result_normalizations"] if r["result_id"] == RID))
        self.witness = self.row["hard_target_success_witness"]
        self.paths = [self.row["record_path"], self.witness["publication_record_path"], self.witness["taskbook_path"]]
        self.before = {p: (REPO / p).read_bytes() for p in self.paths}
        for relative, raw in self.before.items():
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        self.item = json.loads(self.before[self.row["record_path"]])
        self.item["_record_path"] = self.row["record_path"]

    def normalize(self, item=None, row=None):
        return records._normalize_result_item(item or self.item, row or self.row, self.root)

    def rewrite_result_for_negative_probe(self, changes):
        raw = json.loads(self.before[self.row["record_path"]])
        raw.update(changes)
        path = self.root / self.row["record_path"]
        path.write_text(json.dumps(raw) + "\n", encoding="utf-8")
        row = copy.deepcopy(self.row)
        row["record_blob_sha1"] = compatibility._impl._blob(path)
        return {**raw, "_record_path": self.row["record_path"]}, row

    def completed_scope_inputs(self):
        review = {"disposition": "ACCEPTED", "result_id": RID, "task_id": TASK, "publication_id": PID}
        continuation = {
            "source_result_id": RID,
            "parent_objective_id": "OBJ-R005-PRIME-ALGORITHM-LAB",
            "action": "REEVALUATE_CANONICAL_PORTFOLIO",
            "dispatcher": "research_control_dispatch.py",
            "next_action": "Reevaluate the registered R005 relay assets without new mathematical work.",
            "remaining_parent_scope": ["The exact-916 catalogue and seam remain open."],
            "evidence_refs": [self.item["return_path"]],
        }
        names = json.loads((REPO / "research_driver_followup_contract.json").read_bytes())["canonical_gates"]
        gates = {name: {"decision": "SATISFIED_BY_REVIEWED_RESULT"} for name in names}
        return review, continuation, gates

    def test_exact_source_spelling_normalizes_without_mutation_or_grants(self):
        normalized = self.normalize()
        self.assertEqual("SATISFIED", normalized["hard_target_disposition"])
        self.assertEqual(NAME, self.item["hard_target_disposition"])
        expected = copy.deepcopy(self.item)
        expected["hard_target_disposition"] = "SATISFIED"
        self.assertEqual(expected, normalized)
        for path, raw in self.before.items():
            self.assertEqual(raw, (self.root / path).read_bytes())

    def test_missing_or_unsupported_witness_is_rejected(self):
        for field in self.witness:
            row = copy.deepcopy(self.row)
            del row["hard_target_success_witness"][field]
            with self.subTest(field=field), self.assertRaises(records.ResultRecordError):
                self.normalize(row=row)
        row = copy.deepcopy(self.row)
        row["hard_target_success_witness"]["working_truth_granted"] = True
        with self.assertRaises(records.ResultRecordError):
            self.normalize(row=row)

    def test_record_publication_and_book_byte_drift_fail_closed(self):
        for path in self.paths:
            with self.subTest(path=path):
                target = self.root / path
                target.write_bytes(self.before[path] + b"\n")
                with self.assertRaisesRegex(records.ResultRecordError, "blob drift"):
                    self.normalize()
                target.write_bytes(self.before[path])

    def test_identity_and_witness_pins_are_exact(self):
        for field in ("task_id", "publication_id", "publication_record_path", "publication_record_blob_sha1",
                      "taskbook_path", "taskbook_blob_sha1", "declared_success_line"):
            row = copy.deepcopy(self.row)
            row["hard_target_success_witness"][field] += "_OTHER"
            with self.subTest(field=field), self.assertRaises(records.ResultRecordError):
                self.normalize(row=row)
        row = copy.deepcopy(self.row)
        row["result_id"] = "RR-ANOTHER"
        with self.assertRaisesRegex(records.ResultRecordError, "identity mismatch"):
            self.normalize(row=row)

    def test_no_success_from_a_changed_view_or_original_nonpass(self):
        for field in ("result_id", "task_id", "publication_id", "terminal_verdict", "hard_target_disposition"):
            item = copy.deepcopy(self.item)
            item[field] = "CHANGED"
            with self.subTest(field=field), self.assertRaises(records.ResultRecordError):
                self.normalize(item=item)
        for verdict in ("INCOMPLETE", "NEGATIVE_BOUNDARY", "NO_GO"):
            item, row = self.rewrite_result_for_negative_probe({"terminal_verdict": verdict})
            with self.subTest(verdict=verdict), self.assertRaisesRegex(records.ResultRecordError, "original PASS/SUCCESS"):
                self.normalize(item, row)

    def test_generic_or_negative_outcomes_cannot_be_aliased_to_satisfied(self):
        for value in ("SATISFIED", "PASS", "SUCCESS", "PARTIAL", "INCOMPLETE", "NOT_SATISFIED", "NO_GO"):
            item, row = self.rewrite_result_for_negative_probe({"hard_target_disposition": value})
            row["field_aliases"][0]["from"] = value
            with self.subTest(value=value), self.assertRaisesRegex(records.ResultRecordError, "named task success"):
                self.normalize(item, row)

    def test_an_arbitrary_positive_tag_or_wrong_target_is_not_enough(self):
        item, row = self.rewrite_result_for_negative_probe({"hard_target_disposition": "R005_LOOKS_COMPLETE"})
        row["field_aliases"][0]["from"] = "R005_LOOKS_COMPLETE"
        with self.assertRaisesRegex(records.ResultRecordError, "frozen hard target and success declaration"):
            self.normalize(item, row)
        row = copy.deepcopy(self.row)
        row["field_aliases"][0]["to"] = "PASS"
        with self.assertRaises(records.ResultRecordError):
            self.normalize(row=row)

    def test_stale_or_duplicate_special_alias_is_not_ignored(self):
        row = copy.deepcopy(self.row)
        row["field_aliases"] = []
        with self.assertRaisesRegex(records.ResultRecordError, "witness requires"):
            self.normalize(row=row)
        row = copy.deepcopy(self.row)
        row["field_aliases"] *= 2
        with self.assertRaisesRegex(records.ResultRecordError, "exactly one"):
            self.normalize(row=row)

    def test_raw_result_stays_blocked_until_explicit_normalization(self):
        review, continuation, gates = self.completed_scope_inputs()
        args = dict(terminal_scope="TASK", continuation=continuation, tasks=[], gates=gates,
                    root=self.root, current_publication_required=True)
        with self.assertRaisesRegex(followup.DriverFollowupError, "hard_target_disposition SATISFIED"):
            followup._task_scope_continuation(review, self.item, **args)
        self.assertEqual(continuation, followup._task_scope_continuation(review, self.normalize(), **args))

    def test_normalization_cannot_replace_review_scope_or_followup_gates(self):
        normalized = self.normalize()
        review, continuation, gates = self.completed_scope_inputs()
        args = dict(terminal_scope="TASK", continuation=continuation, tasks=[], gates=gates, root=self.root)
        with self.assertRaisesRegex(followup.DriverFollowupError, "ACCEPTED"):
            followup._task_scope_continuation({**review, "disposition": "REQUEST_REVISION"}, normalized, **args)
        with self.assertRaisesRegex(followup.DriverFollowupError, "terminal_scope TASK"):
            followup._task_scope_continuation(review, normalized, **{**args, "terminal_scope": "PARENT"})
        required = copy.deepcopy(gates)
        next(iter(required.values()))["decision"] = "REQUIRED"
        with self.assertRaisesRegex(followup.DriverFollowupError, "REQUIRED"):
            followup._task_scope_continuation(review, normalized, **{**args, "gates": required})
        with self.assertRaisesRegex(followup.DriverFollowupError, "cannot publish new tasks"):
            followup._task_scope_continuation(review, normalized, **{**args, "tasks": [{}]})

    def test_review_binding_remains_the_original_raw_record_digest(self):
        result = self.normalize()
        review, _, _ = self.completed_scope_inputs()
        digest = "sha256:" + hashlib.sha256(self.before[self.row["record_path"]]).hexdigest()
        review.update(result_record_path=self.row["record_path"], result_record_sha256=digest)
        self.assertEqual((self.row["record_path"], digest), followup._result_record_pin(review, result, self.root))
        review["result_record_sha256"] = "sha256:" + "0" * 64
        with self.assertRaisesRegex(followup.DriverFollowupError, "current Result bytes"):
            followup._result_record_pin(review, result, self.root)


if __name__ == "__main__":
    unittest.main()
