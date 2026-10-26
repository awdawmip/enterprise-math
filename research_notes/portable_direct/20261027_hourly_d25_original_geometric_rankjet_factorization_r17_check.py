#!/usr/bin/env python3
"""D25 R17 author exact checks: original finite-face geometric/rank-jet ports.

The full calculation uses the original theta=-p/6 coefficients, retains four genuine
finite-cutoff faces and the full ordered low-high rank carrier. The independent
first-digit certificate uses the R15 factorial formula, not the Ward recurrence.
No floating point or original-class Frobenius experiment is involved.
"""
from fractions import Fraction
from math import isqrt


def primes(limit=997):
    for p in range(7, limit+1):
        if p % 6 == 1 and not any(p % q == 0 for q in range(2, isqrt(p)+1)):
            yield p


def carrier_mod(p, digits=3):
    m, mod = (p-1)//6, p**digits
    L, N = 1-2*m, 2*m-1
    inv = lambda x: pow(x % mod, -1, mod)
    theta = -p*inv(6) % mod
    f = [0]*p
    beta = [None]*p
    valuation, unit = 0, 1
    for r in range(p):
        f[r] = unit*pow(p, valuation, mod) % mod
        if r > 2*m:
            assert valuation == 2
            beta[r] = unit
        if r == p-1:
            break
        a, b = 6*r+1, 3*r+1
        while a % p == 0:
            a //= p
            valuation += 1
        while b % p == 0:
            b //= p
            valuation += 1
        unit = unit*a*b*inv(18*(r+1)**2) % mod
    assert valuation == 2
    Z, E = {}, {}
    for n in range(L, N+1):
        v0 = v1 = 0
        for j in range(max(1, 1-n), min(2*m, 2*m-n)+1):
            ell = j+n
            value = f[j]*beta[p-ell] % mod
            v0 += value
            v1 += j*value
        Z[n] = (2*v1-(p-n)*v0) % mod
    for n in range(L,N+1):
        if n >= 0:
            E[n] = (2*(m+theta)**2*beta[p-n-1]
                    -(6*m*m-8*m*theta+2*theta**2)
                    *f[2*m-n]*beta[4*m]) % mod
        else:
            E[n] = ((20*m*m-14*m*theta+2*theta**2)*f[-n]*beta[p-1]
                    +(2*m*theta-2*theta**2)*f[2*m]
                    *beta[p-(2*m+n+1)]) % mod
        next_z = Z[n+1] if n < N else 0
        assert ((p-n)*Z[n]-(2*(p-n)-1)*inv(2)*next_z-E[n]) % mod == 0
    assert Z[L] == -4*m*f[2*m]*beta[p-1] % mod
    assert Z[L] % p == 0
    return L, N, mod, Z, E


def ports(p, datum, z=2):
    L, N, mod, Z, E = datum
    inv = lambda x: pow(x % mod, -1, mod)
    assert z % p
    weight = lambda n: pow(z, n, mod)
    O = sum(weight(n)*Z[n] for n in range(L, N+1)) % mod
    J = sum(n*weight(n)*Z[n] for n in range(L, N+1)) % mod
    Gm = sum(weight(n)*E[n] for n in range(L, 0)) % mod
    Gp = sum(weight(n)*E[n] for n in range(0, N+1)) % mod
    G = (Gm+Gp) % mod
    # Exact finite discrete integration-by-parts, tested independently of E.
    rhs = ((p-(2*p+1)*inv(2)*inv(z))*O
           -(1-inv(z))*J
           +(p-L+inv(2))*weight(L)*inv(z)*Z[L]) % mod
    assert G == rhs, (p, z, G, rhs)
    # Sign-separated formulas retain the genuine n=0 interface.
    neg = ((p-L)*weight(L)*Z[L]
           +sum(weight(n)*((p-n)-(p-n+inv(2))*inv(z))*Z[n]
                for n in range(L+1, 0))
           -(p+inv(2))*weight(-1)*Z[0]) % mod
    pos = (p*Z[0]
           +sum(weight(n)*((p-n)-(p-n+inv(2))*inv(z))*Z[n]
                for n in range(1, N+1))) % mod
    assert (neg, pos) == (Gm, Gp), (p, z, neg, pos, Gm, Gp)
    # At z=2 and p|Z_L, the first digit remembers the rank jet.
    if z == 2:
        assert G % p == (-O*pow(4,-1,p)-J*pow(2,-1,p)) % p
    return dict(O=O, J=J, G=G, Gminus=Gm, Gplus=Gp,
                Ominus=sum(weight(n)*Z[n] for n in range(L,0))%mod,
                Oplus=sum(weight(n)*Z[n] for n in range(0,N+1))%mod)


