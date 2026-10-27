#!/usr/bin/env python3
"""Exact author-level BRC N=3 two-layer Jensen-gate verification; no floating point."""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256

Y = (F(1,10), F(99,100), F(101,100), F(19,10))
PARAM = {(0,0):F(1,100), (0,1):F(49,100),
         (1,0):F(1,4),   (1,1):F(1,4)}
ACTIONS = ('P','Q','C')

def K(p):
    return (p, F(1,2)-p, F(1,2)-p, p)

def gain(p):
    return F(1)-sum(k*min(y, F(1)) for k,y in zip(K(p), Y))

LEAVES = [(g,j,k, F(1,4)*K(PARAM[g,j])[k],
           Y[k]*F(1,4)*K(PARAM[g,j])[k])
          for g,j,k in product(range(2),range(2),range(4))]
assert len(LEAVES)==16 and all(q>0 and p>0 for *_,q,p in LEAVES)
assert sum(x[3] for x in LEAVES)==sum(x[4] for x in LEAVES)==1
for g,j in product(range(2),repeat=2):
    assert sum(K(PARAM[g,j])) == sum(y*k for y,k in zip(Y,K(PARAM[g,j]))) == 1

G = {(g,j):gain(PARAM[g,j]) for g,j in product(range(2),repeat=2)}
M_g = {g:(G[g,0]+G[g,1])/2 for g in range(2)}
M = (M_g[0]+M_g[1])/2
s_star=M/2

def vals(full_actions, s):
    # full_actions 6 entries: two first-stage g actions, four second-stage g,j actions.
    first, second = full_actions[:2], full_actions[2:]
    eP=eQ=tP=tQ=F(0)
    for g,j,k,q,p in LEAVES:
        a=first[g]
        if a != 'C': t=1
        else:
            a=second[2*g+j]
            if a != 'C': t=2
            else:
                t=3
                a='Q' if Y[k]<1 else 'P'
        eP += p * (a=='Q')
        eQ += q * (a=='P')
        tP += p*t; tQ += q*t
    return eP,eQ,tP,tQ

def objective(o,s): return o[0]+o[1]+s*o[3]

def exact_min(s, compressed):
    policies = product(ACTIONS, repeat=(2 if compressed else 6))
    best = None
    for a in policies:
        full_actions=(a[0],a[0],a[1],a[1],a[1],a[1]) if compressed else a
        o=vals(full_actions,s); cost=objective(o,s)
        if best is None or cost<best[0]: best=(cost,a,o)
    return best

def predicted(s):
    full_gain=sum(max(F(0), (max(F(0),G[g,0]-s)+max(F(0),G[g,1]-s))/2-s)
                  for g in range(2))/2
    lr_gain=max(F(0), M-2*s)
    return F(1)+s-full_gain, F(1)+s-lr_gain

assert G[0,0]==F(139,10000) and G[0,1]==F(4411,10000)
assert G[1,0]==G[1,1]==F(91,400)
assert M_g[0]==M_g[1]==M==F(91,400)
assert s_star==F(91,800)
star_full,star_lr=predicted(s_star)
assert (star_full,star_lr,star_lr-star_full)==(F(87103,80000),F(89100,80000),F(1997,80000))
for s in (F(0),F(1,100),s_star/2,s_star,F(1,8),M,F(1,2),F(1)):
    ff,fl=exact_min(s,False),exact_min(s,True)
    predicted_full,predicted_lr=predicted(s)
    assert (ff[0],fl[0])==(predicted_full,predicted_lr),(s,ff,fl)
    print(f'price={s}: full={ff[0]} LR={fl[0]} gap={fl[0]-ff[0]}')
ff,fl=exact_min(s_star,False),exact_min(s_star,True)
print('P/Q leaf count:',len(LEAVES))
print('G_A0,G_A1,G_B0,G_B1:',tuple(G[g,j] for g,j in product(range(2),repeat=2)))
print('group means:',M_g,'M=',M,'critical price=',s_star)
print('full witness policy:',ff[1],'O=',ff[2]);print('LR optimal policy:',fl[1],'O=',fl[2])
print('EXACT CRITICAL GAP =',fl[0]-ff[0]);
print('ENUMERATION: 3^6=729 full early deterministic action tables; 3^2=9 LR early tables, each price.')
print('CHECK SCOPE: 8 rational prices plus symbolic all-s real theorem in PROOF.md.')
print('ALL EXACT CHECKS PASSED')
