"""A missing execution relation must not hide independent Result defects."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_execution_record_audit_fault_isolation as legacy
from control_plane import research_result_records_impl as records

REPO = Path(__file__).resolve().parents[1]


class ResultAuditCompletenessTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.artifact_path = "research_returns/checked.md"
        artifact = self.root / self.artifact_path
        artifact.parent.mkdir(parents=True)
        artifact.write_bytes(b"fixed Result artifact\n")
        self.prefix = "research_result_records/RS-CHECK/RR-CHECK.json"
        self.execution = {
            "execution_record_id": "ER-CHECK",
            "task_id": "RS-CHECK",
            "publication_id": "TP-CHECK",
            "claim_id": "CLAIM-CHECK",
            "researcher_id": "EM-CHECK",
            "taskbook_blob_sha1": "sha1:" + "a" * 40,
            "execution_branch": "research/check",
        }
        self.result = {
            **self.execution,
            "record_schema": records.RESULT_SCHEMA,
            "result_id": "RR-CHECK",
            "_record_path": self.prefix,
            "return_path": self.artifact_path,
            "return_blob_sha1": records._blob(artifact),
            "return_sha256": records._sha256(artifact),
            "terminal_verdict": "NEGATIVE_BOUNDARY",
            "method_harvest": "RESULT_ONLY",
            "independence_status": "NOT_INDEPENDENT",
            "source_exposure_status": "NONBLIND_DISCLOSED",
            "hard_target_disposition": "A bounded Result is present.",
            "unresolved_residue": "The parent question remains open.",
            "next_control_plane_recommendation": "Request the authorized review.",
            "output_manifest": [{
                "path": self.artifact_path,
                "git_blob_sha1": records._blob(artifact),
                "sha256": records._sha256(artifact),
            }],
        }

    def errors(self, suffixes):
        return [f"{self.prefix}: {suffix}" for suffix in suffixes]

    def test_valid_known_result_passes_without_mutating_inputs_or_files(self):
        before_result = copy.deepcopy(self.result)
        before_execution = copy.deepcopy(self.execution)
        before_artifact = (self.root / self.artifact_path).read_bytes()
        self.assertEqual([], records.audit_result_record(self.result, self.execution, self.root))
        self.assertEqual(before_result, self.result)
        self.assertEqual(before_execution, self.execution)
        self.assertEqual(before_artifact, (self.root / self.artifact_path).read_bytes())

    def test_missing_execution_is_still_an_error_for_valid_result(self):
        self.assertEqual(
            self.errors(["unknown execution record"]),
            records.audit_result_record(self.result, None, self.root),
        )

    def test_unknown_execution_does_not_hide_independent_metadata_or_outputs(self):
        broken = copy.deepcopy(self.result)
        broken.update({
            "record_schema": "WRONG_SCHEMA",
            "return_path": "missing-return.md",
            "terminal_verdict": "NOT_A_VERDICT",
            "method_harvest": "NOT_A_METHOD_CLASS",
            "independence_status": "NOT_AN_INDEPENDENCE_CLASS",
            "source_exposure_status": "NOT_A_SOURCE_CLASS",
            "hard_target_disposition": "",
            "unresolved_residue": " ",
            "next_control_plane_recommendation": "",
            "output_manifest": [False, {"path": "missing-output.json"}],
        })
        self.assertEqual(
            self.errors([
                "wrong result schema", "unknown execution record", "return artifact missing",
                "invalid terminal_verdict", "invalid method_harvest", "invalid independence_status",
                "invalid source_exposure_status", "hard_target_disposition missing",
                "unresolved_residue missing", "next_control_plane_recommendation missing",
                "invalid output manifest row", "output missing: missing-output.json",
            ]),
            records.audit_result_record(broken, None, self.root),
        )

    def test_unknown_execution_does_not_hide_real_digest_drift(self):
        (self.root / self.artifact_path).write_bytes(b"changed artifact\n")
        self.assertEqual(
            self.errors([
                "unknown execution record", "return artifact blob drift",
                "return artifact SHA-256 drift", f"output digest drift: {self.artifact_path}",
            ]),
            records.audit_result_record(self.result, None, self.root),
        )

    def test_unknown_execution_does_not_hide_absent_output_manifest(self):
        for manifest in (None, [], "not-a-list"):
            with self.subTest(manifest=manifest):
                broken = dict(self.result, output_manifest=manifest)
                self.assertEqual(
                    self.errors(["unknown execution record", "output_manifest missing"]),
                    records.audit_result_record(broken, None, self.root),
                )

    def test_known_execution_preserves_all_linked_field_errors_in_order(self):
        fields = ("task_id", "publication_id", "claim_id", "researcher_id", "taskbook_blob_sha1", "execution_branch")
        broken = dict(self.result, **{field: "CHANGED" for field in fields})
        self.assertEqual(
            self.errors([f"execution-linked field mismatch: {field}" for field in fields]),
            records.audit_result_record(broken, self.execution, self.root),
        )

    def test_known_execution_preserves_lane_presence_and_field_errors(self):
        execution = dict(self.execution, execution_cohort_id="COHORT", execution_lane_id="LANE", lane_output_prefix="lanes/a/")
        self.assertEqual(
            self.errors([
                "lane identity presence differs from execution record",
                "execution-linked lane field mismatch: execution_cohort_id",
                "execution-linked lane field mismatch: execution_lane_id",
                "execution-linked lane field mismatch: lane_output_prefix",
            ]),
            records.audit_result_record(self.result, execution, self.root),
        )
        result = dict(self.result, execution_cohort_id="COHORT", execution_lane_id="LANE", lane_output_prefix="lanes/a/")
        self.assertEqual([], records.audit_result_record(result, execution, self.root))
        self.assertEqual(
            self.errors(["lane identity presence differs from execution record"]),
            records.audit_result_record(result, self.execution, self.root),
        )

    def test_bare_historical_git_blob_identity_comparison_is_preserved(self):
        result = copy.deepcopy(self.result)
        result["return_blob_sha1"] = result["return_blob_sha1"].removeprefix("sha1:")
        result["output_manifest"][0]["git_blob_sha1"] = result["output_manifest"][0]["git_blob_sha1"].removeprefix("sha1:")
        self.assertEqual([], records.audit_result_record(result, self.execution, self.root))

    def test_real_raw_audit_reports_unknown_and_other_defects_without_id_alias(self):
        result = copy.deepcopy(self.result)
        result.pop("_record_path")
        result["method_harvest"] = "INVALID_METHOD_CLASS"
        result_path = self.root / self.prefix
        result_path.parent.mkdir(parents=True)
        result_path.write_text(json.dumps(result), encoding="utf-8")
        execution = dict(self.execution)
        execution["record_id"] = execution.pop("execution_record_id")
        execution_path = self.root / "research_execution_records/RS-CHECK/ER-CHECK.json"
        execution_path.parent.mkdir(parents=True)
        execution_path.write_text(json.dumps(execution), encoding="utf-8")
        (self.root / self.artifact_path).write_bytes(b"changed artifact\n")
        raw_results = records.__dict__.get("_history_original_iter_results", records.iter_results)
        raw_reviews = records.__dict__.get("_history_original_iter_reviews", records.iter_reviews)
        raw_audit = records.__dict__.get("_history_original_audit", records.audit)
        with mock.patch.object(records, "iter_results", raw_results), \
             mock.patch.object(records, "iter_reviews", raw_reviews):
            self.assertEqual({}, records.execution_map(self.root))
            self.assertEqual(
                self.errors([
                    "unknown execution record", "return artifact blob drift", "return artifact SHA-256 drift",
                    "invalid method_harvest", f"output digest drift: {self.artifact_path}",
                ]),
                raw_audit(self.root),
            )
            self.assertEqual({}, records.execution_map(self.root))
        self.assertNotIn("execution_record_id", json.loads(execution_path.read_bytes()))

    def test_exact_legacy_relation_reveals_remaining_checks_without_live_map_alias(self):
        expected = {
            "RR-1337737608BDE3D7E620": ["execution-linked field mismatch: taskbook_blob_sha1", "invalid method_harvest"],
            "RR-65F19B398F4D33FEAE9C": ["execution-linked field mismatch: taskbook_blob_sha1"],
            "RR-4B7576B2FDCA2CCBAB37": ["execution-linked field mismatch: taskbook_blob_sha1"],
        }
        before = records.execution_map(REPO)
        rows = [row for row in legacy.validated_rows(REPO) if row["nonlive_basis"] == legacy.BASIS_LEGACY_RESULT]
        self.assertEqual(set(expected), {row["result_id"] for row in rows})
        for row in rows:
            with self.subTest(result_id=row["result_id"]):
                execution = json.loads((REPO / row["record_path"]).read_bytes())
                result = json.loads((REPO / row["result_record_path"]).read_bytes())
                result["_record_path"] = row["result_record_path"]
                self.assertNotIn(row["execution_record_id"], before)
                self.assertNotIn("execution_record_id", execution)
                self.assertEqual(
                    [f"{row['result_record_path']}: {suffix}" for suffix in expected[row["result_id"]]],
                    records.audit_result_record(result, execution, REPO),
                )
                independent = records.audit_result_record(result, None, REPO)
                self.assertIn(f"{row['result_record_path']}: unknown execution record", independent)
                self.assertNotIn("execution_record_id", execution)
        self.assertEqual(before, records.execution_map(REPO))


if __name__ == "__main__":
    unittest.main()
