#!/usr/bin/env python3
"""Sharp budget-six arithmetic and non-nested optimality on the R2 fiber.

The all-prime lower-bound and equality proof is in r2_proof.md. This calculation
checks complete small factorization inputs, phase dictionaries and exact CRT
counts, plus one common integer root with two crossing seven-channel routes.
It does not claim native BRC execution or classification of all seven-covers.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
V9_COMMIT = 'b1de1acbdc97b5e51d486127abd1fadd24babd99'
V9_REL = Path('research_notes/portable_direct/riesel_five_cover_20261123')
A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
L = 80754838636615
R1_RESIDUE = 12926327728523
C = (181, 631, 23311, 54001, 18837001, 29247661)
FACTORS180 = {3: 3, 5: 2, 7: 1, 11: 1, 13: 1, 19: 1, 31: 1,
              37: 1, 41: 1, 61: 1, 73: 1, 109: 1, 151: 1, 181: 1,
              331: 1, 631: 1, 1321: 1, 23311: 1, 54001: 1,
              18837001: 1, 29247661: 1}
ORDER2_C = {181: 180, 631: 45, 23311: 45, 54001: 180,
            18837001: 90, 29247661: 180}


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def factor(n):
    result, p = {}, 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def exact_order(base, q, d):
    return pow(base, d, q) == 1 and all(
        pow(base, d//p, q) != 1 for p in factor(d))


def crt(pairs):
    a, modulus = 0, 1
    for r, q in pairs:
        assert gcd(modulus, q) == 1
        a += modulus*((r-a)*pow(modulus, -1, q) % q)
        modulus *= q
    return a, modulus


def root_pair(q, c):
    r = pow(pow(2, c, q), -1, q)
    return tuple(sorted((r, q-r)))


def locate_prior(explicit):
    if explicit:
        path = Path(explicit)
        assert (path/'fiber/fiber_certificate.json').is_file()
        return path
    for parent in HERE.parents:
        path = parent/V9_REL
        if (path/'fiber/fiber_certificate.json').is_file():
            return path
    raise FileNotFoundError('Pass --prior-dir for retained round-nine sources.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior-dir')
    parser.add_argument('--output', type=Path, default=HERE/'r2_certificate.json')
    args = parser.parse_args()
    prior = locate_prior(args.prior_dir)
    global9 = json.loads((prior/'global/global_certificate.json').read_text())
    fiber9 = json.loads((prior/'fiber/fiber_certificate.json').read_text())
    P, H = set(global9['P']), set(global9['H'])
    assert prod(P) == M and len(H) == 36
    r2, omega = crt([(R1_RESIDUE, L), (0, 433), (38733, 38737)])
    assert r2 == 602924359709868072943
    assert omega == 1354510679787418425415
    base, base_period = crt([(A_STAR, 6*M), (r2, omega)])

    A = {v for v in range(35) if (4+6*v) % 105 in H}
    B = {w for w in range(35) if (2+3*w) % 35 in A}
    assert B == {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}
    A7 = [sum(v % 7 == c for v in A) for c in range(7)]
    B5 = [sum(w % 5 == c for w in B) for c in range(5)]
    assert A7 == [0, 2, 3, 3, 3, 2, 0]
    assert B5 == [5, 3, 0, 5, 0]
    assert sum(sorted(A7, reverse=True)[:4]) == 11

    # Strict alternatives for an arbitrary dictionary with at most six primes.
    sharp = Fraction(1, 420)
    no_basics_gap = Fraction(6, 35)*(1-Fraction(83, 108))
    one_basic_gap = Fraction(3, 35)*(1-Fraction(8, 9))
    no_W_all7_gap = Fraction(13, 420)*(1-Fraction(11, 13))
    no_W_mixed_gap = Fraction(13, 420)*(1-(3*Fraction(3, 13)+Fraction(5, 26)))
    one_W_gap = Fraction(13, 420)*(1-Fraction(1, 3)-3*Fraction(1, 6))
    keep38737_gap = Fraction(13, 1260)*Fraction(1, 2)*Fraction(1, 2)
    assert no_basics_gap == Fraction(5, 126)
    assert one_basic_gap == Fraction(1, 105)
    assert no_W_all7_gap == Fraction(1, 210)
    assert no_W_mixed_gap == Fraction(1, 280)
    assert one_W_gap == Fraction(13, 2520)
    assert keep38737_gap == Fraction(13, 5040)
    assert all(x > sharp for x in (no_basics_gap, one_basic_gap, no_W_all7_gap,
                                  no_W_mixed_gap, one_W_gap, keep38737_gap))
    assert Fraction(2, 3)*Fraction(3, 13) < Fraction(1, 6)
    assert max(Fraction(1, 6), Fraction(5, 39), Fraction(1, 13), Fraction(1, 39)) == Fraction(1, 6)

    # A complete product with trial primality is an exact factorization proof.
    assert prod(q**e for q, e in FACTORS180.items()) == 2**180-1
    assert all(is_prime(q) for q in FACTORS180)
    inactive = {3, 11, 61, 331, 37, 109, 433}
    fixed_primes = {5, 13, 19, 73, 38737}
    candidates = sorted(q for q in FACTORS180
        if q not in P | inactive | fixed_primes and exact_order(2**36, q, 5))
    assert tuple(candidates) == C
    for q in C:
        assert exact_order(2, q, ORDER2_C[q])
    phase_table = {q: {} for q in C}
    for q in C:
        d = ORDER2_C[q]//gcd(ORDER2_C[q], 2)
        for b in (0, 3, 1):
            c = (16+18*b) % d
            roots = root_pair(q, c)
            assert all(r*r*pow(4, c, q) % q == 1 for r in roots)
            phase_table[q][b] = {'w_category': b, 'period_u': d,
                                 'phase_u': c, 'root_residues': roots}
        assert len({r for row in phase_table[q].values() for r in row['root_residues']}) == 6

    # Exact class counts use all weighted category states, not root sampling.
    T = prod(C)
    assert T == 79208819702303143625098260481
    e6_count = T-2*prod(q-2 for q in C)+prod(q-4 for q in C)
    n7_count = T-3*prod(q-2 for q in C)+3*prod(q-4 for q in C)-prod(q-6 for q in C)
    totals = Counter()
    for cats in product((-1, 0, 3, 1), repeat=len(C)):
        weight = prod(q-6 if b == -1 else 2 for q, b in zip(C, cats))
        present = set(cats)
        totals['all'] += weight
        if {0, 3} <= present:
            totals['E6'] += weight
        if {0, 3, 1} <= present:
            totals['N7'] += weight
    assert totals == {'all': T, 'E6': e6_count, 'N7': n7_count}
    assert e6_count == 5823767115854050658573528
    assert n7_count == 2068723011224822069760

    fixed_rows = [(5, 2, 1), (13, 6, 0), (19, 9, 4), (73, 9, 1)]
    def minimum_and_coverage(categories):
        minimum = None
        patterns = starts = 0
        for chosen in permutations(C, len(categories)):
            patterns += 1
            rows = fixed_rows+[(q, phase_table[q][b]['period_u'],
                                phase_table[q][b]['phase_u'])
                               for q, b in zip(chosen, categories)]
            period = lcm(105, *(d for _, d, _ in rows))
            assert period == 630
            remaining = [u for u in range(1, period+1)
                         if u % 105 in H and not any(u % d == c for _, d, c in rows)]
            assert len(remaining) == (3 if len(categories) == 2 else 0)
            for residues in product(*(phase_table[q][b]['root_residues']
                                      for q, b in zip(chosen, categories))):
                starts += 1
                a, modulus = crt([(base, base_period)]+list(zip(residues, chosen)))
                record = {'root': a, 'root_digits': len(str(a)),
                          'category_to_prime': dict(zip(map(str, categories), chosen)),
                          'root_residues': dict(zip(chosen, residues)),
                          'progression_modulus': str(modulus)}
                if minimum is None or a < minimum['root']:
                    minimum = record
        minimum['root'] = str(minimum['root'])
        return {'phase_dictionaries': patterns, 'CRT_progression_starts': starts,
                'minimum': minimum}
    e6_min = minimum_and_coverage((0, 3))
    n7_min = minimum_and_coverage((0, 3, 1))
    assert (e6_min['phase_dictionaries'], e6_min['CRT_progression_starts']) == (30, 120)
    assert (n7_min['phase_dictionaries'], n7_min['CRT_progression_starts']) == (120, 960)

    # A single ordinary integer supports the crossing binary and modulo-five routes.
    crossing_extra = [(181, 16), (631, 25), (23311, 34),
                      (577, 16), (487824887233, 52)]
    crossing, crossing_modulus = crt([(base, base_period)]+[
        (pow(pow(2, c, q), -1, q), q) for q, c in crossing_extra])
    assert crossing == 5638859082119336258239285976823481197493104557616679794390344515886945665210917791971325889059624133
    assert all(is_prime(q) and exact_order(2, q, 144) for q in (577, 487824887233))
    assert crossing % omega == r2 and crossing % (6*M) == A_STAR
    period_n = 5040
    initial_holes = [n for n in range(1, period_n+1)
                     if n % 2 == 0 and (n//2) % 105 in H]
    chains = []
    for label, qs, expected in (
        ('modulo_five', [5, 13, 19, 73, 181, 631, 23311],
         [864, 432, 156, 104, 52, 32, 12, 0]),
        ('binary', [5, 13, 19, 73, 38737, 577, 487824887233],
         [864, 432, 156, 104, 52, 26, 13, 0])):
        remaining = initial_holes[:]
        counts = [len(remaining)]
        for q in qs:
            remaining = [n for n in remaining if crossing*crossing*pow(2, n, q) % q != 1]
            counts.append(len(remaining))
        assert counts == expected and 2*crossing*crossing-1 > max(P | set(qs))
        chains.append({'label': label, 'primes': qs, 'uncovered_counts_mod5040': counts,
                       'all_assigned_divisors_proper': True})

    result = {
        'schema': 'riesel-r2-sharp-budget-six-and-non-nested-optima-v1',
        'status': 'AUTHOR_PROOF_AND_EXACT_ARITHMETIC; NOT_INDEPENDENT_REVIEW',
        'R2': {'observer_channels': 31, 'observer_modulus': omega,
               'observer_residue': r2, 'additional_residues': {'433': 0, '38737': 38733},
               'base_root': str(base), 'root_progression_modulus': str(base_period)},
        'source_dependency': {'commit': V9_COMMIT, 'path': str(V9_REL),
                              'scope': 'Old holes, complete small order exclusions and sharp R1 budgets0through5.'},
        'six_classification_companion': 'proof.md, Sections3.1-3.2, for new fixed-phase prefix exclusion bounds.',
        'residual_w_set_mod35': sorted(B), 'w_mod5_counts': B5,
        'v_mod7_counts_before_W': A7,
        'strict_alternative_gaps': {'neither_basic': str(no_basics_gap),
                                    'exactly_one_basic': str(one_basic_gap),
                                    'no_W_all_order7': str(no_W_all7_gap),
                                    'no_W_mixed_orders': str(no_W_mixed_gap),
                                    'one_W': str(one_W_gap),
                                    'keep_38737_after_both_W': str(keep38737_gap)},
        'complete_factorization_2_180_minus_1': FACTORS180,
        'effective_order5_candidates': list(C), 'base2_orders': ORDER2_C,
        'phase_root_table': phase_table,
        'sharp_staircase_denominator': 5040,
        'sharp_staircase_numerators': [864, 432, 156, 104, 52, 26, 12, 0],
        'no_simultaneous_nested_budget5_and6_optimum': True,
        'best_gap_extending_a_budget5_optimum': '13/5040',
        'unrestricted_budget6_sharp_gap': '1/420',
        'strict_nesting_penalty': '1/5040',
        'observer_modulus_T': T,
        'budget6_equality': {'true_root_classes': e6_count,
                             'relative_density': str(Fraction(e6_count, T)),
                             'least_additive_period': T, **e6_min,
                             'minimum_scope': 'All R2 roots attaining the sharp residual-density bound at budget6; no exact full-cover cost asserted for this minimum.'},
        'optimal6_then_full7': {'true_root_classes': n7_count,
                                'relative_density': str(Fraction(n7_count, T)),
                                'least_additive_period': T, **n7_min,
                                'minimum_scope': 'R2 roots admitting a complete seven-prime cover extending a budget6 equality dictionary; not all delta_P=7 roots.',
                                'exact_supplementary_cost': 7,
                                'total_cost_upper_bound': 27},
        'same_root_crossing_witness': {'root': str(crossing), 'root_digits': len(str(crossing)),
                                       'progression_modulus': str(crossing_modulus),
                                       'extra_phase_rows': [{'prime': q, 'phase_u': c, 'root_residue': crossing % q} for q, c in crossing_extra],
                                       'chains': chains, 'exact_supplementary_cost': 7,
                                       'total_cost_upper_bound': 27,
                                       'native_execution_claimed': False},
        'logical_scope': 'Complete all-prime classification of sharp budget6 equality. Complete classification of a seventh channel extending such equality. The binary route is an explicit seven-cover outside that subclass; all seven-covers are not classified.'
    }
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'candidates': list(C), 'sharp_D6': '1/420',
                      'D6_phase_dictionaries': 30, 'optimal6_then_full7_dictionaries': 120,
                      'E6_min': e6_min['minimum'], 'N7_min': n7_min['minimum'],
                      'output': str(args.output)}))


if __name__ == '__main__':
    main()
