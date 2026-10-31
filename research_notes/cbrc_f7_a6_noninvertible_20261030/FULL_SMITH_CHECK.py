#!/usr/bin/env python3
"""Exact finite regression for F7 A6 arbitrary-index Smith/exponent theorem.

No external dependencies. Universal proof: FULL_SMITH_AND_EXPONENT.md.
"""
from itertools import combinations, permutations, product
from math import gcd, lcm, prod
import json

D = ((1, 1, 0, 0), (1, -1, 0, 0), (0, 0, 1, 1), (0, 0, 1, -1))
MULTIPLIERS = (-3, -2, -1, 1, 2, 3)


def mul(x, y):
    return tuple(
        tuple(sum(x[i][h] * y[h][j] for h in range(len(y)))
              for j in range(len(y[0]))) for i in range(len(x))
    )


def det_minor(a, rows, cols):
    n = len(rows)
    return sum(
        (-1) ** sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        * prod(a[rows[i]][cols[p[i]]] for i in range(n))
        for p in permutations(range(n))
    )


def divisors(a):
    return tuple(
        gcd(*(det_minor(a, rows, cols)
              for rows in combinations(range(4), j)
              for cols in combinations(range(4), j)))
        for j in range(1, 5)
    )


def split_permutations():
    # p[i] = input channel occupying output channel row i.
    for p in permutations(range(4)):
        output_row = {j: p.index(j) for j in range(4)}
        if ((output_row[0] < 2) != (output_row[1] < 2)
                and (output_row[2] < 2) != (output_row[3] < 2)):
            yield p


def slot_order_weights(p, k):
    output_row = {j: p.index(j) for j in range(4)}
    ordered = []
    for pair in ((0, 1), (2, 3)):
        ordered.append(k[next(j for j in pair if output_row[j] < 2)])
        ordered.append(k[next(j for j in pair if output_row[j] >= 2)])
    return ordered


def predicted_divisors(a, b, c, d):
    return (
        gcd(a, b, c, d),
        gcd(2 * a * b, 2 * a * c, 2 * b * d, 2 * c * d,
            a * d + b * c, a * d - b * c),
        4 * gcd(a * b * c, a * b * d, a * c * d, b * c * d),
        16 * abs(a * b * c * d),
    )


def check():
    n = 0
    patterns = list(split_permutations())
    assert len(patterns) == 16
    smith_types = set()
    for p in patterns:
        for k in product(MULTIPLIERS, repeat=4):
            weighted_p = tuple(tuple(k[j] if p[i] == j else 0
                                      for j in range(4)) for i in range(4))
            a_matrix = mul(mul(D, weighted_p), D)
            a, b, c, d = slot_order_weights(p, k)
            expected = predicted_divisors(a, b, c, d)
            observed = divisors(a_matrix)
            assert observed == expected, (p, k, observed, expected)
            s1, s2, s3, s4 = (expected[0], expected[1] // expected[0],
                              expected[2] // expected[1], expected[3] // expected[2])
            assert expected[1] % expected[0] == 0
            assert expected[2] % expected[1] == 0
            assert expected[3] % expected[2] == 0
            assert s2 % s1 == 0 and s3 % s2 == 0 and s4 % s3 == 0
            assert s4 == 4 * lcm(*(abs(x) for x in k))
            if all(abs(x) == 1 for x in k):
                assert (s1, s2, s3, s4) == (1, 2, 2, 4)
            smith_types.add((s1, s2, s3, s4))
            n += 1
    return {
        'status': 'PASS',
        'permutations': len(patterns),
        'multiplier_values': list(MULTIPLIERS),
        'multiplier_tuples_per_permutation': len(MULTIPLIERS) ** 4,
        'matrices_exactly_checked': n,
        'distinct_smith_types_observed': len(smith_types),
        'checked': ['all determinantal divisors 1-4',
                    'Smith divisibility and formula',
                    'cokernel exponent 4*lcm',
                    'unit-multiplier minimum-index corollary'],
        'scope': 'finite regression, not universal proof or Source review',
        'status_note': 'AUTHOR_SIDE_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE',
    }


if __name__ == '__main__':
    print(json.dumps(check(), indent=2, ensure_ascii=False))
