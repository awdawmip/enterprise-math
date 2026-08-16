#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research_results"

REQUIRED = [
    "HODGE_H0A0_COMPARISON_STRENGTH_REGISTRY.json",
    "HODGE_H0A0_GAGA_BOUNDARY_MATRIX.md",
    "HODGE_H0A0_INFORMATION_OPERATIONAL_AXIS.json",
    "HODGE_H0A0_PROOF_LEVERAGE_CERTIFICATE_SPEC.json",
    "HODGE_H0A0_REALIZATION_CLASSIFIER_V2.json",
    "HODGE_H0A0_NONVACUITY_CONTROL_REGISTRY.json",
    "HODGE_H0A0_LEGACY_H0_RETYPE.json",
    "HODGE_H0A0_HODGE_LEVERAGE_INTERFACE.json",
    "HODGE_H0A0_H0A1_DECISION.json",
    "HODGE_H0A0_TARGET_LEAKAGE_LEDGER.json",
    "HODGE_H0A0_CLASSIFICATION.json",
    "HODGE_H0A0_SEMANTIC_CHECKPOINT.md",
]

def load(name):
    return json.loads((R / name).read_text())

checks = []
def ck(cid, cond, detail):
    checks.append({"id": cid, "pass": bool(cond), "detail": detail})

for name in REQUIRED:
    ck(f"FILE:{name}", (R / name).is_file(), "required artifact exists")

comp = load("HODGE_H0A0_COMPARISON_STRENGTH_REGISTRY.json")
axis = load("HODGE_H0A0_INFORMATION_OPERATIONAL_AXIS.json")
spec = load("HODGE_H0A0_PROOF_LEVERAGE_CERTIFICATE_SPEC.json")
clf = load("HODGE_H0A0_REALIZATION_CLASSIFIER_V2.json")
ctrl = load("HODGE_H0A0_NONVACUITY_CONTROL_REGISTRY.json")
legacy = load("HODGE_H0A0_LEGACY_H0_RETYPE.json")
hif = load("HODGE_H0A0_HODGE_LEVERAGE_INTERFACE.json")
dec = load("HODGE_H0A0_H0A1_DECISION.json")
tl = load("HODGE_H0A0_TARGET_LEAKAGE_LEDGER.json")
final = load("HODGE_H0A0_CLASSIFICATION.json")

# Comparison typing / no overloaded load-bearing C(X)
notations = {x["notation"] for x in comp["comparison_levels"]}
required_notations = {"C_full^alg(X)", "C_full^an(X)", "C_top(X)", "C_H(X)", "C_state(X;O)"}
ck("CMP_TYPED_LEVELS", required_notations <= notations, "all required comparison strengths are explicitly typed")
ck("CMP_NO_UNTYPED", comp.get("required_conclusion") == "NO_SINGLE_UNTYPED_CLASSICAL_COMPARISON_OBJECT" and comp["legacy_symbol_policy"].get("status", "").startswith("PROHIBITED"), "bare C(X) is prohibited in load-bearing classifier fields")
ck("CMP_NO_TOTAL_ORDER", comp["partial_order_policy"].get("single_linear_strength_order_assumed") is False, "no unproved total strength order")

# Orthogonal information / operational axes
req_inv = axis["required_invariants"]
for key in [
    "INFORMATION_NONFACTORIZATION_IS_NOT_A_NECESSARY_OPERATIONAL_R2_GATE",
    "WEAK_READOUT_NONFACTORIZATION_DOES_NOT_EARN_R2",
    "INVERTIBILITY_DOES_NOT_FORCE_R0_OR_R1",
    "INFO_ENRICHED_DOES_NOT_IMPLY_R2",
]:
    ck(f"AXIS:{key}", req_inv.get(key) is True, key)
ck("AXIS_DISTINCT_FIELDS", "information_tags" in axis and "operational_axis" in axis, "information tag and operational rank are separate fields")

