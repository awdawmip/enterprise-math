import json
import unittest
from pathlib import Path

from tools import research_task_records as records


ROOT = Path(__file__).resolve().parents[1]
TASK_ID = "RS-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M-PROOF"
OPERATIONAL = "TP2-4EE2618ABEBB6D097023"
RETAINED = "TP2-5547117E54D7A556279B"


class PerfectPrimePublicationResolutionTests(unittest.TestCase):
    def test_parallel_generation_one_publications_have_one_operational_head(self):
        current = records.current_records(ROOT)
        self.assertIn(TASK_ID, current)
        self.assertEqual(OPERATIONAL, current[TASK_ID]["publication_id"])
        self.assertEqual([], records.audit(ROOT))

    def test_resolution_preserves_both_immutable_publications(self):
        payload = json.loads(
            (ROOT / "research_task_publication_resolutions.json").read_text(encoding="utf-8")
        )
        row = next(item for item in payload["resolutions"] if item["task_id"] == TASK_ID)
        self.assertEqual(OPERATIONAL, row["canonical_publication_id"])
        self.assertEqual(OPERATIONAL, row["operational_publication_id"])
        self.assertEqual([RETAINED], row["quarantined_publication_ids"])
        self.assertEqual({OPERATIONAL, RETAINED}, set(row["retained_parallel_publication_ids"]))
        self.assertEqual("chatgpt-ppta-20260828-1424-7c4e2a", row["preserve_existing_claim"])
        self.assertFalse(row["working_truth_granted"])
        self.assertFalse(row["canonical_promotion_granted"])
        self.assertFalse(row["successor_triggered"])


if __name__ == "__main__":
    unittest.main()
