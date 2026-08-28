from __future__ import annotations

import unittest

from control_plane import research_control_bootstrap
from control_plane import research_task_integrity_fault_isolation as isolation


EXPECTED = {
    "RS-NOLLM-EISENSTEIN-ROTATION-ATLAS": "TP2-983B1B8DB12B245368D9",
    "RS-SHOR-FAST-ROUGH-INTERVAL-GCD": "TP2-C193F8CB279ADF29D4ED",
    "RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION": "TP2-9AB05574C3CA5534CB39",
}


class TaskIntegrityFaultIsolationTests(unittest.TestCase):
    def test_integrity_quarantines_are_exact_and_select_no_publication(self) -> None:
        rows = isolation.validated_quarantines()
        self.assertEqual(set(rows), set(EXPECTED))
        for task_id, publication_id in EXPECTED.items():
            row = rows[task_id]
            self.assertEqual(row["publication_id"], publication_id)
            self.assertIsNone(row["operational_publication_id"])
            self.assertFalse(row["working_truth_granted"])
            self.assertFalse(row["foundation_authority_granted"])
            self.assertFalse(row["canonical_promotion_granted"])
            self.assertFalse(row["successor_triggered"])

    def test_exact_known_strict_audit_errors_are_fully_accounted_for(self) -> None:
        self.assertEqual(isolation.audit_task_records(), [])

    def test_integrity_quarantines_are_not_current_and_project_to_blocked(self) -> None:
        research_control_bootstrap.install()
        from tools import research_dispatch, research_task_records

        current = research_task_records.current_records()
        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions()
        }
        for task_id, publication_id in EXPECTED.items():
            self.assertNotIn(task_id, current)
            item = definitions[task_id]
            self.assertEqual(item["base_state"], "BLOCKED")
            self.assertIsNone(item["publication_id"])
            self.assertEqual(item["publication_ids"], [publication_id])
            self.assertEqual(item["registration_source"], "TASK_INTEGRITY_QUARANTINE")
            self.assertEqual(
                item["hard_block"]["code"], "INVALID_CURRENT_TASK_PUBLICATION"
            )
            self.assertIsNone(item["hard_block"]["operational_publication_id"])

    def test_runtime_projection_audit_passes(self) -> None:
        self.assertEqual(isolation.audit_runtime_projection(), [])


if __name__ == "__main__":
    unittest.main()
