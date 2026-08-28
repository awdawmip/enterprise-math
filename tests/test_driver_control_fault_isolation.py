from __future__ import annotations

import unittest

from control_plane import research_control_bootstrap
from control_plane import research_driver_followup_fault_isolation as followup_isolation
from control_plane import research_driver_review_authority_fault_isolation as review_isolation


REVIEW_IDS = {
    "DR-2F834647FD94CAF46D05",
    "DR-B8DA78742C80B152F956",
}
PACKET_ID = "DFU-A74F58729A62AE4956CF"
DERIVED_TASK_ID = "RS-RSA-EXPONENT-COLLISION-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT"
DERIVED_PUBLICATION_ID = "TP2-DCBF9A9ACA18BF64FFCF"


class DriverControlFaultIsolationTests(unittest.TestCase):
    def test_review_quarantine_is_exact_nonoperational_history(self) -> None:
        rows = review_isolation.validated_quarantines()
        self.assertEqual(set(rows), REVIEW_IDS)
        for row in rows.values():
            self.assertFalse(row["operational"])
            self.assertTrue(row["history_preserved"])
            self.assertFalse(row["working_truth_granted"])
            self.assertFalse(row["foundation_authority_granted"])
            self.assertFalse(row["canonical_promotion_granted"])
            self.assertFalse(row["successor_triggered"])

    def test_review_quarantine_is_absent_from_operational_review_view(self) -> None:
        research_control_bootstrap.install()
        from tools import research_result_records

        review_ids = {
            str(item.get("review_id"))
            for item in research_result_records.iter_reviews()
            if isinstance(item.get("review_id"), str)
        }
        self.assertTrue(REVIEW_IDS.isdisjoint(review_ids))

    def test_followup_quarantine_is_exact_and_source_review_bound(self) -> None:
        rows = followup_isolation.validated_quarantines()
        self.assertEqual(set(rows), {PACKET_ID})
        row = rows[PACKET_ID]
        self.assertEqual(row["review_id"], "DR-2F834647FD94CAF46D05")
        self.assertFalse(row["operational"])
        self.assertTrue(row["history_preserved"])
        derived = row["derived_task_publications"]
        self.assertEqual(len(derived), 1)
        self.assertEqual(derived[0]["task_id"], DERIVED_TASK_ID)
        self.assertEqual(derived[0]["publication_id"], DERIVED_PUBLICATION_ID)

    def test_followup_packet_and_derived_task_are_nonoperational(self) -> None:
        research_control_bootstrap.install()
        import research_driver_followup
        from tools import research_dispatch, research_task_records

        packet_ids = {
            str(item.get("packet_id"))
            for item in research_driver_followup.iter_packets()
            if isinstance(item.get("packet_id"), str)
        }
        self.assertNotIn(PACKET_ID, packet_ids)

        current = research_task_records.current_records()
        self.assertNotIn(DERIVED_TASK_ID, current)
        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions()
        }
        item = definitions[DERIVED_TASK_ID]
        self.assertEqual(item["base_state"], "BLOCKED")
        self.assertIsNone(item["publication_id"])
        self.assertEqual(item["publication_ids"], [DERIVED_PUBLICATION_ID])
        self.assertEqual(
            item["registration_source"], "DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE"
        )
        self.assertEqual(
            item["hard_block"]["code"], "NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP"
        )


if __name__ == "__main__":
    unittest.main()
