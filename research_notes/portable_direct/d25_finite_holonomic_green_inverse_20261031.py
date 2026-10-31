#!/usr/bin/env python3
"""Finite coefficient-adjoint inverse over Q and F_p; author-side exact check."""
from fractions import Fraction
from d25_signed_boundary_holonomic_pairing_20261031 import primes_upto, c_coefficients


def op_forward(f, ell):
    """L f, of degree <= ell, exact rational coefficient form."""
    assert len(f) == ell
    out = [0] * (ell + 1)
    for n in range(1, ell + 1):
        fn = f[n] if n < ell else 0
        alpha = n*(n+Fraction(5, 6))*(n+Fraction(2, 3))
        out[n] = alpha*fn-2*n**3*f[n-1]
    return out


def op_backward(y, ell, modulus=None):
    """Unique inverse f from a source y0=0, by descending indices."""
    assert len(y) == ell + 1 and y[0] == 0
    f = [0] * (ell + 1)
    for n in range(ell, 0, -1):
        if modulus is None:
            alpha = n*(n+Fraction(5, 6))*(n+Fraction(2, 3))
            f[n-1] = (alpha*f[n]-y[n])/Fraction(2*n**3)
        else:
            p = modulus
            inv6 = pow(6, -1, p)
            inv3 = pow(3, -1, p)
            alpha = n*(n+5*inv6)*(n+2*inv3) % p
            f[n-1] = (alpha*f[n]-y[n])*pow(2*n**3, -1, p) % p
    return f[:-1]


def test_q():
    for ell in range(1, 13):
        f = [Fraction(n*n+2*n+1, n+2) for n in range(ell)]
        y = op_forward(f, ell)
        assert op_backward(y, ell) == f
        y2 = [0] + [Fraction(n*n+3*n+7, n+5) for n in range(1, ell+1)]
        assert op_forward(op_backward(y2, ell), ell) == y2
    return 12


def test_fp(p):
    ell = (p-1)//6
    c = c_coefficients(p)
    terminal = -20*ell**3*c[ell] % p
    assert terminal != 0
    y = [0]*ell + [terminal]
    f = op_backward(y, ell, p)
    assert f == [10*c[k+1] % p for k in range(ell)]
    assert f[0] == 1
    y2 = [0]+[(n*n+3*n+7) % p for n in range(1, ell+1)]
    ff = op_backward(y2, ell, p)
    inv6, inv3 = pow(6, -1, p), pow(3, -1, p)
    assert all((n*(n+5*inv6)*(n+2*inv3)*
                (ff[n] if n < ell else 0)-2*n**3*ff[n-1]-y2[n])%p == 0
               for n in range(1, ell+1))
    return p, terminal, f[0]


def main():
    tested = [test_fp(p) for p in primes_upto(5000)]
    anchors = [t for t in tested if t[0] in (13, 19, 37, 67, 373)]
    assert [a[0] for a in anchors] == [13,19,37,67,373]
    print('Q inverse/surjectivity, ell 1..', test_q())
    print('finite-field inverse target p=1 mod6 <=5000:', len(tested))
    print('anchors (p, nonzero terminal, recovered f0):', anchors)
    print('PASS_D25_FINITE_HOLONOMIC_GREEN_INVERSE_NO_ERASURE')


if __name__=='__main__':
    main()
