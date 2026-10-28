import importlib.util
import json
import unittest
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_liveness_helper():
    path = ROOT / "tools" / "active_turn_liveness.py"
    spec = importlib.util.spec_from_file_location("enterprise_math_active_turn_liveness", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load active_turn_liveness helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def base_state(**overrides):
    state = {
        "parent_objective_complete": False,
        "user_requested_stop_pause_review_or_wait": False,
        "parent_hard_blocker": False,
        "platform_or_tool_hard_limit": False,
        "independent_safe_work_exhausted": False,
        "same_action_repeated_without_state_change": False,
        "supported_alternative_available": False,
        "parent_state_recomputed_without_change": False,
        "executable_next_actions": 0,
        "continuation_lease_active": False,
    }
    state.update(overrides)
    return state


class ActiveTurnContinuationLivenessTests(unittest.TestCase):
    def test_machine_active_turn_contract_is_current(self):
        data = json.loads(read("active_turn_liveness.json"))
        self.assertEqual("ACTIVE_CANONICAL", data["status"])
        self.assertEqual("ENTERPRISE_MATH_ACTIVE_TURN_LIVENESS_V2", data["schema"])
        self.assertEqual(
            ["PARENT_USER_OBJECTIVE", "CURRENT_SUBFLOW", "NEXT_EXECUTABLE_ACTION"],
            data["execution_stack"],
        )
        for marker in (
            "DETERMINISTIC_NEXT_STEP_EXISTS_IMPLIES_CONTINUE_IN_SAME_TURN",
            "PARENT_INCOMPLETE_AND_EXECUTABLE_ACTION_EXISTS_FORBIDS_FINAL_WITH_OR_WITHOUT_CONTINUATION_LEASE",
            "USER_WAKEUP_MESSAGE_MUST_NOT_BE_REQUIRED_WHEN_IT_ADDS_NO_INFORMATION",
            "USER_INTERRUPT_PREEMPTS_NONESSENTIAL_DIAGNOSTIC_EXPANSION",
            "CONTROL_PLANE_INSPECTION_STOPS_AT_SUFFICIENT_EVIDENCE",
            "READ_SNAPSHOT_IS_NOT_WRITE_AUTHORITY",
            "LONG_RESEARCH_COMPUTE_IS_NOT_CONTROL_PLANE_NO_PROGRESS",
        ):
            self.assertIn(marker, data["core_invariants"])
        self.assertIn("CONTROL_PLANE_MAINTENANCE", data["scope"])
        self.assertFalse(data["continuation_lease"]["base_liveness_dependency"])
        self.assertFalse(data["blocked_subflow_semantics"]["blocked_subflow_is_parent_blocker"])
        self.assertEqual(0, data["loop_safety"]["max_identical_no_progress_retry_without_transition"])
        self.assertTrue(data["stage_rule"]["stage_terminal_requires_same_turn_successor_gate_evaluation"])
        self.assertEqual("tools/active_turn_liveness.py", data["pre_final_guard"]["evaluator"])

    def test_soft_watchdog_is_progress_not_wall_clock_based(self):
        data = json.loads(read("active_turn_liveness.json"))
        policy = data["control_plane_efficiency"]
        self.assertEqual("COOPERATIVE_SOFT_WATCHDOG", policy["model"])
        self.assertFalse(policy["hard_wall_clock_limit"])
        self.assertTrue(policy["research_compute_may_be_long_if_semantic_frontier_advances"])
        self.assertEqual({"min": 2, "max": 3}, policy["default_control_cycle_tool_calls"])
        self.assertEqual(2, policy["max_consecutive_tool_results_without_material_state_change"])
        self.assertEqual(
            "STOP_SAME_INSPECTION_PATH_AND_RETURN_CURRENT_RESULT_OR_SWITCH_STRATEGY",
            policy["after_two_no_progress_results"],
        )
        self.assertEqual("COLLAPSE_TO_ONE_ROOT_CAUSE", policy["same_error_signature"]["rule"])
        self.assertEqual("STOP_DIAGNOSTIC_EXPANSION", policy["sufficient_evidence"]["rule"])

    def test_pre_final_guard_continues_without_continuation_lease(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(base_state(executable_next_actions=1))
        self.assertEqual(liveness.EXECUTE_NEXT_ACTION, decision["transition"])
        self.assertFalse(decision["final_allowed"])
        self.assertFalse(decision["continuation_lease_preserved"])

    def test_pre_final_guard_continues_and_preserves_active_lease(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(executable_next_actions=1, continuation_lease_active=True)
        )
        self.assertEqual(liveness.EXECUTE_NEXT_ACTION, decision["transition"])
        self.assertFalse(decision["final_allowed"])
        self.assertTrue(decision["continuation_lease_preserved"])

    def test_blocked_subflow_does_not_override_other_executable_work(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(parent_hard_blocker=True, executable_next_actions=1)
        )
        self.assertEqual(liveness.EXECUTE_NEXT_ACTION, decision["transition"])
        self.assertFalse(decision["final_allowed"])

    def test_true_parent_blocker_allows_final_only_after_safe_work_exhaustion(self):
        liveness = load_liveness_helper()
        not_exhausted = liveness.evaluate(
            base_state(parent_hard_blocker=True, independent_safe_work_exhausted=False)
        )
        self.assertEqual(liveness.RECOMPUTE_PARENT_STATE, not_exhausted["transition"])
        exhausted = liveness.evaluate(
            base_state(parent_hard_blocker=True, independent_safe_work_exhausted=True)
        )
        self.assertEqual(liveness.FINAL_ALLOWED_WITH_BLOCKER, exhausted["transition"])
        self.assertTrue(exhausted["final_allowed"])

    def test_terminal_blocker_preserves_active_continuation_lease(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(
                parent_hard_blocker=True,
                independent_safe_work_exhausted=True,
                continuation_lease_active=True,
            )
        )
        self.assertEqual(liveness.FINAL_ALLOWED_WITH_BLOCKER, decision["transition"])
        self.assertTrue(decision["continuation_lease_preserved"])

    def test_claimed_safe_work_after_unchanged_recompute_is_inconsistent(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(
                independent_safe_work_exhausted=False,
                parent_state_recomputed_without_change=True,
            )
        )
        self.assertEqual(liveness.CONTROL_STATE_INCONSISTENT, decision["transition"])
        self.assertFalse(decision["final_allowed"])
        self.assertEqual(
            "REBUILD_CONTROL_STATE_FROM_AUTHORITATIVE_PARENT_OBJECTIVE",
            decision["required_action"],
        )

    def test_platform_limit_allows_final_only_after_safe_work_exhaustion(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(platform_or_tool_hard_limit=True, independent_safe_work_exhausted=True)
        )
        self.assertEqual(liveness.FINAL_ALLOWED_WITH_LIMIT, decision["transition"])
        self.assertTrue(decision["final_allowed"])

    def test_explicit_user_stop_is_terminal_even_when_more_actions_exist(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(
                user_requested_stop_pause_review_or_wait=True,
                executable_next_actions=3,
                continuation_lease_active=True,
            )
        )
        self.assertEqual(liveness.FINAL_ALLOWED, decision["transition"])
        self.assertTrue(decision["final_allowed"])

    def test_no_progress_loop_switches_strategy_when_alternative_exists(self):
        liveness = load_liveness_helper()
        decision = liveness.evaluate(
            base_state(
                executable_next_actions=1,
                same_action_repeated_without_state_change=True,
                supported_alternative_available=True,
            )
        )
        self.assertEqual(liveness.SWITCH_STRATEGY, decision["transition"])
        self.assertFalse(decision["final_allowed"])

    def test_no_progress_loop_recomputes_once_then_declares_inconsistency(self):
        liveness = load_liveness_helper()
        first = liveness.evaluate(
            base_state(executable_next_actions=1, same_action_repeated_without_state_change=True)
        )
        self.assertEqual(liveness.RECOMPUTE_PARENT_STATE, first["transition"])
        second = liveness.evaluate(
            base_state(
                executable_next_actions=1,
                same_action_repeated_without_state_change=True,
                parent_state_recomputed_without_change=True,
            )
        )
        self.assertEqual(liveness.CONTROL_STATE_INCONSISTENT, second["transition"])
        self.assertFalse(second["final_allowed"])

    def test_open_parent_with_no_action_or_blocker_recomputes_then_inconsistent(self):
        liveness = load_liveness_helper()
        first = liveness.evaluate(base_state(independent_safe_work_exhausted=True))
        self.assertEqual(liveness.RECOMPUTE_PARENT_STATE, first["transition"])
        second = liveness.evaluate(
            base_state(
                independent_safe_work_exhausted=True,
                parent_state_recomputed_without_change=True,
            )
        )
        self.assertEqual(liveness.CONTROL_STATE_INCONSISTENT, second["transition"])

    def test_exhaustive_boolean_guard_never_allows_premature_final(self):
        liveness = load_liveness_helper()
        bool_keys = [
            "parent_hard_blocker",
            "platform_or_tool_hard_limit",
            "independent_safe_work_exhausted",
            "same_action_repeated_without_state_change",
            "supported_alternative_available",
            "parent_state_recomputed_without_change",
            "continuation_lease_active",
        ]
        for bits in product((False, True), repeat=len(bool_keys)):
            overrides = dict(zip(bool_keys, bits, strict=True))
            with_action = liveness.evaluate(base_state(executable_next_actions=1, **overrides))
            self.assertFalse(with_action["final_allowed"])
            if not overrides["independent_safe_work_exhausted"]:
                without_action = liveness.evaluate(base_state(executable_next_actions=0, **overrides))
                self.assertFalse(without_action["final_allowed"])

    def test_every_transition_has_exact_required_action(self):
        liveness = load_liveness_helper()
        self.assertEqual(set(liveness.REQUIRED_ACTIONS), set(liveness.TRANSITIONS))
        self.assertEqual(
            "EXECUTE_SELECTED_NEXT_ACTION_NOW",
            liveness.REQUIRED_ACTIONS[liveness.EXECUTE_NEXT_ACTION],
        )
        self.assertEqual(
            "TAKE_DIFFERENT_SUPPORTED_ROUTE_NOW",
            liveness.REQUIRED_ACTIONS[liveness.SWITCH_STRATEGY],
        )
        self.assertEqual(
            "RECOMPUTE_PARENT_ROUTING_ONCE",
            liveness.REQUIRED_ACTIONS[liveness.RECOMPUTE_PARENT_STATE],
        )
        self.assertEqual(
            "REBUILD_CONTROL_STATE_FROM_AUTHORITATIVE_PARENT_OBJECTIVE",
            liveness.REQUIRED_ACTIONS[liveness.CONTROL_STATE_INCONSISTENT],
        )

    def test_agents_routes_liveness_and_remote_silence_correctly(self):
        text = read("AGENTS.md")
        for marker in (
            "active_turn_liveness.json",
            "docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md",
            "SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE",
            "DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN",
            "REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED",
            "REMOTE_SILENT` describes repository traffic",
            "USER_INTERRUPT -> PREEMPT_NONESSENTIAL_DIAGNOSTIC_EXPANSION",
        ):
            self.assertIn(marker, text)

    def test_driver_terminal_stage_requires_same_turn_routing_evaluation(self):
        text = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
        self.assertIn("DRIVER_VERDICT != PARENT_OBJECTIVE_COMPLETE", text)
        self.assertIn("STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION", text)
        self.assertIn("Local route closure", text if "Local route closure" in text else "Local route closure is not parent-goal closure")
        self.assertIn("execute the next routed action in the same turn", text)

    def test_remote_and_publication_subflows_resume_parent_task(self):
        remote = read("docs/GITHUB_INTERACTION_BUDGET.md")
        publication = read("docs/ARTIFACT_PUBLICATION_LIVENESS.md")
        self.assertIn("CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK", remote)
        self.assertIn("CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK", remote)
        self.assertIn("REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED", remote)
        self.assertIn("PUBLICATION_COMPLETE -> RESUME_PARENT_TASK", publication)
        self.assertIn(
            "return immediately to the parent research/Driver/user objective in the same turn",
            publication,
        )

    def test_human_architecture_has_current_runtime_and_terminal_conditions(self):
        text = read("docs/RESEARCH_ARCHITECTURE.md")
        self.assertIn("ACTIVE / CANONICAL GOVERNANCE / V2.6", text)
        self.assertIn("research_control_dispatch.py", text)
        self.assertIn("STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_SAME_CLAIM", text)
        self.assertIn("TOOL_COVERAGE_LOOKUP != TOOL_USE", text)
        self.assertIn("Never use `WAITING_FOR_CONTINUE`", text)


if __name__ == "__main__":
    unittest.main()
