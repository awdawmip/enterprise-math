import json
import subprocess
import sys
import unittest
from pathlib import Path

from control_plane import research_result_review_binding_fault_isolation as binding


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ID = "DR-9F0EF13296934CCAD8BD"
DERIVED_TASK_ID = "RS-NATIVE-TRISECTOR-N2-SCALAR-CLOSURE-FOUNDATION-STEWARD-ADMISSION-PRIOR-ART"


class ResultReviewBindingIsolationTests(unittest.TestCase):
    def test_exact_binding_quarantine_is_valid_and_authority_free(self):
        rows = binding.validated_quarantines(ROOT)
        self.assertEqual({REVIEW_ID}, set(rows))
        row = rows[REVIEW_ID]
        self.assertFalse(row["operational"])
        self.assertTrue(row["history_preserved"])
        self.assertEqual(["result record digest drift"], row["allowed_binding_errors"])
        for field in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            self.assertFalse(row[field])

    def test_canonical_bootstrap_removes_review_and_blocks_solely_derived_task(self):
        code = f"""
import json
from control_plane import research_control_bootstrap as bootstrap
bootstrap.install()
from tools import research_dispatch, research_result_records
reviews = [r.get('review_id') for r in research_result_records.iter_reviews()]
defs = {{r.get('task_id'): r for r in research_dispatch.merged_definitions() if isinstance(r, dict)}}
task = defs[{DERIVED_TASK_ID!r}]
print(json.dumps({{
    'review_present': {REVIEW_ID!r} in reviews,
    'base_state': task.get('base_state'),
    'frontier': task.get('frontier'),
    'publication_id': task.get('publication_id'),
    'registration_source': task.get('registration_source'),
}}))
"""
        proc = subprocess.run(
            [sys.executable, "-c", code],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, proc.returncode, msg=proc.stderr)
        payload = json.loads(proc.stdout.strip().splitlines()[-1])
        self.assertFalse(payload["review_present"])
        self.assertEqual("BLOCKED", payload["base_state"])
        self.assertEqual("NONOPERATIONAL_SOURCE_REVIEW_FOLLOWUP", payload["frontier"])
        self.assertIsNone(payload["publication_id"])
        self.assertEqual("DRIVER_FOLLOWUP_AUTHORITY_QUARANTINE", payload["registration_source"])


if __name__ == "__main__":
    unittest.main()
