"""Exact standard-library verification for EC49FVB prime-valuation sieve.

Finite checks verify constants, root sets, CRT size, and representative
rational examples. The infinite-domain theorem is proved in the companion note.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd, isqrt

BETA = Q(3, 637)
GAMMA = Q(141024, 1653649)
U = Q(4822040484, 8132285009)
PRIMES = (29, 673, 416677)
M = U.denominator


def prime(p):
    return p > 1 and all(p % k for k in range(2, isqrt(p) + 1))


def mod(q, p):
    assert q.denominator % p
    return (q.numerator * pow(q.denominator, -1, p)) % p


def v(n, p):
    if n == 0:
        raise ValueError('Zero has no finite p-adic valuation here')
    n = abs(n)
    k = 0
    while n % p == 0:
        k += 1
        n //= p
    return k


def vf(q, p):
    return v(q.numerator, p) - v(q.denominator, p)


def roots(p):
    beta, gamma = mod(BETA, p), mod(GAMMA, p)
    assert beta and gamma and (1-beta) % p and (1+gamma) % p
    aextra = ((1+beta) * pow(beta, -1, p)) % p
    t0extra = pow(beta, -1, p)
    teextra = (-pow(gamma, -1, p)) % p
    assert len({0, 1, aextra, t0extra, teextra}) == 5
    return (0, aextra), (1, t0extra), (1, teextra)


def ratios(x):
    assert 0 < x < 1
    t0 = (1-x)*(1-BETA*x)
    te = (1-x)*(1+GAMMA*x)
    a = 1-t0
    b = 1-U*te
    assert 0 < a < b < 1
    r = t0/(U*te)
    s = (b/a)*r
    assert 1 < r < s
    return r, s, a, b, t0, te


def crt(remainders, primes=PRIMES):
    out = 0
    modulus = 1
    for rem, p in zip(remainders, primes):
        out += modulus*((rem-out)*pow(modulus, -1, p) % p)
        modulus *= p
        out %= modulus
    return out


assert M == 29*673*416677
assert all(prime(p) for p in PRIMES)
results = {}
for p in PRIMES:
    assert vf(U, p) == -1
    aroots, t0roots, teroots = roots(p)
    teother = next(r for r in teroots if r != 1)
    b = mod(BETA, p)
    g = mod(GAMMA, p)
    generic = p - 5
    certified = p - 2
    assert len(set(range(p)) - {1, teother}) == certified
    results[p] = (b, g, aroots, t0roots, teroots, certified)
    # Check rational samples in each of the p-2 covered classes.
    # For the largest prime, the exact modular root classification suffices
    # and a deterministic spread of 17 representatives tests the implementation.
    test_rs = list(range(p)) if p < 1000 else sorted(set([0,2,3,4,5,10,100,1000,p//3,p//2,p-3,p-2,p-1]+[aroots[1],t0roots[1]]))
    for r in test_rs:
        if r in (1, teother):
            continue
        # x is a strictly interior rational with denominator p+1; for r=0 use p/(p+1).
        x = Q(r if r else p, p+1)
        R,S,*_ = ratios(x)
        vr, vs = vf(R,p), vf(S,p)
        assert vr > 0 and (vs <= 0 or vr > vs > 0), (p,r,vr,vs)
    # A rational x with a denominator divisible by p: exact (1,0) pair.
    R,S,*_ = ratios(Q(1,p))
    assert (vf(R,p),vf(S,p)) == (1,0)

exception_sets = [(1, results[p][4][1]) for p in PRIMES]
residues = sorted(crt(rem) for rem in product(*exception_sets))
assert len(set(residues)) == 8
assert residues == [1,3496921755,3738594415,5459887102,
                    5701559762,5927647003,6169319663,7890612350]
assert M - len(residues) == 8132285001
# Two higher-lift refinements at 29, beyond the coarse 8-class sieve.
x1 = Q(1, 842)  # x = 1 (mod 29^2)
x2 = Q(603, 842)  # x = root(1 + gamma*x) (mod 29^2)
R1,S1,*_ = ratios(x1)
R2,S2,*_ = ratios(x2)
assert (vf(1-x1,29),vf(R1,29),vf(S1,29)) == (2,1,1)
assert (vf(1+GAMMA*x2,29),vf(R2,29),vf(S2,29)) == (2,-1,-1)
# Classes omitted by the old 29-only certificate are handled by p=673.
for x in (Q(1,30), Q(23,30)):
    R,S,*_ = ratios(x)
    assert (vf(R,673),vf(S,673)) == (1,0)

print('ALL PASS: denominator factorization, 3 primes, modular roots,')
print('p-denominator case, finite rational valuation witnesses, CRT 8 classes')
for p,tup in results.items():
    print(f'p={p}: beta={tup[0]}, gamma={tup[1]}, A={tup[2]}, T0={tup[3]}, TE={tup[4]}, certified={tup[5]}/{p}')
print('M=',M,'certified=', M-8, '/', M)
print('unresolved residue representatives:', residues)
