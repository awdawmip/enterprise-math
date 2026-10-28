#!/usr/bin/env python3
"""EC49D exact executable certificate; see PROOF.md for all-real proofs."""
import json
from fractions import Fraction as F
from itertools import product
from random import Random
P={(0,0):F(1,8),(0,1):F(3,8),(1,0):F(1,4),(1,1):F(1,4)}
Q={(0,0):F(3,8),(0,1):F(1,8),(1,0):F(3,8),(1,1):F(1,8)}
leaf=list(product(range(2),repeat=3))  # (W,U,V); U fair ancillary
p={(w,u,v):P[w,v]/2 for w,u,v in leaf}
q={(w,u,v):Q[w,v]/2 for w,u,v in leaf}
assert sum(p.values())==sum(q.values())==1 and all(min(p[k],q[k])>0 for k in leaf)
assert len({P[k]/Q[k] for k in P})==4
A=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))]
def O(first,last):
    a=b=ep=eq=F(0)
    for w,u,v in leaf:
        _,accept,c=first(w,u)
        t=last(w,u,v)
        a+=p[w,u,v]*(accept+c*t)
        b+=q[w,u,v]*(accept+c*t)
        ep+=p[w,u,v]*(1+c)
        eq+=q[w,u,v]*(1+c)
    return (a,b,ep,eq)
def reward(o):
    return o[0]-o[1]-F(3,16)*(o[2]+o[3]-2)
C=set(); R=set(); B=set()
for x in range(3):
    for bits in product((0,1),repeat=4):
        C.add(O(lambda w,u,x=x:A[x],lambda w,u,v,bits=bits:F(bits[2*w+v])))
for xs in product(range(3),repeat=2):
    for bits in product((0,1),repeat=4):
        R.add(O(lambda w,u,xs=xs:A[xs[w]],lambda w,u,v,bits=bits:F(bits[2*w+v])))
for xs in product(range(3),repeat=4):
    for bits in product((0,1),repeat=8):
        B.add(O(lambda w,u,xs=xs:A[xs[2*w+u]],lambda w,u,v,bits=bits:F(bits[4*w+2*u+v])))
assert C<=R<=B
assert (max(map(reward,C)),max(map(reward,R)),max(map(reward,B)))==(0,F(1,16),F(1,16))
witness=O(lambda w,u:A[2] if w==0 else A[0],lambda w,u,v:F(P[w,v]>Q[w,v]))
assert witness==(F(3,8),F(1,8),F(3,2),F(3,2)) and witness in B and witness not in C
rng=Random(49102026)
def d3():
    n=[rng.randrange(1,10) for _ in range(3)]; return tuple(F(k,sum(n)) for k in n)
for refined in (False,True):
    for _ in range(700):
        ca=d3(); fa={w:d3() for w in range(2)}; fb={(w,u):d3() for w in range(2) for u in range(2)}
        ta={(w,v):F(rng.randrange(9),8) for w in range(2) for v in range(2)}
        tb={h:F(rng.randrange(9),8) for h in leaf}
        theta=F(rng.randrange(13),12)
        xa=lambda w,u: fa[w] if refined else ca
        xb=lambda w,u: fb[w,u]
        ya=lambda w,u,v:ta[w,v]
        yb=lambda w,u,v:tb[w,u,v]
        oa=O(xa,ya);ob=O(xb,yb)
        mixed=tuple(theta*oa[i]+(1-theta)*ob[i] for i in range(4))
        x=lambda w,u:tuple(theta*xa(w,u)[i]+(1-theta)*xb(w,u)[i] for i in range(3))
        def y(w,u,v):
            aa=theta*xa(w,u)[2];bb=(1-theta)*xb(w,u)[2]
            return (aa*ya(w,u,v)+bb*yb(w,u,v))/(aa+bb) if aa+bb else F(0)
        assert O(x,y)==mixed
# Fixed exogenous prefix: Z0 probability 1/3, Z1 source-neutral uniform W,V.
assert all(F(1,3)*min(P[k],Q[k])>0 for k in P)
assert 4*F(1,6)==F(2,3)
fixed=tuple(F(1,3)*witness[i]+(F(2,3) if i>=2 else F(0)) for i in range(4))
assert fixed==(F(1,8),F(1,24),F(7,6),F(7,6)) and reward(fixed)==F(1,48)
assert F(1,3)*max(map(reward,R))==F(1,48)
assert F(1,3)*max(map(reward,C))==0
cases=[]
for delta in (F(0),F(1,24),F(1,8),F(1,6),F(1,4),F(1)):
    c=max(F(0),F(1,16)-F(3,8)*delta);f=F(1,16)
    assert f-c==min(F(1,16),F(3,8)*delta)
    cases.append((str(delta),str(c),str(f),str(f-c)))
print(json.dumps({"pass":True,"exact":"Fraction","deterministic_counts":[48,144,20736],
 "distinct_raw_deterministic_points":[len(C),len(R),len(B)],
 "root_random_policy_checks":1400,"A_support":["0","1/16"],"B_support":"1/16",
 "A_refined_witness":list(map(str,witness)),"fixed_prefix_gap":"1/48",
 "fixed_prefix_witness":list(map(str,fixed)),
 "delay_rows_delta_coarse_refined_gap":cases},indent=2,sort_keys=True))
