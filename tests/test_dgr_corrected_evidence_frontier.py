import json
import unittest
from pathlib import Path

import research_objective_records as objectives
from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_authority_fault_isolation as result_isolation
from tools import research_result_records as results


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION"
PUBLICATION_ID = "TP2-90D492F7054EDEE0F3CD"
OBJECTIVE_ID = "OBJ-DIAGONAL-GAUGE-REFOUNDATION-TYPED-CORRECTION-EVIDENCE-CLOSURE"
CORRECTED_RESULT_ID = "RR-AE11E20304C60C349CBD"
HISTORICAL_RESULT_ID = "RR-BFB7190B3C8D391C6E9D"
CURRENT_REVIEW_ID = "DR-B8DA78742C80B152F956"


def setUpModule():
    bootstrap.install(ROOT)


class DgrCorrectedEvidenceFrontierTests(unittest.TestCase):
    def test_formal_objective_is_open(self):
        head = objectives.current_head(OBJECTIVE_ID, ROOT)
        self.assertIsNotNone(head)
        self.assertEqual("OPEN", head["objective_status"])
        self.assertEqual("OG-73E5C1A76CFAB901374D", head["objective_generation_id"])

    def test_invalid_corrected_sink_does_not_restore_historical_result(self):
        # The authenticated replacement edge remains valid even when the sink's
        # frozen output digests no longer match. Neither generation is then an
        # operational result, and the older generation must not be resurrected.
        edge = results._replacement_edges(ROOT)[HISTORICAL_RESULT_ID]
        self.assertEqual(CORRECTED_RESULT_ID, edge["corrected_result_id"])
        row = result_isolation.validated_rows(ROOT)[CORRECTED_RESULT_ID]
        self.assertEqual(
            {
                "output digest drift: definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md",
                "output digest drift: definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md",
                "output digest drift: definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
            },
            set(row["allowed_result_audit_errors"]),
        )
        active_ids = {
            item["result_id"]
            for item in results.iter_results(ROOT)
            if item.get("task_id") == TASK_ID and item.get("publication_id") == PUBLICATION_ID
        }
        self.assertEqual(set(), active_ids)
        self.assertNotIn(HISTORICAL_RESULT_ID, active_ids)
        for result_id in (HISTORICAL_RESULT_ID, CORRECTED_RESULT_ID):
            path = ROOT / "research_result_records" / TASK_ID / f"{result_id}.json"
            self.assertEqual(result_id, json.loads(path.read_text(encoding="utf-8"))["result_id"])

    def test_stored_review_bytes_do_not_bypass_operational_quarantine(self):
        state = results.task_result_state(TASK_ID, ROOT, PUBLICATION_ID)
        self.assertIsNotNone(state)
        # Both frozen Result and review remain stored. The invalid Result must
        # request control recovery without becoming terminal or review-ready.
        self.assertEqual("RESULT_CONTROL_AUTHORITY_WITHHELD", state["state"])
        self.assertFalse(state["terminal"])
        self.assertTrue(state["control_recovery_required"])
        self.assertEqual([CORRECTED_RESULT_ID], state["withheld_result_ids"])
        self.assertIsNone(state["result"])
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
