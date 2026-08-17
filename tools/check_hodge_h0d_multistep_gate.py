#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, itertools, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RR = ROOT / "research_results"
errors=[]
passed=[]

def check(cond, label):
    if cond:
        passed.append(label)
    else:
        errors.append(label)

def load(name):
    return json.loads((RR/name).read_text(encoding="utf-8"))

required_json = [
"HODGE_H0D_SOURCE_BASELINE_SANDWICH.json",
"HODGE_H0D_MULTISTEP_SOURCE_REGISTRY.json",
"HODGE_H0D_SUFFIX_QUOTIENT_REGISTRY.json",
"HODGE_H0D_BRANCH_RECOALESCENCE_REGISTRY.json",
"HODGE_H0D_PARTIAL_FUTURE_LANGUAGE_REGISTRY.json",
"HODGE_H0D_COMPARISON_THEOREM_REGISTRY.json",
"HODGE_H0D_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json",
"HODGE_H0D_ATTRIBUTION_CERTIFICATE_REGISTRY.json",
"HODGE_H0D_BASELINE_GAMING_CONTROL.json",
"HODGE_H0D_PRESENTATION_NATURALITY_LEDGER.json",
"HODGE_H0D_PRIOR_ART_NOVELTY_LEDGER.json",
"HODGE_H0D_TARGET_LEAKAGE_LEDGER.json",
"HODGE_H0D_HODGE_R3_PREINTERFACE.json",
"HODGE_H0D_CLASSIFICATION.json",
]
for f in required_json:
    check((RR/f).exists(), f"exists:{f}")
check((RR/"HODGE_H0D_SEMANTIC_CHECKPOINT.md").exists(), "exists:semantic_checkpoint")
if errors:
    print(json.dumps({"checker":"HODGE_H0D_MULTISTEP_GATE_V1","errors":errors,"checks_passed":len(passed)},sort_keys=True))
    raise SystemExit(1)

docs={f:load(f) for f in required_json}
base=docs["HODGE_H0D_SOURCE_BASELINE_SANDWICH.json"]
src=docs["HODGE_H0D_MULTISTEP_SOURCE_REGISTRY.json"]
sq=docs["HODGE_H0D_SUFFIX_QUOTIENT_REGISTRY.json"]
br=docs["HODGE_H0D_BRANCH_RECOALESCENCE_REGISTRY.json"]
pf=docs["HODGE_H0D_PARTIAL_FUTURE_LANGUAGE_REGISTRY.json"]
ct=docs["HODGE_H0D_COMPARISON_THEOREM_REGISTRY.json"]
plc=docs["HODGE_H0D_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json"]
lac=docs["HODGE_H0D_ATTRIBUTION_CERTIFICATE_REGISTRY.json"]
bg=docs["HODGE_H0D_BASELINE_GAMING_CONTROL.json"]
nat=docs["HODGE_H0D_PRESENTATION_NATURALITY_LEDGER.json"]
nov=docs["HODGE_H0D_PRIOR_ART_NOVELTY_LEDGER.json"]
leak=docs["HODGE_H0D_TARGET_LEAKAGE_LEDGER.json"]
r3=docs["HODGE_H0D_HODGE_R3_PREINTERFACE.json"]
cl=docs["HODGE_H0D_CLASSIFICATION.json"]
sem=(RR/"HODGE_H0D_SEMANTIC_CHECKPOINT.md").read_text(encoding="utf-8")

# Criterion/addendum and baseline sandwich.
check(cl["criterion_v2_unchanged"] is True, "criterion_v2_unchanged")
check(cl["attribution_addendum_active"] is True, "attribution_addendum_active")
check(base["status"]=="FROZEN_BEFORE_CANDIDATE_SUCCESS_EVALUATION", "baseline_predeclared")
check(base["hard_target_attribution_required"]=="ROBUST_TRANSFORM_ATTRIBUTED", "robust_attribution_required")
check("suffix/future-signature state" in base["B_raw"]["forbidden"], "Braw_excludes_signature")
check(any("does not introduce a new reusable quotient carrier" in x for x in base["B_std"]["explicit_boundary"]), "Bstd_excludes_qcarrier")
check(any("does not minimize" in x for x in base["B_std"]["explicit_boundary"]), "Bstd_excludes_minimization")
check(base["B_std"]["predeclared_structural_measure"]["source_value"]==18, "baseline_measure_18")
check(base["B_std"]["predeclared_structural_measure"]["stage_values"]==[7,7,4], "baseline_stage_counts")
check("ordinary composition of displayed transition maps/relations" in base["B_std"]["allowed_source_operations"], "Bstd_fair_relation_composition")
check("direct elimination of an explicitly quantified fine intermediate state" in base["B_std"]["allowed_source_operations"], "Bstd_fair_elimination")

