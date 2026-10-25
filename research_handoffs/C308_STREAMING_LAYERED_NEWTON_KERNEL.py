#!/usr/bin/env python3
"""C308 exact one-pass modular Newton-content kernel (Z[t], deg <= d).

Input: s>=1, d>=0; sample(j,N_j) supplies canonical P(T+j)%N_j.
Output: gcd(s,content(P)), and optionally all Newton coefficients mod s.
No float, prime factorization, polynomial expansion, or retained sample vector.
For frozen C195/H168 79-branch-model schedule and circuit tests, see the full
C308_STREAMING_LAYERED_NEWTON.py in the author-level portable archive.
"""
from math import gcd, comb
from random import Random


def support_factorial_prefix(s, d):
    """h[k] = part of k! supported on the prime support of s."""
    if s < 1 or d < 0:
        raise ValueError("require s>=1 and d>=0")
    h = [1]
    for k in range(1, d + 1):
        rem, u = k, 1
        while (v := gcd(rem, s)) > 1:
            u *= v
            rem //= v
        h.append(h[-1] * u)
    return h


def node_and_layer_moduli(s, d):
    h = support_factorial_prefix(s, d)
    M = s * h[d]
    N = [M // gcd(M, comb(d, j)) for j in range(d + 1)]
    R = [s * h[k] for k in range(d + 1)]
    assert all(N[j] == s*h[j]*h[d-j] for j in range(d + 1))
    return N, R


def streaming_content(s, d, sample, *, with_coefficients=False):
    """Call sample(j, N_j) once for each j in ascending order if s>1.

    Sample accepts j and modulus and must return 0 <= residue < modulus.
    The implementation computes N_j just-in-time and retains only
    d+1 per-layer modular accumulators, not a sample-residue vector.
    """
    h = support_factorial_prefix(s, d)
    if s == 1:
        return 1, ([0] * (d + 1) if with_coefficients else None)
    M = s * h[d]
    R = [s*u for u in h]
    A = [0] * (d+1)
    for j in range(d+1):
        N = M//gcd(M, comb(d,j))
        r = sample(j,N)
        if not isinstance(r, int) or r<0 or r>=N:
            raise ValueError("sample must return its canonical modular residue")
        c = 1
        for k in range(j,d+1):
            A[k] = (A[k] + (c*r if (k-j)%2 == 0 else -c*r)) % R[k]
            if k < d:
                c = c*(k+1)//(k+1-j)
    result = s
    unit = 1
    out = []
    for k in range(d+1):
        if k:
            factor = h[k]//h[k-1]
            assert k % factor == 0
            unit = unit*(k//factor) % s
        assert gcd(unit,s) == 1 and A[k]%h[k] == 0
        b = ((A[k]//h[k])*pow(unit,-1,s)) % s
        result = gcd(result,b)
        if with_coefficients:
            out.append(b)
    return result, (out if with_coefficients else None)


def poly_at(coefficients, x):
    y = 0
    for c in reversed(coefficients):
        y = y*x + c
    return y


def independent_coefficients(coefficients, T):
    d=len(coefficients)-1
    row=[poly_at(coefficients,T+j) for j in range(d+1)]
    ans=[]
    factorial=1
    for k in range(d+1):
        if k:
            factorial*=k
        assert row[0]%factorial == 0
        ans.append(row[0]//factorial)
        row=[row[j+1]-row[j] for j in range(len(row)-1)]
    return ans


def exact_synthetic_test(cases=1000,seed=30820261026):
    rng=Random(seed)
    for i in range(cases):
        d=i%13
        s=[1,2,3,4,6,8,9,10,16,25,27,121,256][(i//13)%13]
        T=rng.randint(-11,11)
        coefficients=[rng.randint(-100000,100000) for _ in range(d+1)]
        if i%17 == 0:
            coefficients=[0]*(d+1)
        N,_=node_and_layer_moduli(s,d)
        calls=[0]
        def sample(j, modulus):
            assert modulus == N[j]
            calls[0]+=1
            return poly_at(coefficients,T+j)%modulus
        got,B=streaming_content(s,d,sample,with_coefficients=True)
        assert got == gcd(s,*coefficients)
        assert B == [b%s for b in independent_coefficients(coefficients,T)]
        assert calls[0] == (0 if s==1 else d+1)
    return {"test_cases":cases,"status":"PASS"}


if __name__ == "__main__":
    print("C308_STREAMING_EXACT",exact_synthetic_test())
