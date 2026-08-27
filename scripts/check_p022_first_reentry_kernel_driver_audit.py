#!/usr/bin/env python3
"""Independent Driver-side replay of the P022 q=3r-1 kernel reduction.

This script imports no P022 implementation module. It checks, for every
twin-boundary candidate q=18m-1 below LIMIT, that the Franel recurrence,
the integer terminating kernel S_m, and the fixed rational-parameter reverse
kernel R_m(q) have the same zero/nonzero status modulo q.

The finite range is falsification/regression evidence only. It does not prove
all-m nonvanishing.
"""
from __future__ import annotations

import json
from math import isqrt

LIMIT = 200_000


def sieve(limit: int) -> bytearray:
    prime = bytearray(b"\x01") * (limit + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            start = p * p
            prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return prime


def franel_mod(prime: int, n: int) -> int:
    """F_n mod p from n^2 F_n=(7n^2-7n+2)F_{n-1}+8(n-1)^2F_{n-2}."""
    if n == 0:
        return 1
    previous_previous = 1
    previous = 2 % prime
    if n == 1:
        return previous
    for k in range(2, n + 1):
        numerator = (
            (7 * k * k - 7 * k + 2) * previous
            + 8 * (k - 1) * (k - 1) * previous_previous
        ) % prime
        current = numerator * pow(k * k % prime, -1, prime) % prime
        previous_previous, previous = previous, current
    return previous


def integer_kernel_mod(m: int, prime: int) -> int:
    """S_m = sum (-1)^k C(3m,k)C(6m+k-1,k)C(6m+k,k) mod q."""
    term = 1
    total = 1
    for k in range(0, 3 * m):
        numerator = (-(3 * m - k) * (6 * m + k) * (6 * m + k + 1)) % prime
        denominator = pow(k + 1, 3, prime)
        term = term * numerator % prime * pow(denominator, -1, prime) % prime
        total = (total + term) % prime
    return total


def reverse_kernel_mod(m: int, prime: int) -> int:
    """R_m(q)=sum (-1/6)_j^3/((1/2)_j(-1/2)_j j!) mod q."""
    inverse_two = pow(2, -1, prime)
    inverse_six = pow(6, -1, prime)
    term = 1
    total = 1
    for j in range(0, 3 * m):
        numerator = pow((j - inverse_six) % prime, 3, prime)
        denominator = (
            (j + inverse_two)
            * (j - inverse_two)
            * (j + 1)
        ) % prime
        term = term * numerator % prime * pow(denominator, -1, prime) % prime
        total = (total + term) % prime
    return total


def main() -> None:
    prime = sieve(LIMIT + 1)
    candidates = 0
    survivor_candidates = 0
    franel_zeros = 0
    integer_kernel_zeros = 0
    reverse_kernel_zeros = 0
    zero_status_mismatches: list[dict[str, int]] = []

    for m in range(1, (LIMIT + 1) // 18 + 1):
        q = 18 * m - 1
        if q >= LIMIT:
            break
        if not (prime[q] and prime[12 * m - 1] and prime[12 * m + 1]):
            continue

        candidates += 1
        if q % 72 in (17, 35):
            survivor_candidates += 1

        f = franel_mod(q, 6 * m)
        s = integer_kernel_mod(m, q)
        r = reverse_kernel_mod(m, q)

        if f == 0:
            franel_zeros += 1
        if s == 0:
            integer_kernel_zeros += 1
        if r == 0:
            reverse_kernel_zeros += 1

        if not ((f == 0) == (s == 0) == (r == 0)):
            zero_status_mismatches.append(
                {"m": m, "q": q, "franel": f, "integer_kernel": s, "reverse_kernel": r}
            )

    result = {
        "schema": "P022_FIRST_REENTRY_KERNEL_DRIVER_AUDIT_V1",
        "limit_exclusive": LIMIT,
        "boundary_condition": "q=18m-1, 12m-1 prime, 12m+1 prime",
        "boundary_candidates": candidates,
        "survivor_classes_mod_72": [17, 35],
        "survivor_candidates": survivor_candidates,
        "franel_zeros": franel_zeros,
        "integer_kernel_zeros": integer_kernel_zeros,
        "reverse_kernel_zeros": reverse_kernel_zeros,
        "zero_status_mismatches": zero_status_mismatches,
        "status": (
            "PASS"
            if not zero_status_mismatches
            and franel_zeros == integer_kernel_zeros == reverse_kernel_zeros == 0
            else "FAIL"
        ),
        "role": "FINITE_REGRESSION_ONLY_NOT_A_PROOF",
        "independence": "No P022 implementation import; recurrence and both kernels rebuilt directly",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
