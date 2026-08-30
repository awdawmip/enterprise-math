#!/usr/bin/env python3
"""Exact regression for RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE.

This checker validates the task-local G_poly rank/support theorem on an exhaustive
2x2 affine slice and validates the polynomial-selector endpoint law.

It is intentionally finite evidence for the symbolic proof in the return; it is
not used as a substitute for the all-grammar theorem.
"""
from __future__ import annotations

import json
from itertools import combinations, product
from math import gcd

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23)
SEMIPRIMES = tuple((p, q, p * q) for p, q in combinations(PRIMES, 2))
A1_PATTERNS = (
    ((0, 0), (0, 0)),
    ((1, 0), (0, 0)),
    ((0, 1), (0, 0)),
    ((1, -1), (0, 1)),
    ((-1, 1), (1, 0)),
    ((1, 1), (-1, 1)),
    ((2, -1), (1, -2)),
    ((-2, 0), (1, 2)),
)


def det2(m: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def base_rank_and_delta(
    m: tuple[tuple[int, int], tuple[int, int]]
) -> tuple[int, int]:
    """Return Q-rank and its top determinantal divisor for a 2x2 integer matrix."""
    d = det2(m)
    if d != 0:
        return 2, abs(d)
    g = 0
    for row in m:
        for x in row:
            g = gcd(g, abs(x))
    if g != 0:
        return 1, g
    return 0, 0


def rank_mod(
    m: tuple[tuple[int, int], tuple[int, int]], prime: int
) -> int:
    a, b = (x % prime for x in m[0])
    c, d = (x % prime for x in m[1])
    if (a * d - b * c) % prime:
        return 2
    if any((a, b, c, d)):
        return 1
    return 0


def add_n_multiple(
    a0: tuple[tuple[int, int], tuple[int, int]],
    a1: tuple[tuple[int, int], tuple[int, int]],
    n: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(
        tuple(a0[i][j] + n * a1[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def proper_factor(n: int, d: int) -> bool:
    g = gcd(n, d)
    return g not in (1, n)


def main() -> int:
    matrix_templates = 0
    channel_checks = 0
    asymmetric_support_cases = 0
    support_mismatches = 0
    rank_distribution = {0: 0, 1: 0, 2: 0}

    for coeffs in product(range(-3, 4), repeat=4):
        a0 = ((coeffs[0], coeffs[1]), (coeffs[2], coeffs[3]))
        k, delta = base_rank_and_delta(a0)
        rank_distribution[k] += 1

        for a1 in A1_PATTERNS:
            matrix_templates += 1
            for p, q, n in SEMIPRIMES:
                m = add_n_multiple(a0, a1, n)

                # Exact N-erasure: A0 + N*A1 == A0 (mod N), entrywise.
                assert all(
                    (m[i][j] - a0[i][j]) % n == 0
                    for i in range(2)
                    for j in range(2)
                )

                rp = rank_mod(m, p)
                rq = rank_mod(m, q)
                assert rp == rank_mod(a0, p)
                assert rq == rank_mod(a0, q)

                if k == 0:
                    assert rp == rq == 0
                else:
                    # Rank-drop iff the hidden prime divides the top
                    # determinantal divisor of the N=0 specialization.
                    assert (rp < k) == (delta % p == 0)
                    assert (rq < k) == (delta % q == 0)
                    asymmetric = (rp < k) != (rq < k)
                    support_readout = proper_factor(n, delta)
                    asymmetric_support_cases += int(asymmetric)
                    support_mismatches += int(asymmetric != support_readout)

                channel_checks += 1

    selector_checks = 0
    nontrivial_selector_cases = 0
    selector_endpoint_mismatches = 0
    for c in range(-100, 101):
        for p, q, n in SEMIPRIMES:
            # Every fixed polynomial f(N) is congruent mod N to c=f(0).
            b = c % n
            idempotent = (b * b - b) % n == 0
            nontrivial = idempotent and b not in (0, 1)
            if nontrivial:
                nontrivial_selector_cases += 1
                endpoints = sorted((gcd(n, c), gcd(n, c - 1)))
                if endpoints != sorted((p, q)):
                    selector_endpoint_mismatches += 1
            selector_checks += 1

    # Three explicit mechanism controls.
    n = 15
    support_matrix = ((n + 3, 0), (0, 1))
    assert rank_mod(support_matrix, 3) == 1
    assert rank_mod(support_matrix, 5) == 2
    assert gcd(n, 3) == 3  # exact static-support readout

    for p, q, n in SEMIPRIMES:
        clean_matrix = ((n + 1, 0), (0, 1))
        assert rank_mod(clean_matrix, p) == 2
        assert rank_mod(clean_matrix, q) == 2

        bilateral = ((n, 0), (0, n))
        assert rank_mod(bilateral, p) == 0
        assert rank_mod(bilateral, q) == 0

    result = {
        "schema": "ENTERPRISE_MATH_N_COUPLED_ASYMMETRIC_SINGULARIZATION_CHECK_V1",
        "verdict": "PASS",
        "matrix_base_A0_count": 7 ** 4,
        "matrix_templates": matrix_templates,
        "channel_checks": channel_checks,
        "rank_distribution_base_A0": rank_distribution,
        "asymmetric_support_cases": asymmetric_support_cases,
        "support_mismatches": support_mismatches,
        "selector_checks": selector_checks,
        "nontrivial_selector_cases": nontrivial_selector_cases,
        "selector_endpoint_mismatches": selector_endpoint_mismatches,
        "explicit_controls": {
            "diag_N_plus_3": "ONE_SIDED_AT_N_15_BUT_GCD_SUPPORT_EQ_3",
            "diag_N_plus_1": "BILATERAL_INVERTIBLE_ON_ALL_TESTED_ODD_SEMIPRIMES",
            "N_times_identity": "BILATERAL_SINGULAR_ON_ALL_TESTED_ODD_SEMIPRIMES",
        },
    }
    assert support_mismatches == 0
    assert selector_endpoint_mismatches == 0
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
