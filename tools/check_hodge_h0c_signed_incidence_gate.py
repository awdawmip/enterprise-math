#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from fractions import Fraction
from itertools import product, permutations

ROOT = Path(__file__).resolve().parents[1]
RR = ROOT / "research_results"

def load(name):
    return json.loads((RR/name).read_text(encoding="utf-8"))

gates=[]
def check(name, cond, detail=""):
    gates.append({"gate":name,"pass":bool(cond),"detail":detail})
    if not cond:
        raise AssertionError(name + (": "+detail if detail else ""))

source=load("HODGE_H0C_ALGEBRAIC_OVERLAP_SOURCE_SPEC.json")
car=load("HODGE_H0C_SIGNED_INCIDENCE_CARRIER_REGISTRY.json")
bridge=load("HODGE_H0C_A3_A4_BRIDGE_AUDIT.json")
gen=load("HODGE_H0C_SOURCE_GENERATION_THEOREM_REGISTRY.json")
assembly=load("HODGE_H0C_ASSEMBLY_COMPARISON_REGISTRY.json")
plc=load("HODGE_H0C_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json")
orient=load("HODGE_H0C_ORIENTATION_NATURALITY_LEDGER.json")
rat=load("HODGE_H0C_RATIONAL_COEFFICIENT_INTERFACE.json")
prior=load("HODGE_H0C_PRIOR_ART_NOVELTY_LEDGER.json")
leak=load("HODGE_H0C_TARGET_LEAKAGE_LEDGER.json")
r3=load("HODGE_H0C_HODGE_R3_PREINTERFACE.json")
cls=load("HODGE_H0C_CLASSIFICATION.json")
sem=(RR/"HODGE_H0C_SEMANTIC_CHECKPOINT.md").read_text(encoding="utf-8")

# Protocol / V2
check("criterion_v2_disposition", cls["primary_disposition"]=="H0C_PRIOR_ART_ONLY_NO_ENTERPRISE_CREDIT")
check("hard_target_false", cls["hard_target_pass"] is False)
check("enterprise_r2_false", cls["enterprise_specific_R2_found"] is False)
check("r3_false", cls["R3_found"] is False)
check("h1_blocked", cls["H1_admissible"] is False and r3["H1_admissible"] is False)
check("ci_not_required", cls["CI_status"]=="CI_NOT_REQUIRED_FOR_RESEARCH")
check("no_bare_CX_source", "C(X)" not in json.dumps(source))
check("no_bare_CX_carrier", "C(X)" not in json.dumps(car))
check("support_signed_typed_separately", all(("support_role" in x and "signed_role" in x) if x["id"]=="S1_SUPPORT_INDEXED_A3_SIGNED_FIELD" else True for x in car["carriers"]))
check("source_generation_explicit", len(gen["theorems"])>=5)
check("source_scope_finite", source["scope"]=="FINITE_ALGEBRAIC_STYLE_LOCAL_OVERLAP_SURROGATE_ONLY")
check("no_scheme_overclaim", source["universal_scheme_claim"] is False)
check("no_hodge_claim_source", source["hodge_claim"] is False)

# Forbidden generators
for k,v in source["independence_from_forbidden_targets"].items():
    check("forbidden_source_"+k, v is False)
check("leakage_verdict", leak["verdict"]=="PASS")
for k,v in leak["checks"].items():
    check("leak_"+k, v is False)

# Carrier families
ids={x["id"] for x in car["carriers"]}
check("s1_present","S1_SUPPORT_INDEXED_A3_SIGNED_FIELD" in ids)
check("s2_present","S2_SIGNED_RECOALESCENCE_PATH_WEIGHT" in ids)
check("s3_present","S3_ZERO_CLASS_QUOTIENT_WITH_SUPPORT" in ids)
check("no_enterprise_credit_carrier", car["enterprise_specific_R2_found"] is False)
for x in car["carriers"]:
    check("prior_art_zero_credit_"+x["id"], x["enterprise_novelty"]=="PRIOR_ART_RECOVERY_NO_ENTERPRISE_R2_CREDIT")

# Algebra functions
def zfield(m,c):
    n=len(m)
    return tuple(tuple(m[j]*c[i]-m[i]*c[j] for j in range(n)) for i in range(n))
def lex_forest(n, edges):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    out=[]
    for i,j in sorted(edges):
        a,b=find(i),find(j)
        if a!=b:
            parent[a]=b
            out.append((i,j))
    return out
