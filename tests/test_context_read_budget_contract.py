import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ContextReadBudgetContractTests(unittest.TestCase):
    def test_canonical_policy_blocks_unbounded_conversational_reads(self):
        policy = json.loads((ROOT / "research_context_budget.json").read_text(encoding="utf-8"))
        self.assertEqual("ENTERPRISE_MATH_CONTEXT_READ_BUDGET_V1", policy["schema"])
        self.assertEqual("ACTIVE_CANONICAL", policy["status"])
        invariants = policy["invariants"]
        self.assertEqual("FORBIDDEN", invariants["UNBOUNDED_COLLECTION_READ_FOR_DISCOVERY"])
        self.assertEqual("FORBIDDEN", invariants["RECURSIVE_REPOSITORY_TREE_IN_CONVERSATIONAL_CONTEXT"])
        self.assertEqual("FORBIDDEN", invariants["HIGH_FANOUT_DIRECTORY_ENUMERATION_FOR_DISCOVERY"])
        self.assertEqual("FORBIDDEN", invariants["ISSUE_240_ALL_COMMENTS_IN_CONVERSATIONAL_CONTEXT"])
        self.assertFalse(invariants["TRUNCATION_OR_COMPACTION_IS_A_STOP_BOUNDARY"])
        self.assertLessEqual(policy["bounded_defaults"]["search_results_max"], 20)
        self.assertLessEqual(policy["bounded_defaults"]["file_line_range_soft_max"], 200)
        self.assertLessEqual(policy["bounded_defaults"]["issue_comment_page_size_max"], 20)
        self.assertIn("tests/", policy["high_fanout_paths"])
        self.assertIn("research_tasks/", policy["high_fanout_paths"])

    def test_router_and_github_budget_expose_the_hard_guard(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        github_budget = (ROOT / "docs" / "GITHUB_INTERACTION_BUDGET.md").read_text(encoding="utf-8")
        for text in (agents, github_budget):
            self.assertIn("research_context_budget.json", text)
            self.assertIn("UNBOUNDED_COLLECTION_READ_FOR_DISCOVERY", text)
        self.assertIn("Issue #240", github_budget)
        self.assertIn("tests/", github_budget)
        self.assertIn("context compaction", github_budget.lower())


if __name__ == "__main__":
    unittest.main()
