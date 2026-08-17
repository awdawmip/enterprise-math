#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from itertools import combinations

ROOT = Path(__file__).resolve().parents[1]
RR = ROOT / "research_results"

FILES = [
    "HODGE_H0B_BENCHMARK_REGISTRY.json",
    "HODGE_H0B_ENTERPRISE_CANDIDATE_REGISTRY.json",
    "HODGE_H0B_ENTERPRISE_PRIMITIVE_PROVENANCE.json",
    "HODGE_H0B_COMPARISON_THEOREM_REGISTRY.json",
    "HODGE_H0B_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json",
    "HODGE_H0B_PRESENTATION_NATURALITY_SUBGATE.json",
    "HODGE_H0B_PRIOR_ART_NOVELTY_LEDGER.json",
    "HODGE_H0B_HODGE_R3_PREINTERFACE.json",
    "HODGE_H0B_TARGET_LEAKAGE_LEDGER.json",
    "HODGE_H0B_CLASSIFICATION.json",
]

checks=[]

def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))
    if not cond:
        raise AssertionError(f"{name}: {detail}")

def load(name):
    return json.loads((RR/name).read_text(encoding="utf-8"))

bench=load(FILES[0])
cand=load(FILES[1])
prov=load(FILES[2])
comp=load(FILES[3])
cert=load(FILES[4])
nat=load(FILES[5])
nov=load(FILES[6])
r3=load(FILES[7])
leak=load(FILES[8])
cls=load(FILES[9])

# Protocol / V2
check("criterion_v2", cand["criterion"]=="REALIZATION_CLASSIFIER_V2")
valid_ranks={"R0_INERT_REPARAMETRIZATION","R1_DERIVED_REORGANIZATION","R2_NONTRIVIAL_OPERATIONAL_REALIZATION","R3_HODGE_RELEVANT_OPERATIONAL_REALIZATION"}
for c in cand["candidates"]:
    rank=c["operational_rank"]
    check(f"rank_{c['id']}", rank in valid_ranks)
    check(f"typed_comparison_{c['id']}", "C_state(" in c["typed_comparison"] and c["typed_comparison"] != "C(X)")
    check(f"no_bare_CX_{c['id']}", "C(X)" not in c["typed_comparison"])
    check(f"info_separate_{c['id']}", c["information_tag"].startswith("INFO_"))
check("hard_target_false", cls["hard_target_pass"] is False)
check("disposition", cls["primary_disposition"]=="H0B_R2_PRIOR_ART_CONTROLS_ONLY")
check("H1_blocked", cls["H1_admissible"] is False and r3["H1_admissible"] is False)
check("historical_h0a_suspended", nat["historical_h0a_status"]=="SUSPENDED_DO_NOT_EXECUTE_UNCHANGED")
check("target_leakage_pass", leak["verdict"]=="PASS")
check("finite_not_promoted", leak["finite_computation_promoted_beyond_domain"] is False)

# Finite benchmark reconstruction
fs=bench["finite_exact_surrogate"]
A0=fs["local_states"]["U0"]; A1=fs["local_states"]["U1"]; A2=fs["local_states"]["U2"]
r0=fs["restriction_labels"]["rho_01_U0"]
l1=fs["restriction_labels"]["rho_01_U1"]
r1=fs["restriction_labels"]["rho_12_U1"]
l2=fs["restriction_labels"]["rho_12_U2"]
R01={(a,b) for a in A0 for b in A1 if r0[a]==l1[b]}
R12={(b,c) for b in A1 for c in A2 if r1[b]==l2[c]}
check("R01_exact", sorted([list(x) for x in R01])==sorted(fs["compatibility_relations"]["R01"]))
check("R12_exact", sorted([list(x) for x in R12])==sorted(fs["compatibility_relations"]["R12"]))

def rel_image(R,S):
    return {y for x,y in R if x in S}
check("global_full_support", rel_image(R12, rel_image(R01,set(A0)))==set(A2))
check("consistent_control", bool(rel_image(R12,set(fs["consistent_control"]["start_middle"])) & set(fs["consistent_control"]["allowed_U2"])) is True)
check("inconsistent_control", bool(rel_image(R12,set(fs["inconsistent_control"]["start_middle"])) & set(fs["inconsistent_control"]["allowed_U2"])) is False)

# Candidate A chosen split exactness
branch0=rel_image(R01,{"a0"})
branch1=rel_image(R01,{"a1"})
check("A_split_union_mid", branch0|branch1==rel_image(R01,set(A0)))
check("A_recoalesce_final", rel_image(R12,branch0)|rel_image(R12,branch1)==rel_image(R12,rel_image(R01,set(A0))))

# Candidate B signatures and all set partitions
sig={b:frozenset(rel_image(R12,{b})) for b in A1}
check("B_signature_b00_b10", sig["b00"]==sig["b10"]==frozenset({"c0"}))
check("B_signature_b01_b11", sig["b01"]==sig["b11"]==frozenset({"c1"}))
check("B_signature_distinct", sig["b00"]!=sig["b01"])

def parts(seq):
    if not seq:
        yield []
        return
    x=seq[0]
    for p in parts(seq[1:]):
        yield [[x]]+[b[:] for b in p]
        for i in range(len(p)):
            q=[b[:] for b in p]
            q[i]=[x]+q[i]
            yield q

