#!/usr/bin/env python3
"""D25 independent exact binomial cross-check for frozen target representatives."""
import json
from math import comb
from d25_AF4_low_high_interface_20261109 import calculate
for p in (13,19,373):
    m=p**4; a=[0]*4; c=[0]*4
    for n in range(p):
        ai=comb(2*n,n)**2*comb(3*n,n)
        ci=comb(4*n,2*n)*comb(2*n,n)**2
        va=vc=0
        while ai%p==0:
            ai//=p;va+=1
        while ci%p==0:
            ci//=p;vc+=1
        a[va]=(a[va]+(6*n+1)*ai*pow(p,va,m)*pow(216,-n,m))%m
        c[vc]=(c[vc]+(8*n+1)*ci*pow(p,vc,m)*pow(2304,-n,m))%m
    q=calculate(p)
    assert a==q['W_grades'] and c==q['V_grades']
    print('INDEPENDENT_PASS',p)
