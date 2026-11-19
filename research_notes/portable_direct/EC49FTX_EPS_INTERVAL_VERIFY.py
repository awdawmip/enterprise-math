#!/usr/bin/env python3
"""Exact bivariate proof for EC49FTX 0<=epsilon<=1/1000; no native Bellman run."""
from fractions import Fraction as F
import json
T=F(27,64)
D=F(4246560321495367680000000000)

def add(*ps):
    o={}
    for p in ps:
        for ij,v in p.items(): o[ij]=o.get(ij,F(0))+v
    return {ij:v for ij,v in o.items() if v}
def mul(p,q):
    o={}
    for (i,j),v in p.items():
        for (k,l),w in q.items(): o[(i+k,j+l)]=o.get((i+k,j+l),F(0))+v*w
    return o
def scale(p,c): return {k:v*c for k,v in p.items()}
def dt(p): return {(i-1,j):i*v for (i,j),v in p.items() if i>0}

A=mul({(1,0):F(1,3402000000)},
      {(0,0):F(960000),(0,1):-F(16830),(1,1):F(907),(2,1):-F(8)})
B=mul({(0,0):F(441,2496508125511680000),
       (1,0):-F(64,2496508125511680000)},
      {(0,0):F(764411904000),(0,1):-F(13610488725),
       (1,1):F(606886272),(2,1):-F(462848)})
P={
 (0,0):F(161810711838720000000),
 (0,1):-F(5717812295230560000),
 (0,2):F(50508727815805875),
 (1,1):F(305754824245248000),
 (1,2):-F(5444018553646575),
 (2,1):-F(7490036957184000),
 (2,2):F(259868534207292),
 (3,1):F(362941513728000),
 (3,2):-F(8611122157056),
 (4,2):F(142745649152)
}
assert add(mul(dt(B),A),scale(mul(B,dt(A)),-1))==scale(P,-1/D)
lower=P[(0,0)]+P[(0,1)]+P[(2,1)]*T*T+P[(1,2)]*T+P[(3,2)]*T*T*T
assert lower==F(79917705797600818522071,512)>0
assert all(v>0 for ij,v in P.items()
           if ij not in {(0,1),(2,1),(1,2),(3,2)})
assert F(64,27)-F(1,976)>0
print(json.dumps({
 "schema":"EC49FTX_EPS_INTERVAL_V1",
 "epsilon_interval":"[0,1/1000]",
 "strict_reverse_TP2_for":"0<epsilon<=1/1000",
 "FOSD_for":"0<=epsilon<=1/1000, all m in (1469/64,187/8)",
 "bivariate_P_monomials":len(P),
 "negative_monomials":4,
 "all_domain_P_positive_lower":str(lower),
 "continuous_upper_tail_derivative_lower":str(F(64,27)-F(1,976)),
 "proof":"exact polynomial identity plus all-domain bounds",
 "status":"AUTHOR_PROVED_EXACT_FRACTION_VERIFIED_PARENT_DEPENDENT_NOT_REVIEWED"
},indent=2))
