import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_identity():
    spec = importlib.util.spec_from_file_location(
        "research_identity_footer_test", ROOT / "tools" / "research_identity.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_machine_policy_marker_is_optional_and_grants_no_authority():
    policy = json.loads(read("final_response_identity_policy.json"))
    assert policy["status"] == "ACTIVE"
    assert policy["ordering"]["marker_required"] is False
    assert policy["identity_resolution_before_final"] is False
    assert policy["pre_final_permission_gate"]["registration_authentication_required"] is True
    assert policy["pre_final_permission_gate"]["caller_supplied_parent_status_is_authority"] is False
    assert policy["templates"]["RESEARCH_DRIVER"] == "Driver-ID: <ID> / CONTROL_PLANE"


def test_hot_router_routes_instead_of_repeating_footer_rules():
    text = read("AGENTS.md")
    assert "CONTRIBUTING.md#agentproject-task-entry" in text
    assert "EVERY_ASSISTANT_FINAL_RESPONSE" not in text


def test_role_policy_keeps_identity_and_makes_footer_optional():
    policy = json.loads(read("research_role_policy.json"))
    identity = policy["research_identity"]
    assert identity["final_response_policy"] == "final_response_identity_policy.json"
    assert "optional communication" in "\n".join(identity["rules"])
    assert identity["visible_markers"]["RESEARCH_DRIVER"] == "Driver-ID: <ID> / CONTROL_PLANE"


def test_identity_state_machine_keeps_actual_scope_without_footer_requirement():
    machine = json.loads(read("research_identity_state_machine.json"))
    assert machine["final_response"]["marker_required"] is False
    assert machine["final_response"]["researcher_scope_precedence"] == ["ACTIVE_TASK_ID", "FREE_AXIOM_DISCOVERY", "TASK_RESEARCH"]
    assert machine["final_response"]["direct_is_not_visible_scope"] is True
    assert machine["final_response"]["commentary_progress_exempt"] is True


def test_helper_emits_canonical_driver_task_free_and_direct_markers():
    identity = load_identity()
    assert identity.visible_marker(
        "EM-DVR-Q4N7", role="RESEARCH_DRIVER"
    ) == "Driver-ID: EM-DVR-Q4N7 / CONTROL_PLANE"
    assert identity.visible_marker(
        "EM-R020-ABC123", role="RESEARCHER", task_id="RS-R020-TEST"
    ) == "Researcher-ID: EM-R020-ABC123 / RS-R020-TEST"
    assert identity.visible_marker(
        "EM-FREE-7A2C",
        role="RESEARCHER",
        research_mode="FREE_AXIOM_DISCOVERY",
    ) == "Researcher-ID: EM-FREE-7A2C / FREE_AXIOM_DISCOVERY"
    assert identity.visible_marker(
        "EM-DIRECT-7A2C", role="RESEARCHER"
    ) == "Researcher-ID: EM-DIRECT-7A2C / TASK_RESEARCH"


def test_explicit_task_scope_beats_mode_and_direct_never_leaks_to_marker():
    identity = load_identity()
    marker = identity.visible_marker(
        "EM-R020-ABC123",
        role="RESEARCHER",
        task_id="RS-R020-TEST",
        research_mode="FREE_AXIOM_DISCOVERY",
    )
    assert marker == "Researcher-ID: EM-R020-ABC123 / RS-R020-TEST"
    payload = identity.identity_payload(
        execution_id="EM-DIRECT-7A2C",
        task_id=None,
        role="RESEARCHER",
        source="DIRECT_AUTO_GENERATED",
    )
    assert payload["visible_scope"] == "TASK_RESEARCH"
    assert payload["visible_marker"].endswith("/ TASK_RESEARCH")
    assert "/ DIRECT" not in payload["visible_marker"]


def test_role_documents_keep_optional_markers():
    free = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    driver = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
    assert "final_response_identity_policy.json" in free
    assert "Optional identity marker" in free
    assert "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY" in free
    assert "optional identity marker" in driver
    assert "Driver-ID: <ID> / CONTROL_PLANE" in driver
