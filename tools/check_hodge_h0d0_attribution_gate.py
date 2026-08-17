#!/usr/bin/env python3
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RR = ROOT / "research_results"
errors=[]
checks=[]

def ck(name, cond, detail=""):
    checks.append(name)
    if not cond:
        errors.append({"check":name,"detail":detail})

def load(name):
    return json.loads((RR/name).read_text(encoding="utf-8"))

required=[
"HODGE_H0D0_FOUR_AXIS_MODEL.json",
"HODGE_H0D0_SOURCE_BASELINE_SPEC.json",
"HODGE_H0D0_LEVERAGE_ATTRIBUTION_CERTIFICATE_SPEC.json",
"HODGE_H0D0_CONTROL_RECLASSIFICATION.json",
"HODGE_H0D0_H0B_H0C_ATTRIBUTION_RETYPE.json",
"HODGE_H0D0_NOVELTY_DECOUPLING_LEDGER.json",
"HODGE_H0D0_ROUTE_DECISION.json",
"HODGE_H0D0_TARGET_LEAKAGE_LEDGER.json",
"HODGE_H0D0_CLASSIFICATION.json",
"HODGE_H0D0_SEMANTIC_CHECKPOINT.md",
]
for n in required:
    ck("exists:"+n, (RR/n).exists())

four=load("HODGE_H0D0_FOUR_AXIS_MODEL.json")
base=load("HODGE_H0D0_SOURCE_BASELINE_SPEC.json")
spec=load("HODGE_H0D0_LEVERAGE_ATTRIBUTION_CERTIFICATE_SPEC.json")
ctrl=load("HODGE_H0D0_CONTROL_RECLASSIFICATION.json")
ret=load("HODGE_H0D0_H0B_H0C_ATTRIBUTION_RETYPE.json")
nov=load("HODGE_H0D0_NOVELTY_DECOUPLING_LEDGER.json")
route=load("HODGE_H0D0_ROUTE_DECISION.json")
leak=load("HODGE_H0D0_TARGET_LEAKAGE_LEDGER.json")
cls=load("HODGE_H0D0_CLASSIFICATION.json")
sem=(RR/"HODGE_H0D0_SEMANTIC_CHECKPOINT.md").read_text(encoding="utf-8")

ck("criterion_parent_frozen", four["criterion_parent"]=="HODGE_H0A0_REALIZATION_CLASSIFIER_V2")
ck("four_axes_exact", set(four["axes"])=={"A_INFORMATION_RECOVERABILITY","B_OPERATIONAL_RANK","C_LEVERAGE_ATTRIBUTION","D_NOVELTY_PRIOR_ART"})
ck("information_not_rank_gate", four["axes"]["A_INFORMATION_RECOVERABILITY"]["determines_operational_rank"] is False)
ck("operational_rank_not_rewritten", four["axes"]["B_OPERATIONAL_RANK"]["changed_by_h0d0"] is False)
ck("novelty_not_rank_gate", four["axes"]["D_NOVELTY_PRIOR_ART"]["determines_operational_rank"] is False)
ck("novelty_not_attribution_gate", four["axes"]["D_NOVELTY_PRIOR_ART"]["determines_attribution"] is False)
for inv in [
"NOVELTY_STATUS_DOES_NOT_DETERMINE_OPERATIONAL_RANK",
"PRIOR_ART_IS_NOT_A_NEGATIVE_R2_GATE",
"SOURCE_INHERITED_LEVERAGE_DOES_NOT_EARN_TRANSFORM_ATTRIBUTION",
"KNOWN_PRIOR_ART_TRANSFORM_CAN_PASS_R2",
"NOVEL_THEOREM_NOT_REQUIRED_FOR_R2",
"BASELINE_MUST_BE_PREDECLARED",
"POST_HOC_WEAKENING_OF_SOURCE_BASELINE_IS_FORBIDDEN"]:
    ck("invariant:"+inv, inv in four["frozen_invariants"])

