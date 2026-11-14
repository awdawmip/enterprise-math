#!/usr/bin/env python3
"""R149B exact lag-waveform recheck for R148B infinite Sturmian family."""
from fractions import Fraction as F
from math import gcd
import json

def corr_exact(r,lag):
    b=r+2; d=3*r+2; g=gcd(b,d)
    z=F(g-1,2)
    return sum((((j-2)%g)-z)*(((-3*(j+lag))%g)-z) for j in range(g))/ (g*b*d)

def corr_formula(r,lag):
    b=r+2; d=3*r+2; g=gcd(b,d); k=(lag+2)%g
    return (F(g*g-1,12)-F(k*(g-k),2))/(b*d)

n=0; signs={1:0,2:0,4:0}
for r in range(1,201):
    g=gcd(r+2,3*r+2)
    assert g in (1,2,4)
    signs[g]+=1
    for lag in range(-10,11):
        assert corr_exact(r,lag)==corr_formula(r,lag), (r,lag)
        n+=1
    assert sum(corr_formula(r,h) for h in range(g))==0
    if g==4:
        assert corr_formula(r,2)==F(5,4*(r+2)*(3*r+2))
        assert corr_formula(r,0)==F(-3,4*(r+2)*(3*r+2))
        assert corr_formula(r,1)==F(-1,4*(r+2)*(3*r+2))
    elif g==2:
        assert corr_formula(r,0)==F(1,4*(r+2)*(3*r+2))
        assert corr_formula(r,1)==F(-1,4*(r+2)*(3*r+2))
print(json.dumps({'status':'R149B_SHIFTED_EXTREMAL_WAVEFORM_PASS',
    'r_range':[1,200], 'lags_per_r':21, 'exact_lag_checks':n,
    'gcd_distribution':signs, 'g4_lag2_positive_sharp_examples':signs[4]},indent=2))
