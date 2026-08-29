import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_verification_requests as requests


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticVerificationRequestTests(unittest.TestCase):
    def test_requests_are_nonexecutive_and_bound_to_open_migrations(self):
        reports = requests.check(ROOT)
        self.assertEqual(2, len(reports))
        self.assertTrue(any("CSV-ARCHITECTURE-V2-PUBLICATION-CUTOVER-001" in row for row in reports))
        self.assertTrue(any("CSV-AMBIGUOUS-DISPATCH-FIELD-MEANING-002" in row for row in reports))

    def test_control_requests_cannot_masquerade_as_tasks(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_verification_requests.json").read_text(
                encoding="utf-8"
            )
        )
        for row in data["requests"]:
            self.assertFalse(row["is_research_task"])
            self.assertFalse(row["claimable"])
            self.assertFalse(row["runtime_dispatchable"])
            self.assertFalse(row["authority_granted"])
            publication = row["future_authorized_publication"]
            self.assertEqual("GOVERNANCE", publication["kind"])
            self.assertEqual(
                "research_task_publication_contract_v2.json",
                publication["publication_contract"],
            )
            self.assertEqual("tools/research_task_records.py", publication["publication_tool"])
            self.assertTrue(
                set(publication["publisher_role_must_be_one_of"])
                <= {"RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
            )


if __name__ == "__main__":
    unittest.main()
