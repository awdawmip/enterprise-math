#!/usr/bin/env python3
"""C264 standalone 105-symbol proof tree, exact Fraction replay (no dependencies)."""
from fractions import Fraction as F

NUM=(0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,3,1,6,2,3,6,1,6,3,2,7,3,4,8,1,21,9,6,4,10,14,5,11,2,9,12,13,14,3,7,15,17,14,5,6,13,15,17,10,11,13,16,18,22,28,36,46,63,96,152,246,528,1971,1)
DEN=(1,2057,539,289,136,93,68,51,39,31,27,21,17,15,13,11,10,9,8,7,13,6,11,5,14,13,4,23,7,10,19,3,17,8,5,17,7,9,17,2,41,17,11,7,17,23,8,17,3,13,17,18,19,4,9,19,21,17,6,7,15,17,19,11,12,14,17,19,23,29,37,47,64,97,153,247,529,1972,1)
TREE='1301D3DD1DD01D30DDA1D3DD3013D00DDD3D00DD1DD103DDD03DDD030103BB3BB03BB3BB13BB3BB010BB0BB1BB3013BB3BB1BB0BB'
I=(5,50,55,56); J=tuple(j for j in range(79) if j not in I)
U=tuple(F(x,y) for x,y in zip(NUM,DEN));Q=2**128;Z=F(141421356237309504880,10**20)
A=F(6912*50000**2,17**2);H=2**166
LO=(F(1,135),F(34,49),F(4,5),F(57,71))
HI=(F(3,205),F(12,17),F(4,5),F(22,27))
EXPECTED=95008155998302734852413916540688525

assert len(U)==79 and all(U[j]<U[j+1] for j in range(78))
assert len(TREE)==105 and HI[2]<LO[3]<Z
B={}
for j in J:
    v=F(Q)*A/H/((2-U[j]*U[j])*(3-U[j]*U[j]))**3
    for r in range(79):
        if r!=j:v*=(Z-U[r])/abs(U[j]-U[r])
    B[j]=v.numerator//v.denominator
    assert B[j]>0

def moving(k,lo,hi):
    d=I.index(k);s=(lo[d]+hi[d])/2
    v=F(Q)*A/H/((2-s*s)*(3-s*s))**3
    slope=6*s/(2-s*s)+6*s/(3-s*s)
    for j in J:
        v*=(Z-U[j])/abs(s-U[j]);slope-=1/(s-U[j])
    for p in I:
        if p==k:continue
        d2=I.index(p);e=lo[d2] if p<k else hi[d2]
        v*=(Z-e)/abs(s-e);slope-=1/(s-e)
    return v,v*slope,s

def bound(k,lo,hi):
    d=I.index(k);s=(lo[d]+hi[d])/2
    v=F(0);slope=F(0)
    for j in J:
        t=F(B[j])
        for p in I:
            if p==k:continue
            d2=I.index(p);e=lo[d2] if j>p else hi[d2]
            t*=(Z-e)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-e)
        t*=(Z-s)/(Z-U[k])*abs(U[j]-U[k])/abs(U[j]-s)
        v+=t;slope+=t*(-1/(Z-s)-1/(s-U[j]))
    mv,md,_=moving(k,lo,hi);v+=mv;slope+=md
    v+=slope*((lo[d] if slope>=0 else hi[d])-s)
    for p in I:
        if p==k:continue
        d2=I.index(p);m,dm,mp=moving(p,lo,hi)
        v+=m+dm*((lo[d2] if dm>=0 else hi[d2])-mp)
    return v

methods={'A':5,'B':50,'D':56};cursor=0;margins=[];counts={5:0,50:0,56:0}
def visit(lo,hi):
    global cursor
    sym=TREE[cursor];cursor+=1
    if sym in methods:
        k=methods[sym];v=bound(k,lo,hi)
        m=v.numerator//v.denominator-Q
        assert m>0,(k,m,lo,hi)
        margins.append(m);counts[k]+=1
        return
    d=int(sym);assert d in (0,1,3)
    t=(lo[d]+hi[d])/2
    left=list(hi);left[d]=t
    right=list(lo);right[d]=t
    visit(lo,tuple(left));visit(tuple(right),hi)

visit(LO,HI)
assert cursor==len(TREE) and len(margins)==53
assert counts=={5:1,50:26,56:26} and min(margins)==EXPECTED
print('C264_MINIMAL_REPLAY_PASS',len(margins),'strict_leaves',min(margins),'min_margin',counts)
