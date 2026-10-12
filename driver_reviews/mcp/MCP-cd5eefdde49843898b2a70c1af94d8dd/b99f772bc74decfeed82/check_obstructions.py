#!/usr/bin/env python3
"""Exact symbolic checks for the two stated certificate obstructions."""

import sympy as sp

i, r, n = sp.symbols("i r n")
k = sp.symbols("k", integer=True, nonnegative=True)
a = (i + sp.Rational(1, 6)) * (i + sp.Rational(1, 3)) / (2 * (i + 1) ** 2)
b = 2 * r**2 / ((r + sp.Rational(5, 6)) * (r + sp.Rational(2, 3)))


def li(poly):
    return sp.expand(
        (i + sp.Rational(1, 6))
        * (i + sp.Rational(1, 3))
        * poly.subs(i, i + 1)
        / 2
        - i**2 * poly
    )


def lr(poly):
    return sp.expand(
        2 * r**2 * poly.subs(r, r + 1)
        - (r - sp.Rational(1, 6)) * (r - sp.Rational(1, 3)) * poly
    )


assert sp.cancel(a * (i + 1) ** 2 - (i + sp.Rational(1, 6)) * (i + sp.Rational(1, 3)) / 2) == 0
assert sp.cancel(b * (r + sp.Rational(5, 6)) * (r + sp.Rational(2, 3)) - 2 * r**2) == 0

# A generic finite polynomial checks the operator bookkeeping; the note
# proves commutation at every degree because the variables are separate.
coefficients = sp.symbols("c0:9")
generic = sum(coefficients[3 * u + v] * i**u * r**v for u in range(3) for v in range(3))
assert sp.expand(li(lr(generic)) - lr(li(generic))) == 0

N = r**2 * (r + n + sp.Rational(1, 6)) * (r + n + sp.Rational(1, 3))
M = (r + n + 1) ** 2 * (r + sp.Rational(5, 6)) * (r + sp.Rational(2, 3))
C = (r + n) ** 2 * (r - sp.Rational(1, 6)) * (r - sp.Rational(1, 3))
assert sp.cancel((a * b).subs(i, r + n) - N / M) == 0
assert sp.expand(M.subs(r, r - 1) - C) == 0
assert sp.Poly(N, r).coeff_monomial(r**3) == 2 * n + sp.Rational(1, 2)
assert sp.Poly(C, r).coeff_monomial(r**3) == 2 * n - sp.Rational(1, 2)
assert sp.simplify(k + sp.Poly(N - C, r).coeff_monomial(r**3)) == k + 1

N_roots = [sp.Integer(0), -n - sp.Rational(1, 6), -n - sp.Rational(1, 3)]
C_roots = [-n, sp.Rational(1, 6), sp.Rational(1, 3)]
for root_N in N_roots:
    for root_C in C_roots:
        difference = sp.expand(root_C - root_N)
        # Each difference either has a nonzero n coefficient or is a
        # rational number that is not an integer.
        assert difference.has(n) or difference.is_integer is False

print("PASS: exact adjoint identities, commutation, diagonal ratio, root-orbit separation, and leading coefficient")
