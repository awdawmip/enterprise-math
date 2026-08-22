import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_machine_active_turn_contract_is_current_and_forbids_waiting_for_continue():
    data = json.loads(read("active_turn_liveness.json"))
    assert data["status"] == "ACTIVE_CANONICAL"
    assert data["execution_stack"] == [
        "PARENT_USER_OBJECTIVE",
        "CURRENT_SUBFLOW",
        "NEXT_EXECUTABLE_ACTION",
    ]
    assert "DETERMINISTIC_NEXT_STEP_EXISTS_IMPLIES_CONTINUE_IN_SAME_TURN" in data["core_invariants"]
    assert "USER_WAKEUP_MESSAGE_MUST_NOT_BE_REQUIRED_WHEN_IT_ADDS_NO_INFORMATION" in data["core_invariants"]
    assert data["stage_rule"]["stage_terminal_requires_same_turn_successor_gate_evaluation"] is True
    assert data["forbidden_state"] == "WAITING_FOR_CONTINUE_WHEN_CONTINUE_ADDS_NO_INFORMATION"


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
