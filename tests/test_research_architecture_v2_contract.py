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
    assert free["agenda_visibility_before_candidate_freeze"] == "PRIMITIVE_SUBSTRATE_ONLY"
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
    assert rule["fresh_identity_alone_does_not_make_context_clean"] is True
    assert "ANCHOR_EXPOSED" in identity["role_transition"]["task_to_free_same_conversation"]


def test_axiom_candidate_is_not_working_truth_or_direct_backflow():
    sm = load_json("research_axiom_candidate_state_machine.json")
    arch = load_json("research_architecture.json")
    assert sm["driver_intake"]["raw_blind_candidate_eligible"] is False
    assert sm["driver_intake"]["candidate_status_alone_is_not_working_truth"] is True
    assert sm["foundation_intake"]["raw_candidate_auto_open_foundation_question"] is False
    assert sm["canonicalization"]["direct_candidate_to_main"] is False
    assert arch["axiom_candidate_lifecycle"]["raw_candidate_is_working_truth"] is False


def test_candidate_to_task_transition_preserves_free_origin():
    sm = load_json("research_axiom_candidate_state_machine.json")
    contract = load_json("research_taskbook_contract.json")
    transition = sm["explicit_task_transition"]
    required = transition["taskbook_required_metadata"]
    assert required["origin_kind"] == "FREE_AXIOM_CANDIDATE"
    assert required["origin_candidate_id"] == "candidate_id"
    assert "audited" in required["origin_candidate_state"]
    assert transition["origin_may_be_relabelled_driver_roadmap"] is False
    allowed = set(contract["task_origin_contract"]["free_candidate_allowed_states"])
    assert set(transition["allowed_from"]) == allowed


def test_discovery_and_validation_evidence_are_typed_separately():
    sm = load_json("research_axiom_candidate_state_machine.json")
    assert sm["evidence_typing"]["rule"] == "DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE"


def test_independent_replication_tracks_context_independence_not_just_identity():
    sm = load_json("research_axiom_candidate_state_machine.json")
    repl = sm["independent_replication"]
    assert set(repl["independence_status_values"]) == {
        "CLEAN_INDEPENDENT_CONTEXT",
        "SHARED_AMBIENT_CONTEXT_DISCLOSED",
        "NOT_INDEPENDENT",
    }
    assert repl["fresh_identity_alone_does_not_prove_independence"] is True
    assert repl["candidate_visibility_between_runs_before_freeze"] is False


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
    assert "## 9. Working Truth activation" in text
    assert "MERE_TASK_PUBLICATION != WORKING_TRUTH_ACTIVATION" in text
    assert "NO_IMPLICIT_DEFAULT_NEXT_ROUTE" in text
    assert "alternative_route_or_free_exploration_considered" in text
    assert "origin_kind=FREE_AXIOM_CANDIDATE" in text
    assert "may not reset lineage" in text


def test_role_policy_mirrors_task_origin_and_successor_guards():
    role = load_json("research_role_policy.json")
    auth = role["official_taskbook_authority"]
    assert auth["task_origin_required_for_new_taskbooks"] is True
    assert auth["free_candidate_origin_requires_audited_candidate_id_and_state"] is True
    assert auth["successor_stage_gate_required_for_continuation"] is True
    assert auth["successor_gate_requires_alternative_route_or_free_exploration_considered"] is True
    assert auth["obvious_stage_two_plus_must_be_continuation"] is True
    assert auth["renaming_does_not_reset_semantic_lineage"] is True


def test_taskbook_contract_requires_origin_lineage_and_continuation_gate():
    contract = load_json("research_taskbook_contract.json")
    origin = contract["task_origin_contract"]
    assert origin["required_for_new_taskbooks"] is True
    assert "FREE_AXIOM_CANDIDATE" in origin["allowed_values"]
    assert set(origin["free_candidate_allowed_states"]) == {
        "AUDITED_AXIOM_CANDIDATE",
        "AUDITED_REPLACEMENT_CANDIDATE",
        "EXACT_NEGATIVE_OBSTRUCTION",
    }
    lineage = contract["task_lineage_contract"]
    assert lineage["required_for_new_taskbooks"] is True
    assert "CONTINUATION" in lineage["allowed_values"]
    required = set(lineage["continuation_required_successor_gate_fields"])
    assert {
        "new_information_gap",
        "discriminating_outcomes",
        "kill_condition",
        "alternative_route_or_free_exploration_considered",
    } <= required
    assert lineage["obvious_stage_continuation_rule"]["required_lineage"] == "CONTINUATION"
    assert "Renaming" in lineage["semantic_anti_evasion_rule"]


def test_taskbook_tool_parses_and_enforces_continuation_gate():
    source = (ROOT / "tools" / "research_taskbook.py").read_text(encoding="utf-8")
    ast.parse(source)
    ns = runpy.run_path(str(ROOT / "tools" / "research_taskbook.py"))
    lineage_findings = ns["lineage_findings"]
    incomplete = {
        "task_id": "RS-X-STAGE2-TEST",
        "title": "Stage 2 test",
        "task_lineage": "CONTINUATION",
        "parent_task_id": "RS-PARENT",
        "successor_gate": {"new_information_gap": "something"},
    }
    assert any(item["code"] == "TB-SUCCESSOR-GATE" for item in lineage_findings(incomplete, dispatch=True))
    complete = {
        "task_id": "RS-X-STAGE2-TEST",
        "title": "Stage 2 test",
        "task_lineage": "CONTINUATION",
        "parent_task_id": "RS-PARENT",
        "successor_gate": {
            "new_information_gap": "new discriminator",
            "why_parent_result_does_not_close_it": "parent proves only a weaker object",
            "discriminating_outcomes": ["positive theorem", "exact no-go"],
            "kill_condition": "no structure beyond parent result",
            "alternative_route_or_free_exploration_considered": "independent structural search was considered; this exact dependency remains task-local",
            "why_new_stage_or_task_is_better_than_same_task_or_closure": "requires an independent owner/evidence surface",
        },
    }
    assert not [item for item in lineage_findings(complete, dispatch=True) if item["severity"] == "ERROR"]