# R2/R3 requirements
r2 = clf["ranks"]["R2_NONTRIVIAL_OPERATIONAL_REALIZATION"]
r3 = clf["ranks"]["R3_HODGE_RELEVANT_OPERATIONAL_REALIZATION"]
r2_reqs = set(r2["requirements"])
ck("R2_INDEPENDENT_DEFINITION", "independently_generated_operational_structure" in r2_reqs, "R2 requires independent operational structure")
ck("R2_LEVERAGE_CERT", "PROOF_LEVERAGE_CERTIFICATE_pass" in r2_reqs, "R2 requires strict proof-leverage certificate")
ck("R2_NO_INFO_REQUIREMENT", r2.get("information_nonfactorization_required") is False, "information non-factorization is not required for R2")
ck("R3_HODGE_INTERFACE", "explicit_typed_Hodge_bridge_interface" in set(r3["requirements"]) and "explicit_algebraic_cycle_lifting_interface" in set(r3["requirements"]), "R3 requires Hodge and lifting interfaces")

# Proof leverage certificate non-tautology and exactness
fields = set(spec["required_fields"])
for f in ["independent_enterprise_definition", "comparison_theorem", "non_tautology_audit", "strict_leverage_class", "strict_leverage_witness", "downstream_theorem_obligation_unlocked"]:
    ck(f"CERT_FIELD:{f}", f in fields, f"certificate has {f}")
ck("CERT_NO_TRANSPORTED_ANSWER", "forbidden_shortcut" in spec["independent_definition_rule"], "transported target answer explicitly forbidden")

# Nonvacuity controls: information-equivalent can be R0 and R2(control), enriched can be R0, weak readout rejected.
byid = {x["id"]: x for x in ctrl["controls"]}
ck("CTRL_N0_RENAME_R0", byid["N0_BIJECTIVE_LABEL_RENAMING"]["operational_rank"] == "R0_INERT_REPARAMETRIZATION" and byid["N0_BIJECTIVE_LABEL_RENAMING"]["information_tag"] == "INFO_EQUIVALENT_OR_FULLY_RECOVERABLE", "bijective renaming is info-equivalent R0")
ck("CTRL_N1_COLOR_NOT_R2", byid["N1_ARBITRARY_HIDDEN_COLOR"]["operational_rank"] in {"R0_INERT_REPARAMETRIZATION", "R1_DERIVED_REORGANIZATION"} and byid["N1_ARBITRARY_HIDDEN_COLOR"]["information_tag"] == "INFO_ENRICHED_RELATIVE_TO_DECLARED_READOUT", "hidden color does not earn R2")
ck("CTRL_P1_INVERTIBLE_R2", byid["P1_INVERTIBLE_DFT2_NORMAL_FORM"]["operational_rank"] == "R2_NONTRIVIAL_OPERATIONAL_REALIZATION" and byid["P1_INVERTIBLE_DFT2_NORMAL_FORM"]["information_tag"] == "INFO_EQUIVALENT_OR_FULLY_RECOVERABLE" and byid["P1_INVERTIBLE_DFT2_NORMAL_FORM"]["enterprise_credit"] is False, "fully invertible prior-art normal-form control can operationally reach R2 without Enterprise novelty")
ck("CTRL_P1_EXACT_MEASURE", byid["P1_INVERTIBLE_DFT2_NORMAL_FORM"]["proof_leverage_certificate"]["source_value"] == 2 and byid["P1_INVERTIBLE_DFT2_NORMAL_FORM"]["proof_leverage_certificate"]["target_value"] == 0, "DFT control has predeclared strict exact witness 2 -> 0")
ck("CTRL_P2_OBSTRUCTION_R2", byid["P2_GRAPH_POTENTIAL_FINITE_OBSTRUCTION"]["operational_rank"] == "R2_NONTRIVIAL_OPERATIONAL_REALIZATION" and byid["P2_GRAPH_POTENTIAL_FINITE_OBSTRUCTION"]["enterprise_credit"] is False, "finite-obstruction/local-global prior-art control reaches operational R2 only")
ck("CTRL_B1_WEAK_REJECTED", byid["B1_WEAK_READOUT_GAMING"]["operational_rank"] == "R0_INERT_REPARAMETRIZATION", "weak-readout nonfactorization earns no R2")
ck("CTRL_NONVACUOUS", ctrl.get("nonvacuity_verdict") == "PASS", "control registry declares nonvacuity PASS")