# Bare C(X) prohibition.
for f,d in docs.items():
    text=json.dumps(d,ensure_ascii=False)
    check("C(X)" not in text, f"no_bare_CX:{f}")
check("C(X)" not in sem, "no_bare_CX:semantic")

# Source reconstruction.
stages=src["stages"]
check([len(x["states"]) for x in stages]==[7,7,4,2], "source_stage_counts")
check(src["actions"]==["L","R"], "source_actions")
check(src["globally_nonextendable_state"]["state"]=="a6", "nonextendable_a6")
check(src["consistent_instance"]["final"]=="f1", "consistent_instance")
check(len(src["remaining_suffix_languages"]["S0"])==8, "S0_eight_suffixes")
check(len(src["remaining_suffix_languages"]["S1"])==4, "S1_four_suffixes")
check(len(src["remaining_suffix_languages"]["S2"])==2, "S2_two_suffixes")
check(src["actual_algebraic_stress"]["role"].startswith("sourcing/naturality stress"), "p1_stress_only")

Ss=[stages[i]["states"] for i in range(4)]
T0=src["transition_tables"]["T0"]; T1=src["transition_tables"]["T1"]; T2=src["transition_tables"]["T2"]
Ts=[T0,T1,T2]
actions=src["actions"]
def run(stage,s,w):
    cur=s
    for j,a in enumerate(w):
        cur=Ts[stage+j][cur][a]
    return cur
def sig(stage,s):
    rem=3-stage
    return tuple(("".join(w),run(stage,s,w)) for w in itertools.product(actions, repeat=rem))
# all maps total and stage-typed
for stage,T in enumerate(Ts):
    for s in Ss[stage]:
        check(set(T[s].keys())==set(actions), f"total_actions:{stage}:{s}")
        for a in actions:
            check(T[s][a] in Ss[stage+1], f"typed_transition:{stage}:{s}:{a}")

# Recompute signatures/classes.
expected_counts=[4,4,3]
calc_classes=[]; calc_q=[]
for stage in range(3):
    groups={}
    for s in Ss[stage]:
        groups.setdefault(sig(stage,s),[]).append(s)
    cls=list(groups.values())
    calc_classes.append(cls)
    q={}
    for i,members in enumerate(cls):
        for s in members:q[s]=i
    calc_q.append(q)
    check(len(cls)==expected_counts[stage], f"class_count_stage_{stage}")
    reg=[x["members"] for x in sq["quotient_classes"][f"Q{stage}"]]
    check(reg==cls, f"registry_classes_stage_{stage}")

# Exhaust all set partitions.
def all_parts(seq):
    if not seq:
        yield []
        return
    first=seq[0]
    for part in all_parts(seq[1:]):
        yield [[first]]+[b[:] for b in part]
        for i in range(len(part)):
            q=[b[:] for b in part]
            q[i]=[first]+q[i]
            yield q
def canon(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))
def uniq_parts(seq):
    seen=set()
    for p in all_parts(seq):
        c=canon(p)
        if c not in seen:
            seen.add(c); yield c
expected_partition=[(877,8,4),(877,8,4),(15,2,3)]
for stage in range(3):
    parts=list(uniq_parts(Ss[stage]))
    sufficient=[p for p in parts if all(len({sig(stage,s) for s in block})==1 for block in p)]
    mb=min(len(p) for p in sufficient)
    coarsest=[p for p in sufficient if len(p)==mb]
    exp=expected_partition[stage]
    check(len(parts)==exp[0], f"partition_count_stage_{stage}")
    check(len(sufficient)==exp[1], f"sufficient_count_stage_{stage}")
    check(mb==exp[2], f"coarsest_count_stage_{stage}")
    check(len(coarsest)==1, f"unique_coarsest_stage_{stage}")
    audit=sq["partition_exhaustion"][stage]
    check(audit["all_partition_count"]==len(parts), f"audit_partition_count_stage_{stage}")
    check(audit["sufficient_partition_count"]==len(sufficient), f"audit_sufficient_stage_{stage}")
    check(audit["unique_coarsest"] is True, f"audit_unique_stage_{stage}")

# Quotient transition well-defined and full simulation.
sim=0
for stage in range(2):
    for cid,members in enumerate(calc_classes[stage]):
        for a in actions:
            vals={calc_q[stage+1][Ts[stage][s][a]] for s in members}
            check(len(vals)==1, f"descends:{stage}:{cid}:{a}")
            if len(vals)==1:
                expected=f"q{stage+1}_{next(iter(vals))}"
                check(sq["induced_transitions"][f"Q{stage}_to_Q{stage+1}"][f"q{stage}_{cid}:{a}"]==expected,
                      f"induced_registry:{stage}:{cid}:{a}")
