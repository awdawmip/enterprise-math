#!/usr/bin/env python3
"""Exact arithmetic certificate for S23/AV plateaux 8 through 12.
Proof of quantified coverage is in PLATEAUX8_12.md.
"""
from fractions import Fraction as F
Q=10**26; LO=545569623581288298975349314; HI=LO+1
HMAX=4564603; V0=380295; K0=2074774

def log_bounds(z):
    s=F(0); p=z
    for m in range(45): s+=2*p/(2*m+1); p*=z*z
    return s,s+2*p/(91*(1-z*z))

a,b=log_bounds(F(1,3));c,d=log_bounds(F(1,9));e,f=log_bounds(F(1,15))
assert F(LO,Q)<(3*a-f)/(d+f) and (3*b-e)/(c+e)<F(HI,Q)

def enc(A,B):
    return (A*Q+B*(LO if B>=0 else HI),
            A*Q+B*(HI if B>=0 else LO))

el,eu=enc(-431,79);tl,tu=enc(-60,11);gl,gu=enc(371,-68)
dl,du=enc(K0,-V0)
assert 0<dl<du<el and tl>4800*eu and gl>6*eu
assert eu*HMAX<13*Q and eu*(HMAX+79)<13*Q
assert 79*60-431*11==-1

# 0<x<epsilon implies integer beta=79*x-epsilon*dv in [-12,12].
small=[]
for beta in range(-12,13):
    if not beta:continue
    a0=abs(beta)*tl//eu;a1=abs(beta)*tu//el
    assert a0==a1
    aa=-a0 if beta>0 else a0+1
    dv=79*aa+11*beta;dj=431*aa+60*beta
    low,high=enc(-431*aa-60*beta,79*aa+11*beta)
    assert 0<low<high<el
    C=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
    if C<=HMAX:small.append((beta,aa,dv,dj,C,low))
assert [x[:5] for x in small]==[(-1,4815,380374,2075205,2455579),
                                 (1,-4814,-380295,-2074774,2455069)]
print('PASS_ALL_SUBEPS_DISPLACEMENTS_TO_H12',HMAX,small)

w=[]
for i in range(1,13):
    ai=i*dl//eu
    assert ai*eu<i*dl and i*du<(ai+1)*el
    v=i*V0+79*ai;k=i*K0+431*ai
    low,high=enc(k,-v)
    assert 0<low<high<el
    w.append((i,ai,v,k,low,high))
assert [q[1] for q in w]==[0,1,1,2,2,3,4,4,5,5,6,7]
V2=w[1][2];V4=w[3][2];V7=w[6][2]
assert w[3][5]<min(t[5] for t in w if t[0] in (1,3,5,6,8))
assert all(x[5]>w[3][5] for x in small)
# After v>V7, both exceptional sub-epsilon displacements are impossible.
assert HMAX-(V7+1)<2074774
assert HMAX-2455579<V7+1
print('PASS_GAP_LOWER_BOUNDS','global_gt_delta4',w[3][5], 'above_V7_ge_epsilon',el)

# Universally valid initial witness blocks, with delta4 and delta7 <= delta4.
blocks=[(0,V4,4),(V4+1,V7,7)]
for start,end,i in blocks:
    _,_,v,k,low,high=w[i-1]
    assert v>=end and k>HMAX and high<=w[3][5]
    assert k+v-start<16980210
    print('PASS_LOW_BLOCK',start,end,i,'maxlen',k+v-start)

for i in range(8,13):
    _,ai,v,k,dlo,dhi=w[i-1]
    vi_prev=w[i-2][2]
    Mi=k+v-(vi_prev+1);Hi=v+510
    assert Hi<=HMAX and k>HMAX and Mi>k+3498
    # Remaining medium intervals (V7,V_i] handled by W8,...,Wi;
    # all offsets <epsilon, while all outgoing gaps have width >=epsilon.
    prior=V7
    for s in range(8,i+1):
        _,_,vs,ks,dslo,dshi=w[s-1]
        assert 0<dslo<dshi<el
        assert vs<=v and ks>Hi and ks+vs-(prior+1)<=Mi
        prior=vs
    assert prior==v
    # Top 510 rows use delta_i+gamma-m epsilon in (0,gamma).
    for m in range(1,7):
        L=v+68+79*m; K=k+371+431*m
        low,high=enc(K,-L)
        assert 0<low and high<gl
        if m==6:assert L>=Hi
    # Outer left/right prefix lengths bounded above by Mi.
    left=Hi*Q//LO+1;right=HI*Hi//Q+1
    assert LO*left>Hi*Q and right*Q>HI*Hi
    assert max(left,right)<Mi
    print('PASS_PLATEAU',i,'h_start',vi_prev+511,'h_end',Hi,'N_exact',Mi,'outer',left,right)
assert HMAX==w[11][2]+510
print('PASS_S23_AV_ANALYTIC_PLATEAUX_8_TO_12')