def test_obvious_stage_two_cannot_be_relabelled_new_direction():
    ns = runpy.run_path(str(ROOT / "tools" / "research_taskbook.py"))
    findings = ns["lineage_findings"](
        {
            "task_id": "RS-R999-STAGE2-SOMETHING",
            "title": "R999 Stage 2",
            "task_lineage": "NEW_DIRECTION",
        },
        dispatch=True,
    )
    assert any(item["code"] == "TB-STAGE-LINEAGE" for item in findings)


def test_free_candidate_origin_requires_audited_candidate_provenance():
    ns = runpy.run_path(str(ROOT / "tools" / "research_taskbook.py"))
    origin_findings = ns["origin_findings"]
    missing = {"origin_kind": "FREE_AXIOM_CANDIDATE"}
    assert any(item["code"] == "TB-ORIGIN-CANDIDATE" for item in origin_findings(missing, dispatch=True))
    raw = {
        "origin_kind": "FREE_AXIOM_CANDIDATE",
        "origin_candidate_id": "AX-1",
        "origin_candidate_state": "BLIND_CANDIDATE_FROZEN",
    }
    assert any(item["code"] == "TB-ORIGIN-CANDIDATE-STATE" for item in origin_findings(raw, dispatch=True))
    audited = {
        "origin_kind": "FREE_AXIOM_CANDIDATE",
        "origin_candidate_id": "AX-1",
        "origin_candidate_state": "AUDITED_AXIOM_CANDIDATE",
    }
    assert not [item for item in origin_findings(audited, dispatch=True) if item["severity"] == "ERROR"]


def test_taskbook_policy_digest_includes_architecture_and_candidate_state():
    policy = load_json("research_taskbook_policy.json")
    inputs = set(policy["policy_inputs"])
    assert "research_architecture.json" in inputs
    assert "research_axiom_candidate_state_machine.json" in inputs
    assert "docs/RESEARCH_ARCHITECTURE.md" in inputs
    semantics = "\n".join(policy["semantic_review_requirements"])
    assert "provenance laundering" in semantics
    assert "Stage 2+" in semantics
    assert "independent/free exploration" in semantics


def test_architecture_keeps_common_surface_as_lookup_not_default_context_dump():
    arch = load_json("research_architecture.json")
    assert "LOOKUP" in arch["read_performance"]["shared_common_surface"]
    assert arch["read_performance"]["explicit_task_soft_remote_read_budget_before_substantive_work"] == 3
    assert arch["successor_stage_gate"]["obvious_stage_two_plus_must_be_continuation"] is True
    assert arch["successor_stage_gate"]["renaming_does_not_reset_lineage"] is True
    assert "alternative_route_or_free_exploration_considered" in arch["successor_stage_gate"]["new_continuation_task_requires"]


def test_promotion_lane_is_bounded_attempt_not_ready_pr_lock():
    arch = load_json("research_architecture.json")
    channels = arch["promotion_channels"]
    math_lane = channels["mathematical_l4"]
    gov = channels["governance_maintenance"]
    assert math_lane["ready_pr_is_lane_lock"] is False
    assert math_lane["one_bounded_active_attempt_at_a_time"] is True
    assert math_lane["candidate_readiness_may_persist_without_lock"] is True
    assert gov["eligible_classification"] == "NO_NEW_MATHEMATICS"
    assert gov["may_proceed_while_mathematical_candidates_are_ready"] is True
    assert gov["one_bounded_active_attempt_at_a_time"] is True
    assert gov["requires_current_main_snapshot"] is True
    assert gov["requires_path_and_semantic_conflict_audit"] is True
    assert gov["requires_expected_head_or_equivalent_atomic_merge_guard_when_supported"] is True
    assert "NEW_THEOREM" in gov["forbidden_deltas"]
    assert "NEW_NATIVE_MATHEMATICAL_DEFINITION" in gov["forbidden_deltas"]


def test_governance_liveness_protocol_forbids_permanent_lane_ownership_and_math_smuggling():
    text = (ROOT / "docs" / "GOVERNANCE_MAINTENANCE_LIVENESS.md").read_text(encoding="utf-8")
    assert "READY_PR != PROMOTION_LANE_LEASE" in text
    assert "STALE_OR_UNMERGEABLE_READY_PR != PERMANENT_LANE_LOCK" in text
    assert "Only one governance-maintenance merge attempt" in text
    assert "does not introduce a new theorem" in text
    assert "new native mathematical definition" in text
    assert "expected-head" in text


def test_driver_contract_uses_attempt_semantics_for_promotion():
    text = (ROOT / "docs" / "RESEARCH_DRIVER_OPERATING_CONTRACT.md").read_text(encoding="utf-8")
    assert "READY_PR != PROMOTION_LANE_LEASE" in text
    assert "Mathematical promotion and strict `NO_NEW_MATHEMATICS` governance maintenance use bounded attempts." in text
    assert "release the remote subflow and resume the open parent" in text
    assert "use the governance-maintenance lane to smuggle mathematical claim changes" in text
