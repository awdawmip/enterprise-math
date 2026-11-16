#!/usr/bin/env python3
"""R749SSN exact arithmetic certificate. Requires Python 3 and SymPy.

No floating point arithmetic is used in any logical assertion. Reconstructs
source counts from the frozen five labelled weights (1,1,2,3,6). The
six residue-class quasipolynomials are justified independently by their
rational generating functions; interpolation merely recovers coefficients.
"""
import json
from fractions import Fraction
from sympy import Poly, Rational, Symbol, expand, interpolate

WEIGHTS = (1, 1, 2, 3, 6)
ORIENTATION = (1, -1, -1, 1, 1, -1)  # +1: Y(q) higher, -1: Y(q+1) higher
GAP = Rational(1423720838927976185, 53569280690597608884)
n = Symbol('n', integer=True)
t = Symbol('t', integer=True)


def source_counts(max_weight):
    exact = [0] * (max_weight + 1)
    moment = [0] * (max_weight + 1)
    exact[0] = 1
    for i, w in enumerate(WEIGHTS):
        for j in range(w, max_weight + 1):
            old = exact[j - w]
            exact[j] += old
            moment[j] += moment[j - w] + (old if i == 0 else 0)
    C = [0] * (max_weight + 2)
    T = [0] * (max_weight + 2)
    for q in range(1, max_weight + 2):
        C[q] = C[q - 1] + exact[q - 1]
        T[q] = T[q - 1] + moment[q - 1]
    return C, T


def smooth(q):
    return 18*q**4 + 54*q**3 - 345*q**2 + 2070*q - 16315


def ratio_y(q, e, d, C, T):
    return Rational(q**3)*(T[q] + e)/(C[q] + d) - Rational(smooth(q), 108)


def bounds(q, C, T):
    return ratio_y(q, -2, 2, C, T), ratio_y(q, 2, -2, C, T)


def poly_pair(C, T):
    Cp, Tp = {}, {}
    for r in range(6):
        Cp[r] = expand(interpolate([(i, C[6*i+r]) for i in range(1, 7)], n))
        Tp[r] = expand(interpolate([(i, T[6*i+r]) for i in range(1, 8)], n))
        assert Poly(Cp[r], n).degree() == 5
        assert Poly(Tp[r], n).degree() == 6
        for i in range(8, 16):
            assert Cp[r].subs(n, i) == C[6*i+r]
            assert Tp[r].subs(n, i) == T[6*i+r]
    return Cp, Tp


def prove():
    C, T = source_counts(540)
    Cp, Tp = poly_pair(C, T)
    # G_C(z) = z / ((1-z)^3 (1-z^2)(1-z^3)(1-z^6)),
    # G_T(z) = z^2 / ((1-z)^4 (1-z^2)(1-z^3)(1-z^6)).
    # All poles have order <=6 and <=7 respectively and are sixth roots
    # of unity. Thus C(6n+r) and T(6n+r) are polynomials in n of degree
    # <=5 and <=6, for every integer n>=1. Interpolation is exact.
    records = []
    for r in range(6):
        q, p = 6*n+r, 6*n+r+1
        c, v = Cp[r], Tp[r]
        pn = n + (1 if r == 5 else 0)
        cp, vp = Cp[(r+1) % 6].subs(n, pn), Tp[(r+1) % 6].subs(n, pn)
        if ORIENTATION[r] == 1:
            den = (c+2)*(cp-2)
            numerator = 108*q**3*(v-2)*(cp-2) - 108*p**3*(vp+2)*(c+2) \
                - (smooth(q)-smooth(p))*(c+2)*(cp-2)
        else:
            den = (c-2)*(cp+2)
            numerator = 108*p**3*(vp-2)*(c-2) - 108*q**3*(v+2)*(cp+2) \
                - (smooth(p)-smooth(q))*(cp+2)*(c-2)
        # gap = numerator / (108*den). A certified lower bound GAP
        # is equivalent to numerator-108*GAP*den >=0.
        check_poly = Poly(expand((numerator-108*GAP*den).subs(n, t+84)), t)
        assert check_poly.degree() == 10
        ascending = list(reversed(check_poly.all_coeffs()))
        assert all(v >= 0 for v in ascending)
        if r == 2:
            assert ascending[0] == 0 and all(v > 0 for v in ascending[1:])
        else:
            assert all(v > 0 for v in ascending)
        # Also verify the exact polynomial identities against computed
        # count moments at two arbitrarily chosen admissible integers.
        for i in (84, 88):
            qi = 6*i+r
            lo, hi = bounds(qi, C, T)
            lop, hip = bounds(qi+1, C, T)
            actual = lo-hip if ORIENTATION[r] == 1 else lop-hi
            assert actual == numerator.subs(n,i)/(108*den.subs(n,i))
        records.append({
            'residue': r,
            'higher_cutoff': 'q' if ORIENTATION[r] == 1 else 'q+1',
            'shift': 'n=t+84',
            'shifted_gap_polynomial_degree': int(check_poly.degree()),
            'coefficient_signs_ascending': ''.join('0' if v==0 else '+' for v in ascending),
            'constant_coefficient': str(ascending[0]),
            'leading_coefficient': str(ascending[-1]),
        })
    # Exactly three positions before the uniform n>=84 tail.
    for q in (501, 502, 503):
        lo, hi = bounds(q, C, T)
        lop, hip = bounds(q+1, C, T)
        actual = lo-hip if ORIENTATION[q % 6] == 1 else lop-hi
        assert actual > GAP
    lo506, hi506 = bounds(506, C, T)
    lo507, hi507 = bounds(507, C, T)
    assert lo507-hi506 == GAP  # attained; optimal uniform gap
    # q=500 is a genuine one-read collision, not merely intervals meeting.
    lo500, hi500 = bounds(500, C, T)
    lo501, hi501 = bounds(501, C, T)
    assert lo501 < hi500
    Y = (lo501+hi500)/2
    e500 = (Y+Rational(smooth(500),108))*(C[500]-2)/500**3-T[500]
    e501 = (Y+Rational(smooth(501),108))*(C[501]+2)/501**3-T[501]
    assert -2 < e500 < 2 and -2 < e501 < 2
    assert ratio_y(500,e500,-2,C,T) == Y
    assert ratio_y(501,e501,2,C,T) == Y
    return {
        'research': 'R749SSN',
        'status': 'AUTHOR_EXACT_NOT_REVIEWED',
        'frozen_scientific_pin': 'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'model': {'weights': list(WEIGHTS), 'error_interval': '[-2,2] each real e,d',
                  'observer': 'Y_q=q^3(T_q+e)/(C_q+d)-S(q)/108'},
        'theorem': {'adjacent_cutoff_first_uniform_separation_q': 501,
                    'minimum_gap_numerator': str(GAP.p),
                    'minimum_gap_denominator': str(GAP.q),
                    'attained_at': [506,507],
                    'optimal_nearest_set_noise_radius': str(GAP/2)},
        'counterexample_at_500': {
            'common_observation': str(Y),
            'cutoff_500': {'e': str(e500), 'd': '-2'},
            'cutoff_501': {'e': str(e501), 'd': '2'}},
        'polynomial_certificates': records,
        'proof': '6 quasipolynomial residue classes; 66 nonnegative exact shifted coefficients; finite 501..503 checks, exact 500 collision',
        'checks': 'PASS'
    }


if __name__ == '__main__':
    print(json.dumps(prove(), ensure_ascii=False, indent=2))
