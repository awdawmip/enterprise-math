#!/usr/bin/env python3
"""R701 exact V29 four-ring PASS/counter-PASS BRC count-fiber checks."""
from itertools import product, combinations
from math import comb
from collections import Counter
import json

def compositions(q,n):
    if n==1:
        yield (q,)
    else:
        for k in range(q+1):
            for tail in compositions(q-k,n-1):
                yield (k,)+tail

def build(omega,q):
    v=tuple(max(o,0)+x for o,x in zip(omega,q))
    w=tuple(max(-o,0)+x for o,x in zip(omega,q))
    M=[[0]*4 for _ in range(4)]
    for i in range(4):
        j=(i+1)%4
        M[i][j]=v[i]; M[j][i]=w[i]
    O=tuple(M[i][(i+1)%4]-M[(i+1)%4][i] for i in range(4))
    u=tuple(sum(M[i])-sum(M[j][i] for j in range(4)) for i in range(4))
    P=sum(map(sum,M))
    H=tuple(v[i]+w[i] for i in range(4))
    return v,w,O,u,P,H

checks=0; fibers={}
for Q in range(7):
    qset=list(compositions(Q,4))
    assert len(qset)==comb(Q+3,3)
    fibers[str(Q)]={"states":len(qset),"bits":(len(qset)-1).bit_length()}
    for omega in product((-1,0,1),repeat=4):
        seen=set()
        for q in qset:
            v,w,O,u,P,H=build(omega,q)
            assert O==omega
            assert u==tuple(omega[i]-omega[(i-1)%4] for i in range(4))
            assert P==sum(map(abs,omega))+2*Q
            H3=P-sum(H[:3])
            assert H3==H[3]
            assert all((H[i]+O[i])%2==0 for i in range(4))
            assert tuple((H[i]+O[i])//2 for i in range(4))==v
            assert tuple((H[i]-O[i])//2 for i in range(4))==w
            seen.add((v,w))
            checks+=1
        assert len(seen)==comb(Q+3,3)

witnesses=[]
for observed in combinations(range(4),2):
    missing=[i for i in range(4) if i not in observed]
    qa=[0]*4; qb=[0]*4
    qa[missing[0]]=1; qb[missing[1]]=1
    a=build((0,0,0,0),qa); b=build((0,0,0,0),qb)
    assert a[2]==b[2] and a[4]==b[4]==2
    assert all(a[5][i]==b[5][i] for i in observed)
    assert a[:2]!=b[:2]
    witnesses.append({"observed":observed,"q_A":qa,"q_B":qb})

forward=0
for v in product(range(25),range(19),range(7),range(13)):
    if not any(v): continue
    O=build(v,(0,0,0,0))[2]
    assert O==v
    forward+=1
assert checks==17010 and forward==43224
result={"status":"R701_EXACT_COUNTERFLOW_FIBERS_PASS",
        "domain":"n=4; omega_i in {-1,0,1}; Q=0..6",
        "counterflow_ledgers_checked":checks,
        "forward_only_capacity_box_checked":forward,
        "fibers_by_Q":fibers,
        "two_H_counterexamples":witnesses,
        "universal_scope":"Symbolic theorem for all n>=3, omega integer, Q>=0"}
print(json.dumps(result,ensure_ascii=False,sort_keys=True))
