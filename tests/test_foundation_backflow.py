import copy
import json
import pathlib
import unittest

from tools import check_research_common_surface as common

ROOT = pathlib.Path(__file__).resolve().parents[1]


class FoundationBackflowValidationTests(unittest.TestCase):
    def load_repository_state(self):
        backflow = json.loads((ROOT / "foundation_backflow.json").read_text(encoding="utf-8"))
        scheduler = json.loads((ROOT / "research_scheduler.json").read_text(encoding="utf-8"))
        return backflow, scheduler

    def test_repository_backflow_links_are_valid(self):
        backflow, scheduler = self.load_repository_state()
        self.assertEqual([], common.validate_backflow(backflow, scheduler))

    def test_research_link_must_target_research_task(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-005")
        link["scheduler_task_id"] = "RS-GOV-FOUNDATION-BACKFLOW"
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("requires task kind RESEARCH" in error for error in errors))

    def test_steward_integration_link_must_target_governance(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-005")
        link["scheduler_role"] = "INTEGRATION"
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("requires task kind GOVERNANCE" in error for error in errors))

    def test_research_owner_must_match_scheduler_owner(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-005")
        link["research_owner"] = "program/p018-precision-v2"
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("must match task owner" in error for error in errors))

    def test_question_links_are_unique(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        broken["question_scheduler_links"].append(copy.deepcopy(broken["question_scheduler_links"][0]))
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("duplicate question link" in error for error in errors))

    def test_authority_surfaces_must_align_with_scheduler(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        broken["surfaces"]["research_dispatch_issue"] = 999
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("research dispatch issue" in error for error in errors))

    def test_canonicalized_question_cannot_remain_active(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        canonical = broken["canonicalized_examples"][0]
        broken["question_scheduler_links"].append(
            {
                "question_id": canonical["question_id"],
                "scheduler_task_id": "RS-P022-OBSERVATION-HISTORY",
                "scheduler_role": "RESEARCH",
                "research_owner": "program/p022-geometry-v2",
                "source_refs": ["synthetic regression"],
            }
        )
        errors = common.validate_backflow(broken, scheduler)
        self.assertTrue(any("remains actively scheduled" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
