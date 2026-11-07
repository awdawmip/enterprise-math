#!/usr/bin/env python3
"""Exact finite audit of the fixed-scalar F7 A6 index/exponent count.

Counts ordered positive multipliers, not the 80,621,568 torsion/sign/permutation
choices individually. The unrestricted theorem is in COUNT_INDEX_EXPONENT.md.
"""
from collections import Counter
from math import comb, lcm
import json

CONST = 16 * (2 ** 4) * 48 * (3 ** 8)


def factorization(n):
    f = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(n):
    return tuple(x for x in range(1, n + 1) if n % x == 0)


def quadruples_of_product(m):
    for a in divisors(m):
        for b in divisors(m // a):
            for c in divisors(m // (a * b)):
                yield a, b, c, m // (a * b * c)


def bounded_sum(e, t):
    # coefficient x^e of (1+x+...+x^t)^4.
    if t < 0:
        return 0
    dp = [1] + [0] * e
    for _ in range(4):
        dp = [sum(dp[j - r] for r in range(min(t, j) + 1)) for j in range(e + 1)]
    return dp[e]


def local_count(e, t):
    return bounded_sum(e, t) - bounded_sum(e, t - 1)


def predicted(m, L):
    fm = factorization(m)
    fl = factorization(L)
    value = 1
    for p, e in fm.items():
        value *= local_count(e, fl.get(p, 0))
    return value if all(p in fm for p in fl) else 0


def run():
    total = 0
    nonzero_pairs = 0
    max_m = 128
    example_32 = {}
    for m in range(1, max_m + 1):
        exact = Counter(lcm(*ks) for ks in quadruples_of_product(m))
        expected_total = 1
        for e in factorization(m).values():
            expected_total *= comb(e + 3, 3)
        assert sum(exact.values()) == expected_total, (m, exact, expected_total)
        for L in divisors(m):
            actual = exact.get(L, 0)
            expected = predicted(m, L)
            assert actual == expected, (m, L, actual, expected)
            nonzero_pairs += (actual > 0)
        if m == 32:
            example_32 = dict(sorted(exact.items()))
        total += expected_total
    assert CONST == 80621568
    assert example_32 == {4: 16, 8: 24, 16: 12, 32: 4}, example_32
    return {
        'status': 'PASS',
        'fixed_group_scalar_multiplier': CONST,
        'index_parameter_range': [1, max_m],
        'ordered_positive_multiplier_quadruples': total,
        'distinct_valid_index_exponent_pairs': nonzero_pairs,
        'example_m_32_lcm_multiplicities': example_32,
        'complete_coverage_of_declared_finite_domain': True,
        'unrestricted_formula_status': 'proved algebraically in companion Markdown, not by enumeration',
        'scope': 'AUTHOR_SIDE_NOT_INDEPENDENT_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE'
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