ck("addendum_named", four["hodge_special_R2_addendum"]["name"]=="R2_ATTRIBUTION_ADDENDUM_PASS")
ck("addendum_no_abstract_rewrite", four["hodge_special_R2_addendum"]["abstract_operational_rank_is_not_rewritten"] is True)
ck("baseline_predeclared_status", base["status"]=="FROZEN_BEFORE_ATTRIBUTION_EVALUATION")
ck("baseline_no_universal_impossibility", base["baseline_contract"]["universal_impossibility_claim_forbidden"] is True)
ck("baseline_posthoc_forbidden", base["baseline_contract"]["post_hoc_weakening_forbidden"] is True)
req_fields=set(base["baseline_contract"]["required_fields"])
for b in base["baselines"]:
    ck("baseline_fields:"+b["baseline_id"], req_fields.issubset(b.keys()))
ck("baseline_count", len(base["baselines"])==7)

ck("cert_required_15_fields", len(spec["required_fields"])==15)
ck("cert_has_source_countercheck", "source_baseline_countercheck" in spec["required_fields"])
ck("cert_priorart_not_proxy", "PRIOR_ART_STATUS_CANNOT_DECIDE_ATTRIBUTION" in spec["anti_gaming"])

cm={x["id"]:x for x in ctrl["controls"]}
dft=cm["P1_INVERTIBLE_DFT2_NORMAL_FORM"]
ck("dft_info_equiv", dft["information_tag"]=="INFO_EQUIVALENT_OR_FULLY_RECOVERABLE")
ck("dft_R2", dft["operational_rank"]=="R2_NONTRIVIAL_OPERATIONAL_REALIZATION")
ck("dft_transform_attributed", dft["attribution_status"]=="TRANSFORM_ATTRIBUTED_LEVERAGE")
ck("dft_prior_art", dft["novelty_status"]=="CLASSICAL_PRIOR_ART")
ck("dft_addendum_pass", dft["R2_ATTRIBUTION_ADDENDUM_PASS"] is True)
ck("dft_zero_novelty_credit", dft["external_novelty_credit"]==0)
ren=cm["N0_BIJECTIVE_LABEL_RENAMING"]
ck("rename_R0", ren["operational_rank"]=="R0_INERT_REPARAMETRIZATION")
ck("rename_no_leverage", ren["attribution_status"]=="NO_LEVERAGE_TO_ATTRIBUTE")
col=cm["N1_ARBITRARY_HIDDEN_COLOR"]
ck("color_enriched", col["information_tag"]=="INFO_ENRICHED_RELATIVE_TO_DECLARED_READOUT")
ck("color_R0", col["operational_rank"]=="R0_INERT_REPARAMETRIZATION")
ck("color_no_leverage", col["attribution_status"]=="NO_LEVERAGE_TO_ATTRIBUTE")
ck("controls_nonvacuous", ctrl["nonvacuity_verdict"]=="PASS")

ck("history_H0B_immutable", ret["historical_dispositions_immutable"]["H0B"]=="H0B_R2_PRIOR_ART_CONTROLS_ONLY")
ck("history_H0C_immutable", ret["historical_dispositions_immutable"]["H0C"]=="H0C_PRIOR_ART_ONLY_NO_ENTERPRISE_CREDIT")
rm={x["candidate"]:x for x in ret["records"]}
for cand in [
"ENT-B-FUTURE-SAFE-QUOTIENT-ASSEMBLY",
"S1_SUPPORT_INDEXED_A3_SIGNED_FIELD",
"S2_SIGNED_RECOALESCENCE_PATH_WEIGHT",
"S3_ZERO_CLASS_QUOTIENT_WITH_SUPPORT"]:
    r=rm[cand]
    ck("source_inherited:"+cand, r["attribution_status"]=="SOURCE_INHERITED_LEVERAGE")
    ck("novelty_not_proxy:"+cand, r["novelty_used_as_proxy"] is False)
    ck("abstract_R2_preserved:"+cand, r["axis_B_operational_rank_preserved"]=="R2_NONTRIVIAL_OPERATIONAL_REALIZATION_CONTROL_ONLY")
    ck("addendum_fail:"+cand, r["R2_ATTRIBUTION_ADDENDUM_PASS"] is False)
    ck("hodge_special_R1:"+cand, r["strongest_hodge_special_qualification_under_addendum"]=="R1_DERIVED_REORGANIZATION")
ck("no_existing_attributed_R2", ret["existing_h0b_h0c_attributed_R2_component_count"]==0)
ck("H0B_scope_boundary_present", "larger multi-step" in rm["ENT-B-FUTURE-SAFE-QUOTIENT-ASSEMBLY"]["scope_boundary"])

