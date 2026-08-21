#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, sys
from pathlib import Path
from itertools import product
from collections import defaultdict
from math import gcd

ROOT = Path(__file__).resolve().parents[1]
RR = ROOT / "research_results"
EXPECTED_TASK = "RS-HODGE-H0H-R1-LEFSCHETZ-11-PICARD-LIFTING-CANONICAL-PLANE"
EXPECTED_TASKBOOK = "637ef5cd5dbe3ce1fbe8ef06844c6b28ae36947d"
EXPECTED_COORD = "c4649b276a3d604822c586dddafd028e15d02976"
EXPECTED_H0G = "2335f1b91998943c055b9c02d144d0128e6cdc29"
B = 3

checks = 0
failures = []
def check(cond, label):
    global checks
    checks += 1
    if not cond:
        failures.append(label)

def load(name):
    return json.loads((RR/name).read_text(encoding="utf-8"))

def unit_mul(u,v):
    return (u[0]+v[0],u[1]+v[1],u[2]*v[2])
def unit_inv(u):
    return (-u[0],-u[1],u[2])

edge_names=["01","02","03","12","13","23"]
pairs4=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def allowed_product_edge(edge,u):
    p,q,e=u
    if e not in (-1,1) or max(abs(p),abs(q))>B: return False
    if edge in ("01","23"): return q==0
    if edge in ("02","13"): return p==0
    return edge in ("03","12")

def generate_product():
    g01s=[(a,0,e) for a in range(-B,B+1) for e in (-1,1)]
    g02s=[(0,b,e) for b in range(-B,B+1) for e in (-1,1)]
    g03s=[(c,d,e) for c in range(-B,B+1) for d in range(-B,B+1) for e in (-1,1)]
    out=[]
    for g01,g02,g03 in product(g01s,g02s,g03s):
        g12=unit_mul(unit_inv(g01),g02)
        g13=unit_mul(unit_inv(g01),g03)
        g23=unit_mul(unit_inv(g02),g03)
        edges=(g01,g02,g03,g12,g13,g23)
        if not all(allowed_product_edge(n,u) for n,u in zip(edge_names,edges)):
            continue
        if unit_mul(g01,g12)!=g02: continue
        if unit_mul(g01,g13)!=g03: continue
        if unit_mul(g02,g23)!=g03: continue
        if unit_mul(unit_inv(g12),g13)!=g23: continue
        out.append(edges)
    return out

def allowed_p2(edge,u):
    p,q,e=u
    if e not in (-1,1) or max(abs(p),abs(q))>B: return False
    if edge=="01": return q==0
    if edge=="02": return p==0
    if edge=="12": return p+q==0
    return False

def generate_p2():
    g01s=[(a,0,e) for a in range(-B,B+1) for e in (-1,1)]
    g02s=[(0,b,e) for b in range(-B,B+1) for e in (-1,1)]
    out=[]
    for g01,g02 in product(g01s,g02s):
        g12=unit_mul(unit_inv(g01),g02)
        edges=(g01,g02,g12)
        if all(allowed_p2(n,u) for n,u in zip(["01","02","12"],edges)) and unit_mul(g01,g12)==g02:
            out.append(edges)
    return out

