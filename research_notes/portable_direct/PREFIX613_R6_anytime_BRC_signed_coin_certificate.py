#!/usr/bin/env python3
"""PREFIX613-R6 exact e-martingale certificate; original native BRC law inherited."""
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from functools import reduce
import json
from pathlib import Path

SCIENCE_PIN="f42f2906d77f24085c123f3ccfe9667d41caa96d"
UPSTREAM="9b5a1df1a87eca3478a0b2f665b887135ae14711"

def factor(m,k,p):
    assert 0<=k<=m and 0<p<1
    return F(1,(m+1)*comb(m,k)) / (p**k*(1-p)**(m-k))

def joint_e(state,probs):
    return reduce(lambda a,v:a*v,
        (factor(state[2*i],state[2*i+1],p) for i,p in enumerate(probs)),F(1))

def next_state(state,ell,sign):
    a=list(state);a[2*ell]+=1;a[2*ell+1]+=int(sign==1)
    return tuple(a)

def check_transition(state,probs,q):
    d=len(probs)
    start=joint_e(state,probs)
    rhs=F(q-d,q)*start
    for ell,p in enumerate(probs):
        rhs+=(p*joint_e(next_state(state,ell,+1),probs)
             +(1-p)*joint_e(next_state(state,ell,-1),probs))/q
    return rhs==start

def crossing_probability(probs,q,alpha,horizon,rectangular=False):
    d=len(probs);cur={(0,)*(2*d):F(1)};hit=F(0)
    bound=F(d)/alpha if rectangular else F(1)/alpha
    for _ in range(horizon):
        nxt=defaultdict(F)
        for state,mass in cur.items():
            outs=[(state,F(q-d,q))]
            for ell,p in enumerate(probs):
                outs += [(next_state(state,ell,+1),p/q),
                         (next_state(state,ell,-1),(1-p)/q)]
            for st,pr in outs:
                if not pr: continue
                e= (max(factor(st[2*i],st[2*i+1],p)
                        for i,p in enumerate(probs)) if rectangular
                    else joint_e(st,probs))
                if e>=bound: hit+=mass*pr
                else: nxt[st]+=mass*pr
        cur=nxt
        assert hit+sum(cur.values(),F(0))==1
    return hit

def run():
    checks=0
    for p in (F(1,7),F(2,5),F(3,4)):
        for m in range(21):
            for k in range(m+1):
                assert p*factor(m+1,k+1,p)+(1-p)*factor(m+1,k,p)==factor(m,k,p)
                checks+=1
    probs=[F(1,4),F(3,5)]
    for m0 in range(4):
        for k0 in range(m0+1):
            for m1 in range(4):
                for k1 in range(m1+1):
                    assert check_transition((m0,k0,m1,k1),probs,3)
                    checks+=1
    rows=[]
    for alpha in (F(1,5),F(1,10)):
        for rect in (False,True):
            v=crossing_probability(probs,3,alpha,8,rect)
            assert v<=alpha
            rows.append({"alpha":str(alpha),"rectangle":rect,"P_ever_cross_by_8":str(v)})
            checks+=1
    assert factor(12,6,F(1,2))<240
    assert factor(12,6,F(1,100))>240
    checks+=2
    assert checks==799
    result={"status":"ALL_CHECKS_PASS",
      "status_level":"AUTHOR_PROVED / EXACT_MARTINGALE_CHECKED / UNREVIEWED / NOT_ADMITTED",
      "science_pin":SCIENCE_PIN,"upstream_prefix611_commit":UPSTREAM,
      "factor":"1/((m+1)*C(m,k)*p^k*(1-p)^(m-k))",
      "joint_e":"product of d direction factors",
      "joint_region":"product_l ((m_l+1)*C(m_l,k_l)*p_l^k_l*(1-p_l)^(m_l-k_l)) > alpha",
      "rectangle":"each direction product factor > alpha/d",
      "anytime_coverage":"P_theta(all N>=0, theta in joint or rectangular region)>=1-alpha",
      "checks":checks,"exact_finite_horizon":rows,
      "native_original_graph_reexecuted":False}
    Path(__file__).with_name("PREFIX613_R6_RESULTS.json").write_text(
        json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"checks":checks,"finite":rows}))

if __name__=="__main__":run()
