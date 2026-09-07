"""Owner-directed isolation of six current, invalid X6 publications.

These tests do not declare the publications historically nonoperational and do
not supply replacement research semantics. Mutation probes are in memory or in
temporary fixtures; immutable repository publications are never rewritten.
"""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest import mock

from control_plane import check_post_cutover_publication_envelope as envelope
from control_plane import research_control_bootstrap
from control_plane import research_task_integrity_fault_isolation as isolation
from control_plane import research_task_records_impl as record_core


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "RS-X6-CELL-CHANNEL-INTERNAL-STATE": "TP2-B5E2097A3C6418DF42E5",
    "RS-X6-NATIVE-ROTATION-DYNAMICS": "TP2-6A1F9D8C2047E3B51C01",
    "RS-X6-NATIVE-TIME-DYNAMICS": "TP2-91D4A7C2F63805BE21A3",
    "RS-X6-NONFCC-SLICE-REALIZATION": "TP2-A3C8E1D754209B6F31D4",
    "RS-X6-TRIADIC-CLOSURE-DYNAMICS": "TP2-8B7E13C5904A2D6F1142",
    "RS-X6-UPPER-STRUCTURE-INTEGRATION": "TP2-C7F31A8D520B49E653F6",
}
ERRORS = [
    "mandatory body section is missing or empty: " + section
    for section in (
        "Frozen inputs and scope",
        "Hard target and required outputs",
        "Research value to preserve",
        "Success, kill, and return criteria",
    )
]


@contextmanager
def without_new_rows():
    """Reconstruct the previous manifest view without changing disk bytes."""
    base = isolation.quarantine_rows

    def previous(root=ROOT):
        return {key: row for key, row in base(root).items() if key not in EXPECTED}

    with mock.patch.object(isolation, "quarantine_rows", side_effect=previous):
        yield


class X6CurrentPublicationIntegrityIsolationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        research_control_bootstrap.install(ROOT)

    def test_six_exact_records_and_four_actual_errors_are_pinned(self):
        rows = isolation.validated_quarantines(ROOT)
        for task_id, publication_id in EXPECTED.items():
            with self.subTest(task_id=task_id):
                row = rows[task_id]
                self.assertEqual(publication_id, row["publication_id"])
                self.assertEqual(ERRORS, row["allowed_task_record_audit_errors"])
                body = (ROOT / row["taskbook_path"]).read_text(encoding="utf-8")
                self.assertEqual(ERRORS, record_core.validate_body(body))
                self.assertIsNone(row["operational_publication_id"])
                for flag in (
                    "working_truth_granted", "foundation_authority_granted",
                    "canonical_promotion_granted", "successor_triggered",
                ):
                    self.assertIs(row[flag], False)

    def test_only_the_six_current_definitions_change_and_are_blocked(self):
        from tools import research_dispatch, research_task_records
        from tools import research_runtime_reducer as reducer

        with without_new_rows():
            before_current = research_task_records.current_records(ROOT)
            before = {item["task_id"]: item for item in research_dispatch.merged_definitions(ROOT)}
        after_current = research_task_records.current_records(ROOT)
        after = {item["task_id"]: item for item in research_dispatch.merged_definitions(ROOT)}
        self.assertEqual(set(EXPECTED), set(before_current) - set(after_current))
        self.assertEqual({k: v for k, v in before_current.items() if k not in EXPECTED}, after_current)
        self.assertEqual(set(before), set(after))
        self.assertEqual(
            {k: v for k, v in before.items() if k not in EXPECTED},
            {k: v for k, v in after.items() if k not in EXPECTED},
        )
        for task_id, publication_id in EXPECTED.items():
            with self.subTest(task_id=task_id):
                self.assertEqual("READY", before[task_id]["base_state"])
                item = after[task_id]
                self.assertEqual("BLOCKED", item["base_state"])
                self.assertIsNone(item["publication_id"])
                self.assertEqual([publication_id], item["publication_ids"])
                self.assertEqual("TASK_INTEGRITY_QUARANTINE", item["registration_source"])
                # This is a projection probe, not a claim about live Issue events.
                state = research_dispatch.reduce_definition(
                    item, [], now=reducer.parse_time("2026-09-07T08:20:00Z"), root=ROOT,
                )
                self.assertEqual("BLOCKED", state["state"])
                self.assertIsNone(state["publication_id"])
                self.assertIsNone(state["claim_id"])

    def test_unrelated_authenticated_claim_keeps_its_winner(self):
        from tools import research_dispatch as dispatch
        from tools import research_runtime_reducer as reducer

        definition = {
            "task_id": "RS-OWNER-ISOLATION-SIMULATION", "title": "Fixture only",
            "kind": "RESEARCH", "owner": "taskbook/unassigned", "base_state": "READY",
            "priority": "P2", "leverage": "MEDIUM", "frontier": "fixture",
            "next_action": "continue", "dependencies": [], "source_refs": [],
            "last_progress_at": "2026-09-07T08:00:00Z", "hard_block": None,
            "claim_lease_minutes": 120, "identity_lane": "SIM",
            "publication_id": "TP2-OWNER-ISOLATION-SIMULATION",
            "registration_source": "IMMUTABLE_TASK_RECORD",
        }
        payload = {
            "schema": reducer.EVENT_SCHEMA, "event": "CLAIM",
            "task_id": definition["task_id"], "publication_id": definition["publication_id"],
            "claim_id": "owner-isolation-fixture-claim", "theorem_owner": "fixture",
            "execution_branch": "research/owner-isolation-fixture",
            "execution_branch_base": "1" * 40, "allowed_outputs": ["tests/fixture.txt"],
            "lease_minutes": 120,
        }
        event = dispatch.github_comment_event({
            "id": 900001, "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
            "user": {"login": "awdawmip", "id": 30957095},
            "author_association": "OWNER",
            "created_at": "2026-09-07T08:00:00Z", "updated_at": "2026-09-07T08:00:00Z",
            "body": json.dumps(payload),
        }, root=ROOT)
        self.assertTrue(event[dispatch.GITHUB_META_KEY]["control_authorized"])
        # Freeze only the unrelated fixture's absent lifecycle records. The real
        # parser, authorization filter, publication binding and reducer execute.
        with (
            mock.patch.object(dispatch.research_result_records, "task_result_state", return_value=None),
            mock.patch.object(dispatch.research_execution_records, "intent_for_claim", return_value=None),
            mock.patch.object(dispatch.research_cohort_runtime, "task_active_cohort_state", return_value=None),
        ):
            def run():
                return dispatch.reduce_definition(
                    definition, [event], now=reducer.parse_time("2026-09-07T08:01:00Z"), root=ROOT,
                )
            with without_new_rows():
                before = run()
            after = run()
        self.assertEqual(before, after)
        self.assertEqual("CLAIMED", after["state"])
        self.assertEqual(payload["claim_id"], after["claim_id"])
        self.assertEqual("LEASED", after["dispatch_state"])

    def test_twenty_four_errors_require_the_new_validated_isolation(self):
        rows = isolation.validated_quarantines(ROOT)
        expected = {f"{rows[task]['record_path']}: {error}" for task in EXPECTED for error in ERRORS}
        with without_new_rows():
            self.assertEqual(expected, set(envelope.audit(ROOT)))
        self.assertEqual([], envelope.audit(ROOT))
        self.assertTrue(expected <= isolation.suppression_strings(ROOT))

    def test_record_and_taskbook_pin_drift_fail_closed(self):
        for field in ("record_blob_sha1", "taskbook_blob_sha1"):
            with self.subTest(field=field):
                rows = copy.deepcopy(isolation.quarantine_rows(ROOT))
                rows[next(iter(EXPECTED))][field] = "sha1:" + "0" * 40
                with mock.patch.object(isolation, "quarantine_rows", return_value=rows):
                    with self.assertRaisesRegex(isolation.TaskIntegrityIsolationError, "blob drift"):
                        isolation.validated_quarantines(ROOT)
                    self.assertTrue(any("blob drift" in item for item in envelope.audit(ROOT)))

    def test_missing_and_invented_error_suppressions_fail_strict_audit(self):
        task_id = next(iter(EXPECTED))
        for extra in (False, True):
            with self.subTest(extra=extra):
                rows = copy.deepcopy(isolation.quarantine_rows(ROOT))
                row = rows[task_id]
                if extra:
                    row["allowed_task_record_audit_errors"].append("invented error")
                    marker = "stale or unused suppression: " + row["record_path"] + ": invented error"
                else:
                    removed = row["allowed_task_record_audit_errors"].pop()
                    marker = row["record_path"] + ": " + removed
                with mock.patch.object(isolation, "quarantine_rows", return_value=rows):
                    errors = isolation.audit_task_records(ROOT)
                self.assertTrue(any(marker in item for item in errors), errors)
        # The early envelope gate is not the strict error-set validator; both
        # existing gates are required. No broader exception is introduced here.

    def test_new_bad_record_does_not_inherit_existing_exceptions(self):
        exceptions = envelope._validated_exception_paths(ROOT)
        self.assertEqual([], exceptions[-1])
        row = isolation.validated_quarantines(ROOT)[next(iter(EXPECTED))]
        record = json.loads((ROOT / row["record_path"]).read_text(encoding="utf-8"))
        new_task = "RS-OWNER-UNREGISTERED-BAD-PUBLICATION-FIXTURE"
        new_pub = "TP2-OWNER-UNREGISTERED-BAD-FIXTURE"
        body = (ROOT / row["taskbook_path"]).read_text(encoding="utf-8").replace(record["task_id"], new_task)
        record.update(task_id=new_task, registry_key=new_task, publication_id=new_pub,
                      taskbook_path="research_tasks/new_bad_fixture.md")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / record["taskbook_path"]
            book.parent.mkdir(parents=True)
            book.write_bytes(body.encode("utf-8"))
            record["taskbook_blob_sha1"] = record_core.git_blob_sha1_bytes(book.read_bytes())
            path = root / "research_task_records" / new_task / (new_pub + ".json")
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(record), encoding="utf-8")
            # Reuse the actual validated exception set; only redirect the file
            # fixture. A new path cannot inherit another record's exceptions.
            with mock.patch.object(envelope, "ROOT", root), mock.patch.object(
                envelope, "_validated_exception_paths", return_value=exceptions,
            ):
                found = envelope.audit(root)
        prefix = f"research_task_records/{new_task}/{new_pub}.json: "
        self.assertEqual({prefix + error for error in ERRORS}, set(found))


if __name__ == "__main__":
    unittest.main()
