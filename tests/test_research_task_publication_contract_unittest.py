import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TaskPublicationContractTests(unittest.TestCase):
    def test_all_publishers_share_one_template_and_registry(self):
        publication = json.loads((ROOT / "research_task_publication_contract.json").read_text(encoding="utf-8"))
        taskbook = json.loads((ROOT / "research_taskbook_contract.json").read_text(encoding="utf-8"))
        role = json.loads((ROOT / "research_role_policy.json").read_text(encoding="utf-8"))
        expected = {"RESEARCHER", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"}
        self.assertEqual(set(publication["publisher_roles"]), expected)
        self.assertEqual(set(taskbook["allowed_publisher_roles"]), expected)
        self.assertEqual(set(role["task_publication_authority"]["publisher_roles"]), expected)
        self.assertEqual(publication["mandatory_template"], "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json")
        self.assertEqual(taskbook["publication_template"], "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json")
        self.assertEqual(role["task_publication_authority"]["template"], "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json")

    def test_researcher_publication_does_not_imply_driver_truth_or_promotion_authority(self):
        publication = json.loads((ROOT / "research_task_publication_contract.json").read_text(encoding="utf-8"))
        role = json.loads((ROOT / "research_role_policy.json").read_text(encoding="utf-8"))
        self.assertTrue(publication["researcher_publication"]["allowed"])
        self.assertFalse(publication["researcher_publication"]["driver_approval_required"])
        self.assertEqual(publication["researcher_publication"]["effective_priority_default"], "P2")
        self.assertEqual(publication["researcher_publication"]["effective_leverage_default"], "MEDIUM")
        auth = role["task_publication_authority"]
        self.assertFalse(auth["researcher_driver_approval_required"])
        self.assertFalse(auth["publication_grants_working_truth"])
        self.assertFalse(auth["publication_grants_promotion"])

    def test_free_research_raw_candidate_remains_nonpublishable(self):
        publication = json.loads((ROOT / "research_task_publication_contract.json").read_text(encoding="utf-8"))
        candidate = json.loads((ROOT / "research_axiom_candidate_state_machine.json").read_text(encoding="utf-8"))
        self.assertFalse(publication["free_research_publication"]["raw_phase_a_candidate_task_publication"])
        self.assertFalse(candidate["task_publication"]["raw_blind_candidate_eligible"])
        self.assertFalse(candidate["task_publication"]["researcher_driver_approval_required"])
        self.assertEqual(
            set(candidate["task_publication"]["eligible_from"]),
            {"AUDITED_AXIOM_CANDIDATE", "AUDITED_REPLACEMENT_CANDIDATE", "EXACT_NEGATIVE_OBSTRUCTION"},
        )

    def test_registry_requires_parent_objective_and_research_value(self):
        publication = json.loads((ROOT / "research_task_publication_contract.json").read_text(encoding="utf-8"))
        required = set(publication["publication_record_required_fields"])
        self.assertIn("parent_objective_id", required)
        self.assertIn("research_value", required)
        self.assertIn("publisher_role", required)
        self.assertIn("publisher_id", required)
        self.assertIn("taskbook_blob_sha1", required)


if __name__ == "__main__":
    unittest.main()
