"""Exact maintenance regressions for the five 16cc5663 publication forks.

No fixture publication is written to the repository. Mutations below exercise
the existing validator through isolated snapshots, not relaxed test validators.
"""
from __future__ import annotations

import copy
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from control_plane import check_publication_fault_isolation as checker
from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_publication_fault_isolation as fork
from control_plane import research_task_integrity_fault_isolation as integrity
from control_plane import research_task_record_audit_fault_isolation as record_audit
from control_plane import research_task_records_impl as core

ROOT = Path(__file__).resolve().parents[1]
HEADS = {
    "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE": {
        "TP2-3F6A92D8C1E740B5A2C9", "TP2-4A84B81FD5CAB8CD0359",
        "TP2-FBDBDBE1C5BDF65F97A0",
    },
    "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER": {
        "TP2-2BB590EA80230A7A7D4C", "TP2-6C812E92A7C937795A59",
    },
    "RS-P022-OBSERVATION-HISTORY": {
        "TP2-2346F5D3E731ED56DB0A", "TP2-D78DBA0243911E0363FA",
        "TP2-DE338F269CA11E9BC01B",
    },
    "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF": {
        "TP2-3EAC29B49F71ABB92BEA", "TP2-5547117E54D7A556279B",
    },
    "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE": {
        "TP2-9D0A43C4F217B6E8C531", "TP2-A63015C2EB99D00F2500",
    },
}
FLAGS = (
    "working_truth_granted", "foundation_authority_granted",
    "canonical_promotion_granted", "successor_triggered",
)
P022 = "RS-P022-OBSERVATION-HISTORY"
D78 = "TP2-D78DBA0243911E0363FA"
D78_ERRORS = {
    "mandatory body section is missing or empty: " + title
    for title in (
        "Frozen inputs and scope", "Hard target and required outputs",
        "Research value to preserve", "Success, kill, and return criteria",
    )
}


class OwnerUnresolvedPublicationForkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap.install(ROOT)
        cls.records = core.iter_records(ROOT)

    def test_five_exact_forks_block_without_selecting_any_head(self):
        from tools import research_dispatch
        import research_operational_publications as operational

        rows = fork.validated_quarantines(ROOT)
        current = fork.isolated_current_records(ROOT)
        resolutions = core.publication_resolutions(ROOT)
        definitions = {
            row["task_id"]: row for row in research_dispatch.merged_definitions(ROOT)
        }
        for task, expected in HEADS.items():
            with self.subTest(task=task):
                row = rows[task]
                self.assertEqual(fork.QUARANTINE_STATE, row["state"])
                self.assertEqual(expected, set(row["publication_ids"]))
                self.assertEqual(expected, set(row["_effective_publication_ids"]))
                self.assertNotIn("tracking_mode", row)
                self.assertNotIn("lineage_anchor_publication_ids", row)
                self.assertIsNone(row["operational_publication_id"])
                for flag in FLAGS:
                    self.assertIs(row[flag], False)
                self.assertNotIn(task, resolutions)
                self.assertNotIn(task, current)
                self.assertIsNone(operational.selection(task, ROOT))
                definition = definitions[task]
                self.assertEqual("BLOCKED", definition["base_state"])
                self.assertIsNone(definition["publication_id"])
                self.assertEqual(expected, set(definition["publication_ids"]))
                # Empty-event projection is a deterministic contract probe,
                # not a statement that live runtime event history is empty.
                state = research_dispatch.reduce_definition(
                    definition, [], now=datetime(2026, 9, 7, tzinfo=timezone.utc),
                    root=ROOT,
                )
                self.assertEqual("BLOCKED", state["dispatch_state"])

    def test_new_head_or_removed_head_invalidates_exact_isolation(self):
        records = copy.deepcopy(self.records)
        original = next(r for r in records if r.get("publication_id") == D78)
        added = dict(original, publication_id="TP2-TEST-UNREGISTERED-NEW-HEAD",
                     supersedes_publication_id=None)
        snapshots = [
            records + [added],
            [r for r in records if r.get("publication_id") != D78],
        ]
        for snapshot in snapshots:
            with self.subTest(size=len(snapshot)):
                with mock.patch.object(core, "iter_records", return_value=snapshot):
                    with self.assertRaisesRegex(
                        fork.PublicationFaultIsolationError, "quarantine head set drift"
                    ):
                        fork.validated_quarantines(ROOT)

    def test_residual_resolution_is_rejected_by_validator_and_checker(self):
        with mock.patch.object(core, "publication_resolutions", return_value={P022: {}}):
            with self.assertRaisesRegex(
                fork.PublicationFaultIsolationError, "cannot coexist with operational resolution"
            ):
                fork.validated_quarantines(ROOT)
        snapshot = SimpleNamespace(
            publication_heads=lambda root: {P022: [
                {"publication_id": p} for p in sorted(HEADS[P022])
            ]},
            resolution_map=lambda root: {P022: {}},
            synthesis_map=lambda root: {},
        )
        errors = checker._audit_operational_publications(snapshot, set(HEADS))
        self.assertEqual(1, len(errors))
        self.assertIn("cannot coexist with operational resolution", errors[0])

    def test_isolation_does_not_hide_an_unrelated_unresolved_fork(self):
        task = "RS-TEST-UNRELATED-UNRESOLVED-FORK"
        records = self.records + [
            {"task_id": task, "publication_id": p, "record_state": "ACTIVE"}
            for p in ("TP2-TEST-LEFT", "TP2-TEST-RIGHT")
        ]
        with mock.patch.object(core, "iter_records", return_value=records):
            with self.assertRaisesRegex(core.TaskRecordError, "publication fork for " + task):
                fork.isolated_current_records(ROOT)
        snapshot = SimpleNamespace(
            publication_heads=lambda root: {task: records[-2:]},
            resolution_map=lambda root: {}, synthesis_map=lambda root: {},
        )
        errors = checker._audit_operational_publications(snapshot, set(HEADS))
        self.assertEqual(1, len(errors))
        self.assertIn(task + ": multiple active publication heads", errors[0])

    def test_no_authority_flag_can_be_enabled(self):
        payload = json.loads((ROOT / fork.QUARANTINE_FILE).read_text(encoding="utf-8"))
        for flag in FLAGS:
            changed = copy.deepcopy(payload)
            changed["quarantines"][0][flag] = True
            with self.subTest(flag=flag), mock.patch.object(fork, "_load", return_value=changed):
                with self.assertRaisesRegex(fork.PublicationFaultIsolationError, "cannot grant " + flag):
                    fork.quarantine_rows(ROOT)

    def test_p022_waiver_lifecycle_uses_exact_existing_audit_basis(self):
        waivers = json.loads((ROOT / "research_task_record_compatibility_waivers.json").read_text(encoding="utf-8"))
        self.assertNotIn(D78, {r["publication_id"] for r in waivers["waivers"]})
        rows = record_audit.validated_rows(ROOT)
        row = next(r for r in rows if r["publication_id"] == D78)
        self.assertEqual(record_audit.BASIS_FORK_BLOCKED, row["nonoperational_basis"])
        self.assertEqual("sha1:a7fb4c39766e8895306e21938da35f4a919cb9ef", row["record_blob_sha1"])
        self.assertEqual("sha1:15b495b7a21af748260363a6969097abe1f79611", row["taskbook_blob_sha1"])
        self.assertEqual(D78_ERRORS, set(row["allowed_task_record_audit_errors"]))
        self.assertEqual([], row.get("allowed_publication_envelope_errors", []))
        self.assertIs(row["operational"], False)
        self.assertIs(row["history_preserved"], True)
        for flag in FLAGS + ("operational_publication_selected",):
            self.assertIs(row[flag], False)
        record = next(r for r in self.records if r.get("publication_id") == D78)
        # Check the actual immutable body, independently of the claimed list.
        _, body = core.research_taskbook.split_taskbook(
            (ROOT / record["taskbook_path"]).read_text(encoding="utf-8")
        )
        self.assertEqual(D78_ERRORS, set(core.validate_body(body)))

    def test_p022_audit_basis_fails_when_fork_isolation_disappears(self):
        forks = fork.validated_quarantines(ROOT)
        del forks[P022]
        with mock.patch.object(fork, "validated_quarantines", return_value=forks):
            with self.assertRaisesRegex(
                record_audit.TaskRecordAuditIsolationError,
                "task is not currently blocked by publication-fork quarantine",
            ):
                record_audit.validated_rows(ROOT)

    def test_p022_record_or_taskbook_pin_drift_is_rejected(self):
        rows = record_audit.quarantine_rows(ROOT)
        for field in ("record_blob_sha1", "taskbook_blob_sha1"):
            changed = copy.deepcopy(rows)
            next(r for r in changed if r["publication_id"] == D78)[field] = "sha1:" + "0" * 40
            with self.subTest(field=field), mock.patch.object(record_audit, "quarantine_rows", return_value=changed):
                with self.assertRaisesRegex(record_audit.TaskRecordAuditIsolationError, "blob drift"):
                    record_audit.validated_rows(ROOT)

    def test_exact_audit_suppression_cannot_hide_extra_or_changed_errors(self):
        raw = integrity.audit_task_records(ROOT)
        self.assertEqual([], record_audit.audit_against(raw, ROOT))
        unrelated = "research_task_records/RS-TEST/TP2-TEST.json: wrong record_schema"
        self.assertEqual([unrelated], record_audit.audit_against(raw + [unrelated], ROOT))
        old_error = next(e for e in raw if D78 in e)
        new_error = old_error + " [changed defect]"
        changed = [new_error if e == old_error else e for e in raw]
        errors = record_audit.audit_against(changed, ROOT)
        self.assertIn(new_error, errors)
        self.assertTrue(any("stale or unused suppression: " + old_error in e for e in errors))

    def test_new_unrelated_bad_record_still_produces_a_strict_error(self):
        source = next(r for r in self.records if r.get("task_id") not in HEADS)
        bad = dict(
            source, task_id="RS-TEST-UNRELATED-BAD-RECORD",
            registry_key="RS-TEST-UNRELATED-BAD-RECORD",
            publication_id="TP2-TEST-BAD-SCHEMA", record_schema="INVALID_SCHEMA",
            supersedes_publication_id=None, record_state="ACTIVE",
            _record_path="research_task_records/RS-TEST/TP2-TEST-BAD-SCHEMA.json",
        )
        expected = bad["_record_path"] + ": wrong record_schema"
        with mock.patch.object(core, "iter_records", return_value=self.records + [bad]):
            raw = integrity.audit_task_records(ROOT)
            self.assertIn(expected, raw)
            self.assertIn(expected, record_audit.audit_against(raw, ROOT))


if __name__ == "__main__":
    unittest.main()
