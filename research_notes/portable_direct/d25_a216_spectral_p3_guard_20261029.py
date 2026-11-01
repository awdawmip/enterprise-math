#!/usr/bin/env python3
"""Exact p-local λ-spectral jet for the original 216 weighted finite sum.

This is an author-side pure-integer check, not native H0/B0 evaluation,
formal Source checkpoint, mathematical admission or reviewer verification.
"""
from math import comb, isqrt


def primes_under(bound):
    for p in range(7, bound):
        if p % 6 == 1 and all(p % d for d in range(2, isqrt(p)+1)):
            yield p


def inv(v, modulus):
    return pow(v % modulus, -1, modulus)


def spectral_jets(p):
    """Compute [λ^j] F(λ,z)|_(z=1/2), j<=2, without pole division."""
    assert p % 6 == 1 and p >= 7
    modulus = p**3
    m = (p-1)//6
    coeff = [1, 0, 0]
    val = [0, 0, 0]
    weighted = [0, 0, 0]
    z = 1
    inv2 = inv(2,modulus)
    for n in range(p):
        for j in range(3):
            val[j] = (val[j]+z*coeff[j]) % modulus
            weighted[j] = (weighted[j]+(12*n+1)*z*coeff[j]) % modulus
        if n==p-1: break
        q = (n-m)*(2*n+2*m+1)*inv2 % modulus
        factor=inv((n+1)**2,modulus)
        coeff = [q*coeff[0]*factor%modulus,
                 (q*coeff[1]+coeff[0])*factor%modulus,
                 (q*coeff[2]+coeff[1])*factor%modulus]
        z=z*inv2%modulus
    return val, weighted


def direct_K_H(p):
    """Original 2F1 source recurrence, independent of spectral λ coefficients."""
    modulus = p**3
    a=1
    K=H=0
    for n in range(p):
        K=(K+a)%modulus
        H=(H+(12*n+1)*a)%modulus
        if n < p-1:
            a=a*(6*n+1)*(3*n+1)*inv(36*(n+1)**2, modulus)%modulus
    return K,H


def direct_A(p):
    """Original binomial (6n+1) * C(2n,n)^2*C(3n,n)/216^n."""
    modulus=p**3
    inv216=inv(216,modulus)
    z=1
    total=0
    for n in range(p):
        total=(total+(6*n+1)*comb(2*n,n)**2*comb(3*n,n)*z)%modulus
        z=z*inv216%modulus
    return total


def original_source_high(p):
    """High degree weighted square, keeping the original ordered i,j labels."""
    modulus=p**3
    m=(p-1)//6
    a=[1]
    for n in range(p-1):
        a.append(a[-1]*(6*n+1)*(3*n+1)*inv(36*(n+1)**2,modulus)%modulus)
    K=a[:2*m+1]
    tail=a[2*m+1:]
    high=0
    for i,ai in enumerate(K):
        for j_off,aj in enumerate(tail):
            j=j_off+2*m+1
            if i+j >= p:
                high=(high+2*(1+6*(i+j))*ai*aj)%modulus
    return high


def frozen_R(p):
    """Frozen reflected double-sum, independent of the high-degree square."""
    m=(p-1)//6
    a=[1]
    for n in range(m):
        a.append(a[-1]*(6*n+1)*(3*n+1)*inv(36*(n+1)**2,p)%p)
    val=0
    for i in range(1,m+1):
        c=inv(10,p)
        nested=0
        for r in range(1,i+1):
            if r>1:
                x=r-1
                c=c*36*x*x*inv((6*x+5)*(3*x+2),p)%p
            nested+=(6*(i-r)+1)*c
        val=(val+2*a[i]*nested)%p
    return val


def run_one(p):
    mod=p**3
    lmb=p*(p+1)*inv(36,mod)%mod
    f,h=spectral_jets(p)
    jets=(f[0]*h[0]+lmb*(f[1]*h[0]+f[0]*h[1])+lmb*lmb*(f[2]*h[0]+f[1]*h[1]+f[0]*h[2]))%mod
    g,gh=direct_K_H(p)
    assert jets==(g*gh)%mod,(p,'spectral jet',jets,g*gh)
    assert (f[0]+lmb*f[1]+lmb*lmb*f[2])%mod==g
    assert (h[0]+lmb*h[1]+lmb*lmb*h[2])%mod==gh
    E=original_source_high(p)
    assert E%p**2==0
    r=frozen_R(p)
    assert E//p**2 == r,(p,E,r)
    a=direct_A(p)
    assert (jets-E)%mod==a,(p,jets,E,a)
    if p%24 in (13,19):
        assert f[0]%p==0
        simplified=(f[0]*h[0]+lmb*(f[1]*h[0]+f[0]*h[1])+lmb*lmb*(f[2]*h[0]+f[1]*h[1])-p*p*r)%mod
        assert simplified==a==p,(p,simplified,a)
    return dict(p=p, f0=f[0], f1=f[1], f2=f[2], h0=h[0], h1=h[1], h2=h[2],
                term0=f[0]*h[0]%mod,
                term1=lmb*(f[1]*h[0]+f[0]*h[1])%mod,
                term2=lmb*lmb*(f[2]*h[0]+f[1]*h[1]+f[0]*h[2])%mod,
                tail=E, R=r, A=a, lambda_value=lmb, full=jets)


def main():
    ps=list(primes_under(500))
    for p in ps:
        d=run_one(p)
        if p in (7,13,19,31,37,43,73,373):
            print('SPECTRAL_SOURCE',d)
    print('PASS_A216_P3_SCALAR_SPECTRAL_JET',len(ps),'primes p=1 mod6 <500',sum(p%24 in (13,19) for p in ps),'CM0 target primes')

if __name__ == '__main__': main()
