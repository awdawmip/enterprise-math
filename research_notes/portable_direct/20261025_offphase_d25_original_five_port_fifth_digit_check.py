#!/usr/bin/env python3
"""Portable author regression for original five-port WZ fifth digit.

All arithmetic uses integers or exact fractions; never native CM/DP execution.
Every modulus inversion checks a p-unit denominator.
"""
from fractions import Fraction as F
from math import factorial, gcd

A = (F(250809,17920), F(466056841,63974400),
     F(22193173931,114194304000), F(-98135062039471,1630694661120000))
SAMPLE = (13,19,31,37,43,61,67,73,79,97,103,109,127,211)

def prime(n):
    return n > 1 and all(n % d for d in range(2,int(n**0.5)+1))

def modq(z, modulus):
    z=F(z)
    assert gcd(z.denominator,modulus)==1
    return (z.numerator % modulus)*pow(z.denominator,-1,modulus)%modulus

def harm(k,s,M):
    return sum(pow(pow(j,s,M),-1,M) for j in range(1,k+1))%M

def sigma_jet(p):
    M=p**4; n=(p-1)//3
    a=(2**(p-1)-1)//p; b=(3**(p-1)-1)//p
    X=(modq(F(2567,440),M)-2*a-3*b-harm(n+4,1,M)-2*harm(n-1,1,M)+2*harm(p-1,1,M))%M
    Y=(modq(F(-10548779,3484800),M)+a*a+modq(F(3,2),M)*b*b+
       modq(F(1,2),M)*harm(n+4,2,M)-harm(n-1,2,M)-harm(p-1,2,M))%M
    Z=(modq(F(4622489459,766656000),M)-modq(F(2,3),M)*a*a*a-b*b*b-
       modq(F(1,3),M)*harm(n+4,3,M)-modq(F(2,3),M)*harm(n-1,3,M)+
       modq(F(2,3),M)*harm(p-1,3,M))%M
    L=(p*X+p*p*Y+p**3*Z)%M
    return modq(F(3,220),M)*(1+L+L*L*pow(2,-1,M)+pow(L,3,M)*pow(6,-1,M))%M

def B_jet(p):
    M=p**4
    return sum(pow(p,k,M)*modq(ak,M) for k,ak in enumerate(A))%M

def B_source_ratio(p):
    M=p**4
    r=1; total=0
    for j in range(1,5):
        total=(total+(6*p+6*j+7)*r)%M
        if j<=3:
            k=j
            numerator=(2*p+2*k+3)*(2*p+3*k-1)*(2*p+3*k)
            denominator=4*(2*p+3*k+1)*(p+k+2)*(4*p+3*k+11)
            r=r*numerator*pow(denominator,-1,M)%M
    return total

def source_V(r,t):
    return F(factorial(6*r)*factorial(4*r+2*t)*factorial(3*t),
             3**(6*r)*216**t*factorial(2*r)*factorial(t)**2*
             factorial(2*r+t)**2*factorial(4*r+t))

def source_sigma(p):
    m=(p-1)//6
    return source_V(m+1,4*m+1)/p**2

def source_four_tail(p):
    m=(p-1)//6; M=p**4
    return sum((6*p+6*j+7)*modq(source_V(m+1,4*m+j)/p**2,M)
               for j in range(1,5))%M

def source_S(r):
    return sum((6*t+12*r+1)*source_V(r,t) for t in range(4*r+1))

def old_U(p):
    m=(p-1)//6; n=2*m; M=p**5
    z=(2*m)*pow(108**(p-1),-1,M)%M
    for k in range(2,n+1):
        z=z*(k-p)**2*pow(k,-2,M)%M
    for j in range(1,p-1):
        z=z*(j+p)**2*pow(j,-2,M)%M
    for j in range(1,n):
        z=z*j*pow(j+p,-1,M)%M
    return z

def old_C(p):
    return F((p+1)*(2*p-1)**2*(30*p*p+77*p+40),
             2*(p+2)*(2*p+1)*(4*p-1)*(4*p+5))

def test():
    ps=[p for p in range(13,1000) if p%6==1 and prime(p)]
    assert len(ps)==79
    for p in ps:
        M=p**4
        sigma=sigma_jet(p)
        B=B_jet(p)
        assert sigma == modq(source_sigma(p),M), ('sigma',p)
        assert B == B_source_ratio(p), ('B',p)
        assert sigma*B%M == source_four_tail(p), ('four_tail',p)
    for p in SAMPLE:
        M=p**5; m=(p-1)//6
        predicted=(old_U(p)*modq(old_C(p),M)+p*sigma_jet(p)*B_jet(p))%M
        source=modq((source_S(m+1)-source_S(m))/p,M)
        assert predicted == source, ('full_WZ',p,predicted,source)
    print('PASS: 79/79 authentic sigma and four-tail modulo p^4; 14/14 full five-port WZ modulo p^5')
    for p in (13,19,31,211):
        M=p**5
        full=(old_U(p)*modq(old_C(p),M)+p*sigma_jet(p)*B_jet(p))%M
        print('p=',p,'sigma=',sigma_jet(p),'B=',B_jet(p),'WZ_diff_over_p=',full)

if __name__=='__main__':
    test()
