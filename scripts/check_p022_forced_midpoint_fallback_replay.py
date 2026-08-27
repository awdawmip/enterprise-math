#!/usr/bin/env python3
"""Independent exact-integer regression for the P022 forced-midpoint replay.

This checker intentionally rebuilds the Franel recurrence and the canonical
central-binomial relation without importing the P022 implementation under test.
It is finite falsification evidence only; the general theorem is the exact
support/valuation argument recorded in the research return.
"""

from __future__ import annotations

import json
from functools import lru_cache


LIMIT = 50_000


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    d = 3
    while d * d <= value:
        if value % d == 0:
            return False
        d += 2
    return True


def factor_integer(value: int) -> tuple[tuple[int, int], ...]:
    remaining = value
    output: list[tuple[int, int]] = []
    p = 2
    while p * p <= remaining:
        e = 0
        while remaining % p == 0:
            remaining //= p
            e += 1
        if e:
            output.append((p, e))
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        output.append((remaining, 1))
    return tuple(output)


def freeze(values: dict[int, int]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted((i, e) for i, e in values.items() if e))


@lru_cache(maxsize=None)
def integer_in_central_binomial_basis(value: int) -> tuple[tuple[int, int], ...]:
    if value == 1:
        return ()
    if value == 2:
        return ((1, 1),)
    output: dict[int, int] = {}
    for prime, multiplicity in factor_integer(value):
        if prime == 2:
            output[1] = output.get(1, 0) + multiplicity
            continue
        j = (prime + 1) // 2
        prime_rep: dict[int, int] = {}
        for index, exponent in integer_in_central_binomial_basis(j):
            prime_rep[index] = prime_rep.get(index, 0) + exponent
        prime_rep[1] = prime_rep.get(1, 0) - 1
        prime_rep[j] = prime_rep.get(j, 0) + 1
        prime_rep[j - 1] = prime_rep.get(j - 1, 0) - 1
        for index, exponent in freeze(prime_rep):
            output[index] = output.get(index, 0) + multiplicity * exponent
            if output[index] == 0:
                del output[index]
    return freeze(output)


def composite_relation(segment: int) -> tuple[tuple[int, int], ...]:
    if is_prime(2 * segment - 1):
        raise ValueError("segment has a prime odd boundary")
    output: dict[int, int] = {segment - 1: 1, 1: 1}
    for index, exponent in integer_in_central_binomial_basis(2 * segment - 1):
        output[index] = output.get(index, 0) + exponent
        if output[index] == 0:
            del output[index]
    for index, exponent in integer_in_central_binomial_basis(segment):
        output[index] = output.get(index, 0) - exponent
        if output[index] == 0:
            del output[index]
    frozen = freeze(output)
    if any(index >= segment for index, _ in frozen):
        raise AssertionError("relation lost triangularity")
    return frozen


def franel_mod_table(prime: int, max_index: int) -> list[int]:
    """F_n mod p via n^2 F_n=(7n^2-7n+2)F_(n-1)+8(n-1)^2F_(n-2)."""
    values = [0] * (max_index + 1)
    values[0] = 1
    if max_index:
        values[1] = 2 % prime
    for n in range(2, max_index + 1):
        numerator = (
            (7 * n * n - 7 * n + 2) * values[n - 1]
            + 8 * (n - 1) * (n - 1) * values[n - 2]
        ) % prime
        values[n] = numerator * pow(n * n, -1, prime) % prime
    return values


def is_twin_center(rank: int) -> bool:
    return rank >= 2 and is_prime(2 * rank - 1) and is_prime(2 * rank + 1)


def main() -> None:
    target_primes = 0
    prime_midpoint_support_cases = 0
    primitive_twin_first_zero_cases = 0
    bounded_cases = 0
    bounded_capture_cases: list[dict[str, int | bool]] = []
    failures: list[object] = []

    for q in range(7, LIMIT):
        if not is_prime(q) or q % 24 not in (5, 23):
            continue
        target_primes += 1
        m = (q - 1) // 2
        bound = (q + 1) // 6
        relation = composite_relation(m)
        high = tuple((i, e) for i, e in relation if i > bound)

        if q % 24 == 23 and is_prime(m):
            prime_midpoint_support_cases += 1
            half = (m + 1) // 2
            expected_high = ((half - 1, 1), (half, -1), (m - 1, 1))
        else:
            expected_high = ((m - 1, 1),)
        if high != expected_high:
            failures.append(["support", q, high, expected_high])
            continue

        table = franel_mod_table(q, m)
        if table[m] != 0:
            failures.append(["forced_midpoint", q, table[m]])
            continue
        rank = next(i for i in range(1, m + 1) if table[i] == 0)
        if not is_twin_center(rank):
            continue
        primitive_twin_first_zero_cases += 1
        if q >= 6 * rank - 1:
            continue
        bounded_cases += 1

        if not bound < rank:
            failures.append(["range_equivalence", q, rank, bound])
            continue
        if table[m - 1] == 0:
            failures.append(["adjacent_midpoint_zero", q, m])
            continue
        if any(i <= bound and table[i] == 0 for i, _ in relation):
            failures.append(["primitive_small_support", q, rank, m])
            continue

        location = m
        dangerous_used = False
        if q % 24 == 23 and is_prime(m):
            half = (m + 1) // 2
            dangerous = half - 1
            if table[dangerous] == 0:
                dangerous_used = True
                if not rank + 2 <= dangerous < 2 * rank - 1:
                    failures.append(["dangerous_blackout", q, rank, dangerous])
                    continue
                odd_boundary = 2 * dangerous - 1
                if not (
                    odd_boundary == m - 2
                    and odd_boundary > 3
                    and odd_boundary % 3 == 0
                    and not is_prime(odd_boundary)
                    and table[dangerous - 1] != 0
                ):
                    failures.append(["dangerous_boundary", q, rank, dangerous])
                    continue
                location = dangerous

        bounded_capture_cases.append(
            {
                "q": q,
                "primitive_rank": rank,
                "midpoint": m,
                "small_support_bound": bound,
                "capture_no_later_than": location,
                "dangerous_branch_used": dangerous_used,
            }
        )

    result = {
        "schema": "P022_FORCED_MIDPOINT_FALLBACK_INDEPENDENT_REPLAY_V1",
        "limit_exclusive": LIMIT,
        "target_prime_classes": [5, 23],
        "modulus": 24,
        "target_primes_tested": target_primes,
        "prime_midpoint_special_support_cases": prime_midpoint_support_cases,
        "primitive_twin_first_zero_cases": primitive_twin_first_zero_cases,
        "bounded_q_lt_6r_minus_1_cases": bounded_cases,
        "bounded_captures_verified": len(bounded_capture_cases),
        "bounded_capture_cases": bounded_capture_cases,
        "failures": failures,
        "status": "PASS" if not failures and len(bounded_capture_cases) == bounded_cases else "FAIL",
        "role": "FINITE_REGRESSION_ONLY_NOT_A_PROOF",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
