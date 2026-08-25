import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TaskPublicationTemplateTests(unittest.TestCase):
    def test_mandatory_template_has_required_task_and_registry_fields(self):
        template = json.loads((ROOT / "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json").read_text(encoding="utf-8"))
        self.assertEqual(template["schema"], "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1")
        self.assertEqual(template["status"], "MANDATORY")
        task = template["taskbook_frontmatter_required"]
        for field in (
            "task_id",
            "publication_contract",
            "publication_template",
            "registry_key",
            "parent_objective_id",
            "origin_kind",
            "task_lineage",
            "policy_review",
        ):
            self.assertIn(field, task)
        record = template["registry_record_required"]
        for field in (
            "publisher_role",
            "publisher_id",
            "published_at",
            "research_value",
            "registry_state",
            "terminal_scope",
            "working_truth_granted",
            "canonical_promotion_granted",
        ):
            self.assertIn(field, record)
        self.assertFalse(record["working_truth_granted"])
        self.assertFalse(record["canonical_promotion_granted"])

    def test_five_mandatory_body_sections_are_frozen(self):
        template = json.loads((ROOT / "templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json").read_text(encoding="utf-8"))
        self.assertEqual(
            template["mandatory_body_sections"],
            [
                "Mother question",
                "Frozen inputs and scope",
                "Hard target and required outputs",
                "Research value to preserve",
                "Success, kill, and return criteria",
            ],
        )


if __name__ == "__main__":
    unittest.main()
