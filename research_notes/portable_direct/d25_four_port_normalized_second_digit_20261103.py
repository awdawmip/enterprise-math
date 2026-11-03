#!/usr/bin/env python3
"""Exact p-adic computation for the original weighted 216/2304 reflected kernel."""
from fractions import Fraction


def primes(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for a in range(2, int(n**.5) + 1):
        if sieve[a]:
            sieve[a*a::a] = b'\x00' * ((n-a*a)//a + 1)
    return [p for p in range(13, n+1) if sieve[p] and p % 24 in (13, 19)]


def factorial_unit_mod_table(p, modulus):
    """Strip exactly one p from each multiple of p (4p < p^2 for p>=13)."""
    out = [1]*(4*p+1)
    acc = 1
    for n in range(1, 4*p+1):
        acc = (acc * (n//p if n % p == 0 else n)) % modulus
        out[n] = acc
    return out


def h_reflected(p, k, fact, modulus):
    j = p-k
    num = fact[4*k]*fact[4*j]*fact[k]*fact[j]
    den = fact[2*k]*fact[2*j]*fact[3*k]*fact[3*j]
    return pow(3 * pow(32, -1, modulus), p, modulus) * (num % modulus) * pow(den % modulus, -1, modulus) % modulus


def epsilon(p, k, harm):
    q = {a: a*k//p for a in (2,3,4)}
    r = {a: a*k-p*q[a] for a in (2,3,4)}
    fermat = lambda a: ((pow(a,p-1,p*p)-1)//p) % p
    return (fermat(3)-5*fermat(2)+4*harm[r[4]-1]+harm[k-1]-2*harm[r[2]-1]-3*harm[r[3]-1])%p


def verify_prime(p):
    m = p*p
    f = factorial_unit_mod_table(p,m)
    harmonic = [0]*p
    for i in range(1,p):
        harmonic[i] = (harmonic[i-1]+pow(i,-1,p))%p
    eta = 5 if p%24 == 13 else 3
    z=(eta*p-1)//8
    pole=(p-1)//6
    assert 8*z+1 == eta*p and 6*pole+1 == p
    # Directed observer: the reflected product alone does not retain these separate valuations.
    def vb(k): return 2*k//p+3*k//p
    def vc(k): return 4*k//p
    za = 2 if eta==5 else 1
    assert (vb(z),vc(z),vb(p-z),vc(p-z)) == (za,za,3-za,3-za)
    assert (vb(pole),vc(pole),vb(p-pole),vc(p-pole)) == (0,0,3,3)
    res = {}
    for label,k in (("zero",z),("pole",pole)):
        H = h_reflected(p,k,f,m)
        A = (8*k+1)*(8*(p-k)+1)
        B = (6*k+1)*(6*(p-k)+1)
        E = epsilon(p,k,harmonic)
        if label == "zero":
            assert A%p==0 and B%p != 0
            exact = H*(A//p)*pow(B,-1,m)%m
            base = (4*eta)*pow(7,-1,m)%m
            corr = (8-43*eta)*pow(14,-1,p)%p
        else:
            assert B%p==0 and A%p != 0
            exact = H*A*pow(B//p,-1,m)%m
            base = -7*pow(96,-1,m)%m
            corr = -51*pow(14,-1,p)%p
        predicted = (base*(1+p*((E+corr)%p)))%m
        assert exact == predicted, (p,label, k, exact,predicted,E)
        kk=p-k
        hh=h_reflected(p,kk,f,m)
        assert hh==H
        Aa=(8*kk+1)*(8*(p-kk)+1)
        Bb=(6*kk+1)*(6*(p-kk)+1)
        assert Aa==A and Bb==B
        res[label] = dict(k=k,mirror=p-k,normalized=exact,leading=exact%p,E=E,correction=corr)
    return res


def main():
    pp = primes(2000)
    assert len(pp)==77, len(pp)
    records=[]
    for p in pp:
        r=verify_prime(p)
        if p in (13,19,37,43,61,67,373):
            records.append((p,r))
    print('PASS',len(pp),'target primes, all 4 exceptional oriented indices/prime; normalized residues mod p^2')
    for p,r in records:
        print('p=',p,'eta=',5 if p%24==13 else 3,'Z=',r['zero'],'P=',r['pole'])

if __name__=='__main__': main()
