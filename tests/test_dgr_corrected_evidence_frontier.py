import json
import unittest
from pathlib import Path

import research_objective_records as objectives
from tools import research_result_records as results


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION"
PUBLICATION_ID = "TP2-90D492F7054EDEE0F3CD"
OBJECTIVE_ID = "OBJ-DIAGONAL-GAUGE-REFOUNDATION-TYPED-CORRECTION-EVIDENCE-CLOSURE"
CORRECTED_RESULT_ID = "RR-AE11E20304C60C349CBD"
HISTORICAL_RESULT_ID = "RR-BFB7190B3C8D391C6E9D"
CURRENT_REVIEW_ID = "DR-B8DA78742C80B152F956"


class DgrCorrectedEvidenceFrontierTests(unittest.TestCase):
    def test_formal_objective_is_open(self):
        head = objectives.current_head(OBJECTIVE_ID, ROOT)
        self.assertIsNotNone(head)
        self.assertEqual("OPEN", head["objective_status"])
        self.assertEqual("OG-73E5C1A76CFAB901374D", head["objective_generation_id"])

    def test_corrected_generation_is_operational_not_parallel(self):
        active_ids = {
            item["result_id"]
            for item in results.iter_results(ROOT)
            if item.get("task_id") == TASK_ID and item.get("publication_id") == PUBLICATION_ID
        }
        self.assertEqual({CORRECTED_RESULT_ID}, active_ids)
        self.assertNotIn(HISTORICAL_RESULT_ID, active_ids)

    def test_stored_review_bytes_do_not_bypass_operational_quarantine(self):
        state = results.task_result_state(TASK_ID, ROOT, PUBLICATION_ID)
        self.assertIsNotNone(state)
        # Storage and operational authority are separate.  The immutable review
        # record is retained for provenance, while canonical fault isolation may
        # withhold that review from the operational result state.  Withholding
        # authority must leave the task nonterminal rather than silently accept
        # or discard the stored review.
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertFalse(state["terminal"])
        self.assertEqual(CORRECTED_RESULT_ID, state["result"]["result_id"])
        self.assertIsNone(state["review"])

        review_path = (
            ROOT
            / "research_result_reviews"
            / CORRECTED_RESULT_ID
            / f"{CURRENT_REVIEW_ID}.json"
        )
        self.assertTrue(review_path.is_file())
        stored = json.loads(review_path.read_text(encoding="utf-8"))
        self.assertEqual(CURRENT_REVIEW_ID, stored["review_id"])
        self.assertEqual(CORRECTED_RESULT_ID, stored["result_id"])


if __name__ == "__main__":
    unittest.main()
