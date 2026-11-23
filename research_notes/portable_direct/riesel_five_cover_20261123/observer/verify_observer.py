"""Exact observer counts and CRT minima for the complete five-channel family.

The companion global proof supplies the all-prime completeness theorem.
This script checks its finite phase dictionary, factorized counts and minima.
Only Python standard-library integer arithmetic is used.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from math import gcd, lcm, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
A_STAR = 690786768637635218740714348513373826260012289
P = (7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417)
M = 1397394912916194098609132326092145093313722687204526281
H = (0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45,
     48, 49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78,
     79, 84, 85, 90, 91, 93, 96, 99, 100)
U = (11, 61, 331)
W = (19, 37, 73, 109)
CHANNELS = (5, 13) + U + W
ORDER2 = {5: 4, 13: 12, 11: 10, 61: 60, 331: 30,
          19: 18, 37: 36, 73: 9, 109: 36}
ORDER4 = {q: order // gcd(order, 2) for q, order in ORDER2.items()}
K = 65 * prod(U)
L = K * prod(W)


def factor(n):
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def crt(pairs):
    value, modulus = 0, 1
    for residue, q in pairs:
        assert gcd(modulus, q) == 1
        value += modulus * ((residue-value)*pow(modulus, -1, q) % q)
        modulus *= q
    return value, modulus


def roots_for_phase(q, c):
    z = pow(pow(2, c, q), -1, q)
    return tuple(sorted((z, (-z) % q)))


def basic_phase(epsilon, r13):
    return next(c for c in range(6) if c % 2 == epsilon and c % 3 == r13)


def fiber_origin(epsilon, r13):
    return next(u for u in range(6)
                if u % 2 == epsilon and u % 3 == 1-r13)


def u_phase(q, epsilon, category):
    return next(c for c in range(ORDER4[q])
                if c % 5 == category and (q == 11 or c % 3 == 1)
                and (q != 61 or c % 2 == epsilon))


def w_phase(q, epsilon, r13, category):
    return (fiber_origin(epsilon, r13)+6*category) % ORDER4[q]


def category_tables(epsilon, r13):
    u_table = {q: {r: roots_for_phase(q, u_phase(q, epsilon, r))
                   for r in (0, 1, 4)} for q in U}
    w_table = {q: {r: roots_for_phase(q, w_phase(q, epsilon, r13, r))
                   for r in (0, 1, 2)} for q in W}
    return u_table, w_table


def category(residue, table):
    return next((c for c, values in table.items() if residue in values), None)


def five_cover_count(residues):
    """Number of complete five-prime dictionaries, by the global theorem."""
    for epsilon in (0, 1):
        if residues[5] not in roots_for_phase(5, 1-epsilon):
            continue
        for r13 in (0, 1):
            if residues[13] not in roots_for_phase(13, basic_phase(epsilon, r13)):
                continue
            ut, wt = category_tables(epsilon, r13)
            u_labels = [category(residues[q], ut[q]) for q in U]
            w_labels = [category(residues[q], wt[q]) for q in W]
            type_i = int(r13 == 0 and set(u_labels) == {0, 1, 4})
            wc = Counter(w_labels)
            type_ii = wc[0]*wc[1]*wc[2]
            return type_i + type_ii
    return 0


def patterns():
    result = []
    for epsilon in (0, 1):
        for r13 in (0, 1):
            basic = [(5, 1-epsilon), (13, basic_phase(epsilon, r13))]
            if r13 == 0:
                for assignment in permutations(U):
                    rows = basic + [(q, u_phase(q, epsilon, c))
                                    for q, c in zip(assignment, (0, 1, 4))]
                    result.append({'type': 'I', 'epsilon': epsilon, 'r13': r13,
                                   'rows': rows})
            for selected in combinations(W, 3):
                for assignment in permutations(selected):
                    rows = basic + [(q, w_phase(q, epsilon, r13, c))
                                    for c, q in enumerate(assignment)]
                    result.append({'type': 'II', 'epsilon': epsilon, 'r13': r13,
                                   'rows': rows})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE/'observer_certificate.json')
    args = parser.parse_args()
    assert prod(P) == M and A_STAR % 3 == 0 and 0 < A_STAR < 6*M
    assert gcd(6*M, L) == 1
    assert K == 14436565 and L == 80754838636615
    for q, order in ORDER2.items():
        assert factor(q) == {q: 1}
        assert pow(2, order, q) == 1
        assert all(pow(2, j, q) != 1 for j in range(1, order))

    # Complete supporting factorizations for the conditional three-channel lemma.
    factorizations = {}
    effective_candidates = {}
    excluded = set(P) | {3, 5, 13}
    for f in (3, 4, 5, 7):
        factors = factor((1 << (12*f))-1)
        assert prod(q**e for q, e in factors.items()) == (1 << (12*f))-1
        factorizations[12*f] = factors
        effective_candidates[f] = [q for q in factors if q not in excluded
                                   and all(pow(2, 12*j, q) != 1 for j in range(1, f))]
    assert effective_candidates == {3: list(W), 4: [], 5: list(U),
                                     7: [29, 43, 1429, 5419]}
    assert Counter(h % 5 for h in H if h % 3 == 1) == {0: 5, 1: 5, 4: 3}
    last_three = [h for h in H if h % 3 == 1 and h % 5 == 4]
    assert last_three == [49, 64, 79]
    assert len({h % 7 for h in last_three}) == 3

    phase_tables = []
    for epsilon in (0, 1):
        for r13 in (0, 1):
            ut, wt = category_tables(epsilon, r13)
            for q, table in list(ut.items())+list(wt.items()):
                seen = set()
                for values in table.values():
                    assert len(values) == len(set(values)) == 2
                    assert seen.isdisjoint(values)
                    seen.update(values)
                assert len(seen) == 6
            phase_tables.append({'epsilon': epsilon, 'r13': r13,
                                 'basic_rows': [(5, 1-epsilon), (13, basic_phase(epsilon, r13))],
                                 'fiber_origin': fiber_origin(epsilon, r13),
                                 'U_categories': ut, 'W_categories': wt})

    # Factorized enumeration: at most4^3*4^4 category tuples, not L raw residues.
    u_count = 0
    for labels in product((0, 1, 4, None), repeat=3):
        weight = prod(2 if label is not None else q-6 for q, label in zip(U, labels))
        if set(labels) == {0, 1, 4}:
            u_count += weight
    assert u_count == 48
    w_hist = Counter()
    for labels in product((0, 1, 2, None), repeat=4):
        weight = prod(2 if label is not None else q-6 for q, label in zip(W, labels))
        counts = Counter(labels)
        w_hist[counts[0]*counts[1]*counts[2]] += weight
    assert sum(w_hist.values()) == prod(W)
    B = prod(W)-3*prod(q-2 for q in W)+3*prod(q-4 for q in W)-prod(q-6 for q in W)
    assert B == w_hist[1]+w_hist[2] == 10848
    assert w_hist[1] == 10272 and w_hist[2] == 576

    cover_hist = Counter()
    basic_pair_branch_counts = {}
    for r13 in (0, 1):
        count = 0
        for type_i, u_weight in ((False, prod(U)-48), (True, 48)):
            for w_covers, w_weight in w_hist.items():
                n = int(type_i and r13 == 0)+w_covers
                weight = 8*u_weight*w_weight
                cover_hist[n] += weight
                if n:
                    count += weight
        basic_pair_branch_counts[r13] = count
    # The two other13 phases and inactive basic pairs never satisfy the global theorem.
    total = sum(v for n, v in cover_hist.items() if n)
    assert total == 8*(48*prod(W)+(2*prod(U)-48)*B) == 40693468800
    assert basic_pair_branch_counts == {0: 21418655616, 1: 19274813184}
    assert {n: cover_hist[n] for n in (1, 2, 3)} == {
        1: 38642641536, 2: 2050606080, 3: 221184}

    all_patterns = patterns()
    assert len(all_patterns) == 108
    pattern_counts = Counter((p['type'], p['r13']) for p in all_patterns)
    assert pattern_counts == {('I', 0): 12, ('II', 0): 48, ('II', 1): 48}
    records = []
    crt_count = 0
    for pattern_id, item in enumerate(all_patterns):
        rows = item['rows']
        period = lcm(105, *(ORDER4[q] for q, _ in rows))
        holes = [u for u in range(period) if u % 105 in H]
        assert all(any((u-c) % ORDER4[q] == 0 for q, c in rows) for u in holes)
        private = {q: next(u for u in holes if (u-c) % ORDER4[q] == 0 and
                    all((u-c2) % ORDER4[q2] for q2, c2 in rows if q2 != q))
                   for q, c in rows}
        best = None
        for signs in product((1, -1), repeat=5):
            residues = [(sign*pow(pow(2, c, q), -1, q) % q, q)
                        for sign, (q, c) in zip(signs, rows)]
            root, modulus = crt([(A_STAR, 6*M)]+residues)
            assert root > 0 and root % 3 == 0 and (root-A_STAR) % (2*M) == 0
            assert all(root % q == r for r, q in residues)
            assert 2*root*root-1 > max(P+tuple(q for q, _ in rows))
            current = (root, modulus, residues)
            best = current if best is None or root < best[0] else best
            crt_count += 1
        root, modulus, residues = best
        record = {'pattern_id': pattern_id, 'type': item['type'],
                  'epsilon': item['epsilon'], 'r13': item['r13'],
                  'rows': [{'q': q, 'order_4': ORDER4[q], 'phase_u': c}
                           for q, c in rows],
                  'checked_hole_period_u': period, 'private_old_hole_u': private,
                  'sign_combinations_checked': 32,
                  'least_positive_root_for_pattern': str(root),
                  'progression_modulus_for_pattern': str(modulus),
                  'least_root_residues': {q: r for r, q in residues}}
        records.append(record)
    assert crt_count == 3456
    least = min(records, key=lambda p: int(p['least_positive_root_for_pattern']))
    assert least['least_positive_root_for_pattern'] == '39741911323337250951212360989279347168190786597922987443929'
    least_types = {}
    for typ, r13 in (('I', 0), ('II', 0), ('II', 1)):
        eligible = [p for p in records if p['type'] == typ and p['r13'] == r13]
        least_types[f'{typ}_r13_{r13}'] = min(eligible, key=lambda p: int(p['least_positive_root_for_pattern']))

    # Essential-coordinate witnesses prove least additive period L.
    essential = []
    for q in CHANNELS:
        values = {p: 0 for p in CHANNELS}
        values[5], values[13] = 3, 1
        if q not in W:
            values.update({11: 1, 61: 25, 331: 269})
        else:
            selected = (q,)+tuple(p for p in W if p != q)[:2]
            for c, p in enumerate(selected):
                values[p] = roots_for_phase(p, w_phase(p, 0, 0, c))[0]
        assert five_cover_count(values) > 0
        changed = dict(values)
        changed[q] = 0
        assert five_cover_count(changed) == 0
        a_true, mod_true = crt([(values[p], p) for p in CHANNELS])
        a_false, mod_false = crt([(changed[p], p) for p in CHANNELS])
        assert mod_true == mod_false == L
        assert all(a_true % p == a_false % p for p in CHANNELS if p != q)
        essential.append({'changed_prime': q, 'true_root_residue_mod_L': a_true,
                          'false_root_residue_mod_L': a_false,
                          'true_parameter_j_mod_L': (a_true-A_STAR)*pow(6*M, -1, L) % L,
                          'false_parameter_j_mod_L': (a_false-A_STAR)*pow(6*M, -1, L) % L,
                          'true_cover_count': five_cover_count(values)})

    result = {
        'schema': 'riesel-complete-cost-five-observer-v1',
        'status': 'AUTHOR_DERIVATION_AND_EXACT_FINITE_CALCULATION; NOT_INDEPENDENT_REVIEW',
        'all_prime_completeness_dependency': '../global/proof.md',
        'old_data_source_commit': 'a2ae4d93398425e67dacbb4c99b7f3a6755e5771',
        'old_data_source_path': 'research_notes/portable_direct/riesel_observers_20261122/staircase/proof.md',
        'a_star': str(A_STAR), 'M': str(M), 'P': P, 'H': H,
        'U': U, 'W': W, 'K': K, 'L': L,
        'complete_factorizations_2_power_minus_1': factorizations,
        'effective_order_candidates_in_conditional_lemma': effective_candidates,
        'phase_tables': phase_tables,
        'U_type_I_count': 48, 'W_total_residues': prod(W),
        'W_complete_three_phase_count': B,
        'W_dictionary_multiplicity': dict(w_hist),
        'basic_pair_branch_root_counts_mod_L': basic_pair_branch_counts,
        'all_cost_five_root_classes_mod_L': total,
        'density_within_3_divisible_branch': str(Fraction(total, L)),
        'density_within_entire_old_class': str(Fraction(total, 3*L)),
        'five_prime_dictionary_multiplicity': {n: cover_hist[n] for n in (1, 2, 3)},
        'complete_phase_pattern_count': len(records),
        'phase_type_counts': {'I_r13_0': 12, 'II_r13_0': 48, 'II_r13_1': 48},
        'CRT_progression_descriptions_checked': crt_count,
        'least_positive_root_of_additional_cost_five': least,
        'least_root_by_type': least_types,
        'phase_patterns_and_minima': records,
        'least_additive_period_in_branch_parameter_j': L,
        'essential_coordinate_witnesses': essential,
        'scope': 'The complete cost-five equivalence uses the companion global all-prime classification. The minimum is among all delta_P=5 roots in the fixed old class, not among all Riesel numbers or all square Riesel coefficients. Riesel coefficient is a^2. Total cover size for the least root is bounded above by25, not asserted equal25.',
        'quantifier_note': '3456 counts CRT progression descriptions with differing moduli; they are not disjoint residue classes modulo L. Overlaps are handled by the factorized counting argument.'
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'output': str(args.output), 'patterns': 108,
                      'CRT_descriptions': crt_count, 'observer_modulus': L,
                      'cost_five_residue_classes': total,
                      'least_root': least['least_positive_root_for_pattern']}))


if __name__ == '__main__':
    main()
