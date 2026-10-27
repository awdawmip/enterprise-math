#!/usr/bin/env python3
"""Exact two-law BRC ordered-path/coarse-observer proof witness; no external dependencies."""
from fractions import Fraction as F
from collections import defaultdict
import json

N=4
WORDS=["" ]
for n in range(1,N+1):
    WORDS += [format(k,f"0{n}b") for k in range(2**n)]

def p0(h, law):
    if not h:
        return F(1,2) if law=="P" else F(1,3)
    if len(h)==3:
        return {"001":F(3,4), "010":F(1,4)}.get(h,F(1,2))
    if len(h)<3:
        return F(1,2)
    raise ValueError("Terminal histories have no next transition")

def prefix_mass(law):
    m={"":F(1)}
    for t in range(N):
        for h in (h for h in WORDS if len(h)==t):
            v=p0(h,law)
            m[h+"0"]=m[h]*v
            m[h+"1"]=m[h]*(1-v)
    return m

def x(h): return (len(h), h[0] if h else "*", h.count("0"))
def z(h): return (len(h), h[0] if h else "*")

def explicit_policy(h):
    if len(h)<3: return (F(0), F(0), F(1))
    if len(h)==3: return (F(0),F(0),F(1)) if h=="001" else (F(0),F(1),F(0))
    return (F(1),F(0),F(0)) if h[-1]=="0" else (F(0),F(1),F(0))

def varied_policy(h):
    # A deterministic, non-symmetric family of exact randomized actions.
    t=len(h)
    if t==N:
        a=F(2+(sum(ord(c) for c in h)+t)%5,9)
        return a,1-a,F(0)
    seed=sum((i+1)*(int(c)+1) for i,c in enumerate(h))+7*t+3
    a=F((seed%4)+1,12)
    b=F((seed//3%4)+1,12)
    return a,b,1-a-b

def simulate(law,action,readout):
    alive={"":F(1)}
    obs=defaultdict(F)
    for t in range(N+1):
        for h in (h for h in WORDS if len(h)==t):
            w=alive.get(h,F(0))
            if not w: continue
            a,b,c=action(h)
            assert all(0<=p<=1 for p in (a,b,c)) and a+b+c==1
            if t==N: assert c==0
            key=lambda d:(t,readout(h),d)
            obs[key("A")]+=w*a
            obs[key("B")]+=w*b
            if t<N:
                k=p0(h,law)
                alive[h+"0"]=w*c*k
                alive[h+"1"]=w*c*(1-k)
    assert sum(obs.values(),F(0))==1
    return dict(obs)

def quotient_policy(original,readout):
    # P-survivor weighted policy, applied identically under P and Q.
    m=prefix_mass("P")
    survive={"":F(1)}
    totals=defaultdict(lambda:[F(0),F(0),F(0),F(0)])
    for t in range(N+1):
        for h in (h for h in WORDS if len(h)==t):
            w=survive.get(h,F(0))
            a,b,c=original(h)
            v=w
            row=totals[readout(h)]
            row[0]+=v;row[1]+=v*a;row[2]+=v*b;row[3]+=v*c
            if t<N:
                k=p0(h,"P")
                survive[h+"0"]=w*c*k
                survive[h+"1"]=w*c*(1-k)
    q={}
    for st,(s,a,b,c) in totals.items():
        q[st]=(a/s,b/s,c/s) if s else (F(0),F(1),F(0))
    return q

def fr(q):return f"{q.numerator}/{q.denominator}"

mass={L:prefix_mass(L) for L in ("P","Q")}
for L in ("P","Q"):
    assert len(mass[L])==31
    assert all(p>0 for p in mass[L].values())
    assert sum((mass[L][h] for h in WORDS if len(h)==N),F(0))==1
assert any(mass["P"][h]!=mass["Q"][h] for h in WORDS)
for h in WORDS:
    if not h: assert mass["Q"][h]/mass["P"][h]==1
    else:
        ratio=F(2,3) if h[0]=="0" else F(4,3)
        assert mass["Q"][h]/mass["P"][h]==ratio

assert x("001")==x("010")== (3,"0",2)
assert z("001")==z("010")== (3,"0")
assert p0("001","P")==p0("001","Q")==F(3,4)
assert p0("010","P")==p0("010","Q")==F(1,4)

checks={}
for name,policy in [("isolated_history",explicit_policy),("randomized_history",varied_policy)]:
    q=quotient_policy(policy,z)
    def qa(h):return q[z(h)]
    for L in ("P","Q"):
        original=simulate(L,policy,z)
        projected=simulate(L,qa,z)
        assert original==projected,(name,L,original,projected)
        checks[f"{name}_{L}_joint_equal"]=True
    if name=="isolated_history":
        assert q[(3,"0")]==(F(0),F(3,4),F(1,4))
        assert q[(4,"0")]==(F(3,4),F(1,4),F(0))
        checks["isolated_z_policy_t3_first0"]=[fr(i) for i in q[(3,"0")]]
        checks["isolated_z_policy_t4_first0"]=[fr(i) for i in q[(4,"0")]]

def forced_x_policy(h):
    if len(h)<3: return (F(0),F(0),F(1))
    if len(h)==3:
        return (F(0),F(1,2),F(1,2)) if x(h)==(3,"0",2) else (F(0),F(1),F(0))
    return (F(1),F(0),F(0)) if h[-1]=="0" else (F(0),F(1),F(0))

for L in ("P","Q"):
    original_x=simulate(L,explicit_policy,x)
    proposed_x=simulate(L,forced_x_policy,x)
    assert original_x!=proposed_x
    # The full-x output forces all pre-t3 branches to survive, fixes each t3
    # action other than the merged fiber, and fixes continuation 1/2 there.
    # Any t4 terminal decision can select at most the child-arrival mass.
    if L=="P": assert original_x[(4,(4,"0",3),"A")]==F(3,32)
    else: assert original_x[(4,(4,"0",3),"A")]==F(1,16)

forced_P=F(1,2)*(mass["P"]["0010"]+mass["P"]["0100"])
forced_Q=F(1,2)*(mass["Q"]["0010"]+mass["Q"]["0100"])
original_P=mass["P"]["0010"]
original_Q=mass["Q"]["0010"]
assert (original_P,forced_P,original_P-forced_P)==(F(3,32),F(1,16),F(1,32))
assert (original_Q,forced_Q,original_Q-forced_Q)==(F(1,16),F(1,24),F(1,48))
checks.update({
 "P_original_target_mass":fr(original_P),"P_max_x_only_target_mass":fr(forced_P),
 "P_gap":fr(original_P-forced_P),"Q_original_target_mass":fr(original_Q),
 "Q_max_x_only_target_mass":fr(forced_Q),"Q_gap":fr(original_Q-forced_Q),
 "h001_P":fr(mass["P"]["001"]),"h010_P":fr(mass["P"]["010"]),
 "h001_Q":fr(mass["Q"]["001"]),"h010_Q":fr(mass["Q"]["010"]),
 "positive_prefixes_per_law":31,
 "likelihood_ratio_within_z":"2/3 for first0, 4/3 for first1, 1 at root",
 "x_strong_lumpability":"FAIL, next-count 0 prob 3/4 versus 1/4",
 "coarse_observer_preservation":"PASS for explicit and randomized policies, all (T,first,D) cells under P and Q",
 "universal_result":"HAND PROOF; finite checker is witness-level only",
 "status":"PASS"})
print(json.dumps(checks,indent=2,ensure_ascii=False))
