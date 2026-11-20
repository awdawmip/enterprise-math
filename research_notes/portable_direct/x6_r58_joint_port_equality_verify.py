#!/usr/bin/env python3
"""Exact BRC root two-event equality-channel checks for conditional R57 grammar."""
from fractions import Fraction
from itertools import permutations
import json


def root_masses(p, collision_a, collision_b, weight_a, weight_b):
    # A_i B_j succeeds unless both i and j target the single shared Cell.
    allowed = [(i, j) for i in range(p) for j in range(p)
               if (i, j) != (collision_a, collision_b)]
    product = weight_a * weight_b
    eq = sum(i == j for i, j in allowed)
    neq = len(allowed) - eq
    return {
        'U': p * weight_a,
        'V': p * weight_b,
        'T': len(allowed) * product,
        'W': eq * product,
        'K': neq * product,
        'allowed_pairs': allowed,
    }


def verify(max_p=20):
    tested_geometries = 0
    tested_weighted_instances = 0
    test_weights = [
        (Fraction(1), Fraction(1)),
        (Fraction(2, 3), Fraction(7, 5)),
        (Fraction(5, 4), Fraction(11, 6)),
    ]
    orbit_counts = {}
    for p in range(1, max_p + 1):
        signatures = set()
        for a in range(p):
            for b in range(p):
                tested_geometries += 1
                delta = int(a == b)
                for wa, wb in test_weights:
                    m = root_masses(p, a, b, wa, wb)
                    assert m['U'] == p * wa
                    assert m['V'] == p * wb
                    assert m['T'] == (p * p - 1) * wa * wb
                    assert m['W'] == (p - delta) * wa * wb
                    assert m['K'] == (p * (p - 1) - 1 + delta) * wa * wb
                    assert m['U'] * m['V'] - m['T'] == wa * wb
                    recovered_p_squared = m['U'] * m['V'] / (m['U'] * m['V'] - m['T'])
                    assert recovered_p_squared == p * p
                    recovered_delta = p - p * p * m['W'] / (m['U'] * m['V'])
                    assert recovered_delta == delta
                    signatures.add((m['T'] / (wa * wb), m['W'] / (wa * wb)))
                    tested_weighted_instances += 1
        orbit_counts[str(p)] = len(signatures)
        assert len(signatures) == (1 if p == 1 else 2)

    renaming_checks = 0
    for p in range(1, 6):
        for perm in permutations(range(p)):
            for a in range(p):
                for b in range(p):
                    transformed = root_masses(p, perm[a], perm[b], Fraction(1), Fraction(1))
                    original = root_masses(p, a, b, Fraction(1), Fraction(1))
                    mapped = {(perm[i], perm[j]) for i, j in original['allowed_pairs']}
                    assert mapped == set(transformed['allowed_pairs'])
                    assert (original['T'], original['W']) == (transformed['T'], transformed['W'])
                    renaming_checks += 1

    e1 = {(0, 1), (1, 0)}
    e2 = {(0, 1), (0, 2)}
    assert len(e1) == len(e2) == 2
    assert not any(i == j for i, j in e1 | e2)
    assert sorted(sum(i == a for i, _ in e1) for a in range(3)) != sorted(
        sum(i == a for i, _ in e2) for a in range(3))
    return {
        'status': 'PASS',
        'model': 'R57 ordered single-collision-pair conditional whole-triad BRC',
        'range': {'min_p': 1, 'max_p': max_p},
        'geometries_checked': tested_geometries,
        'weighted_instances_checked': tested_weighted_instances,
        'diagonal_permutation_invariance_checks': renaming_checks,
        'root_orbit_signature_counts': orbit_counts,
        'general_graph_counterexample': {'p': 3, 'C1': sorted(e1), 'C2': sorted(e2),
                                         'same_aggregated_counts': True,
                                         'different_row_degree_multisets': True},
        'unverified': ['Native TRIADIC_CLOSURE_E embedding',
                       'Measurement-error coupling across U,V,T,W',
                       'Independent review'],
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
