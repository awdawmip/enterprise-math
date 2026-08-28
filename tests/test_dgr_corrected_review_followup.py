import unittest
from pathlib import Path

import research_driver_followup_guard as followup
import research_objective_records as objectives
from tools import research_result_records as results
from tools import research_task_records as tasks


ROOT = Path(__file__).resolve().parents[1]
SOURCE_TASK = "RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION"
SOURCE_PUBLICATION = "TP2-90D492F7054EDEE0F3CD"
RESULT_ID = "RR-AE11E20304C60C349CBD"
REVIEW_ID = "DR-B83414A4FCA60228B74C"
FOLLOWUP_TASK = "RS-DGR-CORRECTED-EVIDENCE-ADVERSARIAL-CLOSURE-AUDIT"
FOLLOWUP_PUBLICATION = "TP2-27112C6485E90710810E"
OBJECTIVE = "OBJ-DIAGONAL-GAUGE-REFOUNDATION-TYPED-CORRECTION-EVIDENCE-CLOSURE"


class DgrCorrectedReviewFollowupTests(unittest.TestCase):
    def test_source_result_is_terminal_but_parent_remains_open(self):
        state = results.task_result_state(SOURCE_TASK, ROOT, SOURCE_PUBLICATION)
        self.assertIsNotNone(state)
        self.assertEqual("TERMINAL", state["state"])
        self.assertTrue(state["terminal"])
        self.assertEqual(RESULT_ID, state["result"]["result_id"])
        self.assertEqual(REVIEW_ID, state["review"]["review_id"])
        self.assertEqual("FOLLOWUP_TASKSET_READY", state["driver_followup_state"])

        head = objectives.current_head(OBJECTIVE, ROOT)
        self.assertIsNotNone(head)
        self.assertEqual("OPEN", head["objective_status"])

    def test_followup_packet_single_values_adversarial_audit(self):
        state = followup.state_for_review(REVIEW_ID, ROOT)
        self.assertTrue(state["required"])
        self.assertTrue(state["ready"])
        self.assertEqual("FOLLOWUP_TASKSET_READY", state["state"])
        packet = state["packet"]
        self.assertEqual("TASK_SET_PUBLISHED", packet["decision"])
        self.assertEqual(
            [{
                "task_id": FOLLOWUP_TASK,
                "publication_id": FOLLOWUP_PUBLICATION,
                "task_role": "ADVERSARIAL_AUDIT",
            }],
            packet["task_publications"],
        )

    def test_followup_task_is_unique_current_publication(self):
        current = tasks.current_records(ROOT)
        self.assertIn(FOLLOWUP_TASK, current)
        self.assertEqual(
            FOLLOWUP_PUBLICATION,
            current[FOLLOWUP_TASK]["publication_id"],
        )
        self.assertEqual(OBJECTIVE, current[FOLLOWUP_TASK]["parent_objective_id"])


if __name__ == "__main__":
    unittest.main()
