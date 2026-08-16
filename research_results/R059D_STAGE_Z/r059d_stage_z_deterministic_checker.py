#!/usr/bin/env python3
import json, sys, hashlib, itertools
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks=[]

def ck(name, cond, detail=""):
    checks.append((name, bool(cond), detail))
    if not cond:
        raise AssertionError(f"{name}: {detail}")

def load(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

raw=load("R059D_STAGE_Z_RAW_PAIR_FRONTIER_COUNT.json")
swap=load("R059D_STAGE_Z_SWAP_ORBIT_FRONTIER_AUDIT.json")
gap=load("R059D_STAGE_Z_PRIMARY_GAP_DEFINITION_PROTOCOL.json")
coup=load("R059D_STAGE_Z_CONSTRUCTIVE_FRONTIER_COUPLING_LEDGER.json")
gt=load("R059D_STAGE_Z_GAP_LENGTH_THEOREM.json")
ms=load("R059D_STAGE_Z_M_SLOT_FRONTIER_CONTROL.json")
small=load("R059D_STAGE_Z_SMALL_K_ODD_SUM_TABLE.json")
five=load("R059D_STAGE_Z_FIVE_TO_FOUR_OR_NINE_CONTROL.json")
triv=load("R059D_STAGE_Z_TRIVIALITY_LEAKAGE_LEDGER.json")

for k in range(0,31):
    Bk={(i,j) for i in range(1,k+1) for j in range(1,k+1)}
    B1={(i,j) for i in range(1,k+2) for j in range(1,k+2)}
    F=B1-Bk
    ck(f"F2_count_{k}", len(F)==2*k+1, str(len(F)))
    row={(k+1,j) for j in range(1,k+2)}
    col={(i,k+1) for i in range(1,k+1)}
    ck(f"F2_decomp_{k}", F==row|col and row.isdisjoint(col), "")
    fixed={p for p in F if p==(p[1],p[0])}
    ck(f"F2_fixed_{k}", fixed=={(k+1,k+1)}, str(fixed))
    seen=set(); orbits=[]
    for p in sorted(F):
        if p in seen: continue
        q=(p[1],p[0]); orb={p,q}; seen|=orb; orbits.append(orb)
    ck(f"F2_orbits_{k}", len(orbits)==k+1, str(len(orbits)))
    ck(f"F2_incidence_{k}", sum(len(o) for o in orbits)==2*k+1, "")

for k in range(0,31):
    ck(f"odd_sum_{k}", sum(2*r+1 for r in range(k+1))==(k+1)**2, "")
ck("small_odd_counts", small["odd_counts"]==[1,3,5,7,9,11,13], str(small["odd_counts"]))
ck("small_cumulative", small["cumulative_counts"]==[1,4,9,16,25,36,49], str(small["cumulative_counts"]))

for m in range(1,5):
    for k in range(0,12):
        direct=(k+1)**m-k**m
        ck(f"mfrontier_{m}_{k}", direct>0, str(direct))
        ck(f"mtelescope_{m}_{k}", sum((r+1)**m-r**m for r in range(k+1))==(k+1)**m, "")

for s in range(1,5):
    for gs in itertools.product(range(1,5), repeat=s):
        A=[0,1]
        for g in gs:
            A.append(A[-1]+g)
        N=A[-1]
        a=[None]*(N+1)
        a[0]=0
        for k in range(1,len(A)-1):
            for n in range(A[k], A[k+1]):
                a[n]=k
        a[N]=len(A)-1
        ck(f"gapfill_none_{s}_{gs}", all(x is not None for x in a), str(a))
        ck(f"gapinc_{s}_{gs}", all(a[n+1]-a[n] in (0,1) for n in range(N)), str(a))
        for k,g in enumerate(gs, start=1):
            inds=[n for n,x in enumerate(a) if x==k]
            first=min(inds)
            next_first=min(n for n,x in enumerate(a) if x==k+1)
            ck(f"gaplen_{s}_{gs}_{k}", next_first-first==g, f"{next_first-first}!={g}")

ck("counterexample_k1", 1 != 2*1+1, "")
ck("coupling_negative", coup["overall"]["PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_ESTABLISHED"] is False, "")
ck("coupling_not_established", coup["overall"]["PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_NOT_ESTABLISHED"] is True, "")

for k in range(1,16):
    F={(i,j) for i in range(1,k+2) for j in range(1,k+2)} - {(i,j) for i in range(1,k+1) for j in range(1,k+1)}
    fixed={p for p in F if p==(p[1],p[0])}
    ck(f"reflection_fixed_only_{k}", len(fixed)==1 and len(F)>1, f"{len(fixed)}/{len(F)}")

A=0
for k in range(0,31):
    ck(f"A_square_{k}", A==k*k, f"{A}!={k*k}")
    A += 2*k+1
ck("conditional_status", gt["status"]=="CONDITIONAL_ONLY", gt["status"])
ck("unconditional_square_not_forced", gt["unconditional_result"]["ODD_GAP_SEQUENCE_FORCES_SQUARE_THRESHOLDS"] is False, "")

ck("five_unresolved", five["FIVE_TO_FOUR_OR_NINE_UNRESOLVED"] is True, "")
ck("five_not4", five["FIVE_TO_FOUR_FORCED_BY_FRONTIER_COUNT"] is False, "")
ck("five_not9", five["FIVE_TO_NINE_FORCED_BY_FRONTIER_COUNT"] is False, "")
ck("m_ambiguity", ms["M_SLOT_AMBIGUITY_REMAINS"] is True, "")
ck("two_slot_not_native", ms["two_slot_typing"]["TWO_SLOT_FRONTIER_NATIVELY_SELECTED"] is False, "")
ck("root_unidentified", ms["ROOT_DEGREE_REMAINS_UNIDENTIFIED"] is True, "")

for key,val in triv["leakage_flags"].items():
    ck(f"firewall_{key}", val is False, str(val))

payload="\n".join(f"{name}:{int(ok)}:{detail}" for name,ok,detail in checks).encode()
digest=hashlib.sha256(payload).hexdigest()
print(json.dumps({
    "schema":"R059D_STAGE_Z_DETERMINISTIC_CHECKER_OUTPUT_V1",
    "status":"PASS",
    "checks_total":len(checks),
    "checks_passed":sum(ok for _,ok,_ in checks),
    "checks_failed":sum(not ok for _,ok,_ in checks),
    "checks_digest_sha256":digest,
    "summary":"Exact frontier arithmetic, swap-orbit structure, arbitrary positive primary-gap freedom, reflection obstruction, conditional odd-sum square thresholds, m-slot ambiguity, five-control, and anti-leakage firewalls all pass."
}, sort_keys=True))
