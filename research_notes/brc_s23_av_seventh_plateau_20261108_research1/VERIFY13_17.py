#!/usr/bin/env python3
"""Exact integer-rational certificate for S23/AV plateaux 13-17.
Proof of quantified coverage in PLATEAUX13_17.md; no floating-point decisions.
"""
from fractions import Fraction as F
Q=10**26; LO=545569623581288298975349314; HI=LO+1
HMAX=6466236; V0=380295; K0=2074774

def log_bounds(z):
    s=F(0); p=z
    for m in range(45): s+=2*p/(2*m+1); p*=z*z
    return s,s+2*p/(91*(1-z*z))
a,b=log_bounds(F(1,3));c,d=log_bounds(F(1,9));e,f=log_bounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f) and (3*b-e)/(c+e)<F(HI,Q)

def enc(A,B):
    return (A*Q+B*(LO if B>=0 else HI), A*Q+B*(HI if B>=0 else LO))

el,eu=enc(-431,79);tl,tu=enc(-60,11);gl,gu=enc(371,-68)
dl,du=enc(K0,-V0)
assert 0<dl<du<el and tl>4800*eu and gl>6*eu
assert eu*(HMAX+79)<18*Q
assert 79*60-431*11==-1

# 0<x<epsilon implies integer beta=79*x-epsilon*dv in [-17,17].
# Exactly one integer a is possible for each nonzero beta, from
# the strict interval -beta*eta/epsilon < a < 1-beta*eta/epsilon.
small=[]
for beta in range(-17,18):
    if not beta:continue
    a0=abs(beta)*tl//eu; a1=abs(beta)*tu//el
    assert a0==a1
    aa=-a0 if beta>0 else a0+1
    dv=79*aa+11*beta; dj=431*aa+60*beta
    low,high=enc(-431*aa-60*beta,79*aa+11*beta)
    assert 0<low<high<el
    C=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    if C<=HMAX: small.append((beta,aa,dv,dj,C,low,high))
assert [x[:5] for x in small]==[
 (-2,9630,760748,4150410,4911158),
 (-1,4815,380374,2075205,2455579),
 (1,-4814,-380295,-2074774,2455069),
 (2,-9629,-760669,-4149979,4910648)]
print('PASS_SUBEPS_DISPLACEMENTS_H17',HMAX,small)

w=[]
for i in range(1,18):
    ai=i*dl//eu
    assert ai*eu<i*dl and i*du<(ai+1)*el
    v=i*V0+79*ai; k=i*K0+431*ai
    low,high=enc(k,-v)
    assert 0<low<high<el
    w.append((i,ai,v,k,low,high))
assert [q[1] for q in w]==[0,1,1,2,2,3,4,4,5,5,6,7,7,8,8,9,9]
V7=w[6][2]; V12=w[11][2]
assert all(q[5]>w[6][5] for q in small) # all narrow gaps > delta7
# High-v gaps at HMAX are >= epsilon; neither short positive nor negative
# displacement can begin at v>V12 and remain in the HMAX triangle.
for beta,aa,dv,dj,C,low,high in small:
    if dv<0:
        assert dj<0 and HMAX-(V12+1)<-dj,(beta,dj)
    else:
        assert dv>0 and dj>0 and HMAX-C<V12+1,(beta,C)
print('PASS_LOCALIZED_GAPS','global_min_sub_epsilon_gt_delta7',w[6][5], 'above_V12_ge_epsilon',el)

# Universally valid initial witness blocks, with delta7 and delta12.
baseblocks=[(0,V7,7),(V7+1,V12,12)]
for start,end,i in baseblocks:
    _,_,v,k,low,high=w[i-1]
    assert v>=end and k>HMAX
    assert (high<w[6][5] if i==12 else all(q[5]>high for q in small))
    assert k+v-start<27355373
    print('PASS_BASE_BLOCK',start,end,i,'maxlen',k+v-start)

for i in range(13,18):
    _,ai,v,k,lo,hi=w[i-1]
    prev=w[i-2][2]
    Mi=k+v-(prev+1);Hi=v+510
    assert Hi<=HMAX and k>HMAX and Mi>k+3498
    # Remaining medium intervals (V12,V_i] handled by W13,...,Wi;
    # all outgoing gaps from this v region are >=epsilon.
    pr=V12
    for s in range(13,i+1):
        _,_,vs,ks,dlo,dhi=w[s-1]
        assert 0<dlo<dhi<el and ks>Hi and vs<=v
        assert ks+vs-(pr+1)<=Mi
        pr=vs
    assert pr==v
    # Top 510 rows use delta_i+gamma-m*epsilon in (0,gamma).
    for m in range(1,7):
        L=v+68+79*m;K=k+371+431*m
        low,high=enc(K,-L)
        assert 0<low and high<gl
        if m==6:assert L>=Hi
    # Exterior cells.
    left=Hi*Q//LO+1;right=HI*Hi//Q+1
    assert LO*left>Hi*Q and right*Q>HI*Hi and max(left,right)<Mi
    print('PASS_PLATEAU',i,'h_start',prev+511,'h_end',Hi,'N_exact',Mi,'outer',left,right)
assert HMAX==w[16][2]+510
print('PASS_S23_AV_ANALYTIC_PLATEAUX_13_TO_17')