def canon(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))
all_parts=sorted({canon(p) for p in parts(A1)})
check("B_Bell4_15", len(all_parts)==15)
def sufficient(p):
    return all(len({sig[x] for x in block})==1 for block in p)
suff=[p for p in all_parts if sufficient(p)]
check("B_sufficient_partition_count_4", len(suff)==4)
coarsest=canon([["b00","b10"],["b01","b11"]])
check("B_coarsest_present", coarsest in suff)
check("B_unique_two_block_sufficient", [p for p in suff if len(p)==2]==[coarsest])
bc=next(c for c in cand["candidates"] if c["id"]=="ENT-B-FUTURE-SAFE-QUOTIENT-ASSEMBLY")
check("B_measure_4_to_2", bc["exact_state_count"]==4 and bc["future_safe_class_count"]==2)
bcert=next(c for c in cert["certificates"] if c["certificate_id"]=="PLC-B")
check("B_certificate_control_only", bcert["certificate_verdict"]=="PASS_ABSTRACT_R2_CONTROL_ONLY" and bcert["counts_toward_enterprise_hard_target"] is False)
check("B_leverage_dependency", bcert["strict_leverage_class"]=="DEPENDENCY_REDUCTION")
check("B_predeclared_strict", bcert["predeclared_measure_if_used"]["strict_improvement"] is True)

# Candidate C exact idempotent repair
X=[(0,0),(0,1),(1,0),(1,1)]
q=lambda x:x[0]
T=lambda x:(x[1],x[1])
repair=lambda x:(q(x),q(T(x)))
check("C_T_idempotent", all(T(T(x))==T(x) for x in X))
q_compatible=all(q(x)!=q(y) or q(T(x))==q(T(y)) for x in X for y in X)
check("C_q_not_compatible", q_compatible is False)
repair_compatible=all(repair(x)!=repair(y) or repair(T(x))==repair(T(y)) for x in X for y in X)
check("C_repair_compatible", repair_compatible is True)
check("C_semiconj_diagonal", all(repair(T(x))==(repair(x)[1],repair(x)[1]) for x in X))
check("C_no_class_reduction", len({repair(x) for x in X})==4)
ccert=next(c for c in cert["certificates"] if c["certificate_id"]=="PLC-C")
check("C_certificate_fail", ccert["certificate_verdict"]=="FAIL_R2")

# Candidate D weighted field counterexample
def field(m,c):
    return tuple(tuple(m[j]*c[i]-m[i]*c[j] for j in range(len(m))) for i in range(len(m)))
good=next(t for t in comp["theorems"] if t["id"]=="CT-D-NEG")["good_system"]
bad=next(t for t in comp["theorems"] if t["id"]=="CT-D-NEG")["bad_system"]
check("D_same_capacity_total", good["capacities"]==bad["capacities"] and good["totals"]==bad["totals"])
check("D_field_formula_good", [list(r) for r in field(tuple(good["capacities"]),tuple(good["totals"]))]==good["weighted_field"])
check("D_same_field", good["weighted_field"]==bad["weighted_field"])
check("D_assembly_differs", good["assembly_exists"] is True and bad["assembly_exists"] is False)
dc=next(c for c in cand["candidates"] if c["id"]=="ENT-D-A3-WEIGHTED-RELATION-ASSEMBLY")
check("D_missing_incidence_lift", dc["missing_object"]=="ALGEBRAIC_OVERLAP_INCIDENCE_TO_A3_RICH_RELATION_GENERATION_THEOREM")
check("D_no_R2", dc["operational_rank"]=="R1_DERIVED_REORGANIZATION")

# Novelty firewall
check("no_enterprise_R2_credit", nov["enterprise_specific_R2_credit_awarded"] is False)
for c in cand["candidates"]:
    check(f"target_credit_false_{c['id']}", c["counts_toward_h0b_hard_target"] is False)
for e in nov["entries"]:
    if "PRIOR_ART" in e["status"] or "CLASSICAL" in e["status"] or "GENERIC_RELATIONAL" in e["status"]:
        check(f"prior_art_not_enterprise_{e['candidate']}_{e['object'][:8]}", e["status"]!="ENTERPRISE_SPECIFIC_OPERATIONAL_CANDIDATE")

# R3 / route
check("no_R3", cls["R3_found"] is False and r3["R3_found"] is False)
check("B_missing_CH_bridge", "C_H_TO_" in r3["candidate_assessments"][0]["missing_C_H_bridge"])
check("next_route_different_family", cls["next_route_recommendation"]["class"]=="DIFFERENT_ENTERPRISE_PRIMITIVE_FAMILY")
check("next_route_signed_incidence", cls["next_route_recommendation"]["missing_object"]=="ALGEBRAICALLY_SOURCED_SIGNED_INCIDENCE_RELATION_CARRIER_WITH_EXACT_ASSEMBLY_COMPARISON")
check("v2_not_relaxed", cls["next_route_recommendation"]["do_not_relax"]=="REALIZATION_CLASSIFIER_V2")
check("CI_not_required", cls["CI_status"]=="CI_NOT_REQUIRED_FOR_RESEARCH")

passed=sum(ok for _,ok,_ in checks)
print(f"HODGE_H0B_CHECKER: {passed}/{len(checks)} PASS")
for name,ok,detail in checks:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""))