def independent_factored_digit(p, z=2):
    """No Ward coefficients/sources: independent factorial beta and low f mod p."""
    m = (p-1)//6
    fact = [1]*p
    for r in range(1,p):
        fact[r] = fact[r-1]*r % p
    inv = lambda x: pow(x % p, -1, p)
    C = (-1 if m%2 else 1)*fact[m]*fact[2*m]*inv(18) % p
    beta_ell = {}
    for ell in range(1,2*m+1):
        r = p-ell
        beta_ell[ell] = (C*fact[r-m-1]*fact[r-2*m-1]
                          *inv(fact[r]**2)) % p
    f = [1]+[0]*(2*m)
    for j in range(1,m+1):
        k = j-1
        f[j] = f[j-1]*(6*k+1)*(3*k+1)*inv(18*j*j) % p
    A = [sum(j**k*f[j]*pow(z,-j,p) for j in range(1,m+1))%p
         for k in range(3)]
    B = [sum(ell**k*beta_ell[ell]*pow(z,ell,p)
             for ell in range(1,2*m+1))%p for k in range(3)]
    O = (A[1]*B[0]+A[0]*B[1]) % p
    J = (A[0]*B[2]-A[2]*B[0]) % p
    return A, B, O, J


def exact_rational_audit(p):
    """Independent Q-valued original-parameter recurrence at small p."""
    m = (p-1)//6
    L, N = 1-2*m, 2*m-1
    theta = Fraction(-p,6)
    f = [Fraction(1)]
    for r in range(p-1):
        f.append(f[-1]*Fraction((6*r+1)*(3*r+1),18*(r+1)**2))
    b = {r:f[r]/p**2 for r in range(2*m+1,p)}
    Z, E = {}, {}
    for n in range(L,N+1):
        pairs = [(j,j+n) for j in range(1,2*m+1)
                 if 1<=j+n<=2*m]
        v0 = sum((f[j]*b[p-ell] for j,ell in pairs),Fraction(0))
        v1 = sum((j*f[j]*b[p-ell] for j,ell in pairs),Fraction(0))
        Z[n] = 2*v1-(p-n)*v0
        if n>=0:
            E[n] = (2*(m+theta)**2*b[p-n-1]
                    -(6*m*m-8*m*theta+2*theta**2)
                    *f[2*m-n]*b[4*m])
        else:
            E[n] = ((20*m*m-14*m*theta+2*theta**2)*f[-n]*b[p-1]
                    +(2*m*theta-2*theta**2)*f[2*m]
                    *b[p-(2*m+n+1)])
    for n in range(L,N+1):
        assert (p-n)*Z[n]-Fraction(2*(p-n)-1,2)*Z.get(n+1,0)==E[n]
    O = sum((Fraction(2)**n*Z[n] for n in Z),Fraction(0))
    J = sum((n*Fraction(2)**n*Z[n] for n in Z),Fraction(0))
    Gminus = sum((Fraction(2)**n*E[n] for n in range(L,0)),Fraction(0))
    Gplus = sum((Fraction(2)**n*E[n] for n in range(0,N+1)),Fraction(0))
    rhs = (Fraction(2*p-1,4)*O-Fraction(1,2)*J
           +Fraction(2*p-2*L+1,4)*Fraction(2)**L*Z[L])
    assert Gminus+Gplus==rhs
    return True


def check():
    target = list(primes())
    assert len(target) == 80
    for p in target:
        datum = carrier_mod(p)
        out = ports(p, datum)
        A, B, O, J = independent_factored_digit(p)
        assert (O,J) == (out['O']%p,out['J']%p), (p,O,J,out)
        if p==13:
            assert (A,B,O,J)==([12,7,10],[9,12,8],12,6)
            assert tuple(out[k]%p for k in ['Ominus','Oplus','Gminus','Gplus','G']) == (10,2,5,2,7)
        if p==733:
            assert (A,B,O,J)==([732,1,367],[577,577,40],0,38)
            assert tuple(out[k]%p for k in ['Ominus','Oplus','Gminus','Gplus','G']) == (433,300,285,429,714)
            assert (out['O'],out['G']) == (337753939,76668849)
            assert out['O']%(p*p)==336447
            inv2=pow(2,-1,p)
            assert out['G']%p == -J*inv2%p == 714
            # Hensel lift of the *genuine original moment* O(z), not the
            # previous free-Ward seam Xi(z). Both share z=2 mod p only.
            z=2
            for exponent, correction, expected in [(1,53,38851),(2,479,257400282)]:
                value=ports(p,datum,z)
                assert value['O']%(p**exponent)==0
                derivative=value['J']*pow(z,-1,p)%p
                assert derivative==19
                h=-(value['O']//p**exponent)*pow(derivative,-1,p)%p
                assert (h,z+p**exponent*h)==(correction,expected)
                z=expected
            assert ports(p,datum,z)['O']==0
            assert ports(p,datum,534359)['O']%(p*p)==280739
    for p in (7,13,19):
        exact_rational_audit(p)
    print('PASS: 80 target primes; 80 four-face Ward/source-to-jet identities;')
    print('80 independent factorial factorization checks; exact rational audits 7,13,19;')
    print('p=13/733 tagged original-source witnesses and genuine O_733 Hensel roots')


if __name__ == '__main__':
    check()