def zero_classes(m,c):
    Z=zfield(m,c); n=len(m)
    unseen=set(range(n)); q={}
    k=0
    while unseen:
        s=min(unseen)
        group={i for i in unseen if Z[s][i]==0}
        for i in group:q[i]=k
        unseen-=group;k+=1
    return q
def rho(m,c,i): return Fraction(c[i],m[i])
def eta(m,c,i,j): return rho(m,c,i)-rho(m,c,j)
def pweight(m,c,path):
    return sum((eta(m,c,a,b) for a,b in zip(path,path[1:])), Fraction(0))

pairs=[(0,1),(0,2),(1,2)]
cases=0
strict=0
for m in product((1,2), repeat=3):
    for c in product((-1,0,1), repeat=3):
        Z=zfield(m,c)
        # identities
        for i in range(3):
            check_name=None
            assert Z[i][i]==0
            for j in range(3):
                assert Z[j][i]==-Z[i][j]
                assert Fraction(Z[i][j],m[i]*m[j])==rho(m,c,i)-rho(m,c,j)
                for k in range(3):
                    assert m[k]*Z[i][j]+m[i]*Z[j][k]+m[j]*Z[k][i]==0
        for mask in range(8):
            E=[pairs[k] for k in range(3) if (mask>>k)&1]
            src=all(rho(m,c,i)==rho(m,c,j) for i,j in E)
            ent=all(Z[i][j]==0 for i,j in E)
            assert src==ent
            T=lex_forest(3,E)
            assert all(Z[i][j]==0 for i,j in T)==ent
            q=zero_classes(m,c)
            assert all(q[i]==q[j] for i,j in E)==ent
            if len(T)<len(E): strict+=1
            cases+=1
check("s1_exhaustive_1728", cases==1728, str(cases))
check("s1_comparison_all_pass", assembly["comparisons"][0]["exhaustive_check"]["result"]=="PASS_1728_OF_1728")
check("tree_basis_strict_cases", strict==216, str(strict))
check("tree_triangle_measure", plc["certificates"][0]["predeclared_measure"]["raw_triangle"]==3 and plc["certificates"][0]["predeclared_measure"]["basis_triangle"]==2)
check("s3_exhaustive", assembly["comparisons"][4]["exhaustive_check"]["result"]=="PASS_1728_OF_1728")

# Relabeling equivariance n=3
relab=0
for m in product((1,2), repeat=3):
    for c in product((-1,0,1), repeat=3):
        Z=zfield(m,c)
        for p in permutations(range(3)):
            inv=[0]*3
            for old,new in enumerate(p): inv[new]=old
            m2=tuple(m[inv[i]] for i in range(3))
            c2=tuple(c[inv[i]] for i in range(3))
            Z2=zfield(m2,c2)
            for i in range(3):
                for j in range(3):
                    assert Z2[p[i]][p[j]]==Z[i][j]
            relab+=1
check("patch_permutation_equivariance", relab==8*27*6, str(relab))
check("orientation_ledger_pass", orient["patch_relabeling"]["status"]=="PASS")
check("orientation_reversal_law", orient["orientation_rule"]["reversal"]=="Z_ji=-Z_ij; eta_ji=-eta_ij")
check("no_full_pgl2_overclaim", orient["full_PGL2_naturality_claim"] is False)

# S2 diamond exact
diamond=0
for m in product((1,2), repeat=4):
    for c in product((-1,0,1), repeat=4):
        w1=pweight(m,c,(0,1,3))
        w2=pweight(m,c,(0,2,3))
        assert w1==w2==rho(m,c,0)-rho(m,c,3)
        diamond+=1
check("s2_diamond_1296", diamond==1296, str(diamond))
check("s2_measure_2_to_1", plc["certificates"][1]["predeclared_measure"]["raw_diamond_paths"]==2 and plc["certificates"][1]["predeclared_measure"]["recoalesced_tokens"]==1)
check("naive_cancellation_rejected", "+1 and -1" in assembly["comparisons"][3]["counterexample"])

# S3 cancellation exact
m=(1,1,1,1); c=(1,-1,1,-1); Z=zfield(m,c)
cross=[(0,2),(0,3),(1,2),(1,3)]
vals=[Z[i][j] for i,j in cross]
check("s3_fine_cross_values", vals==[0,2,-2,0], str(vals))
check("s3_coarse_cancel_zero", sum(vals)==0)
check("s3_fine_inconsistent", not all(v==0 for v in vals))
check("bridge_records_cancellation", bridge["tests"]["signed_cancellation"]["status"]=="COUNTEREXAMPLE_CONFIRMED")
check("a3_generated_support_not_source_support", bridge["tests"]["generated_support_identity"]["status"]=="NOT_A_SUBSTITUTE_FOR_SOURCE_OVERLAP")

