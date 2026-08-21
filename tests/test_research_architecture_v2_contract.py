import ast
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def test_role_modes_separate_free_discovery_from_task_research():
    arch = load_json("research_architecture.json")
    role = load_json("research_role_policy.json")
    free = arch["research_modes"]["FREE_AXIOM_DISCOVERY"]
    task = arch["research_modes"]["TASK_RESEARCH"]
    assert free["scheduler_eligible"] is False
    assert free["agenda_visibility_before_candidate_freeze"] == "FOUNDATION_ONLY"
    assert free["inherits_other_branch_working_truth"] is False
    assert task["scheduler_eligible"] is True
    assert role["research_modes"]["FREE_AXIOM_DISCOVERY"]["generic_no_user_task_scheduler_rule_applies"] is False
    assert role["research_modes"]["TASK_RESEARCH"]["scheduler_eligible"] is True


def test_legacy_common_surface_is_explicitly_retyped_not_silently_obeyed():
    arch = load_json("research_architecture.json")
    common = load_json("research_common_surface.json")
    assert common["dispatch_scheduler"]["auto_select_when_user_task_absent"] is True
    assert common["mandatory_preflight"]
    legacy = arch["legacy_surface_interpretation"]
    assert "TASK_RESEARCH" in legacy["research_common_surface_auto_select_when_user_task_absent"]
    assert "TRIGGERED" in legacy["research_common_surface_mandatory_preflight"]


def test_identity_machine_tracks_mode_and_free_context_provenance():
    identity = load_json("research_identity_state_machine.json")
    assert set(identity["research_mode"]["allowed_for_researcher"]) == {"FREE_AXIOM_DISCOVERY", "TASK_RESEARCH"}
    assert identity["scheduler_claim"]["free_axiom_discovery_eligible"] is False
    rule = identity["free_research_context_rule"]
    assert rule["clean_blind_label_requires_preexisting_agenda_absent"] is True
    assert rule["preexisting_agenda_cannot_be_unread"] is True
    assert "ANCHOR_EXPOSED" in identity["role_transition"]["task_to_free_same_conversation"]


def test_axiom_candidate_is_not_working_truth_or_direct_backflow():
    sm = load_json("research_axiom_candidate_state_machine.json")
    arch = load_json("research_architecture.json")
    assert sm["driver_intake"]["raw_blind_candidate_eligible"] is False
    assert sm["driver_intake"]["candidate_status_alone_is_not_working_truth"] is True
    assert sm["foundation_intake"]["raw_candidate_auto_open_foundation_question"] is False
    assert sm["canonicalization"]["direct_candidate_to_main"] is False
    assert arch["axiom_candidate_lifecycle"]["raw_candidate_is_working_truth"] is False


def test_discovery_and_validation_evidence_are_typed_separately():
    sm = load_json("research_axiom_candidate_state_machine.json")
    assert sm["evidence_typing"]["rule"] == "DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE"


def test_foundation_backflow_and_steward_require_audited_candidate_state():
    backflow = load_json("foundation_backflow.json")
    steward = load_json("foundation_steward.json")
    expected = {"AUDITED_AXIOM_CANDIDATE", "AUDITED_REPLACEMENT_CANDIDATE", "EXACT_NEGATIVE_OBSTRUCTION"}
    assert set(backflow["free_axiom_candidate_intake"]["minimum_eligible_states"]) == expected
    assert backflow["free_axiom_candidate_intake"]["raw_candidate_auto_backflow"] is False
    assert set(steward["free_axiom_candidate_intake"]["minimum_eligible_states"]) == expected
    assert steward["free_axiom_candidate_intake"]["raw_candidate_auto_opens_foundation_question"] is False


def test_driver_contract_forbids_automatic_successor_stage_and_raw_working_truth():
    text = (ROOT / "docs" / "RESEARCH_DRIVER_OPERATING_CONTRACT.md").read_text(encoding="utf-8")
    assert "PASS_IS_NOT_A_SUCCESSOR_TRIGGER" in text
    assert "AXIOM_CANDIDATE != WORKING_TRUTH" in text
    assert "Working Truth activation boundary" in text
    assert "NO_IMPLICIT_DEFAULT_NEXT_ROUTE" in text


def test_taskbook_contract_requires_lineage_and_continuation_gate():
    contract = load_json("research_taskbook_contract.json")
    lineage = contract["task_lineage_contract"]
    assert lineage["required_for_new_taskbooks"] is True
    assert "CONTINUATION" in lineage["allowed_values"]
    required = set(lineage["continuation_required_successor_gate_fields"])
    assert {"new_information_gap", "discriminating_outcomes", "kill_condition"} <= required


def test_taskbook_tool_parses_and_enforces_continuation_gate():
    source = (ROOT / "tools" / "research_taskbook.py").read_text(encoding="utf-8")
    ast.parse(source)
    ns = runpy.run_path(str(ROOT / "tools" / "research_taskbook.py"))
    lineage_findings = ns["lineage_findings"]
    incomplete = {
        "task_lineage": "CONTINUATION",
        "parent_task_id": "RS-PARENT",
        "successor_gate": {"new_information_gap": "something"},
    }
    assert any(item["code"] == "TB-SUCCESSOR-GATE" for item in lineage_findings(incomplete, dispatch=True))
    complete = {
        "task_lineage": "CONTINUATION",
        "parent_task_id": "RS-PARENT",
        "successor_gate": {
            "new_information_gap": "new discriminator",
            "why_parent_result_does_not_close_it": "parent proves only a weaker object",
            "discriminating_outcomes": ["positive theorem", "exact no-go"],
            "kill_condition": "no structure beyond parent result",
            "why_new_stage_or_task_is_better_than_same_task_or_closure": "requires an independent owner/evidence surface"
        },
    }
    assert not [item for item in lineage_findings(complete, dispatch=True) if item["severity"] == "ERROR"]


def test_taskbook_policy_digest_includes_architecture_and_candidate_state():
    policy = load_json("research_taskbook_policy.json")
    inputs = set(policy["policy_inputs"])
    assert "research_architecture.json" in inputs
    assert "research_axiom_candidate_state_machine.json" in inputs
    assert "docs/RESEARCH_ARCHITECTURE.md" in inputs


def test_architecture_keeps_common_surface_as_lookup_not_default_context_dump():
    arch = load_json("research_architecture.json")
    assert "LOOKUP" in arch["read_performance"]["shared_common_surface"]
    assert arch["read_performance"]["explicit_task_soft_remote_read_budget_before_substantive_work"] == 3
