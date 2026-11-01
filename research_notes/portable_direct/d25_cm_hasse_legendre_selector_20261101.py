#!/usr/bin/env python3
"""Exact finite checks for CM(-24) Hasse/Legendre selector; not a universal proof."""
from math import comb, isqrt

def primes_upto(N):
    v=bytearray(b'\x01')*(N+1)
    v[:2]=b'\x00\x00'
    for i in range(2,isqrt(N)+1):
        if v[i]:v[i*i:N+1:i]=b'\x00'*((N-i*i)//i+1)
    return [p for p in range(5,N+1) if v[p]]

def mul(a,b,p):
    return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def add(a,b,p):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def scale(a,c,p):return (a[0]*c%p,a[1]*c%p)

def legendre(n,x,p):
    if n==0:return (1,0)
    prev=(1,0);cur=x
    for k in range(1,n):
        nxt=scale(add(scale(mul(x,cur,p),2*k+1,p),scale(prev,-k,p),p),pow(k+1,-1,p),p)
        prev,cur=cur,nxt
    return cur

def hasse_coeff_poly(p):
    """Hasse of E_z=y²=x((x+1)²-z): [x^(p-1)] f(x)^((p-1)/2)."""
    assert p%4==1
    m=(p-1)//2;n=(p-1)//4
    return [((-1)**k*comb(m,k)*comb(p-1-2*k,m))%p for k in range(n+1)]

def hypergeom_coeff_poly(p):
    n=(p-1)//4;out=[1]
    for k in range(n):
        out.append(out[-1]*(4*k+1)*(4*k+3)*pow(16*(k+1)**2,-1,p)%p)
    return out

def evalpoly(coeffs,z,p):
    out=(0,0)
    for c in reversed(coeffs):out=add(mul(out,z,p),(c%p,0),p)
    return out

def assert_exact_cm_j():
    A=2417472;B=-1707264
    assert A*A+2*B*B-4834944*A+14670139392==0
    assert 2*A*B-4834944*B==0
    from fractions import Fraction
    assert Fraction(64**2,36**3)==Fraction(64,729)

def test(N=3000):
    assert_exact_cm_j()
    byclass={};seq=[]
    for p in primes_upto(N):
        if p%4!=1:continue
        n=(p-1)//4
        z=(pow(2,-1,p),-pow(3,-1,p)%p)
        x=(0,2*pow(3,-1,p)%p)
        h=hasse_coeff_poly(p);u=hypergeom_coeff_poly(p)
        assert h==u,('polynomial coefficient mismatch',p)
        a=evalpoly(h,z,p);P=legendre(n,x,p)
        assert a==P,('Legendre/Hasse mismatch',p)
        inert=pow(-6%p,(p-1)//2,p)==p-1
        assert (a==(0,0))==inert,('CM class discrepancy',p,a,inert)
        byclass.setdefault(p%24,[0,0])[0]+=1
        byclass[p%24][1]+=int(a==(0,0))
        if p in [5,13,17,29,37,41,53,61,73,89,109,137,373]:
            seq.append((p,p%24,a,inert))
    print('EXACT_CM_H24: j=2417472-1707264√2; H_-24=X²-4834944X+14670139392; NormΔ=64/729: PASS')
    print('Hasse coefficients / hypergeometric coefficients / Legendre / (-6/p) finite rings: PASS')
    print('Class counts (p mod24 : tested, zero):',byclass)
    print('Representative (p,class,P_n(2√2/3) coordinates,inert):')
    for row in seq:print(row)
    return byclass

if __name__=='__main__':test(3000)
