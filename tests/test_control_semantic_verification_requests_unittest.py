import json
import unittest
from pathlib import Path

from control_plane import check_control_semantic_verification_requests as requests


ROOT = Path(__file__).resolve().parents[1]


class ControlSemanticVerificationRequestTests(unittest.TestCase):
    def test_only_architecture_request_remains_open_and_nonexecutive(self):
        reports = requests.check(ROOT)
        self.assertEqual(1, len(reports))
        self.assertIn("CSV-ARCHITECTURE-V2-PUBLICATION-CUTOVER-001", reports[0])
        self.assertNotIn("CSV-AMBIGUOUS-DISPATCH-FIELD-MEANING-002", reports[0])

    def test_control_requests_cannot_masquerade_as_tasks(self):
        data = json.loads(
            (ROOT / "control_plane" / "control_semantic_verification_requests.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(1, len(data["requests"]))
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
