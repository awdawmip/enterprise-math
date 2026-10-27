#!/usr/bin/env python3
"""Exact author-side check of the finite cutoff bridge; not a native H0/B0 benchmark."""
from fractions import Fraction
from math import comb

def check_formal(nmax=10):
    f = [Fraction(1)]
    g = [Fraction(1)]
    for n in range(nmax):
        f.append(f[-1] * (Fraction(1, 3) + n) * (Fraction(1, 6) + n) / (n + 1)**2)
        g.append(g[-1] * (Fraction(2, 3) + n) * (Fraction(5, 6) + n) / (n + 1)**2)
    d = [Fraction(comb(2*n, n)**2 * comb(3*n, n), 108**n) for n in range(nmax + 1)]
    b = [Fraction(comb(2*n, n), 4**n) for n in range(nmax + 1)]
    for n in range(nmax + 1):
        lhs = sum((f[j]*g[n-j] for j in range(n+1)), Fraction(0))
        rhs = sum((b[j]*d[n-j] for j in range(n+1)), Fraction(0))
        assert lhs == rhs, ("formal_convolution_mismatch", n, lhs, rhs)
    # The source operator -1+(3/2)z*d/dz does not produce weight (3n-1).
    assert (Fraction(3,2)*1 - 1) != 3*1 - 1
    assert (3*1 - 1) == 2

def check_prime(p):
    q = p**3
    inv8 = pow(8, -1, q)
    inv216 = pow(216, -1, q)
    inv2 = pow(2, -1, q)
    t = [comb(2*k,k)**2*comb(3*k,k)*pow(inv216,k,q)%q for k in range(p)]
    b = [comb(2*j,j)*pow(inv8,j,q)%q for j in range(p)]
    prefix = []
    running = 0
    for x in b:
        running = (running+x)%q
        prefix.append(running)
    N=p-1
    s = sum((3*n-1)*sum(b[j]*t[n-j] for j in range(n+1)) for n in range(p))%q
    h = inv2*sum((6*k+1)*t[k]*prefix[N-k] for k in range(p))%q
    k_boundary = 3*inv2*sum((2*(N-k)+1)*t[k]*b[N-k] for k in range(p))%q
    w = sum((6*k+1)*t[k] for k in range(p))%q
    assert s == (h-k_boundary)%q, ("finite_bridge_failed",p)
    assert k_boundary%p == 0, ("boundary_not_p_divisible",p)
    return p,s,w,h,k_boundary,((s-w)%q)//(p*p) if (s-w)%q%(p*p)==0 else None

if __name__ == "__main__":
    check_formal()
    for p in (7,11,13,19,37,43,61,211,373):
        print("p S W H K residual_digit", *check_prime(p))
    assert check_prime(373)==(373,8487242,373,29983232,21495990,61)
    print("PASS_D25_LELAN_FINITE_CUTOFF_BRIDGE_AUTHOR_SIDE")
