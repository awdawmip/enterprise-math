import argparse
import json
from pathlib import Path
import tempfile
import unittest

import tools.research_taskbook as rt


class ResearchTaskbookV7Tests(unittest.TestCase):
    def make_root(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        (root / "research_tasks").mkdir()
        policy = {
            "schema": "ENTERPRISE_MATH_TASKBOOK_POLICY_SET_V4.0",
            "status": "ACTIVE",
            "policy_inputs": ["research_taskbook_contract.json"],
            "conflict_checks": [],
            "restatement_checks": [],
            "override_required_fields": [],
        }
        contract = {
            "schema": "ENTERPRISE_MATH_RESEARCH_TASKBOOK_CONTRACT_V7",
            "new_taskbook_required_metadata": {
                "created_by_role": "<one allowed author role>",
                "task_authority": "SCHEDULER_REVIEW_REQUIRED",
                "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
                "final_response_identity_policy": "INHERIT_GLOBAL",
                "origin_kind": "<one allowed origin kind>",
                "policy_review": {},
            },
            "author_contract": {
                "allowed_roles": ["RESEARCHER", "RESEARCH_DRIVER", "STEWARD"]
            },
            "task_origin_contract": {
                "free_candidate_required_fields": ["origin_candidate_id", "origin_candidate_state"],
                "free_candidate_allowed_states": [
                    "AUDITED_AXIOM_CANDIDATE",
                    "AUDITED_REPLACEMENT_CANDIDATE",
                    "EXACT_NEGATIVE_OBSTRUCTION",
                ],
                "foundation_question_required_field": "origin_foundation_question_id",
            },
            "task_lineage_contract": {
                "continuation_required_successor_gate_fields": [
                    "new_information_gap",
                    "why_parent_result_does_not_close_it",
                    "discriminating_outcomes",
                    "kill_condition",
                    "alternative_route_or_free_exploration_considered",
                    "why_new_stage_or_task_is_better_than_same_task_or_closure",
                ],
            },
            "forbidden_fixed_runtime_metadata": ["researcher_id", "driver_id", "execution_id"],
        }
        (root / "research_taskbook_policy.json").write_text(json.dumps(policy), encoding="utf-8")
        (root / "research_taskbook_contract.json").write_text(json.dumps(contract), encoding="utf-8")
        return td, root

    def write_task(self, root, *, role="RESEARCHER", authority=rt.NEW_TASK_AUTHORITY, state="PUBLISHED"):
        meta = {
            "task_id": "RS-FREE-PUBLISHED",
            "title": "Free published task",
            "kind": "RESEARCH",
            "owner": "taskbook/unassigned",
            "base_state": state,
            "priority": "P1",
            "leverage": "HIGH",
            "frontier": "prove or refute X",
            "next_action": "test X",
            "created_by_role": role,
            "task_authority": authority,
            "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
            "final_response_identity_policy": "INHERIT_GLOBAL",
            "origin_kind": "DIRECT_USER_DIRECTION",
            "task_lineage": "NEW_DIRECTION",
            "policy_review": {
                "policy_set": "research_taskbook_policy.json",
                "policy_digest": rt.policy_digest(root),
                "review_state": "PASS",
                "temporary_overrides": [],
            },
        }
        path = root / "research_tasks" / "FREE.md"
        path.write_text(rt.render_taskbook(meta, "# Work\n"), encoding="utf-8")
        return path

    def test_researcher_authored_taskbook_is_publishable(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root, role="RESEARCHER")
        self.assertEqual([], rt.audit_taskbook(path, root=root, publish=True))

    def test_steward_authored_taskbook_is_publishable(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root, role="STEWARD")
        self.assertEqual([], rt.audit_taskbook(path, root=root, publish=True))

    def test_legacy_driver_approved_authority_cannot_be_newly_published(self):
        td, root = self.make_root()
        self.addCleanup(td.cleanup)
        path = self.write_task(root, role="RESEARCH_DRIVER", authority=rt.LEGACY_TASK_AUTHORITY)
        codes = {item["code"] for item in rt.audit_taskbook(path, root=root, publish=True)}
        self.assertIn("TB-LEGACY-AUTHORITY", codes)

    def test_new_metadata_never_starts_ready(self):
        # base_metadata reads policy from the repository ROOT; only inspect the fixed state/authority
        args = argparse.Namespace(
            task_id="RS-X",
            title="X",
            kind="RESEARCH",
            priority="P1",
            leverage="HIGH",
            lane="X",
            author_role="RESEARCHER",
            origin_kind="DIRECT_USER_DIRECTION",
            origin_candidate_id=None,
            origin_candidate_state=None,
            origin_foundation_question_id=None,
            lineage="NEW_DIRECTION",
            parent_task_id=None,
        )
        meta = rt.base_metadata(args)
        self.assertEqual("DRAFT", meta["base_state"])
        self.assertEqual("RESEARCHER", meta["created_by_role"])
        self.assertEqual("SCHEDULER_REVIEW_REQUIRED", meta["task_authority"])
        self.assertNotEqual("READY", meta["base_state"])


if __name__ == "__main__":
    unittest.main()
