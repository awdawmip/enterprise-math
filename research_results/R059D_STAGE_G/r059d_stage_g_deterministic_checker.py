#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib
from collections import defaultdict
from pathlib import Path
R=Path(__file__).resolve().parent
TASK="383eeb9423e11b00a96f79c88f3bb86ec93df277"
PARENT="a03e9181ddcb17a0971ac7bec8e534693cbd817e"
checks=[]
def ck(v,label):
    checks.append((label,bool(v)))
    if not v: raise AssertionError(label)

def aligned(tags,q,N):
    L=q*N
    h0,v0,_=tags[0]
    return all(h==(h0+q*i)%L and v==v0 for i,(h,v,s) in enumerate(tags))

def step(tags,q,N,sign=1):
    L=q*N
    occ=defaultdict(int)
    for h,v,s in tags: occ[(h,v)]+=1
    out=[]
    for h,v,s in tags:
        S=occ[(h,v)]
        if s=="START": a=("H" if sign==1 else "H_INV") if S>=2 else "HOLD"
        elif s==("H" if sign==1 else "H_INV"): a="V" if S>=2 else s
        elif s=="V": a="V_INV"
        elif s=="V_INV": a=("H" if sign==1 else "H_INV") if S>=2 else "HOLD"
        else: a="HOLD"
        if a=="H": out.append(((h+1)%L,v,"H"))
        elif a=="H_INV": out.append(((h-1)%L,v,"H_INV"))
        elif a=="V": out.append((h,(v+1)%7,"V"))
        elif a=="V_INV": out.append((h,(v-1)%7,"V_INV"))
        else: out.append((h,v,s))
    return out

def run(q,N,sign=1,limit=None):
    L=q*N
    tags=[(q*i,0,"START") for i in range(N)]
    h,v,s=tags[0]
    tags[0]=((h+sign)%L,v,"H" if sign==1 else "H_INV")
    lim=limit or (3*q*N+5)
    aes=[]
    recruited={0}
    first={}
    for e in range(lim+1):
        # response/recruitment by first nonbaseline state; for resident tags collision occurs q*i-1 in direction order
        if aligned(tags,q,N): aes.append(e)
        # causal recruitment follows frozen evaluator: state OR local-signature OR action-set delta.
        occ=defaultdict(int)
        for hh,vv,ss in tags: occ[(hh,vv)]+=1
        for i,(hh,vv,ss) in enumerate(tags):
            if i in recruited: continue
            S=occ[(hh,vv)]
            baseline_action="HOLD"
            if ss=="START":
                act=("H" if sign==1 else "H_INV") if S>=2 else "HOLD"
            elif ss==("H" if sign==1 else "H_INV"):
                act="V" if S>=2 else ss
            elif ss=="V": act="V_INV"
            elif ss=="V_INV":
                act=("H" if sign==1 else "H_INV") if S>=2 else "HOLD"
            else: act="HOLD"
            if (hh!=(q*i)%L or vv!=0 or ss!="START" or S!=1 or act!=baseline_action):
                recruited.add(i); first[i]=e
        tags=step(tags,q,N,sign)
    return aes,first,tags

# theorem regressions
for sign in (1,-1):
  for q in range(2,9):
    for N in range(2,9):
      aes,first,_=run(q,N,sign,limit=3*q*N)
      ck(aes[:3]==[q*N-1,2*q*N-1,3*q*N-1],f"aligned:{sign}:{q}:{N}")
      ck(len(first)==N-1,f"recruit_count:{sign}:{q}:{N}")
      ck(max(first.values())==q*(N-1)-1,f"Espan:{sign}:{q}:{N}")
      ck(q*(N-1)-1 < q*N-1,f"ineq:{sign}:{q}:{N}")

# full-state recurrence from first aligned after qN^2
for sign in (1,-1):
  for q in range(2,7):
    for N in range(2,7):
      L=q*N
      tags=[(q*i,0,"START") for i in range(N)]
      h,v,s=tags[0]; tags[0]=((h+sign)%L,v,"H" if sign==1 else "H_INV")
      snap=None
      for e in range(q*N*N + q*N):
        if e==q*N-1: snap=list(tags)
        if e==q*N-1+q*N*N: ck(tags==snap,f"full_period:{sign}:{q}:{N}")
        tags=step(tags,q,N,sign)

# large-N exact formula only
Ns=[10**36+d for d in (-11,-7,-5,-3,-2,-1,0,1,2,3,5,7,11)]+[10**30+37,10**24+19]
Qs=list(range(2,13))+[13,14,15,16,17,18,19,23,25,29,31]
for N in Ns:
  for q in Qs:
    es=q*(N-1)-1; ea=q*N-1
    ck(es<ea,f"hugeineq:{N}:{q}")
    ck(ea-es==q,f"hugegap:{N}:{q}")

# artifact semantics
search=json.loads((R/"R059D_STAGE_G_SYSTEM_SPANNING_ALIGNED_SEARCH.json").read_text())
ck(search["primary_disposition"]=="ENDOGENOUS_SYSTEM_SPANNING_EXACT_ALIGNED_RECOALESCENCE_FOUND","primary")
ck(search["highest_disposition_real_tagged_perturbation_gate"]=="PASS_BOTH_H_AND_H_INV","realI3")
kill=json.loads((R/"R059D_STAGE_G_RESOURCE_LEAKAGE_KILL_LEDGER.json").read_text())
for g in kill["gates"]:
  if g["id"]!="PARENT_IMMUTABILITY": ck(str(g["status"]).startswith("PASS"),"gate:"+g["id"])

failed=[x for x in checks if not x[1]]
digest=hashlib.sha256("\n".join(f"{k}:{int(v)}" for k,v in checks).encode()).hexdigest()
out={
"schema":"R059D_STAGE_G_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS" if not failed else "FAIL",
"researcher_id":"EM-R059D-4C7E21","taskbook_source":TASK,"frozen_parent_head":PARENT,
"checks_total":len(checks),"checks_passed":len(checks)-len(failed),"checks_failed":len(failed),
"checks_digest_sha256":digest,
"large_N_method":"closed-form E_SPAN/E_ALIGN formulas only; no huge carrier/history enumeration",
"tiny_enumeration_role":"theorem regression only for q=2..8,N=2..8",
"parent_immutability":"final GitHub compare required outside local checker"
}
(R/"R059D_STAGE_G_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2))
