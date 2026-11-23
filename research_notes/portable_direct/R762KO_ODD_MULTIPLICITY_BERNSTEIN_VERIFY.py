#!/usr/bin/env python3
"""Exact R762KO polynomial certificate for all odd m>=3; standard library only."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb

ports=[p for p in combinations(range(6),2) if p not in {(0,1),(2,3),(4,5)}]
assert len(ports)==12
bit={p:1<<i for i,p in enumerate(ports)}
E=[]
for i,j,k in product(range(2),repeat=3):
    a,b,c=(i,2+j),(i,4+k),(2+j,4+k)
    E.append((bit[a]^bit[b],bit[a]^bit[c],bit[b]^bit[c]))
assert len(E)==8 and all(x^y^z==0 for x,y,z in E)
F={0}
forced=[]
for tri in combinations(range(6),3):
    avail=[p for p in combinations(tri,2) if p in bit]
    if len(avail)==2:
        e=bit[avail[0]]^bit[avail[1]]
        forced.append(e)
        F|={x^e for x in tuple(F)}
assert len(forced)==12 and len(F)==512
P={0:(1,)}
for es in E:
    nextP=defaultdict(lambda:[0]*9)
    for x,co in P.items():
        for k,v in enumerate(co):
            if not v: continue
            if k<8: nextP[x][k+1]+=v
            for e in es: nextP[x^e][k]+=v
    P={x:tuple(v) for x,v in nextP.items()}
assert len(P)==2048
assert P[0] == (9,0,16,0,6,0,0,0,1)  # exact p_0(t)
classes=defaultdict(list)
for b in sorted(F-{0}):
    d=tuple(P[0][i]-P.get(b,(0,)*9)[i] for i in range(9))
    R=[]
    for i in range(7):
        R.append(d[i]+(2*R[-1] if R else 0)-(R[-2] if len(R)>1 else 0))
    expanded=[0]*9
    for i,v in enumerate(R):
        expanded[i]+=v
        expanded[i+1]-=2*v
        expanded[i+2]+=v
    assert tuple(expanded)==d
    beta=[sum((Fraction(R[i]*comb(j,i),comb(6,i)) for i in range(j+1)),Fraction(0)) for j in range(7)]
    assert all(z>=1 for z in beta), (b,R,beta)
    classes[tuple(R)].append(b)
assert len(classes)==18 and sum(map(len,classes.values()))==511
assert all(__import__('functools').reduce(lambda x,e:x^e,(es[j] for es in E),0)==0 for j in range(3))

def fiber(m):
    r=m//2
    A,B=(r*(r+1)//2,(r+1)*(r+2)//2) if m%2 else ((r+1)*(r+2)//2,r*(r+1)//2)
    dp={0:1}
    for es in E:
        nd=defaultdict(int)
        for x,v in dp.items():
            nd[x]+=A*v
            for e in es:nd[x^e]+=B*v
        dp=nd
    return {x:dp.get(x,0)-(3 if x==0 else 0) for x in F}

observations=[]
for m in (3,5,7,9,11):
    f=fiber(m)
    r=m//2
    lower=(r+1)**8*(r+2)**6//64-3
    runner=max(f[b] for b in F-{0})
    gap=f[0]-runner
    assert gap>=lower>0
    A,B=(r*(r+1)//2,(r+1)*(r+2)//2)
    assert f[0] == A**8+6*A**4*B**4+16*A**2*B**6+9*B**8-3
    observations.append((m,f[0],runner,gap,lower))
print('POLYNOMIAL_CLASSES',len(classes),'BOUNDARIES',len(F)-1)
print('CLASS_COUNTS',sorted((min(v),len(v)) for v in classes.values()))
print('ODD_EXACT',observations)
print('PASS: exhaustive exact polynomial division, positive Bernstein certificates, odd-m numeric regressions')