def canonical_sha(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

coord=load("HODGE_H0H_R1_COORDINATE_AUTHORITY_LEDGER.json")
src=load("HODGE_H0H_R1_ALGEBRAIC_SOURCE_SPEC.json")
base=load("HODGE_H0H_R1_SOURCE_BASELINE_SANDWICH.json")
pic=load("HODGE_H0H_R1_PICARD_LIFT_REGISTRY.json")
dlog=load("HODGE_H0H_R1_DLOG_BRIDGE_REGISTRY.json")
div=load("HODGE_H0H_R1_DIVISOR_VALUATION_REGISTRY.json")
compat=load("HODGE_H0H_R1_NATIVE_COORDINATE_COMPATIBILITY_LEDGER.json")
plc=load("HODGE_H0H_R1_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json")
attr=load("HODGE_H0H_R1_ATTRIBUTION_CERTIFICATE_REGISTRY.json")
rat=load("HODGE_H0H_R1_RATIONAL_LIFTING_LEDGER.json")
nat=load("HODGE_H0H_R1_PRESENTATION_NATURALITY_LEDGER.json")
leak=load("HODGE_H0H_R1_TARGET_LEAKAGE_LEDGER.json")
r3=load("HODGE_H0H_R1_R3_PRESEED.json")
cls=load("HODGE_H0H_R1_CLASSIFICATION.json")

check(coord["authority"]["commit"]==EXPECTED_COORD,"coordinate authority commit")
check(src["taskbook_source"]==EXPECTED_TASKBOOK,"taskbook source")
check(cls["task_id"]==EXPECTED_TASK,"task id")
check(coord["authority"]["required_facts"]["O_E"]=="0","O_E=0")
check(coord["authority"]["required_facts"]["direction_relation"]=="e1+e2+e3=0","three-positive-axis relation")
check(coord["authority"]["required_facts"]["Q_E"]=="a^2+b^2+c^2-ab-bc-ca","current Q_E")
check(coord["Q_E_used_in_picard_divisor_source"] is False,"Q_E not inserted into Picard")
check(coord["zero_typing"]["identified_by_numeral_alone"] is False,"source/native zero typing")
check(base["status"]=="FROZEN_BEFORE_ENTERPRISE_SUCCESS_COUNTS","baseline frozen status")

prod_full=generate_product()
prod_repr=[[[p,q,e] for p,q,e in ed] for ed in prod_full]
check(len(prod_full)==392,"product full cocycle count")
check(canonical_sha(prod_repr)==src["primary"]["deterministic_generation"]["source_table_sha256"],"product source digest")
for edges in prod_full:
    a,b=edges[0][0],edges[1][1]
    exp=[(u[0],u[1]) for u in edges]
    check(exp==[(a,0),(0,b),(a,b),(-a,b),(0,b),(a,0)],f"product symbolic shape {a},{b}")
    eps=[u[2] for u in edges]
    h=[1,eps[0],eps[1],eps[2]]
    for (u,(i,j)) in zip(edges,pairs4):
        check(h[i]*u[2]*h[j]==1,"constant cocycle is vertex-gauge coboundary")
check(len({(e[0][0],e[1][1]) for e in prod_full})==49,"bounded product gauge class count")

expected_raw=[14,196,392,392,392]
expected_q=[7,49,49,49,49]
sig_maps={}
for k in range(1,7):
    d=defaultdict(set)
    for e in prod_full:
        d[e[:k]].add((e[0][0],e[1][1]))
    sig_maps[k]={p:tuple(sorted(v)) for p,v in d.items()}
    if k<=5:
        check(len(d)==expected_raw[k-1],f"raw prefix count stage {k}")
        check(len(set(sig_maps[k].values()))==expected_q[k-1],f"signature class count stage {k}")
for k in range(1,6):
    bysig=defaultdict(list)
    for p,sig in sig_maps[k].items():
        ns=set()
        for e in prod_full:
            if e[:k]==p:
                ns.add(sig_maps[k+1][e[:k+1]])
        bysig[sig].append(frozenset(ns))
    for sig,vals in bysig.items():
        check(len(set(vals))==1,f"descended relational continuation stage {k}")
check(pic["strict_measure"]["raw"]==sum(expected_raw),"H1 raw total")
check(pic["strict_measure"]["future_quotient"]==sum(expected_q),"H1 quotient total")
check(pic["hodge_special_attribution"]=="SOURCE_INHERITED_LEVERAGE","H1 attribution")
check(pic["R2_ATTRIBUTION_ADDENDUM_PASS"] is False,"H1 attribution addendum")

p2_full=generate_p2()
p2_repr=[[[p,q,e] for p,q,e in ed] for ed in p2_full]
check(len(p2_full)==28,"P2 full cocycle count")
check(canonical_sha(p2_repr)==src["non_product_stress"]["source_table_sha256"],"P2 source digest")
for e in p2_full:
    n=e[0][0]
    check((e[0][0],e[0][1])==(n,0),"P2 g01")
    check((e[1][0],e[1][1])==(0,n),"P2 g02")
    check((e[2][0],e[2][1])==(-n,n),"P2 g12")
check(len({e[0][0] for e in p2_full})==7,"P2 bounded class count")

# dlog controls
check(dlog["controls"]["same_dlog_distinct_units"]["same_dlog"] is True,"dlog constant kernel")
check(dlog["controls"]["additive_match_multiplicative_failure"]["additive_cocycle_condition"]=="PASS","additive dlog control")
check(dlog["controls"]["additive_match_multiplicative_failure"]["multiplicative_cocycle_condition"]=="FAIL","multiplicative failure control")
check(dlog["attribution"]=="SOURCE_INHERITED_LEVERAGE","H2 attribution")

# divisor source arithmetic
pgen=div["product"]["principal_generators"]
# explicit ranks and primitive 2x2 minors
check(pgen==[[1,-1,0,0],[0,0,1,-1]],"product principal generators")
minors=[]
for i in range(4):
    for j in range(i+1,4):
        det=pgen[0][i]*pgen[1][j]-pgen[0][j]*pgen[1][i]
        if det: minors.append(abs(det))
g=0
for v in minors: g=gcd(g,v)
check(g==1,"product principal lattice primitive")
check(div["product"]["principal_rank"]==2,"product divisor principal rank")
check(div["product"]["quotient"]=="torsion-free rank 2 by source SNF/primitivity calculation","product divisor quotient")
p2gen=div["P2_stress"]["principal_generators"]
minors=[]
for i in range(3):
    for j in range(i+1,3):
        det=p2gen[0][i]*p2gen[1][j]-p2gen[0][j]*p2gen[1][i]
        if det: minors.append(abs(det))
g=0
for v in minors: g=gcd(g,v)
check(g==1,"P2 principal lattice primitive")
check(div["P2_stress"]["principal_rank"]==2,"P2 principal rank")
check(div["attribution"]=="SOURCE_INHERITED_LEVERAGE","H3 attribution")

# rational denominator bookkeeping
check(rat["explicit_control"]["N"]==6,"denominator N")
check(rat["explicit_control"]["integral_pair"]==[3,-2],"denominator integral pair")
check(rat["explicit_control"]["alternate_N"]==12,"alternate denominator")
check(rat["explicit_control"]["alternate_integral_pair"]==[6,-4],"alternate pair")
check(rat["integral_Hodge_claim"] is False,"no integral Hodge claim")

# H4 quotient-group coordinate compatibility
def can3(v):
    m=min(v)
    return tuple(x-m for x in v)
def phi(a,b): return can3((a,b,0))
for a in range(-4,5):
    for b in range(-4,5):
        c=phi(a,b)
        check(min(c)==0 and all(x>=0 for x in c),f"H4 canonical rep {a},{b}")
        # inverse from class: differences from 3rd coordinate
        inv=(c[0]-c[2],c[1]-c[2])
        check(inv==(a,b),f"H4 inverse {a},{b}")
for a,b,c,d in product(range(-2,3), repeat=4):
    lhs=can3(tuple(x+y for x,y in zip(phi(a,b),phi(c,d))))
    rhs=phi(a+c,b+d)
    check(lhs==rhs,"H4 canonical group law")
check(compat["H4_control"]["verdict"]=="COORDINATE_COMPATIBLE_NON_LOAD_BEARING","H4 verdict")
check(compat["H4_control"]["Q_E_used"] is False,"H4 no Q_E")
check(compat["load_bearing_H1_H2_H3"]=="COORDINATE_IRRELEVANT","load-bearing coordinate status")

# leakage and classification
check(leak["status"]=="PASS","target leakage pass")
for key,val in leak["forbidden_inputs"].items():
    check(val is False,f"forbidden generator absent: {key}")
check(attr["robust_attributed_R2_found"] is False,"no robust attributed R2")
check(cls["primary_disposition"]=="H0H_R1_SOURCE_PICARD_DIVISOR_NORMAL_FORM_ALREADY_COMPLETE","primary disposition")
check(cls["hard_target_result"]=="NOT_ESTABLISHED","hard target result")
check(cls["H1_ADMISSIBLE"] is False,"H1 blocked classification")
check(r3["H1_admissible"] is False,"H1 blocked R3")
check(r3["Hodge_proved"] is False,"no Hodge proof")
check(r3["status"]=="NOT_ESTABLISHED","R3 not established")

# load-bearing files must not use historical native assumptions
load_bearing_names=[
 "HODGE_H0H_R1_ALGEBRAIC_SOURCE_SPEC.json",
 "HODGE_H0H_R1_PICARD_LIFT_REGISTRY.json",
 "HODGE_H0H_R1_DLOG_BRIDGE_REGISTRY.json",
 "HODGE_H0H_R1_DIVISOR_VALUATION_REGISTRY.json",
 "HODGE_H0H_R1_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json",
 "HODGE_H0H_R1_ATTRIBUTION_CERTIFICATE_REGISTRY.json",
 "HODGE_H0H_R1_RATIONAL_LIFTING_LEDGER.json",
]
for name in load_bearing_names:
    txt=(RR/name).read_text(encoding="utf-8")
    check("O_E=[+1]=[-1]" not in txt,f"no signed-origin-one in load-bearing {name}")
    check("ZERO_IS_NOT_AN_ENTERPRISE_COORDINATE" not in txt,f"no no-native-zero in load-bearing {name}")
    check("sqrt(a^2+b^2+c^2)" not in txt,f"no old native norm in load-bearing {name}")

result={
 "schema":"HODGE_H0H_R1_CHECKER_OUTPUT_V1",
 "task_id":EXPECTED_TASK,
 "checks":checks,
 "passed":checks-len(failures),
 "failed":len(failures),
 "verdict":"PASS" if not failures else "FAIL",
 "failures":failures,
 "summary":{
   "product_full_cocycles":len(prod_full),
   "product_gauge_classes":49,
   "H1_raw_interface_total":sum(expected_raw),
   "H1_future_classes_total":sum(expected_q),
   "P2_full_cocycles":len(p2_full),
   "P2_gauge_classes":7,
   "robust_attributed_R2_found":False,
   "primary_disposition":cls["primary_disposition"],
   "coordinate_authority":EXPECTED_COORD,
   "H1_admissible":False
 }
}
print(json.dumps(result,indent=2,sort_keys=True))
sys.exit(0 if not failures else 1)
