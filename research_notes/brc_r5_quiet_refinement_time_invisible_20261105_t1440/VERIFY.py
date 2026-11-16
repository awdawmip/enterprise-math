#!/usr/bin/env python3
"""Exact R5 quiet-refinement witness. Python standard library only."""
from fractions import Fraction as F
from itertools import product
R = tuple(map(F, ("1/4", "1/2", "1", "3/2", "7/4")))
S = tuple(map(F, ("1/8", "1/4", "1/2", "1", "3/2", "7/4", "15/8")))
K0 = tuple(map(F, ("1/8", "1/4", "1/4", "1/4", "1/8")))
D = (15, -26, 22, -26, 15)
theta, lam, eta, w, c = F(1,512), F(1,16), F(1,16), F(1,2), F(7,32)
KA = tuple(k+theta*d for k,d in zip(K0,D))
KB = tuple(k-theta*d for k,d in zip(K0,D))
def dot(v,u): return sum((x*y for x,y in zip(v,u)),F(0))
def L(r): return max(-r,-F(1))
assert len(R)==len(K0)==len(D)==5
assert sum(D)==0 and dot(D,R)==0
assert dot(K0,R)==sum(K0)==1
assert all(x>0 for x in KA+KB)
assert all(dot(K,R)==sum(K)==1 for K in (KA,KB))
assert all(x>0 for x in S) and sum(S,F(0))==7
M=[]
for r in R:
    rp=(r-eta)/(1-eta)
    assert S[0]<rp<S[-1]
    p=(rp-S[0])/(S[-1]-S[0])
    q=[eta/F(7) for _ in S]
    q[0]+=(1-eta)*(1-p)
    q[-1]+=(1-eta)*p
    row=[lam*x for x in q]
    row[S.index(r)]+=1-lam
    assert all(z>0 for z in row)
    assert sum(row,F(0))==1 and dot(row,S)==r
    M.append(tuple(row))
B=tuple(dot(row,tuple(L(s) for s in S))-L(r) for r,row in zip(R,M))
assert all(0<=v<c for v in B)
assert all(v<=F(7,8)*lam for v in B)
A0=dot(K0,tuple(L(r) for r in R))-L(F(1))
a=tuple(dot(K,tuple(L(r) for r in R))-L(F(1)) for K in (KA,KB))
assert A0==c and a==(c-F(7,4)*theta,c+F(7,4)*theta)
lo,hi=F(37,44),F(51,44)
for K in (KA,KB):
    assert lo-1+dot(K,tuple(max(lo-r,F(0)) for r in R))==0
    assert 1-hi+dot(K,tuple(max(r-hi,F(0)) for r in R))==0
h_lr=L(F(1))-c+max(F(0),A0-c)
h_full=L(F(1))-c+w*max(F(0),a[0]-c)+w*max(F(0),a[1]-c)
assert h_lr==-F(39,32) and h_full==-F(4985,4096)
assert h_full-h_lr==F(7,4096)==F(7,8)*theta
eP=w*sum((r*k for r,k in zip(R,KB) if r<=1),F(0))
eQ=w+w*sum((k for r,k in zip(R,KB) if r>1),F(0))
W=(eP,eQ,F(3,2),F(3,2))
assert W==(F(781,4096),F(715,1024),F(3,2),F(3,2))
assert -eP-eQ-c*W[3]==h_full
assert (h_full-h_lr)/(F(2)+c)==F(7,9088)
# Terminal declaration maximization factorizes over the 2**7 t3 choices.
score2=[(-F(1)-2*c,-r-2*c,dot(row,tuple(L(s) for s in S))-3*c) for r,row in zip(R,M)]
best=None
count=0
for t1 in range(3):
    for t2 in product(range(3),repeat=len(R)):
        count+=1
        score=-F(1)-c if t1<2 else sum((K0[j]*score2[j][t] for j,t in enumerate(t2)),F(0))
        if best is None or score>best: best=score
assert count==729 and best==h_lr
print("R:",R)
print("S:",S)
print("K_A:",KA)
print("K_B:",KB)
print("B:",B)
print("time-roots:",lo,hi)
print("early-A:",a[0],a[1])
print("supports:",h_full,h_lr,"gap:",h_full-h_lr)
print("W:",W,"distance-lower-bound:",F(7,9088))
print("checked deterministic LR roots:",count,"with optimal terminal declarations; expanded policies:",count*(2**len(S)))
print("PASS_EXACT_R5_QUIET_REFINEMENT_TIME_INVISIBLE_FAMILY")
