#!/usr/bin/env python3
"""PREFIX-589-R6: exact native BRC future-operation nonclosure certificate."""
from collections import defaultdict, Counter
from fractions import Fraction as F
import json
from PREFIX565_positive_marginal_certificate import ACTIONS, edge, ZERO_ROOT, SCIENCE_PIN

assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert len(ACTIONS)==6
PLUS={38:116,24:248,34:60}
MINUS={0:160,2:165,7:11,32:88}
assert sum(PLUS.values())==sum(MINUS.values())==424
EXP=[(a,b,k-a-b) for k in range(4) for a in range(k+1) for b in range(k-a+1)]
assert len(EXP)==20

def native_paths(pi, n):
    current={(i,0,0,0):w for i,w in pi.items()}
    for _ in range(n):
        next_paths=defaultdict(int)
        for (i,t,p0,p1),multiplicity in current.items():
            for a in ACTIONS:
                j,w=edge(i,a,ZERO_ROOT)
                delta_t=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
                next_paths[(j,t+delta_t,p0+w[0]+w[1],p1+w[2]+w[3])]+=multiplicity
        current=next_paths
    assert sum(current.values())==424*6**n
    return current

def moments(paths,n):
    denom=424*6**n
    return [F(sum(m*t**a*p0**b*p1**c
               for (_,t,p0,p1),m in paths.items()),denom) for a,b,c in EXP]

P2a=native_paths(PLUS,2)
P2b=native_paths(MINUS,2)
A2,B2=moments(P2a,2),moments(P2b,2)
assert A2==B2
P3a=native_paths(PLUS,3)
P3b=native_paths(MINUS,3)
D={EXP[i]:x-y for i,(x,y) in enumerate(zip(moments(P3a,3),moments(P3b,3)))}
assert D[(0,0,1)]==F(11,159)
assert D[(0,1,0)]==-F(11,159)
assert D[(1,0,0)]==F(34,477)

# Native port-level conditional next-step expectation, not a surrogate dynamic.
G={i:F(sum(edge(i,a,ZERO_ROOT)[1][2]+edge(i,a,ZERO_ROOT)[1][3]
           for a in ACTIONS),6) for i in range(96)}
assert Counter(G.values())=={F(0):64,F(1):32}
def E_g(paths):
    return F(sum(m*G[i] for (i,_,_,_),m in paths.items()),424*36)
assert E_g(P2a)-E_g(P2b)==F(11,159)
# The port-level conditional expectation repairs the next P1 mean.
iP1=EXP.index((0,0,1))
assert moments(P3a,3)[iP1]==A2[iP1]+E_g(P2a)
assert moments(P3b,3)[iP1]==B2[iP1]+E_g(P2b)

result={
 "schema":"PREFIX589_R6_NATIVE_BRC_CUBIC_OBSERVER_FUTURE_NONCLOSURE_V1",
 "status":"ALL_CHECKS_PASS",
 "science_pin":SCIENCE_PIN,
 "model":"96 original native BRC ports; six labeled actions; frozen zero root",
 "initial_laws":"PREFIX588_R6 positive port laws, each denominator 424",
 "depth2_equal_raw_monomials":20,
 "depth3_different_raw_monomials":sum(v!=0 for v in D.values()),
 "depth3_delta_E_P1":str(D[(0,0,1)]),
 "depth3_delta_E_P0":str(D[(0,1,0)]),
 "depth3_delta_E_T":str(D[(1,0,0)]),
 "depth3_delta_E_Y":str(D[(1,0,0)]/192),
 "next_P1_port_expected_reward_values":{"0":64,"1":32},
 "depth2_port_repair_E_g_gap":str(E_g(P2a)-E_g(P2b)),
 "next_P1_mean_repair_verified":True,
 "theorem":"no deterministic S2->S3 update on all degree<=3 pooled moments for arbitrary start-port laws",
 "scope":"one more original native step, depth2 to depth3, zero root, conditionally uniform actions"
}
print("ALL_CHECKS_PASS")
print(json.dumps(result,indent=2,ensure_ascii=False))
