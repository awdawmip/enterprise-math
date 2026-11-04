#!/usr/bin/env python3
"""Exact BRC two-gate source-history separation, full legal stopping/declaring actions."""
from fractions import Fraction as F
from itertools import product
R=(F(1,2),F(1),F(3,2))
K=(F(3,8),F(1,4),F(3,8))
W=(F(1,2),F(1,2))
M=(( ((F(1,4),F(1,2)),(F(3,4),F(1,2))),
      ((F(1,2),F(1,4)),(F(1),F(1,2)),(F(3,2),F(1,4))),
      ((F(5,4),F(1,2)),(F(7,4),F(1,2)))),
   (  ((F(1,4),F(1,2)),(F(3,4),F(1,2))),
      ((F(1,2),F(3,8)),(F(1),F(1,4)),(F(3,2),F(3,8))),
      ((F(5,4),F(1,2)),(F(7,4),F(1,2)))) )
S=tuple(sorted({s for m in M for v in m for s,q in v}))
N=(F(-1),F(-1),F(0),-F(5,32))
assert S==(F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(7,4))
assert sum(K)==sum(k*r for k,r in zip(K,R))==1
for h in range(2):
    for j in range(3):
        assert all(q>0 and s>0 for s,q in M[h][j])
        assert sum(q for s,q in M[h][j])==1
        assert sum(s*q for s,q in M[h][j])==R[j]
        assert sum((s/R[j])*q for s,q in M[h][j])==1

def vec(t1, t2, decl):
    ep=eq=tp=tq=F(0)
    def add(q, ratio, time, label):
        nonlocal ep,eq,tp,tq
        tp+=q*ratio*time
        tq+=q*time
        if label==0: ep+=q*ratio
        else: eq+=q
    for h in range(2):
        if t1[h]!=2: add(W[h],F(1),F(1),t1[h]);continue
        for j in range(3):
            q=W[h]*K[j];action=t2[h][j]
            if action!=2: add(q,R[j],F(2),action)
            else:
                for s,prob in M[h][j]:add(q*prob,s,F(3),decl[h][s])
    return ep,eq,tp,tq

def dot(v,n=N):return sum(x*y for x,y in zip(v,n))
C=lambda r:max(N[0]*r,N[1])
V=tuple(tuple(N[2]*R[j]+N[3]+sum(q*C(s) for s,q in M[h][j])-C(R[j]) for j in range(3)) for h in range(2))
Y=tuple(N[2]+N[3]+sum(K[j]*(C(R[j])-C(F(1))+max(F(0),V[h][j])) for j in range(3)) for h in range(2))
barY=sum(W[h]*Y[h] for h in range(2))
Z=N[2]+N[3]+sum(K[j]*(C(R[j])-C(F(1))+max(F(0),sum(W[h]*V[h][j] for h in range(2)))) for j in range(3))
base=C(F(1))+N[2]+N[3]
full=base+sum(W[h]*max(F(0),Y[h]) for h in range(2))
lr_formula=base+max(F(0),Z)
assert V==((-F(5,32),-F(1,32),-F(5,32)),(-F(5,32),F(1,32),-F(5,32)))
assert Y==(F(1,32),F(5,128)) and barY==F(9,256) and Z==F(1,32)
assert full==-F(287,256) and lr_formula==-F(9,8) and full-lr_formula==F(1,256)

lrmax=None; arg=None; count=0
for stop in (0,1):
    v=vec((stop,stop),((0,0,0),(0,0,0)),({},{ }));q=dot(v);count+=1
    if lrmax is None or q>lrmax:lrmax,arg=q,(('stop',stop),v)
for gates in product((0,1,2),repeat=3):
    for choices in product((0,1),repeat=len(S)):
        labels=dict(zip(S,choices))
        v=vec((2,2),(gates,gates),(labels,labels));q=dot(v);count+=1
        if lrmax is None or q>lrmax:lrmax,arg=q,(('continue',gates,choices),v)
assert count==3458 and lrmax==lr_formula
labels={s:(0 if s<1 else 1) for s in S}
v=vec((2,2),((0,1,1),(0,2,1)),(labels,labels))
assert v==(F(27,128),F(37,64),F(17,8),F(17,8)) and dot(v)==full
assert full-lrmax==F(1,256)
assert (full-lrmax)/sum(map(abs,N))==F(1,552)
print('PASS_EXACT_R5_SECOND_GATE_ISOLATION')
print('Q_SOURCE_WEIGHTS',W,'Q_T2_KERNEL',K,'RATIOS',R)
print('T2_ADVANTAGE_A',*(str(x) for x in V[0]))
print('T2_ADVANTAGE_B',*(str(x) for x in V[1]))
print('FIRST_GATE_ADVANTAGE',*(str(x) for x in Y))
print('FIRST_GATE_JENSEN_RESIDUAL',sum(W[h]*max(F(0),Y[h]) for h in range(2))-max(F(0),barY))
print('SECOND_GATE_JENSEN_RESIDUAL',barY-Z)
print('LR_ENUM_STRATEGIES',count)
print('SUPPORT_FULL',full,'SUPPORT_LR',lrmax,'GAP',full-lrmax)
print('O4_WITNESS',*(str(x) for x in v))
print('LINF_DISTANCE_LOWER_BOUND',F(1,552))
