#!/usr/bin/env python3
"""R446: exact rational-polynomial edge PF3 certificates. Requires sympy."""
import hashlib
import json
import math
from itertools import combinations
from pathlib import Path
import sympy as sp

r, u = sp.symbols('r u', integer=True, positive=True)


def falling(x, n):
    ans = sp.Integer(1)
    for i in range(n):
        ans *= x - i
    return ans


def ratio(h):
    """Exact H(r,r-h)/Catalan(r), valid on r>=2*h+2."""
    sum_terms = sp.Integer(0)
    for q in range(h + 1):
        sum_terms += (
            sp.binomial(h, q) * falling(r, 2*q) * falling(r, 2*h-2*q)
            * (4*q-2*h+1) / (r-2*h+2*q+1)
        )
    return sp.factor(
        (r+1) * falling(2*r-h, h) * sum_terms
        / (sp.factorial(h) * falling(2*r, 2*h))
    )


def binom(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def raw_H(R, h):
    s = R-h
    return binom(2*R-h, h) * sum(
        binom(h, q) * (binom(2*s, R-2*q) - binom(2*s, R-2*q-1))
        for q in range(h+1)
    )


def normalized_poly_certificate(expr, lower):
    numer, denom = sp.fraction(sp.factor(expr))
    # Both polynomial signs should agree at the positive basepoint.
    pn = sp.Poly(sp.expand(numer.subs(r, u+lower)), u)
    pd = sp.Poly(sp.expand(denom.subs(r, u+lower)), u)
    nc = [int(c) for c in reversed(pn.all_coeffs())]
    dc = [int(c) for c in reversed(pd.all_coeffs())]
    if nc[0] < 0 and dc[0] < 0:
        nc = [-x for x in nc]
        dc = [-x for x in dc]
    assert all(x > 0 for x in nc), ('numerator sign failure', lower, expr)
    assert all(x > 0 for x in dc), ('denominator sign failure', lower, expr)
    return nc, dc


def main():
    R = [ratio(h) for h in range(9)]
    for h, f in enumerate(R):
        assert sp.limit(f / r**h, r, sp.oo) == 1/sp.factorial(h)
    independent_raw_checks = 0
    for R0 in (9, 99, 343):
        cat = binom(2*R0, R0) // (R0+1)
        for h in range(min(8, R0-2)+1):
            assert sp.Rational(raw_H(R0, h), cat) == R[h].subs(r, R0)
            independent_raw_checks += 1

    results = []
    for L, lower in ((6, 9), (8, 99)):
        section_start = len(results)
        for m in (1, 2, 3):
            for J in combinations(range(L+1), m):
                matrix = sp.Matrix([
                    [R[j-i] if j >= i else 0 for j in J]
                    for i in range(m)
                ])
                det = sp.factor(matrix.det(method='domain-ge'))
                nc, dc = normalized_poly_certificate(det, lower)
                results.append({
                    'width': L, 'lower_r': lower,
                    'order': m, 'columns': list(J),
                    'numerator_ascending_coefficients': nc,
                    'denominator_ascending_coefficients': dc,
                })
        expected = sum(binom(L+1, m) for m in (1,2,3))
        assert len(results)-section_start == expected
        print('WIDTH_PASS', 'L=',L,'r>=',lower,'determinants=',expected)

    payload = {
        'schema': 'R446_EXACT_RATIONAL_SHIFT_CERTIFICATE_V1',
        'model': 'signed BRC auxiliary scalar Toeplitz; not native X6',
        'arithmetic': 'sympy exact integer/rational polynomial calculations',
        'ratio_basis': 'H(r,r-h)/Catalan(r), no gcd normalization',
        'asymptotic_leading_coefficients': [str(1/sp.factorial(h)) for h in range(9)],
        'raw_coefficient_crosschecks': independent_raw_checks,
        'certificates': results,
    }
    content = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',',':'))+'\n'
    target = Path(__file__).with_name('R446_CERTIFICATES.json')
    target.write_text(content, encoding='utf-8')
    digest = hashlib.sha256(content.encode('utf-8')).hexdigest()
    print('R446_PASS', 'certificates=',len(results),
          'raw_checks=',independent_raw_checks,
          'sha256=',digest,'json_bytes=',len(content.encode('utf-8')))


if __name__ == '__main__':
    main()
