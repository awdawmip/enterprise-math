import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROLE = ROOT / "research_roles" / "EM_FREE_RESEARCHER_ROLE.md"
ANTI = ROOT / "research_roles" / "EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md"


def test_free_researcher_is_axiom_discovery_not_waiting_queue_worker():
    role = ROLE.read_text(encoding="utf-8")
    assert "FREE_RESEARCHER_DEFAULT_OBJECTIVE = DISCOVER_NEW_AXIOM_CANDIDATES" in role
    assert "FREE_RESEARCHER_DEFAULT_STATE = AXIOM_DISCOVERY" in role
    assert "`AXIOM_DISCOVERY`" in role
    assert "not a waiting state" in role
    assert "does **not** apply during autonomous free-axiom discovery" in role


def test_phase_a_blocks_route_scheduler_ambient_tool_and_representation_anchoring():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    for text in (role, anti):
        assert "scheduler" in text.lower()
        assert "recent commit" in text.lower()
        assert "working_truth" in text.lower()
        assert "ambient" in text.lower()
    for invariant in (
        "PHASE_A_RECENT_ROUTE_VISIBILITY = FORBIDDEN_BY_DEFAULT",
        "NO_USER_TOPIC != SCHEDULER_DISPATCH",
        "AMBIENT_RECENT_RESEARCH_CONTEXT = BLINDED_IN_PHASE_A",
        "NEGATIVE_INSTRUCTION_PRIMING = AVOID_BY_GENERIC_BLINDING",
        "TOOL_AVAILABILITY != DISCOVERY_PRIOR",
        "IMPLEMENTATION_CONVENIENCE != AXIOM_PRIOR",
        "FILE_ORDER != RESEARCH_PRIORITY",
        "EXISTING_NAME != REQUIRED_PRIMITIVE",
    ):
        assert invariant in anti
    assert "script/checker/formal module/notebook/visualization/enumerator" in anti
    assert "implementation carriers, coordinate encodings, drawing conventions, filenames or router ordering" in anti


def test_phase_a_role_files_do_not_name_current_numbered_routes():
    for path in (ROLE, ANTI):
        text = path.read_text(encoding="utf-8")
        assert not re.search(r"\bR0\d{2}\b", text), path


def test_candidate_freeze_precedes_prior_work_comparison():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "BLIND_AXIOM_CANDIDATE_PACKET" in role
    assert "BLIND_AXIOM_CANDIDATE_PACKET" in anti
    assert "PHASE_A_CANDIDATE_FREEZE_PRECEDES_PRIOR_WORK_DEDUP" in anti
    assert "Only after" in role
    assert "Phase B" in anti
    assert "post-allocation guard" in anti


def test_free_researcher_does_not_inherit_other_branch_working_truth():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "Driver `WORKING_TRUTH` from another active branch is not inherited" in role
    assert "NO_ACTIVE_BRANCH_WORKING_TRUTH" in anti


def test_current_foundation_is_start_not_required_final_axiom_set():
    role = ROLE.read_text(encoding="utf-8")
    anti = ANTI.read_text(encoding="utf-8")
    assert "not required to remain the final axiom set" in role
    assert "starting substrate and comparison authority" in anti
