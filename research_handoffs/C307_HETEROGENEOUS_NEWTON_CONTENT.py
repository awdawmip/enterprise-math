#!/usr/bin/env python3
"""C307: exact pointwise-optimal heterogeneous modular Newton content.

For P in Z[t], deg P <= d, target s>=1, integer consecutive nodes T,...,T+d:
N_j = M/gcd(M,comb(d,j)), M=s*(d!)_supp(s).
The residues P(T+j) mod N_j recover gcd(s,content(P)) exactly.
See C307_AUTHOR_THEOREM_AND_PROOF_20261026.md for proof and limitations.
All arithmetic is exact integers, no float and no factorization of s.
"""
from __future__ import annotations
from math import gcd, factorial, comb


def s_supported_part(n: int, s: int) -> int:
    if n < 1 or s < 1:
        raise ValueError("positive integers required")
    h, rem = 1, n
    while True:
        g = gcd(rem, s)
        if g == 1:
            return h
        h *= g
        rem //= g


def adaptive_moduli(s: int, d: int) -> tuple[int, int, list[int]]:
    if s < 1 or d < 0:
        raise ValueError("s>=1, d>=0 required")
    h = s_supported_part(factorial(d), s)
    m = s*h
    return m, h, [m//gcd(m, comb(d,j)) for j in range(d+1)]


def content_gcd_from_sample_residues(s: int, d: int, residues: list[int]) -> int:
    """Input j is the least nonnegative residue of P(T+j) modulo its N_j.

    The function expects consistent residues of one integer polynomial.
    """
    m, h, moduli = adaptive_moduli(s,d)
    if len(residues) != d+1:
        raise ValueError("need exactly d+1 consecutive samples")
    if any(r < 0 or r >= n for r,n in zip(residues,moduli)):
        raise ValueError("residue outside node modulus")
    if s == 1:
        return 1
    row = residues[:]
    result = s
    fk = 1
    for k in range(d+1):
        if k:
            fk *= k
        a = gcd(fk,h)
        b = fk//a
        delta = row[0]%(s*a)
        assert delta%a == 0, ("inconsistent polynomial residues", k)
        beta = (delta//a)*pow(b,-1,s)%s
        result = gcd(result,beta)
        if k<d:
            row=[(row[j+1]-row[j])%m for j in range(len(row)-1)]
    return result


def evaluate_integer_poly(coefficients: list[int],x:int) -> int:
    v=0
    for a in reversed(coefficients):
        v=v*x+a
    return v


if __name__=="__main__":
    s,d,T=10,4,-3
    coefficients=[12,-18,0,25,-4]
    m,h,ns=adaptive_moduli(s,d)
    residues=[evaluate_integer_poly(coefficients,T+j)%ns[j] for j in range(d+1)]
    g=content_gcd_from_sample_residues(s,d,residues)
    expected=s
    for a in coefficients:expected=gcd(expected,a)
    assert g==expected
    print("C307_DEMO_PASS", {"s":s,"d":d,"M":m,"N":ns,"gcd":g})
