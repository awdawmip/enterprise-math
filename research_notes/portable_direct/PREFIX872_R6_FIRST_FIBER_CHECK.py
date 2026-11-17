#!/usr/bin/env python3
"""PREFIX-872: exact first-fiber test of 19-bit p=32 endpoint observers.

All arithmetic is integer and applies only to the named-binary-source auxiliary
observer, not to native heartbeat evolution or numerical residual attribution.
"""
import json
from collections import Counter
from math import gcd

P, B = 32, 19
N, Q = 1 << P, (1 << B) - 1
G_CANDIDATES = (1, 3, 5, 7, 9, 11, 13, 15, 19, 21, 23, 25,
                27, 29, 35, 37, 39, 47, 49, 53, 55, 59, 61)


def legal(old, new):
    d = old ^ new
    return 0 <= old < N and 0 <= new < N and (d == 0 or d & (d - 1) == 0)


def first_fiber(q1, g):
    count = Counter()
    for old in range(0, N, q1):
        count[0] += 1  # unchanged transition
        for i in range(P):
            power = 1 << i
            new = old ^ power
            count[(new - old) % g] += 1
    return max((value, residue) for residue, value in count.items())


def collision(q1, q2, cap_old_rows=3000):
    seen = {}
    max_rows = min(cap_old_rows, (N - 1) // q1 + 1)
    for k in range(max_rows):
        old = k * q1
        for i in range(-1, P):
            new = old if i == -1 else old ^ (1 << i)
            r = new % q2
            if r in seen and seen[r] != (old, new):
                lhs = seen[r]
                rhs = (old, new)
                assert all(legal(*v) for v in (lhs, rhs))
                assert lhs[0] % q1 == rhs[0] % q1 == 0
                assert lhs[1] % q2 == rhs[1] % q2 == r
                assert lhs != rhs
                return {'k': k, 'r1': 0, 'r2': r,
                        'first': list(lhs), 'second': list(rhs)}
            seen[r] = (old, new)
    return None


def run():
    rows = []
    for g in G_CANDIDATES:
        A = Q // g
        if A % 2 == 0:
            A -= 1
        for orientation in ('higher_first', 'lower_first'):
            q1, q2 = (g*A, g*(A-2)) if orientation == 'higher_first' else (g*(A-2), g*A)
            assert q1 <= Q and q2 <= Q and gcd(q1, q2) == g
            maximum, residue = first_fiber(q1, g)
            capacity = q2 // g
            witness = collision(q1, q2)
            assert witness is not None, (g, orientation)
            rows.append({'g': g, 'orientation': orientation,
                         'q1': q1, 'q2': q2, 'fiber_r': 0,
                         'max_residue_a': residue,
                         'fiber_class_load': maximum,
                         'fiber_class_capacity': capacity,
                         'fiber_capacity_exceeded': maximum > capacity,
                         'first_collision': witness})
    excluded = [r['g'] for r in rows if r['orientation'] == 'higher_first' and r['fiber_capacity_exceeded']]
    assert excluded == [15, 21, 27, 35, 39]
    assert len(rows) == 46
    assert max(r['first_collision']['k'] for r in rows) == 2366
    return {'schema': 'PREFIX872_R6_FIRST_FIBER_CERTIFICATE_V1',
            'scope': 'auxiliary named binary sources, full one-flip/no-flip ordered transition',
            'frozen_scientific_input': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'p': P, 'peak_bits': B, 'N': N, 'Q': Q,
            'g_candidates': list(G_CANDIDATES),
            'ordered_extremal_pairs_checked': len(rows),
            'first_fiber_excluded_higher_first_g': excluded,
            'all_pairs_have_explicit_collision': True,
            'max_first_collision_old_row': 2366,
            'rows': rows,
            'verification': 'EXACT_INTEGER_ASSERTIONS_PASSED',
            'limitations': 'Only the two maximal odd-cofactor orientations for each surviving gcd; not all admissible 19-bit pairs or a global p=32 no-go.'}


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
