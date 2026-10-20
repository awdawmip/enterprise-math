#!/usr/bin/env python3
"""Independent exact checker for the high-dimensional prime-wall task.

This file intentionally uses only the frozen statement packet and Python's
standard library.  It computes the support spectrum from the defining ordered
positive-square convolution, then constructs every other quantity from that
spectrum.  Arithmetic-function formulas are evaluated separately and compared
only after both sides have been built.
"""

from __future__ import annotations

import argparse
import json
from math import comb, isqrt
from typing import Iterable


Q4_COEFFICIENTS = {4: 2, 3: -4, 2: 3}
Q4_NEGATIVE_CONTROL_COEFFICIENTS = {4: 2, 3: -4, 2: 4}
Q8_COEFFICIENTS = {
    8: 16,
    7: -64,
    6: 112,
    5: -112,
    4: 70,
    3: -28,
    2: 7,
}


def positive_square_spectrum(max_s: int, max_n: int) -> list[list[int]]:
    """Return A_s(n), including the useful A_0(0)=1 identity row."""
    squares = [m * m for m in range(1, isqrt(max_n) + 1)]
    a = [[0] * (max_n + 1) for _ in range(max_s + 1)]
    a[0][0] = 1
    for s in range(1, max_s + 1):
        for n in range(max_n + 1):
            a[s][n] = sum(a[s - 1][n - square] for square in squares if square <= n)
    return a


def support_shell(a: list[list[int]], d: int, n: int) -> int:
    """C_d(n) from the packet's support decomposition."""
    return sum(comb(d, s) * a[s][n] for s in range(1, d + 1))


def weighted_shell(a: list[list[int]], d: int, lam: int, n: int) -> int:
    """W_{d,lambda}(n), extended by W(0)=1."""
    if n == 0:
        return 1
    return sum(comb(d, s) * a[s][n] * lam**s for s in range(1, d + 1))


def direct_nonnegative_shell(d: int, max_n: int) -> list[int]:
    """Coefficient DP for (1+S(q))^d, independent of support assembly."""
    squares = [0] + [m * m for m in range(1, isqrt(max_n) + 1)]
    row = [0] * (max_n + 1)
    row[0] = 1
    for _ in range(d):
        nxt = [0] * (max_n + 1)
        for subtotal, count in enumerate(row):
            if count:
                for square in squares:
                    if subtotal + square <= max_n:
                        nxt[subtotal + square] += count
        row = nxt
    return row


def direct_weighted_shell(d: int, lam: int, max_n: int) -> list[int]:
    """Coefficient DP for (1+lambda*S(q))^d."""
    positive_squares = [m * m for m in range(1, isqrt(max_n) + 1)]
    row = [0] * (max_n + 1)
    row[0] = 1
    for _ in range(d):
        nxt = row.copy()  # choose zero in the new coordinate
        for subtotal, count in enumerate(row):
            if count:
                for square in positive_squares:
                    if subtotal + square <= max_n:
                        nxt[subtotal + square] += lam * count
        row = nxt
    return row


def linear_wall(c_rows: list[list[int]], coefficients: dict[int, int], n: int) -> int:
    return sum(coefficient * c_rows[d][n] for d, coefficient in coefficients.items())


def divisors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
    return small + large[::-1]


def sigma(n: int, power: int) -> int:
    return sum(d**power for d in divisors(n))


def square_indicator(n: int) -> int:
    return int(isqrt(n) ** 2 == n)


def r4_divisor_formula(n: int) -> int:
    return 8 * sum(d for d in divisors(n) if d % 4 != 0)


def r8_divisor_formula(n: int) -> int:
    return 16 * sum(((-1) ** (n + d)) * d**3 for d in divisors(n))


