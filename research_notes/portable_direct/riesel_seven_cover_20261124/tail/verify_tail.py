#!/usr/bin/env python3
"""All three-prime completions of the fixed R2 four-prime prefix.

The all-prime reduction is proved in proof.md. This small exact calculator
checks its arithmetic inputs, reduced phase cases, all 146 dictionaries,
and their sign-specific CRT starts. It is not independent project Review.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = {7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417}
PREFIX = {5, 13, 19, 73}
INACTIVE = {3, 11, 37, 61, 109, 331, 433}
B = {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}
D = (87211, 246241, 262657, 279073)
C = (181, 631, 23311, 54001, 18837001, 29247661)
E = (577, 487824887233)
ORDERS = {87211: 54, 246241: 108, 262657: 27, 279073: 108,
          181: 180, 631: 45, 23311: 45, 54001: 180,
          18837001: 90, 29247661: 180, 577: 144,
          487824887233: 144, 38737: 72}
FACTORS = {
    108: {3: 4, 5: 1, 7: 1, 13: 1, 19: 1, 37: 1, 73: 1,
          109: 1, 262657: 1, 87211: 1, 246241: 1, 279073: 1},
    144: {3: 3, 5: 1, 7: 1, 13: 1, 17: 1, 19: 1, 37: 1,
          73: 1, 97: 1, 109: 1, 241: 1, 257: 1, 433: 1,
          577: 1, 673: 1, 38737: 1, 487824887233: 1},
    180: {3: 3, 5: 2, 7: 1, 11: 1, 13: 1, 19: 1, 31: 1,
          37: 1, 41: 1, 61: 1, 73: 1, 109: 1, 151: 1,
          181: 1, 331: 1, 631: 1, 1321: 1, 23311: 1,
          54001: 1, 18837001: 1, 29247661: 1},
}
A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
L = 80754838636615
BASE = 9807947978443488306255509703402695727949968778703073231931137913705883712843
BASE_STEP = 11356718000553566643685496313583434507970452519839503606327232707476034989690


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def prime_factors(n):
    out, p = [], 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
        while n % p == 0:
            n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def exact_order(base, q, d):
    return pow(base, d, q) == 1 and all(
        pow(base, d // p, q) != 1 for p in prime_factors(d))


def crt(pairs):
    a, m = 0, 1
    for r, q in pairs:
        assert gcd(m, q) == 1
        a += m*((r-a)*pow(m, -1, q) % q)
        m *= q
    return a, m


def root_pair(q, c):
    r = pow(pow(2, c, q), -1, q)
    return sorted((r, q-r))


def complete(rows):
    period = lcm(35, *(h for h, _ in rows))
    holes = [w for w in range(period) if w % 35 in B]
    return all(any(w % h == b for h, b in rows) for w in holes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE/'tail_certificate.json')
    args = parser.parse_args()
    assert prod(P) == M
    base, step = crt([(A_STAR, 6*M), (12926327728523, L),
                      (0, 433), (38733, 38737)])
    assert (base, step) == (BASE, BASE_STEP)
    assert (BASE * BASE * pow(2, 32 + 36, 38737)) % 38737 == 1
    assert (BASE * BASE * pow(2, 32, 38737)) % 38737 != 1

    # Exact products plus deterministic primality establish complete factors.
    for exponent, factors in FACTORS.items():
        assert prod(q**e for q, e in factors.items()) == 2**exponent-1
    checked_primes = sorted(set().union(*(set(fs) for fs in FACTORS.values())))
    assert all(prime(q) for q in checked_primes)
    for q, order in ORDERS.items():
        assert exact_order(2, q, order)
    excluded = P | PREFIX | INACTIVE
    h1 = sorted(q for q in FACTORS[144] if pow(2, 36, q) == 1)
    assert set(h1) <= excluded
    h2 = sorted(q for q in FACTORS[144] if exact_order(2**36, q, 2))
    assert set(h2) - excluded == {38737}
    e1 = sorted(q for q in FACTORS[144] if pow(2, 72, q) == 1)
    assert set(e1) <= excluded | {38737}
    binary = sorted(q for q in FACTORS[144]
                    if q not in excluded | {38737}
                    and exact_order(2**72, q, 2))
    ternary = sorted(q for q in FACTORS[108]
                     if q not in excluded | {38737}
                     and exact_order(2**36, q, 3))
    mod5 = sorted(q for q in FACTORS[180]
                  if q not in excluded | {38737}
                  and exact_order(2**36, q, 5))
    assert tuple(binary) == E and tuple(ternary) == D and tuple(mod5) == C

    incidences = {g: [sum(b % g == c for b in B) for c in range(g)]
                  for g in (1, 5, 7, 35)}
    assert [max(incidences[g]) for g in incidences] == [13, 5, 3, 1]
    assert incidences[5] == [5, 3, 0, 5, 0]
    assert [b for b in sorted(B) if b % 5 == 1] == [21, 26, 31]
    assert len({b % 7 for b in B if b % 5 == 1}) == 3
    assert 1-2*Fraction(5, 13) == Fraction(3, 13)
    assert Fraction(1, 4)+Fraction(5, 13)+Fraction(1, 3) == Fraction(151, 156) < 1
    assert Fraction(3, 13)+2*Fraction(5, 13) == 1

    # The proof first confines all primes to these effective periods.
    # This finite arithmetic check retains overlap, including all lifts.
    reduced_rows = [(h, b) for h in (3, 4, 5, 7) for b in range(h)]
    reduced_covers = [rows for rows in combinations_with_replacement(reduced_rows, 3)
                      if complete(rows)]
    assert reduced_covers == [((3, 0), (3, 1), (3, 2)),
                              ((5, 0), (5, 1), (5, 3))]
    assert [b for b in range(4) if complete([(2, 1), (4, 0), (4, b)])] == [2]

    families = {'binary': (E, (0, 2), 4),
                'ternary': (D, (0, 1, 2), 3),
                'modulo_five': (C, (0, 1, 3), 5)}
    phase_table = {}
    results = {}
    total_dicts = total_starts = 0
    for name, (primes, categories, h) in families.items():
        for q in primes:
            assert gcd(q, BASE_STEP) == 1
            order = ORDERS[q]
            d = order // gcd(order, 2)
            phase_table[q] = {}
            assert order // gcd(order, 36) == h
            for b in categories:
                c = (16 + 18*b) % d
                roots = root_pair(q, c)
                assert all((r*r*pow(2, 32+36*b, q)) % q == 1 for r in roots)
                phase_table[q][b] = {'period_w': h, 'phase_w': b,
                                    'period_u': d, 'phase_u': c,
                                    'root_residues': roots}
            assert len({r for row in phase_table[q].values()
                        for r in row['root_residues']}) == 2*len(categories)
        dictionaries = []
        minimum = None
        starts = 0
        for chosen in permutations(primes, len(categories)):
            rows = [(h, b) for b in categories]
            if name == 'binary':
                rows += [(2, 1)]
            assert complete(rows)
            period = lcm(35, *(f for f, _ in rows))
            holes = [w for w in range(period) if w % 35 in B]
            private = [sum(w % f == b and all(w % f2 != b2
                       for j, (f2, b2) in enumerate(rows) if j != i)
                       for w in holes) for i, (f, b) in enumerate(rows)]
            assert all(private)
            pattern = {'phase_to_prime': dict(zip(map(str, categories), chosen)),
                       'private_B_points_in_complete_w_period': private}
            dictionaries.append(pattern)
            for residues in product(*(phase_table[q][b]['root_residues']
                                      for q, b in zip(chosen, categories))):
                starts += 1
                a, modulus = crt([(BASE, BASE_STEP)]+list(zip(residues, chosen)))
                assert a > 0 and a % BASE_STEP == BASE
                assert 2*a*a-1 > max(P | PREFIX | set(chosen) | {38737})
                if minimum is None or a < minimum['root']:
                    minimum = {'root': a, 'root_digits': len(str(a)),
                               'phase_to_prime': pattern['phase_to_prime'],
                               'root_residues': dict(zip(chosen, residues)),
                               'progression_modulus': str(modulus)}
        minimum['root'] = str(minimum['root'])
        total_dicts += len(dictionaries)
        total_starts += starts
        results[name] = {'candidate_primes': primes, 'w_phases': categories,
                         'effective_w_order': h,
                         'fixed_extra_channel': {'prime': 38737, 'phase_w': 1,
                                                 'period_w': 2} if name == 'binary' else None,
                         'complete_w_period': period,
                         'complete_exponent_coverage_period': 36*period,
                         'phase_dictionaries': len(dictionaries),
                         'CRT_progression_starts': starts,
                         'dictionaries': dictionaries, 'minimum': minimum}
    assert [results[k]['phase_dictionaries'] for k in families] == [2, 24, 120]
    assert [results[k]['CRT_progression_starts'] for k in families] == [8, 192, 960]
    assert (total_dicts, total_starts) == (146, 1160)
    overall_minimum = min((v['minimum'] for v in results.values()),
                          key=lambda x: int(x['root']))
    result = {
        'schema': 'riesel-r2-all-three-prime-tail-classification-v1',
        'status': 'AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW',
        'scope': 'All prime completions of the fixed prefix 5,13,19,73 inside R2; no numerical prime cutoff.',
        'researcher': 'EM-DIRECT-970E1C', 'activity': 'RA-D2EC212845B63844081F9A14',
        'source_dependency': {'commit': 'f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5',
            'path': 'research_notes/portable_direct/riesel_finite_observers_20261124/six/r2_proof.md',
            'scope': 'R2 fixed coordinates, old-hole reduction, incidence formula, sharp six-budget lower bound.'},
        'R2': {'base_root': str(BASE), 'progression_modulus': str(BASE_STEP)},
        'B_mod35': sorted(B), 'u_coordinate': 'u=16+18w', 'n_coordinate': 'n=32+36w',
        'incidence_counts': incidences, 'complete_factorizations': FACTORS,
        'verified_prime_factors': checked_primes, 'base2_orders': ORDERS,
        'effective_order1_primes': h1, 'effective_order2_primes': h2,
        'binary_restricted_order1_primes': e1,
        'all_prime_reduction_without_38737': {'individual_minimum': '3/13',
            'possible_effective_orders': [3, 4, 5, 7],
            'complete_reduced_covers': reduced_covers},
        'phase_root_table': phase_table, 'families': results,
        'total_phase_dictionaries': total_dicts, 'total_CRT_progression_starts': total_starts,
        'minimum_conditional_on_fixed_prefix': overall_minimum,
        'native_semantics': 'Fixed X6; positive singleton BRC weight and multiplicity one; integer state and joint cofactors retained; prime phases are observations, not axes.',
        'review_boundary': 'Arithmetic evidence supplements the analytic all-prime proof; no independent Review, native execution or Foundation promotion claimed.'}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'phase_dictionaries': total_dicts, 'CRT_starts': total_starts,
                      'family_minima': {k: v['minimum']['root'] for k, v in results.items()},
                      'output': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