# H0B incidence boundary repaired
pair=source["required_examples"]["h0b_incidence_boundary_pair"]
check("h0b_same_m", pair["same_m"]==[1,1])
check("h0b_same_c", pair["same_c"]==[0,1])
check("h0b_truth_diff", pair["system_A"]["assembly"] != pair["system_B"]["assembly"])
check("incidence_retained", cls["h0b_incidence_loss_repaired"] is True)

# Rational interface
check("rational_interface_status", rat["status"]=="FROZEN_INTERFACE_ONLY")
check("integer_core", rat["integral_core"]["Z_edge"]=="Z-valued")
check("rational_eta", "rho_i-rho_j" in rat["rational_normalization"]["identity"])
check("no_integral_hodge", rat["hodge_boundary"]["integral_hodge_replacement_claim"] is False)
check("no_CH_bridge", rat["hodge_boundary"]["C_H_to_this_carrier_map_constructed"] is False)

# Prior art
check("prior_matrix_size", len(prior["matrix"])>=6)
for item in prior["matrix"][:5]:
    check("prior_zero_"+item["item"], item["enterprise_credit"]=="ZERO")
check("novelty_conclusion", prior["novelty_conclusion"]=="NO_LOAD_BEARING_ENTERPRISE_SPECIFIC_LEVERAGE_SURVIVES_PRIOR_ART_REDUCTION")
check("support_plus_weight_not_novel", prior["support_plus_integer_weight_is_novel_by_itself"] is False)

# PLC completeness
required_fields=[
"certificate_id","candidate","typed_source_object","typed_enterprise_object",
"source_theorem_critical_predicate_or_operator","independent_enterprise_definition",
"comparison_theorem","non_tautology_audit","strict_leverage_class","strict_leverage_witness",
"presentation_naturality_functoriality_scope","target_leakage_audit",
"prior_art_novelty_status","downstream_theorem_obligation_unlocked","certificate_verdict"
]
for cert in plc["certificates"]:
    for f in required_fields:
        check("plc_"+cert["certificate_id"]+"_"+f, f in cert)
    check("plc_no_enterprise_credit_"+cert["certificate_id"], cert["counts_toward_enterprise_hard_target"] is False)
check("plc_enterprise_count_zero", plc["enterprise_specific_R2_certificate_count"]==0)

# R3 / semantic
check("r3_missing_HBR1", r3["candidate_shape"]["HBR1_C_H_to_enterprise"]=="MISSING")
check("r3_missing_HBR3", r3["candidate_shape"]["HBR3_hodge_to_enterprise_theorem"]=="MISSING")
check("r3_no_HBR5", r3["candidate_shape"]["HBR5_algebraic_cycle_lifting_interface"]=="NOT_AVAILABLE")
check("semantic_disposition", "`H0C_PRIOR_ART_ONLY_NO_ENTERPRISE_CREDIT`" in sem)
check("semantic_h1_blocked", "`NOT_ADMISSIBLE`" in sem)
check("semantic_no_hodge", "No H1 work was started." in sem)

# Final consistency
check("source_generation_success", cls["source_generation_success"] is True)
check("assembly_success", cls["exact_assembly_comparison_success"] is True)
check("strict_controls_success", cls["strict_operational_leverage_controls_found"] is True)
check("do_not_relax_v2", cls["next_route_recommendation"]["do_not_relax"]=="REALIZATION_CLASSIFIER_V2")
check("final_disposition_matches_evidence", cls["primary_disposition"]=="H0C_PRIOR_ART_ONLY_NO_ENTERPRISE_CREDIT")

out={
 "schema":"HODGE_H0C_CHECKER_OUTPUT_V1",
 "status":"PASS",
 "researcher_id":source["researcher_id"],
 "task_id":source["task_id"],
 "gate_count":len(gates),
 "passed":sum(1 for g in gates if g["pass"]),
 "failed":sum(1 for g in gates if not g["pass"]),
 "gates":gates,
 "meaning":"protocol/artifact consistency and declared finite exact computations only; not Enterprise R2/R3 or Hodge proof"
}
(RR/"HODGE_H0C_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"{out['passed']}/{out['gate_count']} PASS")
