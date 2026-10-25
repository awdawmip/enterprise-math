#!/usr/bin/env python3
"""Exact rational checks of Green finite-part strict alternating sign."""
from fractions import Fraction as Q
from math import factorial as f, comb

def check(m):
    L, U = m+1, 2*m
    a = {j: Q((-1)**(j-L)*f(m)*f(j-m-1)*f(2*m),
              f(2*m-j)*f(j)**2) for j in range(L,U+1)}
    h = {l: Q(2*f(m)*f(2*m)*f(l-1)**2,
              f(l+m)*f(l+2*m)) for l in range(1,U+1)}
    B = {j: sum(((j+l)*comb(3*m+l-j,3*m)*h[l]
                 for l in range(j,U+1)),Q(0)) for j in a}
    b = {j: abs(a[j])*B[j] for j in a}
    assert all(b[j]>b[j+1]>0 for j in range(L,U))
    finite_part = Q((-1)**(3*m),2**(3*m))*sum(
        (a[j]*B[j] for j in a),Q(0))
    assert (-1)**m*finite_part>0
    if m>=2:
        assert (b[L]-b[L+1])/2**(3*m) <= (-1)**m*finite_part < b[L]/2**(3*m)
    else:
        assert (-1)**m*finite_part == b[L]/2**(3*m)
    return finite_part

if __name__ == "__main__":
    assert check(1) == Q(-1,144)
    assert check(2) == Q(23,115200)
    assert check(3) == Q(-4273,729907200)
    for m in range(1,31):
        check(m)
    # Optional independent Taylor-jet witness from the previous portable code.
    try:
        import d25_critical_point_residue_check as preceding
    except ImportError:
        print("PASS 30 exact rational sign/bound tests; optional preceding jet script absent.")
    else:
        for m in range(1,13):
            assert check(m) == preceding.finite_part_via_jets(m)
        print("PASS 30 exact rational tests + 12 independent Taylor-jet comparisons.")
