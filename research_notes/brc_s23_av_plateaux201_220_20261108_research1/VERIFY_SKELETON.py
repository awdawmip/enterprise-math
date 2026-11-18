#!/usr/bin/env python3
"""Exact sanity checks for the infinite candidate-plateau Sturmian skeleton.
The infinite statements follow from the floor-function argument in STURMIAN_SKELETON.md.
"""
from fractions import Fraction as F
Q=10**26
LO=545569623581288298975349314
HI=LO+1
A,B=2074774,380295
EL,EU=79*LO-431*Q,79*HI-431*Q
DL,DU=A*Q-B*HI,A*Q-B*LO
assert 79*A-431*B==1
assert 0<EL<EU and 0<DL<DU and 2*DL>EU and 3*DU<2*EL
alpha_lo=F(DL,EU);alpha_hi=F(DU,EL)
assert F(1,2)<alpha_lo<alpha_hi<F(2,3)

def a(i):
    z=i*DL//EU
    assert z==i*DU//EL, ('needs more log precision',i)
    return z

def quantities(i):
    ai=a(i); ai0=a(i-1); e=ai-ai0
    V=B*i+79*ai
    K=A*i+431*ai
    H=V+510
    M=K+V-(B*(i-1)+79*ai0)-1
    assert M==A*i+380294+431*ai+79*e
    return ai,e,V,K,H,M

history=[quantities(i) for i in range(0,10001)]
for i in range(1,10001):
    e=history[i][1]
    assert e in (0,1)
    if i>=2:
        assert history[i-1][1]+e>=1
        assert history[i][4]-history[i-1][4] in (B,B+79)
        jump=history[i][5]-history[i-1][5]
        assert jump==A+431*e+79*(e-history[i-1][1])
        assert jump in (2074695,2075205,2075284)
    if i>=3:
        assert history[i-2][1]+history[i-1][1]+e<=2

for i in (1,2,20,201,220,10000):
    ai,e,V,K,H,M=history[i]
    dlo=i*DL-ai*EU; dhi=i*DU-ai*EL
    assert 0<=dlo<dhi<EU
    print('CANDIDATE',i,'a',ai,'e',e,'V',V,'H',H,'M',M,'residual_scaled_bounds',dlo,dhi)

print('ALPHA_RATIONAL_INTERVAL',alpha_lo,alpha_hi)
print('PASS_STURMIAN_S23_CANDIDATE_SKELETON finite_i_1_to_10000')
