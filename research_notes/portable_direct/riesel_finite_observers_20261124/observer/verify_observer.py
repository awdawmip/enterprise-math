"""New observer arithmetic and the fixed 31-channel all-cost construction.

The exhaustive six-prime theorem is a companion mathematical dependency.
The previous eight-class/minimum and native certificates are reused; this
calculation checks new partitions, the 31-channel congruence, modified seed
coverage, and one compact seven-prime member. It does not rerun prior gcds.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import gcd, lcm, prod
from pathlib import Path
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

A_STAR = 690786768637635218740714348513373826260012289
M = 1397394912916194098609132326092145093313722687204526281
L = 80754838636615
R1_RESIDUE = 12926327728523
B = (433, 38737)
Z = prod(B)
P = (7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417)
H = frozenset((0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36,
               45, 48, 49, 51, 54, 55, 63, 64, 66, 69, 70,
               75, 76, 78, 79, 84, 85, 90, 91, 93, 96, 99, 100))
OLD_PRIVATE = (37, 3, 89, 5, 293, 117, 413, 113, 41, 33, 87,
               233, 773, 207, 237, 257, 53, 593, 63, 111)
PHASES = {
    433: {0: (150, 283), 1: (4, 429)},
    38737: {0: (2677, 36060), 1: (4, 38733)}
}
CORE = [('5', 4, 2, 1), ('13', 12, 6, 0),
        ('19', 18, 9, 4), ('73', 9, 9, 1)]
V9_COMMIT = 'b1de1acbdc97b5e51d486127abd1fadd24babd99'
V9_PATH = 'research_notes/portable_direct/riesel_five_cover_20261123/fiber/fiber_certificate.json'
V8_PATH = 'research_notes/portable_direct/riesel_observers_20261122/fixed_observer/fixed_observer_certificate.json'
V7_PATH = 'research_notes/portable_direct/riesel_spectrum_20261121/spectrum/small_spectrum_certificate.json'


def locate(explicit, relative):
    if explicit:
        return Path(explicit)
    for ancestor in Path(__file__).resolve().parents:
        candidate = ancestor / relative
        if candidate.is_file():
            return candidate
    raise FileNotFoundError('Pass the existing dependency path: ' + relative)


def crt(pairs):
    value, modulus = 0, 1
    for residue, q in pairs:
        assert gcd(modulus, q) == 1
        value += modulus * ((residue-value)*pow(modulus, -1, q) % q)
        modulus *= q
    return value, modulus


def root_pair(q, phase):
    value = pow(pow(2, phase, q), -1, q)
    return tuple(sorted((value, q-value)))


def seed_check(rows):
    period = lcm(105, *(d for _, _, d, _ in rows))
    private = {}
    for u in range(1, period+1):
        if u % 105 not in H:
            continue
        hits = [label for label, _, d, c in rows if (u-c) % d == 0]
        assert hits, (u, rows)
        if len(hits) == 1:
            private.setdefault(hits[0], u)
    assert len(private) == len(rows)
    assert all(210 % order != 0 for _, order, _, _ in rows)
    # The only odd-order extra channel is unchanged 73; all old odd witnesses
    # avoid its n=2 mod9 phase. Every other row has an even exponent phase.
    assert all(n % 9 != 2 for n in OLD_PRIVATE)
    assert [label for label, o, _, _ in rows if o % 2] == ['73']
    return {'additional_count': len(rows), 'hole_period_u': period,
            'rows': [{'prime_or_symbol': q, 'order_2': o,
                      'period_u': d, 'phase_u': c} for q, o, d, c in rows],
            'private_old_hole_u': private,
            'prime_existence_scope': 'Named earlier seed primes reuse their exact proofs; new order-labelled rows use the inherited primitive-prime theorem.'}


def compact_cover(a, rows, period):
    holes = [n for n in range(1, period+1)
             if n % 2 == 0 and (n//2) % 105 in H]
    remaining = list(holes)
    counts = [len(remaining)]
    for q, _, c in rows:
        assert a*a*pow(4, c, q) % q == 1
        remaining = [n for n in remaining if a*a*pow(2, n, q) % q != 1]
        counts.append(len(remaining))
    assert not remaining
    private = {}
    for n in holes:
        hits = [q for q, _, _ in rows if a*a*pow(2, n, q) % q == 1]
        if len(hits) == 1:
            private.setdefault(hits[0], n)
    assert len(private) == len(rows)
    assert 2*a*a-1 > max(P+tuple(q for q, _, _ in rows))
    return {'root': str(a), 'root_digits': len(str(a)),
            'root_sha256': sha256(str(a).encode()).hexdigest(),
            'ordered_rows': [{'q': q, 'order_2': o, 'phase_u': c,
                              'root_residue': a % q} for q, o, c in rows],
            'full_coverage_period_n': period, 'uncovered_counts': counts,
            'private_old_hole_indices': private,
            'all_assigned_divisors_proper': True,
            'minimum_scope': 'Only the eight specified binary completion progressions in R2; no density-optimality or all-cost-seven minimum claim.',
            'delta_P': 7,
            'delta_lower_bound_dependency': 'Complete six-prime classification on R1; 433 is inactive throughout R2.',
            'total_cover_minimum_equality_claimed': False,
            'native_execution_claimed_here': False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--v9-certificate')
    parser.add_argument('--v8-certificate')
    parser.add_argument('--v7-certificate')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('observer_certificate.json'))
    args = parser.parse_args()
    v9 = json.loads(locate(args.v9_certificate, V9_PATH).read_text())
    v8 = json.loads(locate(args.v8_certificate, V8_PATH).read_text())
    v7 = json.loads(locate(args.v7_certificate, V7_PATH).read_text())
    previous = v9['R1']
    assert previous['L'] == L and previous['observer_residue'] == R1_RESIDUE
    assert previous['relative_predicate_period_Z'] == Z == 16773121
    for q in B:
        for parity in (0, 1):
            assert root_pair(q, 16+18*parity) == PHASES[q][parity]

    counts = Counter()
    for labels in product((-1, 0, 1), repeat=2):
        weight = prod(q-4 if label == -1 else 2 for q, label in zip(B, labels))
        active = sum(x != -1 for x in labels)
        kind = ('none' if active == 0 else 'one_active' if active == 1
                else 'same_phase' if labels[0] == labels[1] else 'opposite_phases')
        counts[kind] += weight
    assert sum(counts.values()) == Z
    assert counts == {'none': 16616457, 'one_active': 156648,
                      'same_phase': 8, 'opposite_phases': 8}
    E5 = Z-counts['none']
    assert E5 == previous['predicate_counts_per_Z']['E5'] == 156664
    assert counts['opposite_phases'] == previous['predicate_counts_per_Z']['nested6']
    assert Fraction(8, E5) == Fraction(1, 19583)
    true_classes = sorted(crt([(r, 433), (s, 38737)])[0]
                          for parity in (0, 1)
                          for r in PHASES[433][parity]
                          for s in PHASES[38737][1-parity])
    assert true_classes == previous['nested6_CRT_classes']

    r2, modulus2 = crt([(R1_RESIDUE, L), (0, 433), (38733, 38737)])
    base2, step2 = crt([(A_STAR, 6*M), (r2, modulus2)])
    assert modulus2 == L*Z
    assert (r2, modulus2) == (602924359709868072943, 1354510679787418425415)
    assert {36, 60, 72} <= {abs(n-m) for n in OLD_PRIVATE for m in OLD_PRIVATE}
    assert pow(2, 72, 433) == 1 and pow(2, 36, 433) != 1
    assert pow(pow(2, 34, 38737), -1, 38737) == 38733

    inherited_members = []
    witnesses = [(x['additional_cost'], x, 'v8') for x in v8['new_explicit_witnesses']
                 if x['additional_cost'] in (6, 7)]
    witnesses.append((8, v7['numeric_cost_8'], 'v7'))
    for cost, row, source in witnesses:
        a = int(row['root_hex'], 16)
        assert (a-A_STAR) % (6*M) == 0 and a % L == R1_RESIDUE
        membership = a % modulus2 == r2
        assert membership == (cost in (7, 8))
        assert (a % 433, a % 38737) == ((150, 38733) if cost == 6 else (0, 38733))
        inherited_members.append({'additional_cost': cost, 'source': source,
                                  'root_decimal_sha256': sha256(str(a).encode()).hexdigest(),
                                  'R2_member': membership,
                                  'root_residues_433_38737': [a % 433, a % 38737],
                                  'new_check': 'R2 congruence only; existing exact-cost, pairwise-gcd and native evidence reused.'})

    rows7 = CORE + [('38737', 72, 36, 34), ('577', 144, 72, 16),
                    ('487824887233', 144, 72, 52)]
    rows8 = CORE + [('38737', 72, 36, 34), ('487824887233', 144, 72, 52),
                    ('1153', 288, 144, 16), ('6337', 288, 144, 88)]
    translated = ((2, 1), (3, 1), (4, 2), (6, 0), (12, 8))
    original = ((2, 0), (3, 0), (4, 1), (6, 5), (12, 7))
    assert all(any((v-b) % m == 0 for m, b in translated) for v in range(12))
    translated_private = (3, 4, 2, 12, 8)
    for index, witness in enumerate(translated_private):
        assert [i for i, (m, b) in enumerate(translated) if (witness-b) % m == 0] == [index]
    rows9 = CORE + [('38737' if m == 2 else f'primitive_order_{36*m}',
                     36*m, 18*m, 16+18*b) for m, b in translated]
    rows10 = CORE + [('38737', 72, 36, 34)] + [
        (f'primitive_order_{72*m}', 72*m, 36*m, 16+36*b) for m, b in original]
    seed_checks = [seed_check(rows) for rows in (rows7, rows8, rows9, rows10)]
    assert [s['additional_count'] for s in seed_checks] == [7, 8, 9, 10]
    for rows in (rows7, rows8, rows9, rows10):
        assert [row for row in rows if row[1] == 72] == [('38737', 72, 36, 34)]
        assert all(row[1] not in (10, 30, 36, 60) for row in rows)
        assert max(row[2] for row in rows) >= 72

    candidates = []
    for c1, c2 in ((16, 52), (52, 16)):
        for r, s in product(root_pair(577, c1), root_pair(487824887233, c2)):
            a, progression = crt([(base2, step2), (r, 577), (s, 487824887233)])
            candidates.append({'a': a, 'phase_577': c1, 'phase_large': c2,
                               'residue_577': r, 'residue_large': s,
                               'progression_modulus': progression})
    best = min(candidates, key=lambda x: x['a'])
    assert best['a'] == 142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303
    numeric_rows = [(5, 4, 1), (13, 12, 0), (19, 18, 4), (73, 9, 1),
                    (38737, 72, 34), (577, 144, best['phase_577']),
                    (487824887233, 144, best['phase_large'])]
    compact = compact_cover(best['a'], numeric_rows, 5040)
    assert compact['uncovered_counts'] == [864, 432, 156, 104, 52, 26, 13, 0]

    result = {
        'schema': 'riesel-complete-six-observer-and-r2-spectrum-v1',
        'status': 'Author derivation and exact finite arithmetic; no independent Review.',
        'all_prime_six_classification_dependency': '../six/proof.md',
        'reused_v9_source': {'commit': V9_COMMIT, 'path': V9_PATH},
        'R1_complete_delta6': {
            'period_Z': Z, 'binary_root_table': PHASES,
            'phase_dictionary_count': 2, 'root_class_count': 8,
            'classes_mod_Z': true_classes,
            'density': str(Fraction(8, Z)),
            'least_additive_period': Z,
            'least_period_witnesses_reused': previous['least_period_essential_coordinate_witnesses']['nested6'],
            'least_root_reused': previous['compact_minimum_nested6_witness']['root_decimal'],
            'minimum_scope': 'All R1 roots with additional cost six, by the new complete six-prime theorem.',
            'minimum_computation_reused_without_rerun': True,
            'native_membership_reused': {'commit': V9_COMMIT,
                'path': 'research_notes/portable_direct/riesel_five_cover_20261123/native/native_certificate.json',
                'case_label': 'R1_least_nested_optimal_six_root'},
            'total_cost_bound': 26, 'total_cost_equality_claimed': False,
            'category_partition': dict(counts),
            'E5_count': E5,
            'E5_but_not_delta6_count': E5-8,
            'conditional_delta6_density_given_E5': str(Fraction(8, E5))
        },
        'R2': {
            'observer_channel_count': 31, 'observer_modulus': modulus2,
            'observer_residue': r2, 'new_root_residues': {'433': 0, '38737': 38733},
            'base_root': str(base2), 'root_progression_modulus': str(step2),
            'all_roots_delta_lower_bound': 7,
            'all_finite_exact_costs': 'Every integer s>=7, with infinitely many roots for each s and total cost20+s.',
            'construction_change': 'Use seeds7,8, a translated five-child refinement forseed9, and refinement of433 inseed6 forseed10; then add4 repeatedly.',
            'modified_four_seeds': seed_checks,
            'translated_refinement_cover': list(translated),
            'translated_private_v': list(translated_private),
            'forcing_old_private_index_pairs': {'gap36': [5, 41], 'gap60': [3, 63], 'gap72': [41, 113]},
            'existing_root_membership_checks': inherited_members,
            'compact_cost7_example': compact,
            'binary_progressions_checked': len(candidates),
            'binary_progression_minima': [{k: str(v) if k in ('a', 'progression_modulus') else v
                                         for k, v in x.items()} for x in candidates],
            'optimization_scope': 'No all-seven classification or density-optimality claim is made here.'
        }
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'output': str(args.output),
                      'R1_cost6_classes': 8, 'R2_observer_modulus': modulus2,
                      'modified_seeds': [7, 8, 9, 10],
                      'compact_cost7_root_digits': compact['root_digits']}))


if __name__ == '__main__':
    main()
