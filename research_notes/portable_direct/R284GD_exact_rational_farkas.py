#!/usr/bin/env python3
"""R284GD: exact Farkas certificates for R284GC's unbounded-q six-condition lemma.

SciPy/HiGHS searches for coefficients only. Every returned certificate is
reconstructed as Fraction and checked in pure integer/rational arithmetic.
A passing branch is a mathematical contradiction for all real q>=5.

Run: python R284GD_exact_rational_farkas.py [--emit certificates.json]
"""
import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

from scipy.optimize import linprog

PATTERNS = range(1, 8)
PHASES = range(4)
HEAVY = (3, 5, 6)
ADJACENT = {(0, 1), (0, 3), (1, 2), (2, 3)}
BITS = {p: (0, p & 1, (p >> 1) & 1, (p >> 2) & 1)
        for p in PATTERNS}
LAST = {(p, i): next(e for e in ((i - 1 - t) % 4 for t in PHASES)
                      if BITS[p][e] != BITS[p][(e + 1) % 4])
        for p in PATTERNS for i in PHASES}
STAR_PAIRS = ((0, 1), (0, 2), (0, 3))
DISTANCE_PAIRS = ((1, 2), (1, 3), (2, 3))
EQUALITY = (-4, 1, 1, 1, 1, 1, 1, 1)  # E(q,x)=sum(x)-4q=k


def changed(pair):
    i, j = pair
    return tuple(p for p in PATTERNS if BITS[p][i] != BITS[p][j])


def star_cuts(pair):
    i, j = pair
    edges = [(p, LAST[p, i], 4 + LAST[p, j]) for p in changed(pair)]
    masks = {}
    for vertices in range(1, 256):
        mask = tuple(p for p, a, b in edges
                     if vertices & (1 << a) and vertices & (1 << b))
        if mask:
            masks[mask] = min(vertices.bit_count(), masks.get(mask, 9))
    return tuple(sorted(masks.items()))


def branch_constraints(cuts, light):
    """All constraints are a_i dot (q,x1..x7) >= b_i, integers only."""
    rows = []

    def lower(label, mask, q_coefficient, rhs):
        rows.append((label, (-q_coefficient,) + tuple(int(p in mask)
                                                    for p in PATTERNS), rhs))

    for pair in DISTANCE_PAIRS:
        lower('D' + ''.join(map(str, pair)), changed(pair), 2,
              5 if pair in ADJACENT else 3)
    for pair, (mask, vertex_count) in zip(STAR_PAIRS, cuts):
        lower('S' + ''.join(map(str, pair)) + ':' + ''.join(map(str, mask)),
              mask, vertex_count, 3)
    for p in light:
        rows.append(('L' + str(p), (2,) + tuple(-int(t == p)
                                                for t in PATTERNS), -1))
    rows.append(('Q5', (1,) + (0,) * 7, 5))
    for p in PATTERNS:
        rows.append(('X' + str(p), (0,) + tuple(int(t == p)
                                                for t in PATTERNS), 0))
    return rows


def rational_certificate(k, rows):
    """Farkas: sum lambda_i a_i + mu E=0, sum lambda_i b_i + mu*k > 0."""
    m = len(rows)
    eq = [[float(rows[i][1][j]) for i in range(m)] + [float(EQUALITY[j])]
          for j in range(8)]
    lower = [-float(rows[i][2]) for i in range(m)] + [-float(k)]
    found = linprog([1.0] * m + [0.0],
                    A_eq=eq, b_eq=[0.0] * 8,
                    A_ub=[lower], b_ub=[-1.0],
                    bounds=[(0, None)] * m + [(None, None)], method='highs')
    if found.status != 0:
        raise AssertionError(('candidate-search-not-solved', found.message))
    v = [Fraction(float(t)).limit_denominator(100000) for t in found.x]
    if any(z < 0 for z in v[:-1]):
        raise AssertionError('negative multiplier')
    if any(sum(v[i] * rows[i][1][j] for i in range(m))
           + v[-1] * EQUALITY[j] != 0 for j in range(8)):
        raise AssertionError('rational coefficients do not cancel exactly')
    rhs = sum(v[i] * rows[i][2] for i in range(m)) + v[-1] * k
    if rhs <= 0:
        raise AssertionError('rational contradiction is not strictly positive')
    return v, rhs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--emit', type=Path)
    args = ap.parse_args()
    stars = [star_cuts(pair) for pair in STAR_PAIRS]
    assert tuple(map(len, stars)) == (7, 9, 7)
    reports = []
    all_certificates = []
    for k in (8, 9):
        checked = 0
        largest_support = 0
        biggest_denominator = 1
        for idx in product(*(range(len(s)) for s in stars)):
            chosen = tuple(stars[j][idx[j]] for j in range(3))
            for light in combinations(HEAVY, 2):
                rows = branch_constraints(chosen, light)
                coefficients, rhs = rational_certificate(k, rows)
                checked += 1
                support = [(rows[i][0], str(z)) for i, z in enumerate(coefficients[:-1]) if z]
                largest_support = max(largest_support, len(support))
                biggest_denominator = max(biggest_denominator,
                                          *(v.denominator for v in coefficients))
                if args.emit:
                    all_certificates.append({'k': k, 'star_indices': idx,
                                             'light': light, 'lambda': support,
                                             'mu': str(coefficients[-1]),
                                             'contradiction': str(rhs)})
        assert checked == 7 * 9 * 7 * 3 == 1323
        reports.append((k, checked, largest_support, biggest_denominator))
    if args.emit:
        args.emit.write_text(json.dumps({
            'schema': 'R284GD_EXACT_RATIONAL_FARKAS_V1',
            'variable_order': ['q'] + [f'x{p}' for p in PATTERNS],
            'star_order': ['01', '02', '03'],
            'star_masks': [[list(mask) + [size] for mask, size in s] for s in stars],
            'certificates': all_certificates}, ensure_ascii=False,
            separators=(',', ':')) + '\n')
    for k, count, support, denom in reports:
        print(f'k={k}: {count} exact rational Farkas certificates verified; '
              f'max-support={support}; max-denominator={denom}')
    print('PASS: 2646 exact contradiction certificates for all real q>=5, '
          'k=8,9 and every reduced six-condition non-heavy branch')


if __name__ == '__main__':
    main()
