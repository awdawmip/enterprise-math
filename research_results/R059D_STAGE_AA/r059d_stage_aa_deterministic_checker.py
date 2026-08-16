#!/usr/bin/env python3
import json, itertools, math, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checks=[]
def ck(name,cond,detail=""):
    checks.append((name,bool(cond),str(detail)))
    if not cond:
        raise AssertionError(f"{name}: {detail}")
def load(n):
    return json.loads((ROOT/n).read_text(encoding="utf-8"))
orbit=load("R059D_STAGE_AA_ORBIT_FRONTIER_REGISTRY.json")
coup=load("R059D_STAGE_AA_ORBIT_COUPLING_LEDGER.json")
tri=load("R059D_STAGE_AA_TRIANGULAR_THRESHOLD_THEOREM.json")
low=load("R059D_STAGE_AA_LOW_N_DISCRIMINATOR.json")
five=load("R059D_STAGE_AA_FIVE_CONTROL.json")
mc=load("R059D_STAGE_AA_M_SLOT_SYMMETRIC_CONTROL.json")
triv=load("R059D_STAGE_AA_TRIVIALITY_LEAKAGE_LEDGER.json")
claim=load("R059D_STAGE_AA_NATIVE_SEMANTICS_CLAIM_LEDGER.json")
for k in range(0,41):
    Bk={(i,j) for i in range(1,k+1) for j in range(1,k+1)}
    B1={(i,j) for i in range(1,k+2) for j in range(1,k+2)}
    F=B1-Bk
    ck(f"raw_count_{k}",len(F)==2*k+1,len(F))
    seen=set(); orbits=[]
    for p in sorted(F):
        if p in seen: continue
        q=(p[1],p[0]); o={p,q}; seen|=o; orbits.append(o)
    fixed=[o for o in orbits if len(o)==1]
    two=[o for o in orbits if len(o)==2]
    ck(f"orbit_count_{k}",len(orbits)==k+1,len(orbits))
    ck(f"fixed_count_{k}",len(fixed)==1,len(fixed))
    ck(f"two_count_{k}",len(two)==k,len(two))
    ck(f"diag_fixed_{k}",fixed[0]=={(k+1,k+1)},fixed[0])
for s in range(1,6):
    for gs in itertools.product(range(1,5), repeat=s):
        A=[0,1]
        for g in gs: A.append(A[-1]+g)
        N=A[-1]
        a=[None]*(N+1); a[0]=0
        for k in range(1,len(A)-1):
            for n in range(A[k],A[k+1]): a[n]=k
        a[N]=len(A)-1
        ck(f"gap_fill_{s}_{gs}",all(v is not None for v in a),a)
        ck(f"binary_inc_{s}_{gs}",all(a[n+1]-a[n] in (0,1) for n in range(N)),a)
        for k,g in enumerate(gs, start=1): ck(f"gap_exact_{s}_{gs}_{k}",A[k+1]-A[k]==g,(A,g))
for k in range(1,20):
    q=k+1
    for g in range(1,2*k+5):
        age=[r if r<=k else None for r in range(g)]
        age_bij=(g==q and set(age)==set(range(q)) and None not in age)
        ck(f"age_iff_{k}_{g}",age_bij==(g==q),(age,g,q))
        cyc=[r%q for r in range(g)]
        cyc_bij=(len(cyc)==q and len(set(cyc))==q)
        ck(f"cyc_iff_{k}_{g}",cyc_bij==(g==q),(cyc,g,q))
        start=7*k+3
        absr=[(start+r)%q for r in range(g)]
        abs_bij=(len(absr)==q and len(set(absr))==q)
        ck(f"abs_iff_{k}_{g}",abs_bij==(g==q),(absr,g,q))
    ck(f"short_witness_{k}",k!=q,(k,q))
    ck(f"long_witness_{k}",k+2!=q,(k+2,q))
    if k>=2: ck(f"bit_image_too_small_{k}",2<q,(2,q))
ck("coupling_negative",coup["freezes"]["PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_ESTABLISHED"] is False)
ck("coupling_not_established",coup["freezes"]["PRIMARY_GAP_TO_SWAP_ORBIT_FRONTIER_COUPLING_NOT_ESTABLISHED"] is True)
for k in range(1,60):
    A=1+sum(r+1 for r in range(1,k))
    ck(f"tri_{k}",A==k*(k+1)//2,(A,k))
ck("tri_conditional",tri["unconditional_status"]["TRIANGULAR_ACTIVATION_THRESHOLDS_CONDITIONAL_ONLY"] is True)
ck("tri_not_unconditional",tri["unconditional_status"]["TRIANGULAR_ACTIVATION_THRESHOLDS_ESTABLISHED"] is False)
sq={1:1,2:1,3:1,4:2,5:2,6:2}; tr={1:1,2:1,3:2,4:2,5:2,6:3}
for row in low["controls"]:
    n=row["n"]
    ck(f"low_sq_{n}",row["square_activation_control_level"]==sq[n],row)
    ck(f"low_tr_{n}",row["orbit_triangular_control_level"]==tr[n],row)
ck("n3_diverges",sq[3]!=tr[3],(sq[3],tr[3]))
ck("n3_under",low["freezes"]["LOW_N_N3_REMAINS_UNDERDETERMINED"] is True)
ck("n3_not_identified",low["freezes"]["LOW_N_N3_DISCRIMINATOR_IDENTIFIED"] is False)
for m in range(1,5):
    for k in range(0,7):
        vals=range(1,k+2)
        frontier=[t for t in itertools.product(vals, repeat=m) if max(t)==k+1]
        reps={tuple(sorted(t)) for t in frontier}
        formula=math.comb(k+m-1,m-1)
        ck(f"m_orbit_{m}_{k}",len(reps)==formula,(len(reps),formula))
        table=mc["small_table"][k][f"m{m}"]
        ck(f"m_table_{m}_{k}",table==formula,(table,formula))
ck("m_ambiguity",mc["typing"]["M_SLOT_AMBIGUITY_REMAINS"] is True)
ck("two_slot_not_native",mc["typing"]["TWO_SLOT_FRONTIER_NATIVELY_SELECTED"] is False)
ck("root_unidentified",mc["typing"]["ROOT_DEGREE_REMAINS_UNIDENTIFIED"] is True)
ck("five_no4",five["freezes"]["FIVE_TO_FOUR_FORCED_BY_AA"] is False)
ck("five_no9",five["freezes"]["FIVE_TO_NINE_FORCED_BY_AA"] is False)
for key,val in triv["leakage_flags"].items(): ck(f"firewall_{key}",val is False,(key,val))
ck("native_unresolved",claim["admissibility_verdict"]=="UNRESOLVED",claim["admissibility_verdict"])
ck("target_leakage_pass",claim["target_leakage_audit"].startswith("PASS"),claim["target_leakage_audit"])
payload="\n".join(f"{n}:{int(ok)}:{d}" for n,ok,d in checks).encode()
digest=hashlib.sha256(payload).hexdigest()
print(json.dumps({"schema":"R059D_STAGE_AA_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS","exit_code":0,"checks_total":len(checks),"checks_passed":sum(ok for _,ok,_ in checks),"checks_failed":sum(not ok for _,ok,_ in checks),"checks_digest_sha256":digest,"summary":"Orbit-frontier k+1 counting, arbitrary positive gap freedom, all predeclared online candidate failures, conditional triangular thresholds, low-n n=3 underdetermination, m-slot quotient controls, native-semantics typing, and anti-leakage firewalls all pass."},sort_keys=True))