# Legacy history preserved, no retroactive victory.
ck("LEGACY_HISTORY_PRESERVED", legacy["required_statements"].get("historical_result_remains_true_under_legacy_gate") is True and legacy["required_statements"].get("retroactive_victory_forbidden") is True, "H0 history preserved without retroactive victory")
legacy_ranks = {x["candidate_id"]: x["v2_highest_established_rank_from_existing_artifacts_only"] for x in legacy["candidate_reassessment"]}
ck("LEGACY_A_R1", legacy_ranks.get("ENT-A-PRECISION-COLLAPSE") == "R1_DERIVED_REORGANIZATION", "Candidate A V2 highest established from old artifacts is R1")
ck("LEGACY_B_R1", legacy_ranks.get("ENT-B-BRC-INCIDENCE-PATH") == "R1_DERIVED_REORGANIZATION", "Candidate B V2 highest established from old artifacts is R1")

# Hodge interface / leakage / H1 block
ck("HODGE_INTERFACE_TYPED", hif.get("status") == "TYPE_INTERFACE_ONLY_NO_HODGE_PROOF" and len(hif.get("future_required_maps_and_objects", [])) >= 6, "typed R3/Hodge leverage interface exists without proof claim")
ck("H1_BLOCKED_INTERFACE", hif.get("H1_status") == "NOT_ADMISSIBLE_IN_H0A0", "H1 is blocked in H0A0")
ck("H1_BLOCKED_CLASSIFIER", clf["H1_gate"].get("H0A0_can_open_H1") is False and clf["H1_gate"].get("R2_alone_sufficient_for_H1") is False, "R2 alone cannot open H1 under V2 default")
ck("TARGET_LEAKAGE_PASS", tl.get("overall") == "PASS", "target-leakage ledger passes")

# Suspended H0A receives exactly one allowed disposition.
allowed = {
    "PROMOTE_SUSPENDED_H0A_TO_H0A1_WITH_REPAIRED_GATE",
    "RETYPE_H0A1_AS_PRESENTATION_NATURALITY_SUBPROBLEM",
    "RETIRE_PRESENTATION_FAMILY_AS_MAINLINE",
    "CRITERION_REPAIR_INCOMPLETE",
}
ck("H0A1_DECISION_ALLOWED", dec.get("decision") in allowed, "one taskbook-allowed post-H0A0 decision")
ck("H0A_HISTORICAL_NOT_EXECUTED", dec.get("historical_h0a_execution") == "DO_NOT_EXECUTE_UNCHANGED", "suspended historical H0A remains held")
ck("NO_AUTO_STAGE", dec.get("automatic_h0a1_start") is False and dec.get("automatic_h1_start") is False, "no automatic H0A1/H1")

# GAGA matrix contains the exact negative boundary, without Hodge shortcut.
gaga_text = (R / "HODGE_H0A0_GAGA_BOUNDARY_MATRIX.md").read_text()
ck("GAGA_BOUNDARY", "GAGA_DOES_NOT_SOLVE_RATIONAL_HODGE_CONJECTURE" in gaga_text, "GAGA negative boundary frozen")
ck("GAGA_NO_SHORTCUT", "does not" in gaga_text.lower() and "Hodge" in gaga_text, "GAGA text explicitly denies Hodge shortcut")

# Final disposition / hard target.
ck("FINAL_DISPOSITION", final.get("primary_disposition") == "H0A0_CRITERION_V2_FROZEN_NONVACUOUS", "permitted successful H0A0 disposition")
ck("HARD_TARGET_PASS", final.get("hard_target", {}).get("name") == "HODGE_RELEVANT_REALIZATION_CRITERION_IS_WELL_TYPED_AND_NONVACUOUS" and final.get("hard_target", {}).get("result") == "PASS", "hard target passes")
ck("FINAL_H1_BLOCKED", final.get("H1_admissible") is False and final.get("H0A1_auto_start") is False, "final classification does not auto-advance")

passed = sum(c["pass"] for c in checks)
failed = [c for c in checks if not c["pass"]]
result = {
    "schema": "HODGE_H0A0_CHECKER_OUTPUT_V1",
    "task_id": "RS-HODGE-H0A0-REALIZATION-COMPARISON-CRITERION-REPAIR",
    "researcher_id": "EM-HODGE-H0-2F8C71",
    "protocol_integrity": "PASS" if not failed else "FAIL",
    "checks_passed": passed,
    "checks_total": len(checks),
    "checks_failed": len(failed),
    "failed": failed,
    "checks": checks,
    "interpretation": "Checker PASS validates H0A0 criterion/protocol consistency and declared exact controls only. It is not proof of an Enterprise realization, H1 readiness, an algebraic lifting theorem, or the Hodge conjecture."
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(0 if not failed else 1)
