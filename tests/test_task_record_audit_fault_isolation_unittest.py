import unittest
from pathlib import Path

from control_plane import research_task_integrity_fault_isolation as current_isolation
from control_plane import research_task_record_audit_fault_isolation as audit_isolation


ROOT = Path(__file__).resolve().parents[1]


class TaskRecordAuditFaultIsolationTests(unittest.TestCase):
    def test_real_audit_only_rows_are_exactly_nonoperational(self):
        rows = audit_isolation.validated_rows(ROOT)
        self.assertEqual(7, len(rows))
        bases = {row["nonoperational_basis"] for row in rows}
        self.assertEqual(
            {
                audit_isolation.BASIS_SUPERSEDED,
                audit_isolation.BASIS_FORK_BLOCKED,
            },
            bases,
        )
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

    def test_prior_art_g4_is_history_and_g5_is_current_quarantine(self):
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
        self.assertEqual("TP2-63DEB843280700CC0701", current["publication_id"])

    def test_only_latest_bridge_head_uses_fork_blocked_basis(self):
        rows = {
            row["publication_id"]: row for row in audit_isolation.validated_rows(ROOT)
        }
        self.assertEqual(
            audit_isolation.BASIS_SUPERSEDED,
            rows["TP2-33C39F540E894E7602AC"]["nonoperational_basis"],
        )
        self.assertEqual(
            audit_isolation.BASIS_FORK_BLOCKED,
            rows["TP2-CFE6E9F14623E929911E"]["nonoperational_basis"],
        )

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
