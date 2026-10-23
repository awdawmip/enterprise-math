#!/usr/bin/env python3
"""Exact two-method proof-certificate checker; only built-in Python integers/Fractions."""
from fractions import Fraction as F
A={'0':(1,665,1,333),'2':(333,333,1,333),'3':(1,1,1,997)}
W='032020'
G=(3,6,10,12)
assert all(sum(x)==1000 and min(x)>0 for x in A.values())
v=[0]*16; v[0]=1
n1=[0]
for a in W:
    u=[0]*16
    for m,weight in enumerate(v):
        for k,pk in enumerate(A[a]):
            u[m|(1<<k)]+=weight*pk
    v=u
    n1.append(sum(v[g] for g in G))
n2=[0]
for t in range(1,7):
    total=0
    for g in G:
        i,j=[x for x in range(4) if (g>>x)&1]
        both=only_i=only_j=1
        for a in W[:t]:
            q=A[a]
            both*=q[i]+q[j]
            only_i*=q[i]
            only_j*=q[j]
        total+=both-only_i-only_j
    n2.append(total)
expected=[0,0,666000,554226216,626011982376,429146205098784,436231737917062944]
assert n1==n2==expected
d=[F(n1[t],1000**t) for t in range(7)]
D=[F(0)]+[d[t]-d[t-1] for t in range(1,7)]
M=[max(d[:t+1]) for t in range(7)]
R=[F(0)]*7
for t in range(2,7):
    R[t]=sum((max(F(0),D[j]) for j in range(2,t+1)),F(0))-M[t]
assert [t for t in range(2,7) if R[t]>R[t-1]]==[4,6]
eta=F(1,2000)
for t in range(3,7):
    assert abs(D[t])>(2*t-1)*eta
    assert d[2]-d[t]>(t+2)*eta
assert M[2:]==[d[2]]*5
assert min(min(v) for v in A.values())==1
assert F(1,1000)>eta
# Parametric law changes exactly by TV=(83/250)*(1-z).
assert F(83,250)*F(1,664)==eta
print('PASS: exact 16-state and good-pair checks, TV-open-ball proof margins')
print('N=',n1)
print('deltas=',[str(x) for x in D])
print('residuals=',[str(x) for x in R])
print('positive margin at t=6:',D[6]-11*eta)
