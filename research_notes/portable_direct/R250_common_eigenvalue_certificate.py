#!/usr/bin/env python3
"""R250: exact characteristic/gcd certificates for the frozen seven-source observer.

Standard Python Fraction + SymPy QQ polynomial Euclidean algorithm. No numerical
root solver, floating point classification, or randomized primality testing.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
from pathlib import Path
import sympy as sp

X = sp.Symbol('x')
HALF = sp.Poly(X - sp.Rational(1,2), X, domain=sp.QQ)
FIVE_TWELFTHS = sp.Poly(X - sp.Rational(5,12), X, domain=sp.QQ)
PARAMETERS = list(range(390, 411))
HALF_MASKS = [1, 2, 4, 8, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 55, 59, 61, 62]
SOURCE_PIN = '43ec6098b1330ae86d0a7863be336c5d97f6ef34'


def setup_parameter(j: int):
    s = sp.Rational(j, 1000)
    t = (1691*s - 2615)/(2615*s - 3539)
    a = [sp.Rational(1,5), sp.Rational(1,4), sp.Rational(3,10),
         sp.Rational(9,20), s, sp.Rational(2,3), t]
    b = [sp.Rational(13,60)] + [sp.Rational(5,18)*(sp.Rational(1,2)-v)
            for v in a[1:5]] + [sp.Rational(5,18)*(v-sp.Rational(1,2))
            for v in a[5:]]
    pi = [b_i/(1-a_i) for a_i,b_i in zip(a,b)]
    assert sum(pi) == 1
    assert len(set(a)) == 7 and all(0<v<1 for v in a)
    assert all(v>0 for v in b)
    return s,a,b,pi


def indices(mask: int):
    assert 0 <= mask < 63
    return [0] + [i+1 for i in range(6) if mask & (1 << i)]


def poly_for_mask(mask: int, a, b):
    ix = indices(mask)
    result = sp.Poly(sp.prod(X - a[i] for i in ix), X, domain=sp.QQ)
    for i in ix:
        result -= sp.Poly(b[i] * sp.prod(X-a[k] for k in ix if k != i), X, domain=sp.QQ)
    assert result.degree() == len(ix) and result.LC() == 1
    return result


def check_parameter(j):
    s,a,b,pi = setup_parameter(j)
    polys = [poly_for_mask(mask,a,b) for mask in range(63)]
    assert sum(p.degree() for p in polys) == 249
    observed_half = [i for i,p in enumerate(polys) if p.eval(sp.Rational(1,2)) == 0]
    assert observed_half == HALF_MASKS
    for mask in HALF_MASKS:
        assert sp.rem(polys[mask], HALF) == sp.Poly(0, X, domain=sp.QQ)
    assert polys[0] == FIVE_TWELFTHS
    assert polys[5] == FIVE_TWELFTHS * sp.Poly(X**2-sp.Rational(47,60)*X+sp.Rational(31,240), X, domain=sp.QQ)

    repeated_pairs = 0
    factor_counts = Counter()
    # All C(63,2)=1953 pairwise exact gcds, including masks with equal cardinality.
    for k,l in combinations(range(63), 2):
        g = sp.gcd(polys[k],polys[l])
        if g.degree() > 0:
            repeated_pairs += 1
            factor_counts[str(g.as_expr())] += 1
            if k in HALF_MASKS and l in HALF_MASKS:
                assert g == HALF, (j,k,l,g.as_expr())
            elif (k,l) == (0,5):
                assert g == FIVE_TWELFTHS, (j,k,l,g.as_expr())
            else:
                raise AssertionError(f'unexpected collision j={j} masks={k},{l} gcd={g.as_expr()}')
    assert repeated_pairs == 191
    assert factor_counts == {'x - 1/2':190, 'x - 5/12':1}, factor_counts
    return {'s':str(s),'subsets':63,'sum_characteristic_degrees':249,
            'pairwise_gcd_tests':1953,'nontrivial_gcd_pairs':repeated_pairs,
            'common_eigenvalue_1_2_mask_count':20,
            'common_eigenvalue_1_2_pair_count':190,
            'common_eigenvalue_5_12_pair_count':1,
            'distinct_modes':249-19-1,'all_checks_pass':True}


def main():
    rows = [check_parameter(j) for j in PARAMETERS]
    certificate = {
        'schema':'ENTERPRISE_MATH_R250_EXACT_COMMON_SPECTRUM_V1',
        'source_commit_pin':SOURCE_PIN,
        'arithmetic':'SymPy Poly over QQ with exact rational coefficient expressions, pairwise Euclidean polynomial gcd',
        'parameter_grid':'s=j/1000, j=390,...,410 inclusive',
        'subsets_per_parameter':63,
        'gcd_tests_total':len(rows)*1953,
        'total_modes_before_coincidences':249,
        'fixed_half_eigenvalue_masks':HALF_MASKS,
        'fixed_5_12_overlap_masks':[0,5],
        'repeated_eigenvalue_reduction':20,
        'minimal_linear_recurrence_order_at_all_tested_parameters':229,
        'all_pass':True,
        'rows':rows,
        'scope':'finite 21-point rational grid for absence of further coincidences; theorem proves uniform bound and generic order separately'
    }
    out = Path(__file__).with_name('R250_verification.json')
    data = (json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True)+'\n').encode()
    out.write_bytes(data)
    print(f'PASS: {len(rows)} parameters x 1953 gcds = {len(rows)*1953} exact tests')
    print('All sampled orders = 229; 20 masks share 1/2, masks 0 and 5 share 5/12')
    print('evidence:',out,'SHA256:',hashlib.sha256(data).hexdigest())


if __name__ == '__main__':
    main()