for cid,members in enumerate(calc_classes[2]):
    for a in actions:
        vals={T2[s][a] for s in members}
        check(len(vals)==1, f"final_descends:{cid}:{a}")
        if len(vals)==1:
            check(sq["induced_transitions"]["Q2_to_final"][f"q2_{cid}:{a}"]==next(iter(vals)), f"final_registry:{cid}:{a}")

def runq(stage,cid,w):
    cur=cid
    for j,a in enumerate(w):
        st=stage+j
        if st<2:
            cur=int(sq["induced_transitions"][f"Q{st}_to_Q{st+1}"][f"q{st}_{cur}:{a}"].split("_")[1])
        else:
            return sq["induced_transitions"]["Q2_to_final"][f"q2_{cur}:{a}"]
for stage in range(3):
    rem=3-stage
    for s in Ss[stage]:
        for w in itertools.product(actions, repeat=rem):
            check(run(stage,s,w)==runq(stage,calc_q[stage][s],w), f"sim:{stage}:{s}:{''.join(w)}")
            sim+=1
check(sim==92, "simulation_check_count_92")
check(sq["finite_exact_simulation"]["fine_representative_suffix_checks"]==92, "simulation_registry_92")

# Leverage / attribution.
measure=sq["state_count_measure"]
check(measure["source_total"]==18, "measure_source_18")
check(measure["quotient_total"]==11, "measure_target_11")
check(measure["strict_reduction"] is True, "measure_strict")
d1plc=next(x for x in plc["certificates"] if x["candidate"]=="D1_RECURSIVE_FULL_SUFFIX_QUOTIENT")
check(d1plc["certificate_verdict"]=="PASS_R2_V2", "D1_V2_R2_pass")
check("DEPENDENCY_REDUCTION" in d1plc["strict_leverage_class"], "D1_dependency_reduction")
check("COMPOSITIONAL_FACTORING" in d1plc["strict_leverage_class"], "D1_compositional")
check(d1plc["predeclared_measure"]["source"]==18 and d1plc["predeclared_measure"]["enterprise"]==11, "D1_measure_certificate")
d1lac=next(x for x in lac["certificates"] if x["candidate"]=="D1_RECURSIVE_FULL_SUFFIX_QUOTIENT")
check(d1lac["attribution_status"]=="ROBUST_TRANSFORM_ATTRIBUTED", "D1_robust_attribution")
check(d1lac["R2_ATTRIBUTION_ADDENDUM_PASS"] is True, "D1_attribution_addendum_pass")
check("CLASSICAL_PRIOR_ART" in d1lac["novelty_status"], "D1_prior_art_allowed")
check(lac["hard_target_witness"]=="LAC-D1", "hard_target_witness_D1")

# D2 shared/partial, D3 unused.
check(br["predeclared_measure"]["fine"]==7 and br["predeclared_measure"]["after_suffix_grouping"]==4, "D2_branch_7_to_4")
check(br["exact_checks"]["all_pass"] is True, "D2_exact_pass")
check(br["attribution_decomposition"]["overall"]=="ATTRIBUTION_SHARED_OR_PARTIAL", "D2_shared_partial")
d2lac=next(x for x in lac["certificates"] if x["candidate"]=="D2_SUFFIX_SAFE_BRANCH_RECOALESCENCE")
check(d2lac["attribution_status"]=="ATTRIBUTION_SHARED_OR_PARTIAL", "D2_lac_shared")
check(d2lac["R2_ATTRIBUTION_ADDENDUM_PASS"] is False, "D2_no_independent_addendum")
check(pf["status"]=="NOT_USED", "D3_not_used")
check(pf["undefined_sink_added"] is False, "D3_no_undefined_sink")

# Baseline gaming control.
check(bg["attribution"]=="BASELINE_SENSITIVE_ATTRIBUTION", "baseline_gaming_sensitive")
check(bg["hard_target_credit"] is False, "baseline_gaming_no_credit")
check(bg["candidate_transform"]["result"]==[["x0","y0"],["x1","y1"]], "baseline_composed_relation")
check("B_std explicitly permits ordinary relation composition" in bg["B_std_audit"], "baseline_std_catches_game")

