#!/usr/bin/env python3
"""Exact 15-label phase-collision census on the frozen R5 P/Q-BRC observer.
Self-contained: standard library Fraction; integer Boolean-lattice DP.
Frozen inputs: original R5 PR #2102 (commit 435e77af0d180eac32bd1f9c4c464bc4010b7551).
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter

R=(2,10,15,20,25,30,38)
PORTS=(1,2,3,5)
J=(1,2,5)
V=tuple((i,j) for j in PORTS for i in range(7))
IX={v:k for k,v in enumerate(V)}
X=tuple(map(F,('250555781039/3397584400000,854053219229681/5470110884000000,'
 '155682221/156288882400000,1/800000,1/800000,19487331497/781444412000000,'
 '1001314300627/47566181600000,1/800000,6101786845061/95132363200000,'
 '19640941861/6795168800000,1/800000,1/800000,1/800000,1326387507069/95132363200000,'
 '155682221/25142124560000000,155682221/25142124560000000,'
 '969901373288483/5782688648800000,1627075388860003/11721666180000000,'
 '14139282599219/169879220000000,165067666637733/7814444120000000,'
 '1696529496568917/144567216220000000,31271973479/25142124560000000,'
 '12993863727852929/4047882054160000000,7517305745629/5782688648800000,'
 '36686587724849/3907222060000000,1308842702731/169879220000000,'
 '331925821992147/7814444120000000,54684907960963337/2023941027080000000').split(',')))
assert len(X)==28
x=X[IX[(0,3)]]
assert x==F(155682221,25142124560000000)
H=[0]*28
for i,a in [(1,-23),(2,28),(6,-5)]:
    H[IX[(i,3)]]=a
    H[IX[(i,1)]]=-a
assert sum(H)==0

def basis(i):
    a=[0]*7
    a[0]=R[i]-R[6]
    a[i]=R[6]-R[0]
    a[6]=R[0]-R[i]
    return a

def atom(j,i):
    a=[0]*28
    for k,v in enumerate(basis(i)):
        a[IX[(k,j)]]+=v
        a[IX[(k,3)]]-=v
    return a

coeff={1:(12,8,1,13,8),2:(3,13,7,4,2),5:(-15,-21,-8,-17,-10)}
steps=[tuple(c*v for v in atom(j,i)) for j in J for i,c in enumerate(coeff[j],1)]
assert len(steps)==15
S=1<<15
P=[[0]*28 for _ in range(S)]
for mask in range(1,S):
    t=mask&-mask
    j=t.bit_length()-1
    prev=P[mask^t]
    P[mask]=[prev[k]+steps[j][k] for k in range(28)]
epsmax=F(9,115400000)
assert min(X[k]+epsmax*F(P[-1][k],36) for k in range(28))==0

def classify(r):
    eta=x*r
    qval={q:(x-23*eta)/q for q in (3,12,15)}
    tags=[None]*S
    for mask in range(1,S):
        t=min(36*(X[k]+eta*H[k])/(-P[mask][k])
              for k in range(28) if P[mask][k]<0)
        if t>epsmax: tag=('O',0)  # safe at every phase in the closed ray
        elif t==epsmax: tag=('E',0)
        elif t in qval.values(): tag=('Q',next(q for q,v in qval.items() if t==v))
        else:
            n=36*x/t
            assert n.denominator==1 and n>=3,(mask,r,t,n)
            tag=('F',int(n))
        tags[mask]=tag
    return tags

plus=classify(F(1,1000000))
minus=classify(F(-1,1000000))
print('TAGS_PLUS',len(set(plus[1:])),Counter(t[0] for t in plus[1:]))
print('TAGS_MINUS',len(set(minus[1:])),Counter(t[0] for t in minus[1:]))
assert len(set(plus[1:]))==len(set(minus[1:]))==1149

@lru_cache(None)
def fullcount(sign,r,theta,include_at):
    tags=plus if sign>0 else minus
    factor=1-23*r
    def value(tag):
        if tag[0]=='F': return F(36,tag[1])
        if tag[0]=='Q': return factor/tag[1]
        if tag[0]=='E': return epsmax/x
        return F(10**9)
    allowed=[True]+[(value(tag)>=theta if include_at else value(tag)>theta) for tag in tags[1:]]
    dp=[0]*S
    dp[0]=1
    for mask in range(1,S):
        if allowed[mask]:
            bits=mask
            z=0
            while bits:
                bit=bits&-bits
                z+=dp[mask^bit]
                bits-=bit
            dp[mask]=z
    return dp[-1]

def drop(sign,r,typ,num):
    theta=F(36,num) if typ=='F' else F(1-23*r,num)
    return fullcount(sign,r,theta,True)-fullcount(sign,r,theta,False)

cases={+1:[(12443,15,541),(9959,12,433),(6233,15,542),(4991,12,434),
           (4163,15,543),(3335,12,435),(3128,15,544)],
       -1:[(12397,15,539),(9913,12,431),(6187,15,538)]}
for sign,seq in cases.items():
    vals=[F(0)]+[F(1,d) for d,_,_ in seq]+[F(1,2507 if sign==1 else 4945)]
    for i,(den,q,n) in enumerate(seq,1):
        before=sign*(vals[i-1]+vals[i])/2
        after=sign*(vals[i]+vals[i+1])/2
        pre=(drop(sign,before,'F',n),drop(sign,before,'Q',q))
        post=(drop(sign,after,'F',n),drop(sign,after,'Q',q))
        assert sum(pre)==sum(post),(sign,den,pre,post)
        print('COLLISION',sign,den,'F',n,'Q',q,
              'BEFORE',pre,'AFTER',post,
              'TRANSFER_MOVING',post[1]-pre[1],'COMBINED',sum(pre))

r=F(1,2507)
for q,n in [(3,109),(12,436),(15,545)]:
    assert F(36,n)==F(1-23*r,q)
    print('POS_BOUNDARY_COLLISION',q,n,'SINGLE_COMBINED',drop(1,r,'F',n))
r=F(-1,4945)
q,n=12,430
assert F(36,n)==F(1-23*r,q)
print('NEG_BOUNDARY_COLLISION',q,n,'SINGLE_COMBINED',drop(-1,r,'F',n))
print('PASS_R5_EXACT_ALL_TEN_INTERIOR_AND_FOUR_ENDPOINT_PAIR_COLLISIONS')
