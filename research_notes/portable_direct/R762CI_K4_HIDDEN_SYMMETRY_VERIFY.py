#!/usr/bin/env python3
"""R762CI author-side exact integer verifier for K4 hidden signed S4 action.

No numerical floating point or external libraries. Read the mathematical
argument in R762CI_K4_HIDDEN_SYMMETRY_THEOREM.md. This tests the conditional
pair-area diagnostic observer, not the native TRIADIC_CLOSURE_E event license.
"""
from itertools import combinations, permutations, product
from math import comb, gcd, prod
import json
import sys

VERTICES = tuple(range(4))
EDGES = tuple(''.join(map(str, e)) for e in combinations(VERTICES, 2))
HIDDEN = (('01', '23'), ('02', '13'), ('03', '12'))
ALL_PAIRS = tuple(combinations(EDGES, 2))


def edge_image(edge, p):
    return ''.join(str(x) for x in sorted((p[int(edge[0])], p[int(edge[1])])))


def action(p):
    result = []
    for a, b in HIDDEN:
        image = (edge_image(a, p), edge_image(b, p))
        if image in HIDDEN:
            result.append((HIDDEN.index(image), 1))
        else:
            assert image[::-1] in HIDDEN
            result.append((HIDDEN.index(image[::-1]), -1))
    return tuple(result)


def apply(v, a, q):
    out = [None] * 3
    for i, (j, sign) in enumerate(a):
        out[j] = sign * v[i] % q
    return tuple(out)


def weight(v, q):
    return prod(2 if k == 0 else comb(q, k) for k in v)


def orbit_partition(q, actions):
    unseen = set(product(range(q), repeat=3))
    result = []
    while unseen:
        v = min(unseen)
        orbit = {apply(v, a, q) for a in actions}
        assert orbit <= unseen
        unseen -= orbit
        assert len({weight(x, q) for x in orbit}) == 1
        result.append({
            'representative': list(v),
            'size': len(orbit),
            'mass': sum(weight(x, q) for x in orbit),
            'weight_per_state': weight(v, q),
        })
    return result


def verify():
    actions = [action(p) for p in permutations(VERTICES)]
    assert len(actions) == len(set(actions)) == 24
    expected = {
        tuple((perm[i], signs[i]) for i in range(3))
        for perm in permutations(range(3))
        for signs in product((-1, 1), repeat=3)
        if prod(signs) == 1
    }
    assert set(actions) == expected

    edge_pair_orbits = {
        frozenset(tuple(sorted((edge_image(a, p), edge_image(b, p))))
                  for p in permutations(VERTICES))
        for a, b in ALL_PAIRS
    }
    assert sorted(map(len, edge_pair_orbits)) == [3, 12]
    assert frozenset(tuple(sorted(h)) for h in HIDDEN) in edge_pair_orbits

    rows = []
    for q in range(2, 13):
        orbits = orbit_partition(q, actions)
        g = gcd(2, q)
        numerator = q**3 + 6*q*q + 8*q + 3*q*g*g + 6*g*g
        assert numerator % 24 == 0
        assert len(orbits) == numerator // 24
        assert sum(o['size'] for o in orbits) == q**3
        assert sum(o['mass'] for o in orbits) == 2**(3*q)
        fixed = sum(
            apply(v, a, q) == v
            for a in actions for v in product(range(q), repeat=3)
        )
        assert fixed == numerator
        rows.append({
            'q': q,
            'gcd_2_q': g,
            'orbits': len(orbits),
            'orbit_size_distribution': {
                str(k): sum(o['size'] == k for o in orbits)
                for k in sorted({o['size'] for o in orbits})
            },
            'source_total': str(2**(3*q)),
            'q3_witness_orbit_masses':
                sorted(o['mass'] for o in orbits) if q == 3 else None,
        })
    assert [(r['q'], r['orbits']) for r in rows if r['q'] in (2, 3, 4, 5)] == [
        (2, 4), (3, 5), (4, 11), (5, 14)
    ]
    assert next(r for r in rows if r['q'] == 3)['q3_witness_orbit_masses'] == [
        8, 72, 108, 108, 216
    ]
    assert any(apply((1, 0, 0), a, 3) == (2, 0, 0) for a in actions)
    assert (1 + 2) % 3 == 0 and (2 + 2) % 3 != 0

    return {
        'id': 'R762CI',
        'review': 'NOT_REVIEWED',
        'scope': 'Conditional K4 edge-label pair-area observer and exact N-BRC weights; native licensing not established',
        'group_order': len(actions),
        'group_signed_image': 'all even-sign signed permutations of three coordinates (D3)',
        'pair_orbit_sizes': sorted(map(len, edge_pair_orbits)),
        'hidden_pairs': [list(h) for h in HIDDEN],
        'burnside_formula': '(q^3+6*q^2+8*q+3*q*gcd(2,q)^2+6*gcd(2,q)^2)/24',
        'odd_q_formula': '(q+1)*(q+2)*(q+3)/24',
        'tested_q_inclusive': [2, 12],
        'named_guard_counterexample': {
            'q': 3, 'z': [1, 0, 0], 'z_prime': [2, 0, 0],
            'same_symmetry_orbit': True, 'query': '[z_0+2=0 mod 3]',
            'values': [True, False]
        },
        'rows': rows,
        'verification': '24 matrices, 15 pairs, 11 q-values, exhaustive orbit/fixed-point and positive mass checks',
    }


if __name__ == '__main__':
    data = json.dumps(verify(), ensure_ascii=False, sort_keys=True, indent=2) + '\n'
    if len(sys.argv) == 3 and sys.argv[1] == '--output':
        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            f.write(data)
    else:
        print(data, end='')
