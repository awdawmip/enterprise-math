import unittest
from pathlib import Path

from control_plane import research_task_integrity_fault_isolation as current_isolation
from control_plane import research_task_record_audit_fault_isolation as audit_isolation


ROOT = Path(__file__).resolve().parents[1]


class TaskRecordAuditFaultIsolationTests(unittest.TestCase):
    def test_real_audit_only_rows_are_exactly_nonoperational(self):
        rows = audit_isolation.validated_rows(ROOT)
        self.assertGreater(len(rows), 0)
        bases = {row["nonoperational_basis"] for row in rows}
        self.assertTrue(bases)
        self.assertTrue(bases <= audit_isolation.BASES)
        for row in rows:
            self.assertFalse(row["operational"])
            self.assertTrue(row["history_preserved"])
            self.assertFalse(row["working_truth_granted"])
            self.assertFalse(row["foundation_authority_granted"])
            self.assertFalse(row["canonical_promotion_granted"])
            self.assertFalse(row["successor_triggered"])
            self.assertFalse(row["operational_publication_selected"])

    def test_audit_only_and_current_task_quarantines_do_not_overlap(self):
        audit_publications = {
            row["publication_id"] for row in audit_isolation.validated_rows(ROOT)
        }
        current_publications = {
            row["publication_id"]
            for row in current_isolation.validated_quarantines(ROOT).values()
        }
        self.assertTrue(audit_publications)
        self.assertTrue(current_publications)
        self.assertEqual(set(), audit_publications & current_publications)

    def test_prior_art_history_is_retained_and_current_quarantine_tracks_latest_head(self):
        rows = {
            row["publication_id"]: row for row in audit_isolation.validated_rows(ROOT)
        }
        self.assertEqual(
            audit_isolation.BASIS_SUPERSEDED,
            rows["TP2-487CC790F9F7AA01CAAF"]["nonoperational_basis"],
        )
        current = current_isolation.validated_quarantines(ROOT)[
            "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT"
        ]
        self.assertEqual("TP2-2F8C6A1D9E7043B5C812", current["publication_id"])

    def test_fork_blocked_rows_track_live_forks_and_resolved_history_is_superseded(self):
        from control_plane import research_publication_fault_isolation as publication_isolation
        from tools import research_dispatch

        rows = {
            row["publication_id"]: row for row in audit_isolation.validated_rows(ROOT)
        }
        self.assertEqual(
            audit_isolation.BASIS_SUPERSEDED,
            rows["TP2-CFE6E9F14623E929911E"]["nonoperational_basis"],
        )
        forks = publication_isolation.validated_quarantines(ROOT)
        fork_rows = [
            row for row in rows.values()
            if row["nonoperational_basis"] == audit_isolation.BASIS_FORK_BLOCKED
        ]
        for row in fork_rows:
            self.assertIn(row["task_id"], forks)
            fork = forks[row["task_id"]]
            effective = set(fork.get("_effective_publication_ids", fork["publication_ids"]))
            self.assertIn(row["publication_id"], effective)

        blocked_tasks = {
            "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
            "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N13-COLLISION-FRONTIER",
            "RS-P022-OBSERVATION-HISTORY",
            "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF",
            "RS-R043C4-NATIVE-INTERFACE-LINK-SEPARATOR-CLOSURE",
        }
        current = publication_isolation.isolated_current_records(ROOT)
        definitions = {row["task_id"]: row for row in research_dispatch.merged_definitions(ROOT)}
        for task in blocked_tasks:
            with self.subTest(task=task):
                self.assertIn(task, forks)
                self.assertEqual(publication_isolation.QUARANTINE_STATE, forks[task]["state"])
                self.assertIsNone(forks[task]["operational_publication_id"])
                self.assertNotIn(task, current)
                self.assertEqual("BLOCKED", definitions[task]["base_state"])
                self.assertIsNone(definitions[task]["publication_id"])

        # Superseded generations remain valid history even when their family's
        # later active heads still form an unresolved fork.
        for publication_id in (
            "TP2-D4A7C19E5B306F821472",
            "TP2-E5B7C19A3D604F821583",
        ):
            self.assertEqual(
                audit_isolation.BASIS_SUPERSEDED,
                rows[publication_id]["nonoperational_basis"],
            )
        resolved_history = rows["TP2-6866CB3F890F6563C474"]
        self.assertEqual("RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS", resolved_history["task_id"])
        self.assertNotIn(resolved_history["task_id"], forks)
        self.assertEqual(audit_isolation.BASIS_SUPERSEDED, resolved_history["nonoperational_basis"])
        self.assertTrue(resolved_history["history_preserved"])

    def test_every_declared_suppression_is_exact_record_prefixed(self):
        rows = audit_isolation.validated_rows(ROOT)
        expected = sum(len(row["allowed_task_record_audit_errors"]) for row in rows)
        suppressions = audit_isolation.suppression_strings(ROOT)
        self.assertEqual(expected, len(suppressions))
        for row in rows:
            prefix = row["record_path"] + ": "
            self.assertTrue(any(value.startswith(prefix) for value in suppressions))


if __name__ == "__main__":
    unittest.main()
