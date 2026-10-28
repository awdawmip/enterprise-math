#!/usr/bin/env python3
"""GH-53/54: direct-source p-adic reverse deformation and L4 boundary checks.
Author-side mathematical evidence, not native execution or independent admission.
"""
from fractions import Fraction
from math import isqrt


def primes(limit):
    return [p for p in range(7, limit) if p % 4 == 3 and all(p % k for k in range(2, isqrt(p)+1))]


def fourpoly(poly, t):
    """L_t applied to polynomial coefficients over the rationals."""
    D = lambda n: Fraction(4*n + 2 - t, 4)
    A = lambda n: Fraction(4*n + 3 - t, 4)
    B = lambda n: Fraction(4*n + 4 - t, 4)
    C = lambda n: Fraction(4*n + 5 - t, 4)
    return [(n*D(n)**3*(poly[n] if n<len(poly) else 0)
             - n*A(n-1)*B(n-1)*C(n-1)*(poly[n-1] if 0<=n-1<len(poly) else 0))
            for n in range(len(poly)+1)]


def exact(d):
    p=4*d+3
    rho0=[Fraction(1)]
    rhop=[Fraction(1)]
    for j in range(d):
        rho0.append(rho0[-1]*Fraction((4*j+3)*(4*j+4)*(4*j+5),(4*j+6)**3))
        rhop.append(rhop[-1]*Fraction((4*j+3-p)*(4*j+4-p)*(4*j+5-p),(4*j+6-p)**3))
    assert fourpoly(rhop,p)==[Fraction(0)]*(d+2)
    lhs=fourpoly(rho0,0)
    assert lhs[:d+1]==[Fraction(0)]*(d+1)
    assert lhs[d+1]==-Fraction(p*(p+1)**2*(p+2),256)*rho0[d]
    c=[Fraction(1)]
    for j in range(d):
        c.append(c[-1]*Fraction((4*j+1)**3,(4*j+2)*(4*j+3)*(4*j+4)))
    assert all(c[d-r] == c[d]*rhop[r] for r in range(d+1))
    for z in [2,9,-1]:
        direct=sum(Fraction(8*r+1)*c[r]*z**r for r in range(d+1))
        inverse=c[d]*z**d*sum(Fraction(2*p-5-8*r)*rhop[r]/z**r for r in range(d+1))
        assert direct==inverse


def check_prime(p):
    d=(p-3)//4; mod=p**3
    c=[1];r0=[1];rp=[1];H=[0];L=[0]
    h=s=0
    for j in range(d):
        c.append(c[-1]*(4*j+1)**3*pow((4*j+2)*(4*j+3)*(4*j+4),-1,mod)%mod)
        r0.append(r0[-1]*(4*j+3)*(4*j+4)*(4*j+5)*pow(4*j+6,-3,mod)%mod)
        rp.append(rp[-1]*(4*j+3-p)*(4*j+4-p)*(4*j+5-p)*pow((4*j+6-p),-3,mod)%mod)
        q=3*pow(4*j+6,-1,mod)-sum(pow(4*j+k,-1,mod) for k in (3,4,5))
        q2=3*pow(4*j+6,-2,mod)-sum(pow(4*j+k,-2,mod) for k in (3,4,5))
        h=(h+q)%mod;s=(s+q2)%mod
        H.append(h)
        L.append((h*h+s)*pow(2,-1,mod)%mod)
    assert all(c[d-r]*pow(c[d],-1,mod)%mod==rp[r] for r in range(d+1))
    assert all(rp[r]==r0[r]*(1+p*H[r]+p*p*L[r])%mod for r in range(d+1))
    for z in (2,9,-1):
        u=pow(z,-1,mod)
        direct=sum((8*r+1)*c[r]*pow(z,r,mod) for r in range(d+1))%mod
        mirror=sum((2*p-5-8*r)*rp[r]*pow(u,r,mod) for r in range(d+1))%mod
        lift=sum((-(8*r+5)+p*(2-(8*r+5)*H[r])+p*p*(2*H[r]-(8*r+5)*L[r]))*r0[r]*pow(u,r,mod) for r in range(d+1))%mod
        assert direct==c[d]*pow(z,d,mod)*mirror%mod
        assert mirror==lift
    inv=lambda k:pow(k,-1,p)
    half=inv(2);fourth=inv(4)
    def op0(seq,n):
        q=n*pow((n+half)%p,3,p)*(seq[n] if n<len(seq) else 0)
        if n: q-=n*n*(n-fourth)*(n+fourth)*seq[n-1]
        return q%p
    def op1(seq,n):
        q=-3*fourth*n*pow((n+half)%p,2,p)*(seq[n] if n<len(seq) else 0)
        if n:
            pairs=n*(n+fourth)+(n-fourth)*(n+fourth)+(n-fourth)*n
            q+=fourth*n*pairs*seq[n-1]
        return q%p
    A=[r0[r]*H[r]%p for r in range(d+1)]
    for n in range(d+2):
        expected=0 if n<=d else r0[d]*inv(128)%p
        assert (op0(A,n)+op1(r0,n))%p==expected,(p,n,(op0(A,n)+op1(r0,n))%p,expected)
    # Separate conditional second-digit certificate at z=9 (finite observation).
    z=9; mod2=p*p; u=pow(z,-1,mod2)
    phi=sum((8*r+5)*r0[r]*pow(u,r,mod2) for r in range(d+1))%mod2
    if phi%p==0:
        q=phi//p
        rr=sum(r0[r]*pow(u,r,mod2) for r in range(d+1))%p
        phia=sum((8*r+5)*r0[r]*H[r]*pow(u,r,mod2) for r in range(d+1))%p
        correction=(2*rr-phia)%p
        direct=sum((8*r+1)*c[r]*pow(z,r,mod2) for r in range(d+1))%mod2
        assert direct%p==0
        assert direct//p==c[d]*pow(z,d,p)*(correction-q)%p
    else:
        q=correction=None
    # Valuation one: rho_d is p-adic unit; 1/256*(p+1)^2*(p+2) also unit.
    assert r0[d]%p and (p+1)*(p+2)%p
    return (p,c[d]%p,d,q,correction)

if __name__ == '__main__':
    for d in range(1,11):exact(d)
    print('PASS_GH53_GH54_EXACT_Q 10 d=1..10')
    cases=[check_prime(p) for p in primes(2000)]
    print('PASS_GH53_GH54_PADIC_MOD_P3',len(cases),'primes p<2000')
    for p,cd,d,q,correction in cases:
        if p in (7,11,19,43,67):print('WITNESS',p,'d',d,'c_d mod p',cd,'q',q,'correction',correction)