# Naturality / novelty / historical controls.
check(nat["finite_source_scope"]["explicit_pair_swap_test"]["result"].startswith("PASS"), "finite_relabeling_pass")
check(nat["actual_algebraic_toy"]["global_claim"].startswith("NONE"), "p1_no_global_claim")
check(nat["historical_H0A_status"]=="SUSPENDED_AS_MAINLINE", "H0A_still_suspended")
d1nov=next(x for x in nov["entries"] if x["candidate"]=="D1")
check(d1nov["attribution"]=="ROBUST_TRANSFORM_ATTRIBUTED", "novelty_ledger_D1_attribution")
check("CLASSICAL_PRIOR_ART" in d1nov["novelty"], "novelty_ledger_prior_art")
hist=next(x for x in nov["entries"] if x["candidate"]=="H0B/H0C_NEGATIVE_CONTROLS")
check(hist["status"]=="UNCHANGED", "historical_controls_unchanged")
check(hist["attribution"]=="SOURCE_INHERITED_ON_FROZEN_SCOPES", "historical_source_inherited")

# Leakage / R3 / classification.
check(leak["status"]=="PASS" and leak["verdict"]=="PASS", "target_leakage_pass")
for k,v in leak["forbidden_generator_audit"].items():
    check(v is False, f"leak_forbidden_false:{k}")
check(r3["robust_attributed_R2_available"] is True, "R3_has_R2_component")
check(r3["status"]=="NO_R3_SEED", "R3_not_found")
check(r3["H1_admissible"] is False, "H1_blocked_r3")
check(cl["primary_disposition"]=="H0D_ROBUST_TRANSFORM_ATTRIBUTED_R2_FOUND", "classification_disposition")
check(cl["hard_target_pass"] is True, "classification_hard_target_pass")
check(cl["candidate_results"]["D1_RECURSIVE_FULL_SUFFIX_QUOTIENT"]["R2_ATTRIBUTION_ADDENDUM_PASS"] is True, "classification_D1_addendum")
check(cl["R3_found"] is False, "classification_R3_false")
check(cl["H1_admissible"] is False, "classification_H1_false")
check(cl["automatic_H1_start"] is False, "no_auto_H1")
check(cl["Hodge_proved"] is False, "no_Hodge_proof")
check(cl["CI_status"]=="CI_NOT_REQUIRED_FOR_RESEARCH", "CI_not_required")

# Semantic digest.
core={
 "schema":"HODGE_H0D_SEMANTIC_CORE_V1",
 "researcher_id":cl["researcher_id"],
 "task_id":cl["task_id"],
 "taskbook_source":cl["taskbook_source"],
 "primary_disposition":cl["primary_disposition"],
 "hard_target":{"name":cl["hard_target"],"pass":cl["hard_target_pass"],"witness":"D1_RECURSIVE_FULL_SUFFIX_QUOTIENT"},
 "baseline_sandwich":{"B_raw_fine_counts":[7,7,4],"B_std_fine_counts":[7,7,4],"fair_source_ops_include_direct_query_composition":True,"behavioral_quotient_preinstalled":False},
 "D1":{"quotient_counts":[4,4,3],"source_total":18,"quotient_total":11,"partition_exhaustion":[[877,8,4],[877,8,4],[15,2,3]],"simulation_checks":92,"attribution":"ROBUST_TRANSFORM_ATTRIBUTED","novelty":"CLASSICAL_PRIOR_ART / PROJECT_EXISTING_REPACKAGING"},
 "D2":{"branch_tokens":[7,4],"attribution":"ATTRIBUTION_SHARED_OR_PARTIAL","independent_hard_target_credit":False},
 "D3":"NOT_USED",
 "baseline_gaming_control":"BASELINE_SENSITIVE_ATTRIBUTION",
 "R3_found":False,
 "H1_admissible":False,
 "Hodge_proved":False,
 "historical_H0B_H0C_retype":"UNCHANGED",
 "CI_status":"CI_NOT_REQUIRED_FOR_RESEARCH"
}
digest=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
check(digest==cl["semantic_core_sha256"], "semantic_digest_classification")
check(digest in sem, "semantic_digest_markdown")
check("H0D_ROBUST_TRANSFORM_ATTRIBUTED_R2_FOUND" in sem, "semantic_disposition")
check("H1_ADMISSIBLE = false" in sem, "semantic_H1_false")
check("No Hodge proof is claimed" in sem, "semantic_no_hodge")

out={
 "checker":"HODGE_H0D_MULTISTEP_GATE_V1",
 "errors":errors,
 "checks_passed":len(passed),
 "primary_disposition":cl["primary_disposition"],
 "hard_target_pass":cl["hard_target_pass"],
 "robust_attributed_witness":"D1_RECURSIVE_FULL_SUFFIX_QUOTIENT",
 "protocol_integrity":"PASS" if not errors else "FAIL"
}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
raise SystemExit(0 if not errors else 1)
