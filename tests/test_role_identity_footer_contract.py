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


def test_machine_policy_requires_every_research_role_final_exactly_once():
    policy = json.loads(read("final_response_identity_policy.json"))
    assert policy["status"] == "ACTIVE"
    assert policy["core_invariant"] == (
        "ACTIVE_ENTERPRISE_MATH_RESEARCH_ROLE -> "
        "EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER"
    )
    assert "CONTROL_PLANE_MAINTENANCE" in policy["non_research_modes"]
    assert policy["control_plane_finalization"]["research_role_footer_required"] is False
    assert policy["ordering"]["identity_marker_count"] == 1
    assert policy["registration_pending_does_not_suppress_marker"] is True
    assert policy["templates"]["RESEARCH_DRIVER"] == "Driver-ID: <ID> / CONTROL_PLANE"
    assert policy["templates"]["RESEARCHER_TASK"] == "Researcher-ID: <ID> / <TASK_ID>"
    assert policy["templates"]["RESEARCHER_FREE"] == (
        "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY"
    )
    assert policy["templates"]["RESEARCHER_DIRECT_TASK_FALLBACK"] == (
        "Researcher-ID: <ID> / TASK_RESEARCH"
    )


def test_hot_router_matches_research_role_footer_scope_and_control_exclusion():
    text = read("AGENTS.md")
    assert "final_response_identity_policy.json" in text
    assert (
        "ACTIVE_ENTERPRISE_MATH_RESEARCH_ROLE -> "
        "EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER"
        in text
    )
    assert "`CONTROL_PLANE_MAINTENANCE` alone does not activate a research-role identity marker." in text
    assert "Driver-ID: <ID> / CONTROL_PLANE" in text
    assert "Researcher-ID: <ID> / <TASK_ID>" in text
    assert "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY" in text
    assert "Researcher-ID: <ID> / TASK_RESEARCH" in text
    assert "Do not use `DIRECT` as a visible researcher scope" in text


def test_role_policy_has_no_substantive_final_escape_hatch():
    policy = json.loads(read("research_role_policy.json"))
    identity = policy["research_identity"]
    assert policy["schema"] == "ENTERPRISE_MATH_RESEARCH_ROLE_POLICY_V10"
    assert identity["final_response_policy"] == "final_response_identity_policy.json"
    combined = "\n".join(identity["rules"])
    assert "Every assistant final response" in combined
    assert "Every substantive final" not in combined
    assert identity["visible_markers"]["RESEARCH_DRIVER"] == (
        "Driver-ID: <ID> / CONTROL_PLANE"
    )
    assert identity["visible_markers"]["RESEARCHER_FREE"] == (
        "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY"
    )


def test_identity_state_machine_binds_resolution_to_final_visibility():
    machine = json.loads(read("research_identity_state_machine.json"))
    assert machine["schema"] == "ENTERPRISE_MATH_RESEARCH_IDENTITY_STATE_MACHINE_V5"
    assert machine["final_response_policy"] == "final_response_identity_policy.json"
    assert "every assistant final response" in machine["final_response_invariant"]
    assert machine["final_response"]["marker_count"] == 1
    assert machine["final_response"]["researcher_scope_precedence"] == [
        "ACTIVE_TASK_ID",
        "FREE_AXIOM_DISCOVERY",
        "TASK_RESEARCH",
    ]
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


def test_free_and_driver_role_specific_contracts_share_current_footer_policy():
    free = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    driver = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
    assert "final_response_identity_policy.json" in free
    assert "ACTIVE_EM_FREE_RESEARCHER -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_RESEARCHER_ID_MARKER" in free
    assert "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY" in free
    assert "End with:" in driver
    assert "Driver-ID: <ID> / CONTROL_PLANE" in driver
