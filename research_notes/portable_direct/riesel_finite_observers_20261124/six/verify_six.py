#!/usr/bin/env python3
"""Exact supporting arithmetic for the all-six classification on R1.

The all-prime necessity proof is in proof.md. Previous complete factorizations,
the eight-class minimum, and native execution are reused at their stated scopes.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
V9_COMMIT = 'b1de1acbdc97b5e51d486127abd1fadd24babd99'
V9_REL = Path('research_notes/portable_direct/riesel_five_cover_20261123')


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def factor(n):
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0)+1
    return factors


def exact_order(base, q, d):
    return pow(base, d, q) == 1 and all(
        pow(base, d//p, q) != 1 for p in factor(d))


def locate_prior(explicit):
    if explicit:
        path = Path(explicit)
        assert (path/'global/global_certificate.json').is_file()
        return path
    for parent in HERE.parents:
        path = parent/V9_REL
        if (path/'global/global_certificate.json').is_file():
            return path
    raise FileNotFoundError('Pass --prior-dir for the retained round-nine directory.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior-dir')
    parser.add_argument('--output', type=Path, default=HERE/'six_certificate.json')
    args = parser.parse_args()
    prior = locate_prior(args.prior_dir)
    old = json.loads((prior/'global/global_certificate.json').read_text())
    fiber = json.loads((prior/'fiber/fiber_certificate.json').read_text())
    P, H = set(old['P']), set(old['H'])
    assert len(P) == 20 and len(H) == 36
    U, W = {11, 61, 331}, {19, 37, 73, 109}
    inactive = {3, 11, 61, 331, 37, 109}
    fixed = {5: (2, 1), 13: (6, 0), 19: (9, 4), 73: (9, 1)}
    R1 = fiber['R1']
    assert R1['observer_residue'] == 12926327728523
    assert R1['W_residues'] == {'19': 6, '37': 0, '73': 37, '109': 0}

    # A new complete factorization needed by the sharper parity bound.
    f28 = factor(2**28-1)
    assert f28 == {3: 1, 5: 1, 29: 1, 43: 1, 113: 1, 127: 1}
    assert all(is_prime(q) for q in f28)
    e7 = sorted(q for q in f28 if q not in P | {3, 5, 13}
                and exact_order(16, q, 7))
    assert e7 == [29, 43]

    inherited_factors = {int(n): {int(q): e for q, e in row.items()}
                        for n, row in old['complete_factorizations'].items()}
    e9 = sorted(q for q in inherited_factors[36]
                if q not in P | {3, 5, 13} and exact_order(16, q, 9))
    assert e9 == [19, 37, 73, 109]
    # The inherited exclusion of e<=6, reconstructed at these small values.
    excluded_small = P | {3, 5, 11, 13}
    small_parity_factors = {e: factor(2**(4*e)-1) for e in range(1, 7)}
    assert all(set(row) <= excluded_small for row in small_parity_factors.values())

    parity_counts = []
    for epsilon in (0, 1):
        points = [u for u in range(630) if u % 105 in H and u % 2 == epsilon]
        assert len(points) == 108
        hits = {q: sum(u % d == c for u in points)
                for q, (d, c) in fixed.items() if q in (19, 73)}
        assert hits == {19: 13, 73: 13}
        parity_counts.append({'parity_u': epsilon, 'old_holes': 108,
                              'fixed_channel_hits': hits})

    assert all(Fraction(v) <= Fraction(1, 9)
               for v in old['global_bulk_density_bounds'])
    no_basic = Fraction(21+13+13+12+12+12, 108)
    one_basic = 2*Fraction(7, 36)+3*Fraction(1, 6)
    parity_bulk = [Fraction(1, 8), Fraction(23, 144), Fraction(11, 72),
                   Fraction(7, 72), Fraction(1, 6), Fraction(1, 9),
                   Fraction(1, 18), Fraction(1, 36)]
    assert no_basic == Fraction(83, 108) < 1
    assert one_basic == Fraction(8, 9) < 1
    assert max(parity_bulk) == Fraction(1, 6)
    assert Fraction(13, 108) < Fraction(1, 6)

    A = {v for v in range(35) if (4+6*v) % 105 in H}
    assert A == {1, 2, 10, 11, 12, 16, 17, 22, 25, 26, 30, 31, 32}
    maxima = {g: max(sum(v % g == c for v in A) for c in range(g))
              for g in (1, 5, 7, 35)}
    assert maxima == {1: 13, 5: 5, 7: 3, 35: 1}
    threshold = 1-Fraction(1, 3)-2*Fraction(3, 13)
    assert threshold == Fraction(8, 39)
    assert max(Fraction(1, 6), Fraction(5, 26), Fraction(1, 13)) < threshold
    assert Fraction(3, 26) < threshold <= Fraction(3, 13)
    f7 = sorted(q for q in inherited_factors[84]
                if q not in P | {3, 5, 13} and exact_order(2**12, q, 7))
    assert f7 == [29, 43, 1429, 5419]
    one_W_bound = Fraction(1, 3)+Fraction(2, 3)*Fraction(9, 13)
    assert one_W_bound == Fraction(31, 39) < 1

    f72 = {int(q): e for q, e in
           fiber['complete_factorizations_of_2_power_minus_1']['72'].items()}
    final_candidates = sorted(q for q in f72
        if q not in P | inactive | set(fixed) and exact_order(2**36, q, 2))
    assert final_candidates == [433, 38737]
    assert all(exact_order(2, q, 72) for q in final_candidates)
    assert 2**36+1 == 17*241*433*38737

    patterns = []
    for phase433, phase38737 in ((16, 34), (34, 16)):
        rows = list(fixed.items())+[(433, (36, phase433)), (38737, (36, phase38737))]
        period = lcm(105, *(d for _, (d, _) in rows))
        assert period == 1260
        old_holes = [u for u in range(1, period+1) if u % 105 in H]
        private = {}
        for u in old_holes:
            hits = [q for q, (d, c) in rows if u % d == c]
            assert hits
            if len(hits) == 1:
                private.setdefault(hits[0], 2*u)
        assert set(private) == {5, 13, 19, 73, 433, 38737}
        roots = {}
        for q, (d, c) in rows:
            r = pow(pow(2, c, q), -1, q)
            roots[q] = sorted((r, q-r))
            assert all(a*a*pow(4, c, q) % q == 1 for a in roots[q])
        patterns.append({'rows': [{'prime': q, 'period_u': d, 'phase_u': c,
                                  'root_residues': roots[q]}
                                 for q, (d, c) in rows],
                         'complete_period_u': period,
                         'private_old_hole_n': private})

    # Scope promotion of an unchanged, previously complete CRT calculation.
    old_min = R1['compact_minimum_nested6_witness']
    assert old_min['root_decimal'] == '1597463687996365290740241630260436015028835427889255944107518938773290244463'
    assert len(R1['nested6_CRT_classes']) == 8
    result = {
        'schema': 'riesel-r1-complete-six-classification-v1',
        'status': 'AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW',
        'scope': 'All complete supplements of at most six distinct new primes for every positive root in the fixed R1 fiber; no prime-size or order cutoff.',
        'source_dependency': {'commit': V9_COMMIT, 'path': str(V9_REL),
                              'scope': 'Old holes, all-prime incidence bounds, complete earlier small factorizations, R1 trajectory and nested-six calculation.'},
        'new_complete_factorization_2_28_minus_1': f28,
        'small_parity_order_exclusions': small_parity_factors,
        'parity_effective_order_7_candidates': e7,
        'parity_effective_order_9_candidates': e9,
        'fixed_phase_counts_inside_both_parities': parity_counts,
        'new_strict_bounds': {'no_basic_primes': str(no_basic),
                              'exactly_one_basic_prime': str(one_basic),
                              'parity_generic_cap': str(max(parity_bulk)),
                              'one_W_each_other_required': str(threshold),
                              'one_W_after_order_7_forcing': str(one_W_bound)},
        'A_incidence_maxima': maxima,
        'forced_order_7_candidates_in_one_W_case': f7,
        'final_binary_candidates': final_candidates,
        'complete_prime_set': [5, 13, 19, 73, 433, 38737],
        'complete_phase_dictionary_count': 2,
        'complete_phase_dictionaries': patterns,
        'all_roots_delta_lower_bound': 6,
        'complete_delta6_observer': {'modulus': R1['relative_predicate_period_Z'],
                                    'true_root_classes': R1['nested6_CRT_classes'],
                                    'class_count': 8,
                                    'relative_density': '8/16773121',
                                    'least_additive_period': 16773121},
        'reused_minimum': {'root_decimal': old_min['root_decimal'],
                           'root_decimal_digits': old_min['root_decimal_digits'],
                           'new_scope': 'Least positive root among all delta_P=6 roots in R1.',
                           'old_scope': old_min['minimum_scope'],
                           'calculation_status': 'REUSED_V9_COMPLETE_EIGHT_CLASS_CALCULATION',
                           'native_execution_status': 'REUSED_V9_NATIVE_EXECUTION',
                           'total_cost_upper_bound': 26,
                           'exact_total_cost_claimed': False},
        'logical_role': 'The written all-prime necessity proof establishes exhaustiveness. This calculation checks its new exact arithmetic and final phase coverage; unchanged prior CRT and native results are reused.'
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'phase_dictionaries': 2,
                      'complete_delta6_root_classes': 8,
                      'least_period': 16773121, 'output': str(args.output)}))


if __name__ == '__main__':
    main()
