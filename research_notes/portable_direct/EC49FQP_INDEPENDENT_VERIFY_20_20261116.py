#!/usr/bin/env python3
"""EC49FQP independent exact verification.
Run INSIDE the unpacked EC49FQP_EVIDENCE directory:
    PYTHONPATH=code python3 code/EC49FQP_VERIFY_20261116.py
Needs the bundled native-data reader, frozen sources, and all 61 certificates.
No third-party packages or floating-point Bellman arithmetic.
"""
import json, hashlib
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from EC49FQI_NATIVE_DATA import V, weights, reps, cost_pair, PIN, MASTER, CSV

ROOT=Path(__file__).resolve().parent.parent
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert hashlib.sha256((ROOT/"source/frozen_original_master.txt").read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((ROOT/"source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest()==CSV
assert len(V)==228 and len(reps)==141 and sum(weights)==310

def bits(mask):
    while mask:
        low=mask&-mask
        yield low.bit_length()-1
        mask^=low

physical=[]; dedup={}
for q,row in enumerate(V):
    g={}
    for i,v in enumerate(row):
        g[v]=g.get(v,0)|(1<<i)
    values=tuple(g.values())
    physical.append(values)
    dedup.setdefault(tuple(sorted(values)),q)
assert len(dedup)==209
distinct=list(dedup.items())
FULL=(1<<141)-1

def bellman(r,t,n,d):
    # A distinct weighted Bellman recurrence with safe two-step UB pruning.
    w=[310*(d-n)+141*n*m for m in weights]
    assert sum(w)==141*310*d
    price=[t]*144+[r]*84
    min_price=min(r,t)
    @lru_cache(None)
    def mass(mask):return sum(w[i] for i in bits(mask))
    @lru_cache(None)
    def one(mask):
        if mask.bit_count()==1:return 0
        ans=10**80
        for blocks,q in distinct:
            if all((c&mask).bit_count()<=1 for c in blocks):
                ans=min(ans,price[q])
                if ans==min_price:break
        return ans
    @lru_cache(None)
    def two(mask):
        if mask.bit_count()==1:return 0
        ans=10**80
        for blocks,q in distinct:
            subs=[c for b in blocks if (c:=b&mask)]
            if len(subs)<2:continue
            val=price[q]*mass(mask)+sum(one(s)*mass(s) for s in subs if s.bit_count()>1)
            ans=min(ans,val)
        return ans
    @lru_cache(None)
    def dp(mask):
        if mask.bit_count()==1:return 0
        best=two(mask)
        for blocks,q in distinct:
            subs=[c for b in blocks if (c:=b&mask)]
            if len(subs)<=1:continue
            alive=[s for s in subs if s.bit_count()>1]
            if price[q]*mass(mask)+min_price*sum(mass(s) for s in alive)>=best:continue
            cur=price[q]*mass(mask)
            for s in alive:
                cur+=dp(s)
                if cur>=best:break
            best=min(best,cur)
        assert best<10**80
        return best
    optimum=dp(FULL)
    first=[]
    for q,branches in enumerate(physical):
        if len(branches)<=1:continue
        if price[q]*mass(FULL)+sum(dp(c) for c in branches if c.bit_count()>1)==optimum:
            first.append(q)
    return optimum,first

def A(l,x):return (1-l)*(6*x+290)/141+l*(6*x+751)/310
def B(l,x):return (1-l)*(5*x+293)/141+l*(5*x+704)/310
def C(l,x):return (1-l)*(5*x+295)/141+l*(5*x+685)/310
def gamma(x):return Q(310)*(3-x)/(7557-169*x)

GNEW=[Q(13,8),Q(15,8),Q(17,8),Q(19,8),Q(23,8)]
beta=Q(620,3299)
count=0
for x in GNEW:
    for lam,expected_first in [
        (Q(0),[32,34]),
        (gamma(x),[32,34,140,142]),
        (beta,[16,23,140,142]),
        (Q(1),[16,23])
    ]:
        fname=f"r{x.numerator}_t{x.denominator}_lambda_{lam.numerator}_{lam.denominator}.json"
        cert=json.loads((ROOT/"certificates"/fname).read_text())
        assert cert["frozen_scientific_commit"]==PIN
        assert cert["source_master_sha256"]==MASTER
        assert cert["native_root_costs_sha256"]==CSV
        assert cert["raw_multiplicities"]==weights and cert["reps"]==reps
        assert cert["prices"]=={"root":x.numerator,"terminal":x.denominator}
        assert cert["interpolation"]["numerator"]==lam.numerator
        assert cert["interpolation"]["denominator"]==lam.denominator
        actual,first=bellman(x.numerator,x.denominator,lam.numerator,lam.denominator)
        mathematical=min(A(lam,x),B(lam,x),C(lam,x))*x.denominator*141*310*lam.denominator
        assert mathematical.denominator==1
        assert actual==mathematical.numerator==cert["optimal_total_interpolated"]
        assert first==expected_first==sorted(map(int,cert["all_optimal_first_trees"]))
        for label,tree in cert["all_optimal_first_trees"].items():
            assert tree["q"]==int(label)
            c=cost_pair(tree)
            Z=310*(lam.denominator-lam.numerator)*(c["U_R"]*x.numerator+c["U_T"]*x.denominator)
            Z+=141*lam.numerator*(c["M_R"]*x.numerator+c["M_T"]*x.denominator)
            assert Z==actual
        print("EXACT_BELLMAN",x,lam,actual,first,flush=True)
        count+=1
assert count==20

old=json.loads((ROOT/"previous/EC49FQO_MACHINE_SUMMARY.json").read_text())
assert len(old["certificates"])==41
for item in old["certificates"]:
    assert hashlib.sha256((ROOT/item["path"]).read_bytes()).hexdigest()==item["sha256"]
G=sorted(GNEW+[Q(1),Q(7,6),Q(4,3),Q(3,2),Q(7,4),Q(2),Q(9,4),
               Q(5,2),Q(8,3),Q(17,6),Q(3)])
assert len(G)==16
area=sum((b-a)*(gamma(a)-gamma(b)) for a,b in zip(G,G[1:]))
assert area==Q(43591107646076555945,3699405948091520330244)
assert area/2<Q(3,500)
assert sum(b-a==Q(1,6) for a,b in zip(G,G[1:]))==5
assert all(b-a<=Q(1,8) or (b-a==Q(1,6) and b<=Q(17,6)) for a,b in zip(G,G[1:]))
k=lambda x:7557-169*x
assert Q(50,1)*Q(1,8)/(4*k(Q(3)))==Q(1,4512)
assert Q(50,1)*Q(1,6)/(4*k(Q(8,3)))>Q(1,4512)
assert (Q(8,3),Q(17,6)) in set(zip(G,G[1:]))
for x in G:
    assert (1-gamma(x))/141+gamma(x)/310==50/k(x)
print("EC49FQP_20_INDEPENDENT_BELLMAN_AND_16_PRICE_REGION_PASS")
