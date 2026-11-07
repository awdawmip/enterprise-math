#!/usr/bin/env python3
"""Exact independent Stage307-B finite-instance check, standard library only.

All probabilities are Fraction. 128 deterministic binary-history policies per
(W,Y1) fiber are enumerated for three future H/F visits; the general n theorem
is proved in PROOF_STAGE307B.md rather than inferred from this finite test.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb

P = (Q(1,4), Q(3,4))
W = {}
for s,j,w,y in product(range(2),repeat=4):
    pj = Q(7,8) if j==s else Q(1,8)
    pw = Q(3,4) if w==s else Q(1,4)
    py = P[s] if y else 1-P[s]
    W[s,j,w,y] = Q(1,2)*pj*pw*py
assert sum(W.values())==1
assert all(w>0 for w in W.values())

D = lambda a,b,n: Q(1,2)*sum(comb(n,k)*abs(a**k*(1-a)**(n-k)-b**k*(1-b)**(n-k)) for k in range(n+1))
weights = {(j,w,y):tuple(W[s,j,w,y] for s in range(2)) for j,w,y in product(range(2),repeat=3)}
map_rate = {(j,w,y): (P[0] if weights[j,w,y][0]>weights[j,w,y][1] else P[1]) for j,w,y in product(range(2),repeat=3)}
assert all(a!=b for a,b in weights.values())
assert sum(min(a,b) for a,b in weights.values())==Q(7,64)
assert min(abs(a-b)/(a+b) for a,b in weights.values())==Q(1,8)
assert D(*P,1)==Q(1,2) and D(*P,3)==Q(11,16)

def audit(policy,rates,g,tagged=False):
    """Trace each policy over all 8 binary outcome strings, exactly."""
    w,y=g
    orig,sim=defaultdict(Q),defaultdict(Q)
    for s,j in product(range(2),repeat=2):
        for bits in product(range(2),repeat=3):
            node=0
            trace=[]
            po=ps=W[s,j,w,y]
            for bit in bits:
                act = (policy>>node)&1  # 1=F, 0=H
                trace.append((act,bit))
                po *= (P[s] if bit else 1-P[s]) if act else Q(1,2)
                t=rates[j,w,y]
                ps *= (t if bit else 1-t) if act else Q(1,2)
                node=2*node+1+bit
            key=((s,j,tuple(trace)) if tagged else tuple(trace))
            orig[key]+=po;sim[key]+=ps
    return Q(1,2)*sum(abs(orig[k]-sim[k]) for k in orig.keys()|sim.keys())

def fff(rates,tagged=False):
    return sum(audit(127,rates,g,tagged) for g in product(range(2),repeat=2))

T_min=Q(7,64)*D(*P,3)
assert T_min==Q(77,1024)
P_map=Q(1,16)*D(*P,3)
assert P_map==Q(11,256)
assert fff(map_rate,True)==T_min
assert fff(map_rate,False)==P_map

# Explicit feasible public/joint tradeoff point, leaving middle fibers unchanged.
trade=map_rate.copy()
trade[0,0,0]=Q(1,4)
trade[1,0,0]=Q(1,2)
trade[0,1,1]=Q(1,2)
trade[1,1,1]=Q(3,4)
assert fff(trade,False)==Q(3,128)
assert fff(trade,True)==Q(165,2048)

# All 128 causal policies on the three-level binary-output history tree per g.
for label,rates,expected_public,expected_tagged in [
    ('MAP',map_rate,P_map,T_min),
    ('TRADEOFF',trade,Q(3,128),Q(165,2048)),
]:
    maxima=[]
    for tagged,expected in [(False,expected_public),(True,expected_tagged)]:
        mx=Q(0)
        for g in product(range(2),repeat=2):
            best=max(audit(policy,rates,g,tagged) for policy in range(128))
            assert best==audit(127,rates,g,tagged)
            mx+=best
        assert mx==expected
        maxima.append(mx)
    # Certified linear outer-Pareto bound: T-Tmin >= (P_map-P)_+/8.
    assert maxima[1]-T_min >= max(Q(0),P_map-maxima[0])/8
    print(f'{label} ALL_512_POLICIES_PER_OBSERVER_EXACT: public={maxima[0]} joint={maxima[1]}')

for n in range(1,10):
    dn=D(*P,n)
    formula=sum(comb(n,k)*((Q(3,4)**(n-k))*(Q(1,4)**k)-(Q(1,4)**(n-k))*(Q(3,4)**k)) for k in range((n+1)//2))
    assert dn==formula
    assert Q(7,64)*dn<=Q(7,64)
    print(f'n={n} D_n={dn} joint_min={Q(7,64)*dn} public_at_joint_min={dn/16}')

print('STAGE307B_TAGGED_ALL_HORIZONS_AND_PARETO_EXACT_PASS')