nrules={x["rule"] for x in nov["rules"]}
for rule in [
"PRIOR_ART_IS_NOT_A_NEGATIVE_R2_GATE",
"NOVEL_THEOREM_NOT_REQUIRED_FOR_R2",
"NOVELTY_STATUS_DOES_NOT_DETERMINE_OPERATIONAL_RANK",
"SOURCE_ALREADY_HAS_SAME_LEVERAGE => NO_ATTRIBUTION_CREDIT"]:
    ck("novelty_rule:"+rule, rule in nrules)
ck("no_retro_novelty", nov["stage_reinterpretation"]["does_not_retroactively_claim_novelty"] is True)
ck("no_retro_H1", nov["stage_reinterpretation"]["does_not_retroactively_open_H1"] is True)

allowed_routes={
"USE_EXISTING_ATTRIBUTED_R2_COMPONENT_FOR_R3_BRIDGE_SEARCH",
"NO_EXISTING_ATTRIBUTED_R2_COMPONENT__SEARCH_NEW_OPERATIONAL_SOURCE",
"ATTRIBUTION_CRITERION_INCOMPLETE"}
ck("route_allowed", route["decision"] in allowed_routes)
ck("route_expected", route["decision"]=="NO_EXISTING_ATTRIBUTED_R2_COMPONENT__SEARCH_NEW_OPERATIONAL_SOURCE")
ck("route_no_auto_stage", route["automatic_next_stage"] is False)
ck("route_H1_blocked", route["H1_admissible"] is False)

ck("leakage_pass", leak["verdict"]=="PASS" and leak["status"]=="PASS")
ck("no_new_carrier_search", leak["new_carrier_search_performed"] is False)
ck("no_H1_start", leak["H1_started"] is False)
ck("no_Hodge_proof", leak["Hodge_proved"] is False)
ck("historical_H0A_suspended", leak["historical_H0A_status"]=="SUSPENDED_DO_NOT_EXECUTE_UNCHANGED")

ck("classification_disposition", cls["primary_disposition"]=="H0D0_ATTRIBUTION_CRITERION_FROZEN_NONVACUOUS")
ck("hard_target_pass", cls["hard_target_pass"] is True)
ck("classification_four_axes", cls["four_axes_separated"] is True)
ck("classification_baseline_frozen", cls["source_baseline_contract_frozen"] is True)
ck("classification_addendum_frozen", cls["R2_attribution_addendum_frozen"] is True)
ck("classification_novelty_decoupled", cls["novelty_decoupled_from_operational_rank"] is True)
ck("classification_no_existing_component", cls["existing_H0B_H0C_attributed_R2_component_found"] is False)
ck("classification_history_not_rewritten", cls["historical_H0B_H0C_dispositions_rewritten"] is False)
ck("classification_H1_false", cls["H1_admissible"] is False)
ck("classification_Hodge_false", cls["Hodge_proved"] is False)
ck("CI_not_required", cls["CI_status"]=="CI_NOT_REQUIRED_FOR_RESEARCH")

ck("semantic_has_disposition", "H0D0_ATTRIBUTION_CRITERION_FROZEN_NONVACUOUS" in sem)
ck("semantic_has_DFT_attribution", "TRANSFORM_ATTRIBUTED_LEVERAGE" in sem)
ck("semantic_has_source_inherited", sem.count("SOURCE_INHERITED_LEVERAGE")>=4)
ck("semantic_has_route", route["decision"] in sem)
ck("semantic_H1_blocked", "H1_ADMISSIBLE = false" in sem)

# Bare legacy C(X) is forbidden in load-bearing H0D0 artifacts.
all_text="\n".join((RR/n).read_text(encoding="utf-8") for n in required)
ck("no_bare_CX", "C(X)" not in all_text)

out={
"checker":"HODGE_H0D0_ATTRIBUTION_GATE_V1",
"status":"PASS" if not errors else "FAIL",
"passed":len(checks)-len(errors),
"total":len(checks),
"errors":errors,
"primary_disposition":cls["primary_disposition"],
"route_decision":route["decision"],
"protocol_integrity":"PASS" if not errors else "FAIL"
}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
sys.exit(0 if not errors else 1)
