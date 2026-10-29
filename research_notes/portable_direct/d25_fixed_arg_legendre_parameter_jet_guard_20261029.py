#!/usr/bin/env python3
"""Exact author-side D25 finite p^2 Legendre/parameter-jet transport.

Tests original (1/8, 3/8) truncation, both coefficient and Euler-jet ports.
This is not a native H0/B0 or Source-admitted certificate.
"""
from math import comb, isqrt


def primes_below(limit):
    sieve = bytearray(b'\x01') * limit
    sieve[:2] = b'\x00\x00'
    for d in range(2, isqrt(limit - 1) + 1):
        if sieve[d]:
            sieve[d*d:limit:d] = b'\x00' * len(sieve[d*d:limit:d])
    return [p for p in range(5, limit) if sieve[p]]


def route(p):
    lam = 1 if p % 8 in (1, 3) else 5
    q = 1 if p % 8 in (1, 5) else 3
    r = (lam*p - q) // 8
    hits = [next(j for j in range(p) if (8*j+k) % p == 0) for k in (1, 3)]
    b = max(hits)
    assert r == min(hits) and r < b < p
    assert (2*(b+r)+1) % p == 0
    return lam, q, r, b


def independent_legendre_even(r, p):
    """Evaluate P_(2r)(sqrt(8/9)) by the independent binomial formula."""
    m = p*p
    y = 8*pow(9,-1,m)%m
    total = 0
    for j in range(r+1):
        total += (-1)**j * comb(2*r,j)*comb(4*r-2*j,2*r)*pow(y,r-j,m)
    return total * pow(4*r*0+4**r,-1,m)%m


def certificate(p):
    lam,q,r,b = route(p)
    m=p*p
    delta=lam*p*pow(8,-1,m)%m
    coeff=f=1; g=0
    zpow=1
    k_val=f_val=g_val=k_theta=f_theta=g_theta=0
    fports=[]; gports=[]
    for n in range(p):
        assert coeff==(f+delta*g)%m, ('coefficient',p,n)
        if n>r: assert f==0, ('terminating',p,n)
        if n>b: assert coeff==0 and g%p==0, ('finite_tail',p,n)
        k_val=(k_val+coeff*zpow)%m
        f_val=(f_val+f*zpow)%m
        g_val=(g_val+g*zpow)%m
        k_theta=(k_theta+n*coeff*zpow)%m
        f_theta=(f_theta+n*f*zpow)%m
        g_theta=(g_theta+n*g*zpow)%m
        fports.append(f%p); gports.append(g%p)
        if n==p-1: break
        halfdeninv=pow(2*(n+1)**2,-1,m)
        rat=(n-r)*(2*n+2*r+1)*halfdeninv%m
        der=(4*r+1)*halfdeninv%m
        new_f=f*rat%m
        new_g=(g*rat+f*der)%m
        # Parameter differentiation of finite hypergeometric recurrence.
        assert (2*(n+1)**2*new_g-(n-r)*(2*n+2*r+1)*g-(4*r+1)*f)%m==0
        f,g=new_f,new_g
        coeff=coeff*(8*n+1)*(8*n+3)*pow(64*(n+1)**2,-1,m)%m
        zpow=zpow*pow(9,-1,m)%m
    assert k_val==(f_val+delta*g_val)%m
    assert k_theta==(f_theta+delta*g_theta)%m
    # The source term (2r+1/2)F in the Picard-Fuchs jet equation.
    # At n=b the truncation boundary vanishes mod p because b+r+1/2=0.
    for n in range(p):
        nxt=gports[n+1] if n+1<p else 0
        assert (2*(n+1)**2*nxt - (n-r)*(2*n+2*r+1)*gports[n] - (4*r+1)*fports[n])%p==0,('PF',p,n)
    expected=(1 if q==1 else -1)*pow(4,-1,p)%p
    assert (4*r+1)*pow(2,-1,p)%p==expected
    return {'p':p, 'branch':p%24, 'lam':lam, 'r':r, 'b':b,
            'K':k_val,'Legendre':f_val,'delta_G':delta*g_val%m,
            'theta_K':k_theta,'theta_F':f_theta,'delta_theta_G':delta*g_theta%m,
            'forcing':expected}


def main():
    primes=primes_below(1200)
    out=[certificate(p) for p in primes]
    assert len(primes)==194
    for a in out:
        if a['branch'] in (13,23):
            assert a['K']==0,('finite Root2 evidence',a)
    for p in (13,17,19,23,37,61,373):
        a=certificate(p)
        assert a['Legendre']==independent_legendre_even(a['r'],p),('independent P',p)
        print('CASE',a)
    print('PASS_D25_FINITE_P2_LEGENDRE_PARAMETER_JET',len(primes),'primes p<1200')
    print('PASS_PICARD_FUCHS_SOURCE_EULER_JET_AND_INDEPENDENT_LEGENDRE')


if __name__=='__main__':
    main()
