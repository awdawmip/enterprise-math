#!/usr/bin/env python3
"""Exact Stage160 dual-ray closure after Stage159, not a primal theorem."""
from fractions import Fraction as F
from functools import lru_cache
N=14;P=(F(1,8),F(1,24),F(5,6))
K=F(580027221414,1887912013);L=F(566236422120,1887912013)
DK=-F(1);DL=-F(25280,14751)
def r(s):return F(2)**(s[1]+s[2])/F(3)**s[1]
def child(s,i):return s[0]+1,s[1]+(i==0),s[2]+(i==1)
@lru_cache(None)
def ray(s):
    C=[(K*r(s),DK*r(s)),(L,DL)]
    if s[0]<N:
        z=[ray(child(s,i)) for i in range(3)]
        C.append((1+sum(P[i]*z[i][0] for i in range(3)),
                  sum(P[i]*z[i][1] for i in range(3))))
    m=min(v for v,d in C); choice=min((i for i,c in enumerate(C) if c[0]==m),key=lambda i:C[i][1])
    return C[choice][0],C[choice][1],C,choice
candidates=[]
for n in range(15):
    for a in range(n+1):
        for b in range(n-a+1):
            s=(n,a,b);v,d,C,chosen=ray(s)
            for i,(vv,dd) in enumerate(C):
                gap=vv-v; slope=dd-d
                if gap>0 and slope<0:candidates.append((gap/(-slope),s,i))
t,s,action=min(candidates)
assert t==F(6084006567309,15514860922834),(t,s,action)
assert s==(13,5,2) and action==2
K2=K+DK*t;L2=L+DL*t
assert K2==F(2521611,8218) and L2==F(1229640,4109)
@lru_cache(None)
def bell(s):
    C=[K2*r(s),L2]
    if s[0]<N:C.append(1+sum(P[i]*bell(child(s,i))[0] for i in range(3)))
    return min(C),C
ties={};gaps=[]
for n in range(15):
    for a in range(n+1):
        for b in range(n-a+1):
            s=n,a,b;v,C=bell(s)
            eq=[('P','Q','C')[i] for i,q in enumerate(C) if q==v]
            if len(eq)>1:ties[s]=eq
            gaps += [q-v for q in C if q>v]
assert ties=={(10,2,0):['P','C'],(13,5,2):['P','C']},ties
assert len(gaps)==1238 and min(gaps)==F(565771,37868544)
print('DUAL_ONLY Stage160:', 't',t, 'K',K2, 'L',L2)
print('PASS 680 states, ties',ties, '1238 positive gaps, min',min(gaps))
