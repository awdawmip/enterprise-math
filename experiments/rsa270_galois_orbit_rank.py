#!/usr/bin/env python3
"""
Regression verifier for the exact Galois-orbit rank theorem.

Researcher-ID: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
from fractions import Fraction
from math import gcd


def prime_factors(n):
    out = set()
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root_prime_power(l, e):
    m = l**e
    phi = (l-1)*l**(e-1)
    pf = prime_factors(phi)
    for g in range(2, m):
        if gcd(g,m)==1 and all(pow(g, phi//q, m) != 1 for q in pf):
            return g
    raise AssertionError("primitive root not found")


def ramanujan_pp(l, e, k):
    m=l**e; n=l**(e-1); k%=m
    if k==0: return (l-1)*n
    if k%n==0: return -n
    return 0


def H_values_on_generator_order(l,e,B=10,b=1):
    m=l**e
    phi=(l-1)*l**(e-1)
    g=primitive_root_prime_power(l,e)
    n=l**(e-1)

    def G(x):
        return sum((B**j)*ramanujan_pp(l,e,x-(b+j*n)) for j in range(l))
    def H(x):
        return G(x)-G((-x)%m)

    vals=[]
    x=1
    for _ in range(phi):
        vals.append(H(x))
        x=(x*g)%m
    return vals


def rank_fraction(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
    while r<m and c<n:
        piv=next((i for i in range(r,m) if A[i][c]), None)
        if piv is None:
            c+=1; continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i==r: continue
            f=A[i][c]
            if f:
                A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1; c+=1
    return r


def check_case(l,e):
    h=H_values_on_generator_order(l,e)
    phi=len(h)
    # Left translations in cyclic generator coordinates are circulant shifts.
    M=[h[-s:]+h[:-s] if s else h[:] for s in range(phi)]
    rank=rank_fraction(M)
    expected=((l-1)**2 * l**(e-2))//2
    assert rank==expected,(l,e,rank,expected)
    return phi,rank


def main():
    cases=[(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(11,2)]
    for l,e in cases:
        phi,rank=check_case(l,e)
        print(f"l={l} e={e}: |G|={phi}, orbit-rank={rank} PASS")
    print("ALL PASS")

if __name__=="__main__":
    main()
