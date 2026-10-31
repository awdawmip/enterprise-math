#!/usr/bin/env python3
"""Exact Fraction interval witness for Stage325-B auxiliary BRC model."""
from fractions import Fraction as Q
from math import comb
P=tuple(Q(k,160) for k in (61,21,9,9))
XS=(Q(231083940855521,10**15),Q(231083940855522,10**15))
YS=(Q(555508857277,10**12),Q(555508857278,10**12))
X=Q(63,250)
YR=(Q(61157,100000),Q(61158,100000))
q=(Q(6,25),Q(29,50))
def B(k,z):return z**k*(1-z)**(3-k)
def rng(k,iv):
 l,h=iv; vals=[B(k,l),B(k,h)]
 if k in (1,2) and l<=Q(k,3)<=h:vals.append(B(k,Q(k,3)))
 return min(vals),max(vals)
def arng(l,h):return max(0,l,-h),max(abs(l),abs(h))
def sumiv(terms):
 return (sum((c*v[0] for c,v in terms),Q(0)),sum((c*v[1] for c,v in terms),Q(0)))
def resid(k,xi,yi):
 l,h=rng(k,xi);a,z=rng(k,yi)
 return Q(4,5)*l+Q(1,5)*a-P[k],Q(4,5)*h+Q(1,5)*z-P[k]
def b(xi,yi):
 return sumiv([(Q(5*comb(3,k),32),arng(*resid(k,xi,yi))) for k in range(4)])
def D(a,zi):
 return sumiv([(Q(comb(3,k),2),arng(B(k,a)-rng(k,zi)[1],B(k,a)-rng(k,zi)[0])) for k in range(4)])
def c(xi,yi):
 return sumiv([(Q(63,256),D(Q(1,4),xi)),(Q(1,256),D(Q(3,4),xi)),(Q(9,256),D(Q(1,4),yi)),(Q(7,256),D(Q(3,4),yi))])
def sub(a,b):return a[0]-b[1],a[1]-b[0]
lo=resid(1,(X,X),(YR[0],YR[0]))[0]
hi=resid(1,(X,X),(YR[1],YR[1]))[0]
assert YR[0]>Q(1,3) and lo>0 and hi<0
assert X>XS[1] and YR[0]>YS[1]
bs=b(XS,YS);br=b((X,X),YR);bq=b((q[0],q[0]),(q[1],q[1]))
cs=c(XS,YS);cr=c((X,X),YR);cq=c((q[0],q[0]),(q[1],q[1]))
assert bq[0]==bq[1] and cq[0]==cq[1]
eps=sub(br,bs)
bg=(bs[0]+br[0]-2*bq[1],bs[1]+br[1]-2*bq[0])
cg=(cs[0]+cr[0]-2*cq[1],cs[1]+cr[1]-2*cq[0])
assert eps[0]>Q(7,1000) and eps[1]<Q(71,10000)
assert bg[0]>Q(1,1000) and cg[0]>Q(3,4000)
print("ROOT_SIGNS",lo,hi)
print("ROOT_BRACKET",YR)
print("EPSILON_BRACKET",eps)
print("PUBLIC_FEASIBILITY_GAP",bg)
print("TAGGED_COST_ADVANTAGE",cg)
print("STAGE325B_TWO_BLOCK_COUNTEREXAMPLE_TO_SINGLE_BLOCK_CONTINUATION_EXACT_PASS")
