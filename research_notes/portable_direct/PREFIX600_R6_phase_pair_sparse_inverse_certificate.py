#!/usr/bin/env python3
"""PREFIX-600: 48-phase exact structural certificate for native X6 BRC.
Run beside frozen PREFIX565_positive_marginal_certificate.py; stdlib only.
"""
from collections import Counter
from PREFIX565_positive_marginal_certificate import SCIENCE_PIN, PHASES, NEXT, TARGET, ROOTS, ACTIONS, edge
assert SCIENCE_PIN=='f42f2906d77f24085c123f3ccfe9667d41caa96d'
n=48
assert len(PHASES)==len(NEXT)==n and TARGET==4 and len(ROOTS)==9
I=[[int(i==j) for j in range(n)] for i in range(n)]
S=[[int(NEXT[i][0]==j) for j in range(n)] for i in range(n)]
A=[[NEXT[i].count(j) for j in range(n)] for i in range(n)]
assert set(NEXT[i][0] for i in range(n))==set(range(n))
ST=[[S[j][i] for j in range(n)] for i in range(n)]
def prod(X,Y):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*Y)] for row in X]
def lin(X,Y,a=1,b=1):
    return [[a*x+b*y for x,y in zip(r,s)] for r,s in zip(X,Y)]
B=lin(prod(ST,A),I,1,-1)
F=[[int(i!=j and PHASES[i][:2]==PHASES[j][:2]) for j in range(n)] for i in range(n)]
assert all(sum(row)==1 for row in F) and prod(F,F)==I
assert prod(B,B)==lin(I,F,2,2)
assert prod(B,F)==B and prod(F,B)==B
assert all(B[i][i]==0 for i in range(n))
assert all(sum(row)==2 for row in B)
# 24 F-twin pairs and a fixed-point-free 12-transposition tau on the pairs.
pairs=sorted(tuple(j for j in range(n) if F[i][j] or i==j)
             for i in range(n) if i<next(j for j in range(n) if F[i][j]))
assert len(pairs)==24
index={j:k for k,pair in enumerate(pairs) for j in pair}
tau=[]
for pair in pairs:
    succ=[j for j in range(n) if B[pair[0]][j]]
    assert succ==[j for j in range(n) if B[pair[1]][j]]
    assert len(succ)==2 and index[succ[0]]==index[succ[1]]
    tau.append(index[succ[0]])
assert all(tau[tau[k]]==k and tau[k]!=k for k in range(24))
# Three times the inverse is integral and has exactly four nonzero entries per row.
X=prod(lin(lin(I,B,1,1),F,1,-2),ST)
assert all(sorted(x for x in row if x)==[-2,1,1,1] for row in X)
assert prod(A,X)==lin(I,I,3,0) and prod(X,A)==lin(I,I,3,0)
seen=set();cycles=[]
for i in range(n):
    if i in seen: continue
    c=[];j=i
    while j not in seen: c.append(j);seen.add(j);j=NEXT[j][0]
    assert j==i
    cycles.append(c)
assert len(cycles)==8 and all(len(c)==6 for c in cycles)
P=[i for i in range(n) if TARGET in NEXT[i]]
assert P==[3,14,15] and [NEXT[i].index(TARGET) for i in P]==[0,1,1]
assert [PHASES[i][2] for i in P]==[1,1,1]
def contrast(p,r,action_label):
    c=Counter()
    for i,sgn in ((2*p,1),(2*p+1,-1)):
        for action in ACTIONS:
            j,w=edge(i,action,r)
            c[(action,j,w) if action_label else (j,w)]+=sgn
    return {k:v for k,v in c.items() if v}
for r in ROOTS:
    raw=[contrast(p,r,False) for p in range(n)]
    act=[contrast(p,r,True) for p in range(n)]
    assert all(not raw[p] and not act[p] for p in range(n) if p not in P)
    assert raw[3]==raw[14]==raw[15] and len(raw[3])==2
    assert act[14]==act[15] and len(act[3])==len(act[14])==2
    assert {k[0] for k in act[3]}=={(0,1)} and {k[0] for k in act[14]}=={(1,1)}
print('ALL_CHECKS_PASS')
print('det(A)=3^12; SNF(A)=diag(1^36,3^12); rank O7=49, rank O7+act=50, all nine roots')
