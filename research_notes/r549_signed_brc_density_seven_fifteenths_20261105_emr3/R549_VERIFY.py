#!/usr/bin/env python3
"""R549: rational-only phase-sector proof, with Machin-series certificate for pi."""
from fractions import Fraction as F
from math import factorial, gcd

def alternating(x, terms, kind):
    exponent = 1 if kind == 'sin' else 0
    return sum(((-1)**j * x**(2*j + exponent) / factorial(2*j + exponent)
                for j in range(terms)), F(0))

def atan_partial(x, last):
    return sum(((-1)**j * x**(2*j+1) / (2*j+1)
                for j in range(last+1)), F(0))

pi_lower = 4*(4*atan_partial(F(1,5),5)-atan_partial(F(1,239),2))
pi_upper = 4*(4*atan_partial(F(1,5),4)-atan_partial(F(1,239),3))
assert F(333,106) < pi_lower < pi_upper < F(355,113)
LPI, UPI = F(333,106), F(355,113)

def tan_bounds(n,d):
    low = F(n,d)*LPI; high = F(n,d)*UPI
    assert 0 < low <= high < 1
    sin_low = alternating(low,6,'sin')
    sin_high = alternating(high,7,'sin')
    cos_low = alternating(high,6,'cos')
    cos_high = alternating(low,7,'cos')
    assert min(sin_low, cos_low, cos_high)>0
    return sin_low/cos_high, sin_high/cos_low

b7 = tan_bounds(2,7)
b22 = tan_bounds(3,11)
b20 = tan_bounds(3,10)
assert F(5,4)<b7[0] and b7[1]<F(251,200)
assert b22[1]<F(7,6)
assert b20[0]>F(4,3)

root_disks = [
    (5,'1247.313','1468.117','0.1'),
    (6,'3292.954','3962.354','0.1'),
    (7,'3.177694','3.914665','0.001'),
    (8,'4.036005','5.081137','0.001'),
    (9,'4.987574458','6.397700798','0.001'),
    (10,'6.033407511','7.862167698','0.001'),
]
for k,a,b,e in root_disks:
    a,b,e = F(a), F(b), F(e)
    slope_lower, slope_upper = (b-e)/(a+e), (b+e)/(a-e)
    assert slope_lower > F(7,6) and slope_upper < F(4,3)
    if k<=7: assert slope_upper < F(5,4)
    else: assert slope_lower > F(251,200)
    print('k=%d cone_ok rational_slope=[%s,%s]'%(k,slope_lower,slope_upper))

small = [(p,q) for q in range(1,30) for p in range(1,q)
         if 8*p>q and 6*p<q and gcd(p,q)==1]
assert [(p,q) for p,q in small if q<15]==[(1,7),(2,13)]
assert [(p,q) for p,q in small if q%2==0]==[(3,20),(3,22)]
for q in range(1,3001):
    if q%2 and q>=15: assert F(q-1,2*q)>=F(7,15)
    if q%2==0 and q>=30: assert F(q-2,2*q)>=F(7,15)
print('pi_exact_bracket_OK; tan_bounds:',[(n,d,float(tan_bounds(n,d)[0]),float(tan_bounds(n,d)[1])) for n,d in [(2,7),(3,11),(3,10)]])
print('small_rational_rotations:',small)
print('R549_EXACT_7_OVER_15_DENSITY_CERT_PASS')
