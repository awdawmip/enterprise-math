import copy
import json
import pathlib
import unittest

from tools import foundation_backflow as fb

ROOT = pathlib.Path(__file__).resolve().parents[1]


class FoundationBackflowValidationTests(unittest.TestCase):
    def load_repository_state(self):
        backflow = json.loads((ROOT / "foundation_backflow.json").read_text(encoding="utf-8"))
        scheduler = json.loads((ROOT / "research_scheduler.json").read_text(encoding="utf-8"))
        return backflow, scheduler

    def test_repository_backflow_links_are_valid(self):
        backflow, scheduler = self.load_repository_state()
        self.assertEqual([], fb.validate_backflow(backflow, scheduler))

    def test_research_link_must_target_research_task(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-005")
        link["scheduler_task_id"] = "RS-GOV-FOUNDATION-BACKFLOW"
        errors = fb.validate_backflow(broken, scheduler)
        self.assertTrue(any("requires task kind RESEARCH" in error for error in errors))

    def test_steward_integration_link_must_target_governance(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-004")
        link["scheduler_task_id"] = "RS-P022-OBSERVATION-HISTORY"
        errors = fb.validate_backflow(broken, scheduler)
        self.assertTrue(any("requires task kind GOVERNANCE" in error for error in errors))

    def test_research_owner_must_match_scheduler_owner(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        link = next(item for item in broken["question_scheduler_links"] if item["question_id"] == "FQ-20260809-005")
        link["research_owner"] = "program/p018-precision-v2"
        errors = fb.validate_backflow(broken, scheduler)
        self.assertTrue(any("must match task owner" in error for error in errors))

    def test_question_links_are_unique(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        broken["question_scheduler_links"].append(copy.deepcopy(broken["question_scheduler_links"][0]))
        errors = fb.validate_backflow(broken, scheduler)
        self.assertTrue(any("duplicate question link" in error for error in errors))

    def test_authority_surfaces_must_align_with_scheduler(self):
        backflow, scheduler = self.load_repository_state()
        broken = copy.deepcopy(backflow)
        broken["surfaces"]["research_dispatch_issue"] = 999
        errors = fb.validate_backflow(broken, scheduler)
        self.assertTrue(any("research dispatch issue" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
