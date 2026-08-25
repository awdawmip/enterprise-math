import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_liveness_helper():
    path = ROOT / "tools" / "active_turn_liveness.py"
    spec = importlib.util.spec_from_file_location("enterprise_math_active_turn_liveness", path)
    assert spec is not None and spec.loader is not None
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


def test_machine_active_turn_contract_is_current_and_forbids_waiting_for_continue():
    data = json.loads(read("active_turn_liveness.json"))
    assert data["status"] == "ACTIVE_CANONICAL"
    assert data["schema"] == "ENTERPRISE_MATH_ACTIVE_TURN_LIVENESS_V2"
    assert data["execution_stack"] == [
        "PARENT_USER_OBJECTIVE",
        "CURRENT_SUBFLOW",
        "NEXT_EXECUTABLE_ACTION",
    ]
    assert "DETERMINISTIC_NEXT_STEP_EXISTS_IMPLIES_CONTINUE_IN_SAME_TURN" in data["core_invariants"]
    assert "PARENT_INCOMPLETE_AND_EXECUTABLE_ACTION_EXISTS_FORBIDS_FINAL_WITH_OR_WITHOUT_CONTINUATION_LEASE" in data["core_invariants"]
    assert "USER_WAKEUP_MESSAGE_MUST_NOT_BE_REQUIRED_WHEN_IT_ADDS_NO_INFORMATION" in data["core_invariants"]
    assert data["continuation_lease"]["base_liveness_dependency"] is False
    assert data["blocked_subflow_semantics"]["blocked_subflow_is_parent_blocker"] is False
    assert data["loop_safety"]["max_identical_no_progress_retry_without_transition"] == 0
    assert data["stage_rule"]["stage_terminal_requires_same_turn_successor_gate_evaluation"] is True
    assert data["pre_final_guard"]["evaluator"] == "tools/active_turn_liveness.py"
    assert data["forbidden_state"] == "WAITING_FOR_CONTINUE_WHEN_CONTINUE_ADDS_NO_INFORMATION"


def test_pre_final_guard_continues_without_continuation_lease():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(base_state(executable_next_actions=1))
    assert decision["transition"] == liveness.EXECUTE_NEXT_ACTION
    assert decision["final_allowed"] is False
    assert decision["continuation_lease_preserved"] is False


def test_pre_final_guard_continues_and_preserves_active_lease():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(
        base_state(executable_next_actions=1, continuation_lease_active=True)
    )
    assert decision["transition"] == liveness.EXECUTE_NEXT_ACTION
    assert decision["final_allowed"] is False
    assert decision["continuation_lease_preserved"] is True


def test_blocked_subflow_does_not_override_other_executable_work():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(
        base_state(parent_hard_blocker=True, executable_next_actions=1)
    )
    assert decision["transition"] == liveness.EXECUTE_NEXT_ACTION
    assert decision["final_allowed"] is False


def test_true_parent_blocker_allows_final_only_after_safe_work_exhaustion():
    liveness = load_liveness_helper()
    not_exhausted = liveness.evaluate(
        base_state(parent_hard_blocker=True, independent_safe_work_exhausted=False)
    )
    assert not_exhausted["transition"] == liveness.RECOMPUTE_PARENT_STATE
    exhausted = liveness.evaluate(
        base_state(parent_hard_blocker=True, independent_safe_work_exhausted=True)
    )
    assert exhausted["transition"] == liveness.FINAL_ALLOWED_WITH_BLOCKER
    assert exhausted["final_allowed"] is True


def test_platform_limit_allows_final_only_after_safe_work_exhaustion():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(
        base_state(platform_or_tool_hard_limit=True, independent_safe_work_exhausted=True)
    )
    assert decision["transition"] == liveness.FINAL_ALLOWED_WITH_LIMIT
    assert decision["final_allowed"] is True


def test_explicit_user_stop_is_terminal_even_when_more_actions_exist():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(
        base_state(
            user_requested_stop_pause_review_or_wait=True,
            executable_next_actions=3,
            continuation_lease_active=True,
        )
    )
    assert decision["transition"] == liveness.FINAL_ALLOWED
    assert decision["final_allowed"] is True


def test_no_progress_loop_switches_strategy_when_alternative_exists():
    liveness = load_liveness_helper()
    decision = liveness.evaluate(
        base_state(
            executable_next_actions=1,
            same_action_repeated_without_state_change=True,
            supported_alternative_available=True,
        )
    )
    assert decision["transition"] == liveness.SWITCH_STRATEGY
    assert decision["final_allowed"] is False


def test_no_progress_loop_recomputes_once_then_declares_inconsistency():
    liveness = load_liveness_helper()
    first = liveness.evaluate(
        base_state(
            executable_next_actions=1,
            same_action_repeated_without_state_change=True,
        )
    )
    assert first["transition"] == liveness.RECOMPUTE_PARENT_STATE
    second = liveness.evaluate(
        base_state(
            executable_next_actions=1,
            same_action_repeated_without_state_change=True,
            parent_state_recomputed_without_change=True,
        )
    )
    assert second["transition"] == liveness.CONTROL_STATE_INCONSISTENT
    assert second["final_allowed"] is False


def test_open_parent_with_no_action_or_blocker_recomputes_then_inconsistent():
    liveness = load_liveness_helper()
    first = liveness.evaluate(base_state(independent_safe_work_exhausted=True))
    assert first["transition"] == liveness.RECOMPUTE_PARENT_STATE
    second = liveness.evaluate(
        base_state(
            independent_safe_work_exhausted=True,
            parent_state_recomputed_without_change=True,
        )
    )
    assert second["transition"] == liveness.CONTROL_STATE_INCONSISTENT


def test_agents_routes_active_turn_contract_and_remote_silent_is_not_conversation_silent():
    text = read("AGENTS.md")
    for marker in (
        "active_turn_liveness.json",
        "docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md",
        "SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE",
        "DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN",
        "REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED",
        "REMOTE_SILENT` describes repository traffic",
    ):
        assert marker in text


def test_driver_terminal_stage_requires_same_turn_routing_evaluation():
    text = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
    assert "DRIVER_VERDICT != PARENT_OBJECTIVE_COMPLETE" in text
    assert "STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION" in text
    assert "Do **not** stop merely after writing“no next Stage opened”" not in text  # typography guard
    assert "Do **not** stop merely after writing “no next Stage opened”" in text
    assert "continue`/`do not stop`" in text
    assert "execute the next routed action in the same turn" in text


def test_remote_and_publication_subflows_resume_parent_task():
    remote = read("docs/GITHUB_INTERACTION_BUDGET.md")
    publication = read("docs/ARTIFACT_PUBLICATION_LIVENESS.md")
    assert "CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK" in remote
    assert "CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK" in remote
    assert "REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED" in remote
    assert "PUBLICATION_COMPLETE -> RESUME_PARENT_TASK" in publication
    assert "return immediately to the parent research/Driver/user objective in the same turn" in publication


def test_human_architecture_has_parent_goal_stack_and_terminal_conditions():
    text = read("docs/RESEARCH_ARCHITECTURE.md")
    assert "PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION" in text
    assert "STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION" in text
    assert "Never use `WAITING_FOR_CONTINUE`" in text
