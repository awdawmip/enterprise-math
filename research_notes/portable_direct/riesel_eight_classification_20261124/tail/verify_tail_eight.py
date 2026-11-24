#!/usr/bin/env python3
"""All four-prime tails in R3 conditional on the four-prime prefix.

The analytic all-prime reduction is in proof.md.  This standard-library
calculator verifies its complete prime inventories, reduced covers, every
phase dictionary and root category.  It does not classify eight-prime covers
that omit 19 or 73.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path

P = {7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417}
PREFIX = {5, 13, 19, 73}
B = {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}
BZ = {18*b % 35 for b in B}
INACTIVE = {3, 11, 37, 61, 109, 331, 433, 181, 577, 631, 23311, 54001,
            87211, 262657, 279073, 18837001, 29247661}
FIXED_ACTIVE_TAIL = {38737: (2, 1), 246241: (3, 1), 487824887233: (4, 2)}
FAMILIES = {
    'binary': {'primes': (193, 1153, 6337, 22253377, 38941695937, 278452876033),
               'w_period': 8, 'phases': (0, 4), 'fixed': ((38737, 2, 1), (487824887233, 4, 2))},
    'ternary': {'primes': (33975937, 138991501037953),
                'w_period': 6, 'phases': (0, 2), 'fixed': ((38737, 2, 1), (246241, 3, 1))},
    'modulo_five': {'primes': (61681, 4562284561, 168692292721, 469775495062434961),
                    'w_period': 10, 'phases': (0, 6, 8), 'fixed': ((38737, 2, 1),)},
}
ORDERS = {193: 96, 1153: 288, 6337: 288, 22253377: 96, 38941695937: 288,
          278452876033: 288, 33975937: 216, 138991501037953: 216,
          61681: 40, 4562284561: 120, 168692292721: 360, 469775495062434961: 360}
FACTORS = {
    216: {3:4,5:1,7:1,13:1,17:1,19:1,37:1,73:1,109:1,241:1,433:1,38737:1,
          87211:1,246241:1,262657:1,279073:1,33975937:1,138991501037953:1},
    288: {3:3,5:1,7:1,13:1,17:1,19:1,37:1,73:1,97:1,109:1,193:1,241:1,257:1,
          433:1,577:1,673:1,1153:1,6337:1,38737:1,65537:1,22253377:1,
          38941695937:1,278452876033:1,487824887233:1},
    360: {3:3,5:2,7:1,11:1,13:1,17:1,19:1,31:1,37:1,41:1,61:1,73:1,109:1,
          151:1,181:1,241:1,331:1,433:1,631:1,1321:1,23311:1,38737:1,54001:1,
          61681:1,18837001:1,29247661:1,4562284561:1,168692292721:1,469775495062434961:1},
}
LUCAS = {
    138991501037953: {'factorization': {2:7,3:3,79:1,509081623:1}, 'witness': 5},
    469775495062434961: {'factorization': {2:4,3:2,5:1,7:1,151:1,617280951149:1}, 'witness': 19},
}


def prime_trial(n: int) -> bool:
    if n < 2 or n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def prime_divisors(n: int) -> list[int]:
    factors, d = [], 2
    while d*d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def exact_order(base: int, q: int, order: int) -> bool:
    return pow(base, order, q) == 1 and all(pow(base, order//p, q) != 1 for p in prime_divisors(order))


def complete(rows: tuple[tuple[int, int], ...], holes: set[int]) -> bool:
    period = lcm(35, *(m for m, b in rows))
    return all(any(w % m == b for m, b in rows) for w in range(period) if w % 35 in holes)


def root_pair(q: int, phase: int) -> list[int]:
    root = pow(pow(2, 16+18*phase, q), -1, q)
    return sorted((root, q-root))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('tail_eight_certificate.json'))
    args = parser.parse_args()
    assert BZ == {0, 4, 5, 13, 14, 15, 19, 20, 25, 28, 29, 33, 34}
    all_factors = set().union(*(set(fs) for fs in FACTORS.values()))
    trial_set = (all_factors-set(LUCAS)) | set().union(*(set(item['factorization']) for item in LUCAS.values()))
    assert all(prime_trial(q) for q in trial_set)
    lucas_receipts = {}
    for q, item in LUCAS.items():
        factors, a = item['factorization'], item['witness']
        assert prod(p**e for p, e in factors.items()) == q-1
        assert pow(a, q-1, q) == 1
        checks = {p: gcd(pow(a, (q-1)//p, q)-1, q) for p in factors}
        assert all(g == 1 for g in checks.values())
        lucas_receipts[q] = {**item, 'fermat_remainder': 1, 'gcd_checks': checks}
    for exponent, factors in FACTORS.items():
        assert prod(q**e for q, e in factors.items()) == 2**exponent-1
    for q, order in ORDERS.items():
        assert exact_order(2, q, order)
    incidences = {g: [sum(b % g == c for b in BZ) for c in range(g)] for g in (1, 5, 7, 35)}
    assert [max(incidences[g]) for g in incidences] == [13, 5, 3, 1]
    assert incidences[5] == [5, 0, 0, 3, 5]
    remaining_after_max5 = [b for b in sorted(BZ) if b % 5 not in (0, 4)]
    assert remaining_after_max5 == [13, 28, 33]
    assert len({b % 7 for b in remaining_after_max5}) == 3

    # Small orders are checked against complete factor products, not a bound
    # on the size of searched primes.
    excluded = P | PREFIX | INACTIVE
    hw1 = [q for q in FACTORS[288] if pow(2, 36, q) == 1]
    hw2 = [q for q in FACTORS[288] if exact_order(2**36, q, 2)]
    hw3 = [q for q in FACTORS[216] if exact_order(2**36, q, 3)]
    hw4 = [q for q in FACTORS[288] if exact_order(2**36, q, 4)]
    hw5 = [q for q in FACTORS[360] if exact_order(2**36, q, 5)]
    assert set(hw1) <= excluded
    assert set(hw2)-excluded == {38737}
    assert set(hw3)-excluded == {246241}
    assert set(hw4)-excluded == {487824887233}
    assert set(hw5) <= excluded
    ze1 = [q for q in FACTORS[288] if pow(2, 72, q) == 1]
    ze2 = [q for q in FACTORS[288] if exact_order(2**72, q, 2)]
    ze3 = [q for q in FACTORS[216] if exact_order(2**72, q, 3)]
    ze4 = [q for q in FACTORS[288] if exact_order(2**72, q, 4)]
    ze5 = [q for q in FACTORS[360] if exact_order(2**72, q, 5)]
    assert set(ze1) <= excluded | {38737}
    assert set(ze2)-excluded == {487824887233}
    assert set(ze3)-excluded == {246241, 33975937, 138991501037953}
    assert set(ze4)-excluded == set(FAMILIES['binary']['primes'])
    assert set(ze5)-excluded == set(FAMILIES['modulo_five']['primes'])
    te2 = [q for q in FACTORS[288] if exact_order(2**144, q, 2)]
    assert set(te2)-excluded == set(FAMILIES['binary']['primes'])

    # Full-prime forcing bounds for the required 38737 row.
    bounds = {
        'no_38737_or_246241_or_487824887233': 4*Fraction(3,13),
        'only_487824887233': Fraction(1,4)+3*Fraction(3,13),
        '246241_and_487824887233': Fraction(1,2)+2*Fraction(3,13),
        'only_246241_and_one_generic_not_h7': Fraction(1,3)+2*Fraction(3,13)+Fraction(5,26),
        'period4_exclusion': Fraction(1,4)+Fraction(5,13)+Fraction(1,3),
    }
    assert all(value < 1 for value in bounds.values())
    fixed_union_period = lcm(35,3,4)
    original_holes = [w for w in range(fixed_union_period) if w % 35 in B]
    fixed_union = [w for w in original_holes if w%3 == 1 or w%4 == 2]
    assert Fraction(len(fixed_union), len(original_holes)) == Fraction(1,2)

    # The analytic reduction confines the remaining three classes to these
    # periods when the fixed period-two z observer is not selected.
    candidates = [(e,c) for e in (3,4,5,7) for c in range(e)]
    reduced_covers = [rows for rows in combinations_with_replacement(candidates,3) if complete(rows,BZ)]
    assert reduced_covers == [((3,0),(3,1),(3,2)), ((5,0),(5,3),(5,4))]

    families = {}
    total_dictionaries = total_signed_descriptions = 0
    phase_root_table = {}
    for name, family in FAMILIES.items():
        qs, phases, period = family['primes'], family['phases'], family['w_period']
        for q in qs:
            assert exact_order(2**36, q, period)
            phase_root_table[q] = {}
            for phase in phases:
                pair = root_pair(q,phase)
                assert all((a*a*pow(2,32+36*phase,q)-1)%q == 0 for a in pair)
                phase_root_table[q][phase] = pair
            assert len({r for pair in phase_root_table[q].values() for r in pair}) == 2*len(phases)
        dictionaries = []
        for selected in permutations(qs,len(phases)):
            rows = family['fixed'] + tuple((q,period,phase) for q,phase in zip(selected,phases))
            assert len(rows) == len({q for q,e,c in rows}) == 4
            assert complete(tuple((e,c) for q,e,c in rows),B)
            dictionaries.append({'rows': rows,
                                 'new_root_categories': {q: phase_root_table[q][phase] for q,phase in zip(selected,phases)}})
        count, signed = len(dictionaries), len(dictionaries)*2**len(phases)
        families[name] = {'candidate_primes': qs, 'w_period': period, 'phases': phases,
                          'phase_dictionary_count': count, 'signed_CRT_description_count': signed,
                          'phase_dictionaries': dictionaries}
        total_dictionaries += count
        total_signed_descriptions += signed
    assert [families[name]['phase_dictionary_count'] for name in FAMILIES] == [30,2,24]
    assert (total_dictionaries,total_signed_descriptions) == (56,320)
    certificate = {
        'schema': 'riesel-r3-eight-cover-four-prefix-tail-classification-v1',
        'scope': 'All complete at-most-eight-prime supplements in R3 containing 5,13,19,73',
        'full_eight_prime_classification_claimed': False,
        'fixed_root_fiber': 'The unchanged 43-prime R3 fiber of the v12 source',
        'native_semantics': 'Fixed-X6 typed integer register x -> 2x+1; residual observations preserve the full integer',
        'residual_B': sorted(B), 'even_coordinate_BZ': sorted(BZ),
        'fixed_active_tail_rows': FIXED_ACTIVE_TAIL,
        'complete_mersenne_factorizations': FACTORS,
        'deterministic_trial_primes': sorted(trial_set), 'Lucas_certificates': lucas_receipts,
        'prime_base2_orders': ORDERS, 'incidences_on_BZ': incidences,
        'small_order_inventories': {'w_h1':hw1,'w_h2':hw2,'w_h3':hw3,'w_h4':hw4,'w_h5':hw5,
                                   'z_e1':ze1,'z_e2':ze2,'z_e3':ze3,'z_e4':ze4,'z_e5':ze5,'t_e2':te2},
        'strict_rational_bounds': {name:str(value) for name,value in bounds.items()},
        'remaining_three_class_patterns': reduced_covers,
        'families': families, 'phase_root_table': phase_root_table,
        'total_phase_dictionaries': total_dictionaries, 'total_signed_CRT_descriptions': total_signed_descriptions,
        'mathematical_completeness_basis': 'All-prime incidence and lifting proof, then complete finite-order factorization',
        'independent_project_review': False,
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({'status':'PASS','scope':certificate['scope'],'phase_dictionaries':total_dictionaries,
                      'signed_CRT_descriptions':total_signed_descriptions,
                      'family_counts':{name:item['phase_dictionary_count'] for name,item in families.items()},
                      'output':str(args.output)},indent=2))


if __name__ == '__main__':
    main()
