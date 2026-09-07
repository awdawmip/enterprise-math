"""Audit-only legacy ER provenance; real temporary files, no live events or writes."""
import copy
import hashlib
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

from control_plane import research_execution_record_audit_fault_isolation as isolation
from control_plane import research_runtime_guard_core as guard

REPO = Path(__file__).resolve().parents[1]


class ExactLegacyExecutionAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        registry = json.loads((REPO / isolation.REGISTRY).read_text(encoding="utf-8"))
        self.row = copy.deepcopy(next(r for r in registry["quarantines"] if r["nonlive_basis"] == isolation.BASIS_LEGACY_RESULT))
        self.registry = {"schema": isolation.SCHEMA, "status": "ACTIVE", "quarantines": [self.row]}
        self.er_path = self.row["record_path"]
        self.rr_path = self.row["result_record_path"]
        self.er = json.loads((REPO / self.er_path).read_text(encoding="utf-8"))
        self.rr = json.loads((REPO / self.rr_path).read_text(encoding="utf-8"))
        publication_path = f"research_task_records/{self.er['task_id']}/{self.er['publication_id']}.json"
        self.publication = json.loads((REPO / publication_path).read_text(encoding="utf-8"))
        for name in (self.er_path, self.rr_path, publication_path, self.publication["taskbook_path"]):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((REPO / name).read_bytes())
        self.save_registry()

    def write_json(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def save_registry(self):
        self.write_json(isolation.REGISTRY, self.registry)

    def repin_result(self, result):
        self.write_json(self.rr_path, result)
        self.row["result_record_blob_sha1"] = isolation.record_core.git_blob_sha1_bytes((self.root / self.rr_path).read_bytes())
        self.save_registry()

    def repin_pair(self, execution):
        self.write_json(self.er_path, execution)
        raw = (self.root / self.er_path).read_bytes()
        self.row["record_blob_sha1"] = isolation.record_core.git_blob_sha1_bytes(raw)
        result = copy.deepcopy(self.rr)
        for field in ("task_id", "publication_id", "claim_id", "researcher_id", "execution_branch", "execution_branch_base"):
            result[field] = execution[field]
        entry = next(x for x in result["output_manifest"] if x["path"] == self.er_path)
        entry["git_blob_sha1"] = self.row["record_blob_sha1"]
        entry["sha256"] = "sha256:" + hashlib.sha256(raw).hexdigest()
        self.repin_result(result)

    def test_exact_legacy_binding_suppresses_only_original_four_errors(self):
        raw = isolation.research_execution_records.audit(self.root)
        self.assertEqual(4, len(raw))
        self.assertTrue(any("missing execution_record_id" in e for e in raw))
        self.assertEqual([], isolation.audit(self.root))

    def test_canonical_identity_is_not_inferred_from_filename(self):
        self.row["execution_record_id"] = "ER-FILENAME-IS-NOT-AUTHORITY"
        self.save_registry()
        with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "literal legacy record_id mismatch"):
            isolation.validated_rows(self.root)

    def test_old_basis_does_not_gain_a_record_id_alias(self):
        self.row["nonlive_basis"] = isolation.BASIS_RESULT
        self.save_registry()
        with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "unknown execution_record_id"):
            isolation.validated_rows(self.root)

    def test_canonical_execution_id_must_be_truly_absent(self):
        for value in (None, self.row["execution_record_id"]):
            with self.subTest(value=value):
                execution = dict(self.er, execution_record_id=value)
                self.repin_pair(execution)
                with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "to be absent"):
                    isolation.validated_rows(self.root)

    def test_record_and_result_byte_drift_are_rejected(self):
        for path in (self.er_path, self.rr_path):
            target = self.root / path
            original = target.read_bytes()
            target.write_bytes(original + b" ")
            with self.subTest(path=path), self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "source blob drift"):
                isolation.validated_rows(self.root)
            target.write_bytes(original)

    def test_every_result_execution_identity_binding_is_checked(self):
        for field in ("task_id", "publication_id", "claim_id", "researcher_id", "execution_branch", "execution_branch_base", "execution_record_id"):
            result = dict(self.rr, **{field: "CHANGED"})
            self.repin_result(result)
            with self.subTest(field=field), self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "binding mismatch"):
                isolation.validated_rows(self.root)

    def test_frozen_and_terminal_evidence_is_required(self):
        for field in ("frozen_at", "terminal_verdict"):
            self.repin_result(dict(self.rr, **{field: ""}))
            with self.subTest(field=field), self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "lacks"):
                isolation.validated_rows(self.root)
        self.repin_result(dict(self.rr, terminal_verdict="DIFFERENT"))
        with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "terminal verdict differs"):
            isolation.validated_rows(self.root)

    def test_manifest_path_blob_duplicate_and_sha256_cannot_mismatch(self):
        for mutation in ("path", "blob", "duplicate", "sha256"):
            result = copy.deepcopy(self.rr)
            item = next(x for x in result["output_manifest"] if x["path"] == self.er_path)
            if mutation == "path":
                item["path"] += ".other"
            elif mutation == "blob":
                item["git_blob_sha1"] = "sha1:" + "0" * 40
            elif mutation == "duplicate":
                result["output_manifest"].append(dict(item, git_blob_sha1="sha1:" + "0" * 40))
            else:
                item["sha256"] = "sha256:" + "0" * 64
            self.repin_result(result)
            with self.subTest(mutation=mutation), self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "manifest"):
                isolation.validated_rows(self.root)

    def test_no_authority_flag_or_external_source_path_is_accepted(self):
        self.row["runtime_authority_granted"] = True
        self.save_registry()
        with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "cannot grant"):
            isolation.validated_rows(self.root)
        self.row["runtime_authority_granted"] = False
        self.row["result_record_path"] = "../outside.json"
        self.save_registry()
        with self.assertRaisesRegex(isolation.ExecutionAuditIsolationError, "escapes"):
            isolation.validated_rows(self.root)

    def test_stale_missing_and_extra_errors_remain_failures(self):
        original = list(self.row["allowed_execution_record_audit_errors"])
        self.row["allowed_execution_record_audit_errors"] = original + ["unobserved error"]
        self.save_registry()
        self.assertTrue(any("stale or unused suppression" in e for e in isolation.audit(self.root)))
        self.row["allowed_execution_record_audit_errors"] = original[1:]
        self.save_registry()
        self.assertTrue(any("missing execution_record_id" in e for e in isolation.audit(self.root)))
        self.row["allowed_execution_record_audit_errors"] = original
        self.repin_pair(dict(self.er, execution_branch_base="INVALID"))
        errors = isolation.audit(self.root)
        self.assertTrue(any("execution_branch_base invalid" in e for e in errors))

    def test_audit_registration_does_not_normalize_lookup_or_runtime_binding(self):
        arguments = (self.er["task_id"], self.er["claim_id"], self.root)
        before = isolation.research_execution_records.intent_for_claim(*arguments)
        self.assertNotIn("execution_record_id", before)
        self.assertNotIn("allowed_outputs", before)
        self.assertEqual([], isolation.audit(self.root))
        after = isolation.research_execution_records.intent_for_claim(*arguments)
        self.assertEqual(before, after)
        claim = {"event": "CLAIM", "task_id": self.er["task_id"], "claim_id": self.er["claim_id"]}
        # Hypothetical accepted winning-claim prefix; no actual Issue event is
        # asserted or emitted. The unchanged real guard must still reject the
        # historical payload's missing taskbook pin, before any output scope.
        reduced = {"dispatch_state": "LEASED", "claim_id": self.er["claim_id"], "researcher_id": self.er["researcher_id"], "ignored_events": []}
        with mock.patch.object(guard, "_registered_definition", return_value=self.publication), \
             mock.patch.object(guard.research_dispatch, "_event_authentication_filter", return_value=([claim], [])), \
             mock.patch.object(guard.research_dispatch, "_filter_registered_events", return_value=([claim], [])), \
             mock.patch.object(guard.research_runtime_reducer, "reduce_task", return_value=reduced):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "taskbook pin is stale"):
                guard.canonical_live_claim_binding(self.er["task_id"], [claim], now=datetime(2026, 9, 7, tzinfo=timezone.utc), root=self.root)


if __name__ == "__main__":
    unittest.main()
