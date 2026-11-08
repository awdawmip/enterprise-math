#!/usr/bin/env python3
"""Independent stdlib exact 48-phase certificate for PREFIX-586; frozen original 96-port BRC."""
from fractions import Fraction as Q
from collections import Counter
S4=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):return tuple(-k if c>0 else k for k in S4[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in S4[a] for t in (-1,1) for p in near(a,t*k))
IX={p:i for i,p in enumerate(P)}
def nxt(i):
 a,p,c=P[i];b=next(b for b in range(4) if b!=a and abs(c) in S4[b])
 return tuple(IX[t] for t in [(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)])
N=tuple(nxt(i) for i in range(48));S=[[int(j in N[i]) for j in range(48)] for i in range(48)]
A=[list(map(Q,row))+[Q(i==j) for j in range(48)] for i,row in enumerate(S)]
det=Q(1)
for k in range(48):
 r=next(i for i in range(k,48) if A[i][k]);A[r],A[k]=A[k],A[r]
 if r!=k:det=-det
 v=A[k][k];det*=v;A[k]=[t/v for t in A[k]]
 for i in range(48):
  if i!=k and A[i][k]:
   v=A[i][k];A[i]=[a-v*b for a,b in zip(A[i],A[k])]
assert det==3**12
T=[[int(3*A[i][48+j]) for j in range(48)] for i in range(48)]
assert all(Q(T[i][j])==3*A[i][48+j] for i in range(48) for j in range(48))
assert Counter(v for r in T for v in r)==Counter({0:2112,1:144,-2:48})
for i in range(48):
 assert sorted(v for v in T[i] if v)==[-2,1,1,1]
 js=[j for j,t in enumerate(T[i]) if t]
 assert all(abs(P[j][2])==abs(P[i][1]) for j in js)
 assert len([j for j in range(48) if i in N[j]])==3
 assert all(abs(P[j][2])==abs(P[i][1]) for j in range(48) if i in N[j])
 for j in range(48):
  assert sum(S[i][k]*T[k][j] for k in range(48))==3*int(i==j)
  assert sum(T[i][k]*S[k][j] for k in range(48))==3*int(i==j)
print('PASS: 48 phases; det(S)=3^12; ST=TS=3I; T has 48 (-2), 144 (+1); 96 positive-cone inequalities')
