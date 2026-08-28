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
        self.assertLessEqual(policy["bounded_defaults"]["matching_test_files_soft_max"], 3)
        self.assertIn("tests/", policy["high_fanout_paths"])
        self.assertIn("research_tasks/", policy["high_fanout_paths"])

    def test_high_fanout_sources_have_explicit_bounded_read_intents(self):
        policy = json.loads((ROOT / "research_context_budget.json").read_text(encoding="utf-8"))
        guidance = policy["collection_read_guidance"]

        tests = guidance["tests"]
        self.assertIn("LOCATE_EXISTING_REGRESSION_TEST_HOME", tests["purpose"])
        self.assertIn("DIRECTORY_ENUMERATION_TO_FIND_ONE_TEST", tests["not_for"])
        self.assertEqual("SEARCH_BY_TARGET_COMPONENT_SYMBOL_OR_ERROR_TEXT", tests["safe_sequence"][0])
        self.assertIn("OPEN_ONE_TO_THREE_MATCHING_TEST_FILES", tests["safe_sequence"])

        issue = guidance["issue_240"]
        self.assertIn("VERIFY_RUNTIME_EVENT_LINEAGE_FOR_A_SPECIFIC_TASK_OR_CLAIM", issue["purpose"])
        self.assertIn("READ_GITHUB_SERVER_CREATED_AT_FOR_AUTHORITATIVE_EVENT_TIME", issue["purpose"])
        self.assertIn("LOADING_THE_FULL_SCHEDULER_HISTORY_INTO_CONTEXT", issue["not_for"])
        self.assertEqual("GITHUB_SERVER_CREATED_AT", issue["authoritative_clock"])
        self.assertEqual("DESCRIPTIVE_ONLY", issue["body_declared_clock"])

    def test_router_and_github_budget_expose_the_hard_guard(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        github_budget = (ROOT / "docs" / "GITHUB_INTERACTION_BUDGET.md").read_text(encoding="utf-8")
        for text in (agents, github_budget):
            self.assertIn("research_context_budget.json", text)
            self.assertIn("UNBOUNDED_COLLECTION_READ_FOR_DISCOVERY", text)
        self.assertIn("Issue #240", github_budget)
        self.assertIn("tests/", github_budget)
        self.assertIn("regression placement", github_budget.lower())
        self.assertIn("scheduler runtime evidence", github_budget.lower())
        self.assertIn("context compaction", github_budget.lower())


if __name__ == "__main__":
    unittest.main()
