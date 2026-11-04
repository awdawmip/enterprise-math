"""Exact rational S23 all-K certificate: s=1/10, h=1/42; observation model only."""
from fractions import Fraction as Q
from math import isqrt, factorial

v=Q(1,21); s=Q(1,10); k=s/(2-s); delta=Q(3,400)

def sqrt_enclosure(x, scale=10**26):
    assert x > 0
    z=isqrt(x.numerator*scale*scale//x.denominator)
    return Q(z,scale),Q(z+1,scale)

def atanh_enclosure(x, n=10):
    assert 0<x<1
    a=sum((x**(2*j+1)/Q(2*j+1) for j in range(n)), Q(0))
    return a,a+x**(2*n+1)/(Q(2*n+1)*(1-x*x))

def exp_positive_enclosure(x, n=8):
    assert 0<=x<1
    a=sum((x**j/Q(factorial(j)) for j in range(n+1)),Q(0))
    return a,a + x**(n+1)/Q(factorial(n+1))/(1-x/Q(n+2))

def neglog_lower(z):
    assert 0<z<1
    w=(1-z)/(1+z)
    return 2*sum((w**(2*j+1)/Q(2*j+1) for j in range(7)),Q(0))

def neglog_upper(z):
    assert 0<z<1
    w=(1-z)/(1+z)
    return neglog_lower(z)+2*w**15/(Q(15)*(1-w*w))

rlo,rhi=sqrt_enclosure(1-v*v)
rblo,rbhi=sqrt_enclosure(1-k*k*v*v)
alo,ahi=atanh_enclosure(v)
glo,ghi=atanh_enclosure(k*v)

ztlo=1-s+s*rlo
cthi=neglog_upper(ztlo)

exp1lo,exp1hi=exp_positive_enclosure(ahi*delta)
exp2lo,exp2hi=exp_positive_enclosure(ghi*delta)
zbhi=s*rhi*exp1hi/2 + (2-s)*rbhi/(2*exp2lo)
cbprobe_lo=neglog_lower(zbhi)
margin=19*cbprobe_lo-10*cthi
assert margin>Q(1,10**9), 'strict T-to-B efficiency certificate failed'
assert ztlo<1 and zbhi<1

print('PASS_BRC_S23_S110_ALL_K_PURE_B_RATIONAL_CERT_20261104')
print('domain: s=1/10, h=1/42, all integer K>=1, m,n>=0 with 19m+10n<=10K')
print('witness delta=3/400; common Chernoff exponent used for mixtures')
print('certified: 19*f_B(3/400)-10*C_T > 1/1000000000')
print('certified margin lower in units of 1e-12:', (margin*10**12).numerator//(margin*10**12).denominator)
print('certificate check:', margin > Q(1,10**9))