def eta_2z_power_12(max_n: int) -> list[int]:
    """Coefficients a(n) of eta(2z)^12=q*prod_(m>=1)(1-q^(2m))^12."""
    product = [0] * max_n
    product[0] = 1
    for m in range(1, (max_n - 1) // 2 + 1):
        step = 2 * m
        factor = [(j * step, comb(12, j) * ((-1) ** j)) for j in range(13)]
        nxt = [0] * max_n
        for degree, coefficient in enumerate(product):
            if coefficient:
                for shift, factor_coefficient in factor:
                    if degree + shift < max_n:
                        nxt[degree + shift] += coefficient * factor_coefficient
        product = nxt
    result = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        result[n] = product[n - 1]
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def convolve_at(left: list[int], right: list[int], n: int) -> int:
    return sum(left[k] * right[n - k] for k in range(n + 1))


def first_mismatch(pairs: Iterable[tuple[int, int, int]]) -> dict[str, int] | None:
    for n, left, right in pairs:
        if left != right:
            return {"n": n, "left": left, "right": right}
    return None


def run(max_n: int) -> dict[str, object]:
    if max_n < 125:
        raise ValueError("max_n must be at least 125 to exercise every pressure class")

    a = positive_square_spectrum(12, max_n)
    c_rows = [[0] * (max_n + 1) for _ in range(13)]
    for d in range(1, 13):
        c_rows[d] = [1] + [support_shell(a, d, n) for n in range(1, max_n + 1)]

    # H1: compare support assembly against a direct nonnegative-coordinate DP.
    h1_mismatches: list[dict[str, int]] = []
    for d in range(1, 13):
        direct = direct_nonnegative_shell(d, max_n)
        mismatch = first_mismatch((n, c_rows[d][n], direct[n]) for n in range(max_n + 1))
        if mismatch:
            mismatch["d"] = d
            h1_mismatches.append(mismatch)

    # H2: the carrier recoloring action multiplies the support-grade weight.
    h2_mismatch = first_mismatch(
        (
            n,
            weighted_shell(a, d=7, lam=6, n=n),
            sum(comb(7, s) * a[s][n] * (2**s) * (3**s) for s in range(1, 8)),
        )
        for n in range(1, max_n + 1)
    )

    # H3: include W(0)=1 on both sides of the additive convolution.
    h3_mismatches: list[dict[str, int]] = []
    for d, e, lam in ((1, 2, 2), (3, 4, -2), (4, 4, 3)):
        left = [weighted_shell(a, d, lam, n) for n in range(max_n + 1)]
        right = [weighted_shell(a, e, lam, n) for n in range(max_n + 1)]
        total = [weighted_shell(a, d + e, lam, n) for n in range(max_n + 1)]
        mismatch = first_mismatch(
            (n, total[n], convolve_at(left, right, n)) for n in range(max_n + 1)
        )
        if mismatch:
            mismatch.update({"d": d, "e": e, "lambda": lam})
            h3_mismatches.append(mismatch)

    # H4: cross-multiplied fixed-face survival identity, avoiding fractions.
    h4_mismatches: list[dict[str, int]] = []
    for d in range(2, 13):
        for n in range(1, max_n + 1):
            total = c_rows[d][n]
            if total == 0:
                continue
            support_sum = sum(s * comb(d, s) * a[s][n] for s in range(1, d + 1))
            left = d * c_rows[d - 1][n]
            right = d * total - support_sum
            if left != right:
                h4_mismatches.append({"d": d, "n": n, "left": left, "right": right})
                break

    q4 = [0] * (max_n + 1)
    q8 = [0] * (max_n + 1)
    q4_bad = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        q4[n] = linear_wall(c_rows, Q4_COEFFICIENTS, n)
        q8[n] = linear_wall(c_rows, Q8_COEFFICIENTS, n)
        q4_bad[n] = linear_wall(c_rows, Q4_NEGATIVE_CONTROL_COEFFICIENTS, n)

    # Signed-coordinate counts are computed from W independently of the walls.
    signed = {d: direct_weighted_shell(d, 2, max_n) for d in (4, 8, 12)}
    wall_signed_mismatch = {
        "d4": first_mismatch(
            (n, signed[4][n], 8 * (q4[n] - square_indicator(n)))
            for n in range(1, max_n + 1)
        ),
        "d8": first_mismatch(
            (n, signed[8][n], 16 * (q8[n] - square_indicator(n)))
            for n in range(1, max_n + 1)
        ),
    }

    arithmetic_mismatch = {
        "r4_all_n": first_mismatch(
            (n, signed[4][n], r4_divisor_formula(n)) for n in range(1, max_n + 1)
        ),
        "r8_all_n": first_mismatch(
            (n, signed[8][n], r8_divisor_formula(n)) for n in range(1, max_n + 1)
        ),
        "q4_odd": first_mismatch(
            (n, q4[n], sigma(n, 1) + square_indicator(n))
            for n in range(1, max_n + 1, 2)
        ),
        "q8_odd": first_mismatch(
            (n, q8[n], sigma(n, 3) + square_indicator(n))
            for n in range(1, max_n + 1, 2)
        ),
    }

    prime_wall_mismatch = {
        "q4": first_mismatch(
            (n, int(is_prime(n)), int(q4[n] == n + 1))
            for n in range(3, max_n + 1, 2)
        ),
        "q8": first_mismatch(
            (n, int(is_prime(n)), int(q8[n] == n**3 + 1))
            for n in range(3, max_n + 1, 2)
        ),
    }

    semiprime_examples = []
    for p, q in ((3, 5), (3, 7), (5, 11), (7, 13)):
        n = p * q
        if n <= max_n:
            semiprime_examples.append(
                {
                    "n": n,
                    "p": p,
                    "q": q,
                    "q4_excess": q4[n] - (n + 1),
                    "expected": p + q,
                }
            )

    pressure_values = {
        "prime_powers": [n for n in (9, 25, 27, 49, 81, 121, 125) if n <= max_n],
        "two_distinct_primes": [n for n in (15, 21, 35, 55, 77, 91) if n <= max_n],
        "three_distinct_primes": [n for n in (105, 165, 195, 231, 255) if n <= max_n],
        "four_adic": [n for n in (4, 8, 12, 16, 20, 28, 32, 36, 48, 64) if n <= max_n],
    }
    pressure = {
        category: [
            {
                "n": n,
                "q4": q4[n],
                "q8": q8[n],
                "r4_div8": r4_divisor_formula(n) // 8,
                "r8_div16": r8_divisor_formula(n) // 16,
                "square_indicator": square_indicator(n),
            }
            for n in values
        ]
        for category, values in pressure_values.items()
    }

    negative_control_failure = first_mismatch(
        (n, q4_bad[n], sigma(n, 1) + square_indicator(n))
        for n in range(3, max_n + 1, 2)
    )

    # H7 coefficient-level criterion on the prime-admissible nonsquare grades 2,3,4.
    q4_support_weights = {2: 3, 3: 4, 4: 2}
    h7_lambdas = []
    for lam in range(-20, 21):
        if lam == 0:
            continue
        weighted = {s: comb(4, s) * lam**s for s in (2, 3, 4)}
        cross_products = {
            weighted[s] * q4_support_weights[t]
            for s in (2, 3, 4)
            for t in (2, 3, 4)
            if s != t
        }
        # Pairwise proportionality is checked explicitly below; the set above is retained
        # only to keep this block visibly coefficient-level.
        proportional = all(
            weighted[s] * q4_support_weights[2]
            == weighted[2] * q4_support_weights[s]
            for s in (3, 4)
        )
        if proportional:
            h7_lambdas.append(lam)
        assert cross_products  # negative guard against an accidentally empty grade set

    eta12 = eta_2z_power_12(max_n)
    h8_odd_mismatch = first_mismatch(
        (n, signed[12][n], 8 * sigma(n, 5) + 16 * eta12[n])
        for n in range(1, max_n + 1, 2)
    )

    failures = {
        "h1": h1_mismatches,
        "h2": h2_mismatch,
        "h3": h3_mismatches,
        "h4": h4_mismatches,
        "wall_signed": wall_signed_mismatch,
        "arithmetic": arithmetic_mismatch,
        "prime_walls": prime_wall_mismatch,
        "h8_odd": h8_odd_mismatch,
    }
    if any(
        value
        for group in failures.values()
        for value in (group.values() if isinstance(group, dict) else [group])
    ):
        raise AssertionError(json.dumps(failures, sort_keys=True))
    if any(example["q4_excess"] != example["expected"] for example in semiprime_examples):
        raise AssertionError("semiprime excess mismatch")
    if h7_lambdas != [2]:
        raise AssertionError(f"H7 integer scan mismatch: {h7_lambdas}")
    if not negative_control_failure:
        raise AssertionError("negative control did not fail")

    return {
        "schema": "HIGHDIM_PRIME_WALL_FILTER_EQUIVALENCE_CHECK_V1",
        "max_n": max_n,
        "max_d": 12,
        "definition_checks": {
            "H1_support_decomposition": "PASS",
            "H2_support_grade_recoloring": "PASS",
            "H3_dimension_convolution_with_n0": "PASS",
            "H4_fixed_face_cross_multiplication": "PASS",
        },
        "wall_checks": {
            "signed_wall_relation_all_n": "PASS",
            "divisor_formula_all_n": "PASS",
            "odd_q4_sigma1_plus_square": "PASS",
            "odd_q8_sigma3_plus_square": "PASS",
            "prime_biconditionals": "PASS",
            "semiprime_excess": semiprime_examples,
        },
        "lambda2_coefficient_criterion": {
            "integer_scan_domain": [-20, 20],
            "nonzero_solutions": h7_lambdas,
            "symbolic_equations": ["2*lambda^2=lambda^3", "lambda^3=lambda^4/2"],
        },
        "twelve_square_odd_identity": "PASS",
        "negative_control": {
            "coefficients": Q4_NEGATIVE_CONTROL_COEFFICIENTS,
            "first_failure": negative_control_failure,
        },
        "pressure": pressure,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=512)
    args = parser.parse_args()
    print(json.dumps(run(args.max_n), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
