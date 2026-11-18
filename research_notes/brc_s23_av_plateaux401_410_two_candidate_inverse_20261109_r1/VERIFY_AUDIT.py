#!/usr/bin/env python3
"""Independent finite endpoint audit using exact fixed rational logarithm bounds."""
from fractions import Fraction
Q=10**26
LO=545569623581288298975349314
HI=LO+1

def log_interval(z):
    x=Fraction(0); pow_z=z
    for m in range(45):
        x += 2*pow_z/(2*m+1)
        pow_z*=z*z
    return x, x+2*pow_z/(91*(1-z*z))
a,b=log_interval(Fraction(1,3));c,d=log_interval(Fraction(1,9));e,f=log_interval(Fraction(1,15))
rlo=(3*a-f)/(d+f); rhi=(3*b-e)/(c+e)
assert Fraction(LO,Q)<rlo<rhi<Fraction(HI,Q)
EL=79*LO-431*Q;EU=79*HI-431*Q
DL=2074774*Q-380295*HI;DU=2074774*Q-380295*LO
assert 0<DL<DU<EL<EU

def floor_alpha(i):
    ans=i*DL//EU
    assert ans*EU<i*DL and i*DU<(ans+1)*EL, i
    return ans

def endpoint(i):
    ai=floor_alpha(i);prev=floor_alpha(i-1)
    V=380295*i+79*ai
    Vprev=380295*(i-1)+79*prev
    K=2074774*i+431*ai
    H=V+510
    M=K+V-Vprev-1
    return H,M,Vprev+511,V-Vprev,ai

last=152136996
for i in range(401,411):
    H,M,lo,width,ai=endpoint(i)
    assert lo==last+1, (i,lo,last)
    assert width in (380295,380374)
    print(f'AUDITED {i} alpha_floor={ai} start={lo} end={H} width={width} capacity={M}')
    last=H
assert endpoint(400)[:2]==(152136996,830390827)
assert last==155940420
print('PASS_10_EXACT_FLOOR_ENDPOINT_CONTIGUITY')
