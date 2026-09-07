import copy
import json
import pathlib
import unittest

from control_plane import research_control_bootstrap as bootstrap
from tools import check_research_common_surface as common
from tools import research_dispatch

ROOT = pathlib.Path(__file__).resolve().parents[1]
RESEARCH_TASK = "RS-TEST-BACKFLOW-RESEARCH"
GOVERNANCE_TASK = "RS-TEST-BACKFLOW-GOVERNANCE"
UNRELATED_TASK = "RS-TEST-BACKFLOW-UNRELATED"
RESEARCH_OWNER = "synthetic/backflow-research-owner"
ACTIVE_FQ = "FQ-20990101-001"
CANONICAL_FQ = "FQ-20990101-004"


def synthetic_state():
    """In-memory validator inputs only; no task/FQ publication or legacy file."""
    runtime_policy = {
        "schema": "ENTERPRISE_MATH_RESEARCH_RUNTIME_POLICY_V2",
        "status": "ACTIVE_CANONICAL",
        "task_definition_source": "IMMUTABLE_V2_TASK_PUBLICATIONS",
        "legacy_task_definition_source": None,
        "legacy_runtime_on_main": False,
        "runtime_issue": 240,
    }
    tasks = [
        {
            "task_id": RESEARCH_TASK,
            "kind": "RESEARCH",
            "owner": RESEARCH_OWNER,
            "foundation_questions": [ACTIVE_FQ, CANONICAL_FQ],
        },
        {
            "task_id": GOVERNANCE_TASK,
            "kind": "GOVERNANCE",
            "owner": "synthetic/backflow-steward",
        },
        {
            "task_id": UNRELATED_TASK,
            "kind": "RESEARCH",
            "owner": RESEARCH_OWNER,
            "foundation_questions": ["FQ-20990101-005"],
        },
    ]
    backflow = {
        "schema": "ENTERPRISE_MATH_FOUNDATION_BACKFLOW_V1",
        "status": "ACTIVE",
        "surfaces": {
            "research_relay_issue": 82,
            "foundation_problem_issue": 164,
            "research_dispatch_issue": 240,
            "canonical_dispatch": "tools/research_dispatch.py",
            "dispatch_contract": "research_dispatch_contract.json",
            "task_record_store": "research_task_records/<task-id>/<publication-id>.json",
            "legacy_scheduler_config": "research_runtime_policy_v2.json",
            "runtime_event_reducer": "tools/research_runtime_reducer.py",
        },
        "feedback_packet_fields": [
            "candidate_object_or_tool", "weakest_scope_hypotheses",
            "minimal_state", "minimal_repair_or_extension", "negative_boundary",
            "cross_route_evidence", "proof_status", "tool_surface",
            "prior_art_and_owner", "foundation_destination",
        ],
        "handling_classes": [
            "DIRECT_FOUNDATION_MAINTENANCE", "FOUNDATION_QUESTION",
            "APPLICATION_LOCAL_OR_NOT_READY",
        ],
        "scheduler_link_contract": {
            "research_task_question_field": "foundation_questions",
            "task_definition_authority": "IMMUTABLE_V2_TASK_PUBLICATIONS_WITH_FAULT_ISOLATION",
            "task_definition_tool": "tools/research_dispatch.py",
            "new_foundation_task_requires_immutable_registration": True,
        },
        "question_scheduler_links": [
            {
                "question_id": ACTIVE_FQ,
                "scheduler_task_id": RESEARCH_TASK,
                "scheduler_role": "RESEARCH",
                "research_owner": RESEARCH_OWNER,
                "source_refs": ["synthetic in-memory research fixture"],
            },
            {
                "question_id": "FQ-20990101-002",
                "scheduler_task_id": GOVERNANCE_TASK,
                "scheduler_role": "INTEGRATION",
                "source_refs": ["synthetic in-memory integration fixture"],
            },
            {
                "question_id": "FQ-20990101-003",
                "scheduler_task_id": GOVERNANCE_TASK,
                "scheduler_role": "STEWARD_VERIFICATION",
                "source_refs": ["synthetic in-memory stewardship fixture"],
            },
        ],
        "canonicalized_examples": [
            {"question_id": CANONICAL_FQ, "canonical_merge": "synthetic-test-only"},
        ],
        "authority_boundaries": {"canonical_truth": "gated source-repository main"},
    }
    return backflow, runtime_policy, tasks


