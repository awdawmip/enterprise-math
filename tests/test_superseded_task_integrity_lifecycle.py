import unittest
from pathlib import Path

from control_plane import research_task_integrity_fault_isolation as current_isolation
from control_plane import research_task_record_audit_fault_isolation as audit_isolation

ROOT = Path(__file__).resolve().parents[1]
TASK = "RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE"
OLD = "TP2-D425335E9566A3F6A54C"
NEW = "TP2-75A6C3F81E2D094B67CF"


class SupersededTaskIntegrityLifecycleTests(unittest.TestCase):
    def test_geo8_old_generation_is_history_not_runtime_block(self):
        self.assertNotIn(TASK, current_isolation.validated_quarantines(ROOT))
        rows = {row["publication_id"]: row for row in audit_isolation.validated_rows(ROOT)}
        self.assertIn(OLD, rows)
        self.assertEqual(rows[OLD]["nonoperational_basis"], "DIRECTLY_SUPERSEDED_SAME_TASK")

    def test_geo8_old_body_errors_remain_exactly_suppressed(self):
        prefix = (
            "research_task_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/"
            "TP2-D425335E9566A3F6A54C.json: "
        )
        suppressions = audit_isolation.suppression_strings(ROOT)
        self.assertIn(prefix + "mandatory body section is missing or empty: Frozen inputs and scope", suppressions)
        self.assertIn(prefix + "mandatory body section is missing or empty: Hard target and required outputs", suppressions)

    def test_geo8_current_record_is_direct_superseder(self):
        rows = audit_isolation.validated_rows(ROOT)
        old = next(row for row in rows if row["publication_id"] == OLD)
        self.assertEqual(old["task_id"], TASK)
        records = __import__("control_plane.research_task_records_impl", fromlist=["iter_records"])
        matches = [
            row for row in records.iter_records(ROOT)
            if row.get("task_id") == TASK and row.get("publication_id") == NEW
        ]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].get("supersedes_publication_id"), OLD)


if __name__ == "__main__":
    unittest.main()
