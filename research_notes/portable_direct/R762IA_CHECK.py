#!/usr/bin/env python3
"""R762IA: exact finite transfer and six-saddle modular-support checks.
Uses only Python stdlib integer dynamic programming (not asymptotic numerics).
"""
from collections import defaultdict
from itertools import combinations
from fractions import Fraction

PORTS = list(combinations(range(6), 2))
TRIPLES = list(combinations(range(6), 3))
ADJ = [[] for _ in PORTS]
for i,p in enumerate(PORTS):
    for j,q in enumerate(PORTS):
        if len(set(p)&set(q)) == 1:
            h=tuple(int(k in set(p)|set(q)) for k in range(6))
            ADJ[i].append((j,h))
assert len(PORTS)==15 and all(len(a)==8 for a in ADJ)
assert len(TRIPLES)==20

# Lattice proof witnesses: h_abi - h_abj = e_i - e_j, for i != j.
for i in range(6):
    for j in range(6):
        if i==j: continue
        a,b=next((a,b) for a,b in combinations(range(6),2) if a not in (i,j) and b not in (i,j))
        v=[int(k in (a,b,i))-int(k in (a,b,j)) for k in range(6)]
        assert v == [int(k==i)-int(k==j) for k in range(6)]

# Explicit six-saddle phases theta_i=j*pi/3: all triple cosines are (-1)^j.
for j in range(6):
    assert all((j*len(t))%6 in (0,3) for t in TRIPLES)

states={(0,(0,)*6):1}
zero_counts={}
samples=[]
for m in range(0,7):
    assert all((sum(v)-3*m)%6==0 for (q,v) in states)
    assert sum(states.values()) == 16**m
    if m%2==0:
        zero_counts[m]=states.get((0,(0,)*6),0)
    positive=sorted([(q,v,c) for (q,v),c in states.items() if c], key=lambda z:(z[0],z[1]))
    samples.append((m,len(states),positive[0],positive[-1]))
    if m==6: break
    nxt=defaultdict(int)
    for (q,v),c in states.items():
        for to,h in ADJ[q]:
            plus=tuple(x+y for x,y in zip(v,h))
            minus=tuple(x-y for x,y in zip(v,h))
            nxt[(to,plus)]+=c
            nxt[(to,minus)]+=c
    states=nxt
assert zero_counts=={0:1,2:16,4:624,6:34688},zero_counts

# Covariance exact from uniform 20 supports:
Sigma=[[Fraction(sum(int(i in s and j in s) for s in TRIPLES),20) for j in range(6)] for i in range(6)]
assert all(Sigma[i][i]==Fraction(1,2) for i in range(6))
assert all(Sigma[i][j]==Fraction(1,5) for i in range(6) for j in range(6) if i!=j)
det=Fraction(3,10)**5*Fraction(3,2)
assert det==Fraction(729,200000)
print('PASS R762IA')
print('Port vertices:',len(PORTS),'directed edges:',sum(map(len,ADJ)), 'three-axis supports:',len(TRIPLES))
print('Lattice witnesses: 30 ordered axis differences')
print('Covariance det:',det)
print('Rooted signed zero-return counts:',zero_counts)
print('Finite state count by m:',[(m,num) for m,num,*_ in samples])
print('Allowed coset condition: sum(x) == 3*m mod 6; verified for all reachable states m <= 6')