class FoundationBackflowIntegrationTests(unittest.TestCase):
    def test_repository_backflow_links_are_valid(self):
        # Match the current public checker input: runtime policy plus immutable
        # dispatch definitions with the canonical, exact isolation installed.
        bootstrap.install(ROOT)
        backflow = json.loads((ROOT / "foundation_backflow.json").read_text(encoding="utf-8"))
        runtime_policy = json.loads((ROOT / "research_runtime_policy_v2.json").read_text(encoding="utf-8"))
        tasks = research_dispatch.merged_definitions(ROOT)
        self.assertTrue(tasks)
        self.assertEqual("IMMUTABLE_V2_TASK_PUBLICATIONS", runtime_policy["task_definition_source"])
        self.assertEqual([], common.validate_backflow(backflow, runtime_policy, tasks))


class FoundationBackflowValidationTests(unittest.TestCase):
    def setUp(self):
        self.backflow, self.runtime_policy, self.tasks = synthetic_state()
        # Negative cases must start from valid, nonempty active links even when
        # all real repository FQs have moved to answered/canonicalized history.
        self.assertEqual(3, len(self.backflow["question_scheduler_links"]))
        self.assertEqual([], common.validate_backflow(self.backflow, self.runtime_policy, self.tasks))

    def test_synthetic_research_and_governance_links_are_valid(self):
        self.assertEqual(
            {"RESEARCH", "INTEGRATION", "STEWARD_VERIFICATION"},
            {link["scheduler_role"] for link in self.backflow["question_scheduler_links"]},
        )

    def test_research_link_must_target_research_task(self):
        self.tasks[0]["kind"] = "GOVERNANCE"
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("requires task kind RESEARCH" in error for error in errors))

    def test_steward_integration_link_must_target_governance(self):
        for role in ("STEWARD_VERIFICATION", "INTEGRATION"):
            with self.subTest(role=role):
                broken = copy.deepcopy(self.backflow)
                broken["question_scheduler_links"][0]["scheduler_role"] = role
                errors = common.validate_backflow(broken, self.runtime_policy, self.tasks)
                self.assertTrue(any("requires task kind GOVERNANCE" in error for error in errors))

    def test_research_owner_must_match_task_owner(self):
        self.backflow["question_scheduler_links"][0]["research_owner"] = "synthetic/other-owner"
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("must match task owner" in error for error in errors))

    def test_same_owner_but_unrelated_task_cannot_carry_fq(self):
        self.backflow["question_scheduler_links"][0]["scheduler_task_id"] = UNRELATED_TASK
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("must explicitly declare" in error for error in errors))

    def test_research_task_must_explicitly_declare_fq(self):
        self.tasks[0].pop("foundation_questions")
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("must explicitly declare" in error for error in errors))

    def test_question_links_are_unique(self):
        self.backflow["question_scheduler_links"].append(
            copy.deepcopy(self.backflow["question_scheduler_links"][0])
        )
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("duplicate question link" in error for error in errors))

    def test_authority_surfaces_must_align_with_runtime_policy(self):
        self.backflow["surfaces"]["research_dispatch_issue"] = 999
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("research dispatch issue" in error for error in errors))

    def test_canonicalized_question_cannot_remain_active(self):
        self.backflow["question_scheduler_links"].append(
            {
                "question_id": CANONICAL_FQ,
                "scheduler_task_id": RESEARCH_TASK,
                "scheduler_role": "RESEARCH",
                "research_owner": RESEARCH_OWNER,
                "source_refs": ["synthetic in-memory canonicalized reactivation"],
            }
        )
        errors = common.validate_backflow(self.backflow, self.runtime_policy, self.tasks)
        self.assertTrue(any("remains actively scheduled" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
