#!/usr/bin/env python3
"""Short exact reproducer for R4-EC26. Standard library; Python 3.10+."""
from fractions import Fraction
from math import comb, factorial

N = 64
K = 24


def add(a, b, sign=1):
    out = [0] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += sign*v
    return out


def term(a, d, c): return [0]*d + [c*x for x in a]


def binomial_poly(n, m):
    out = 1
    for i in range(m): out *= n-i
    return out//factorial(m)


def gamma_formula(n, k, formal=False):
    bc = binomial_poly if formal else lambda x, m: comb(x,m) if x >= m else 0
    acc = 0
    for a in range(k//2 + 1):
        for b in range(k//3 + 1):
            h = 2*a+3*b
            c = (-2)**a*comb(a+b,a)
            if h == k: acc += c*bc(n-3*a-5*b,a+b)
            if h == k-1: acc -= c*bc(n-2-3*a-5*b,a+b)
    return acc


E, G = [], []
for n in range(N+1):
    ep = add(E[n-1]+[0], [0]+E[n-1]) if n else [1]
    if n >= 4: ep = add(ep,term(E[n-4],2,-2))
    if n >= 6: ep = add(ep,term(E[n-6],3,1))
    if n == 2: ep = add(ep,[0,-1])
    E.append(ep)
    gp = G[n-1][:] if n else [1]
    if n >= 4: gp = add(gp,term(G[n-4],2,-2))
    if n >= 6: gp = add(gp,term(G[n-6],3,1))
    if n == 2: gp = add(gp,[0,-1])
    G.append(gp)
    reconstructed = [0]*(n+1)
    for k in range(n//2+1):
        assert gp[k] == gamma_formula(n,k), (n,k)
        for j in range(n-2*k+1):
            reconstructed[k+j] += gp[k]*comb(n-2*k,j)
    assert reconstructed == ep[:n+1], n

for k in range(2,K+1):
    for ell in range(1,(k+1)//3+1):
        assert gamma_formula(2*k-ell,k,True) == 0
    degree = k//2
    if k%2 == 0:
        expected = Fraction((-2)**degree,factorial(degree))
    else:
        expected = Fraction((degree+2)*(-2)**(degree-1),factorial(degree))
    vals = [gamma_formula(2*k+i,k) for i in range(degree+2)]
    for d in range(degree+2):
        if d == degree: assert vals[0] == expected*factorial(degree)
        if d == degree+1: assert vals[0] == 0
        vals = [b-a for a,b in zip(vals,vals[1:])]

print("PASS: gamma expansion, binomial formula, divisibility roots and leading terms",N,K)
