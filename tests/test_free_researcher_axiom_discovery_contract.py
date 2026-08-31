import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLE = ROOT / "research_roles" / "EM_FREE_RESEARCHER_ROLE.md"
ANTI = ROOT / "research_roles" / "EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md"


def test_free_researcher_is_axiom_discovery_not_waiting_queue_worker():
    role = ROLE.read_text(encoding="utf-8")
    assert "FREE_RESEARCHER_DEFAULT_OBJECTIVE = DISCOVER_NEW_AXIOM_CANDIDATES" in role
    assert "FREE_RESEARCHER_DEFAULT_STATE = AXIOM_DISCOVERY" in role
    assert "Research mode: `FREE_AXIOM_DISCOVERY`" in role
    assert "Do not enter waiting state" in role
    assert "do not auto-claim scheduler work" in role


def test_phase_a_blocks_route_scheduler_ambient_tool_and_representation_anchoring():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    combined = role + "\n" + anti
    for marker in (
        "TOOL_AVAILABILITY != DISCOVERY_PRIOR",
        "IMPLEMENTATION_CONVENIENCE != AXIOM_PRIOR",
        "FILE_ORDER != RESEARCH_PRIORITY",
        "EXISTING_NAME != REQUIRED_PRIMITIVE",
    ):
        assert marker in anti
    assert "NO_ACTIVE_BRANCH_WORKING_TRUTH" in anti
    assert "PHASE_A_RECENT_ROUTE_VISIBILITY = FORBIDDEN_BY_DEFAULT" in anti
    assert "NO_USER_TOPIC != SCHEDULER_DISPATCH" in anti
    assert "AMBIENT_RECENT_RESEARCH_CONTEXT = BLINDED_IN_PHASE_A" in anti
    assert "NEGATIVE_INSTRUCTION_PRIMING = AVOID_BY_GENERIC_BLINDING" in anti


def test_phase_a_role_files_do_not_name_current_numbered_routes():
    for path in (ROLE, ANTI):
        text = path.read_text(encoding="utf-8")
        assert not re.search(r"\bR0\d{2}\b", text), path


def test_clean_context_and_snapshot_required_for_blind_provenance():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "BLINDNESS_STATUS = CLEAN" in role
    assert "ANCHOR_EXPOSED" in role
    assert "FOUNDATION_SNAPSHOT_REF" in role
    assert "WORLDVIEW_SNAPSHOT_REF" in role
    assert "PHASE_A_CONTEXT_CLEAN_REQUIRED_FOR_BLIND_LABEL = true" in anti
    assert "PREEXISTING_AGENDA_EXPOSURE_CANNOT_BE_UNREAD = true" in anti


def test_candidate_freeze_precedes_prior_work_comparison_and_working_truth():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "research_axiom_candidate_state_machine.json" in role
    assert "candidate freeze" in role.lower()
    assert "Only after freeze" in role
    assert "RAW_AXIOM_CANDIDATE != WORKING_TRUTH" in anti
    assert "post-allocation guard" in anti


def test_free_researcher_does_not_inherit_other_branch_working_truth():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "Another branch's `WORKING_TRUTH` is not inherited unless explicitly supplied." in role
    assert "NO_ACTIVE_BRANCH_WORKING_TRUTH" in anti


def test_independent_replication_is_isolated_until_freeze():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    for text in (role, anti):
        assert "separate fresh contexts" in text
        assert "before each" in text and "freezes" in text
    assert "INDEPENDENT_CONVERGENCE = STRUCTURAL_INTEREST_SIGNAL_NOT_PROOF" in anti
