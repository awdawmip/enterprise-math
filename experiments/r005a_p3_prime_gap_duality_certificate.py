#!/usr/bin/env python3
"""R005-A p=3 post-Axler prime-gap duality certificate.

Goal
----
Extend the p=3 danger-zone least-basis certificate beyond the endpoint of the
uniform Axler sufficient inequality.

For one basin:
    A = k^3
    U = (k+1)^3 - 1
    F = floor(sqrt(U))
    D = floor(sqrt(U/2))

Every danger witness q <= D has cofactor point x=A/q.  Since x>F, the witness
q is forced whenever the next prime b after x satisfies b <= U/q, equivalently

    b/x <= U/A = 1 + u(k).

Prime-gap duality
-----------------
If a<b are consecutive primes surrounding x (a < x < b), then failure of the
e=1 cofactor certificate is equivalent to

    q in (U/b, A/a].

In particular it requires the relative prime gap

    (b-a)/a > u(k).

Hence, on a whole k-range [K0,K1], if every consecutive-prime gap intersecting
the union of all uncertified cofactor x-bands obeys

    (b-a)/a <= min_{K0<=k<=K1} u(k) = u(K1),

then every danger witness is forced throughout the whole range.

The Axler n=3 theorem already handles x >= xcrit(k), where

    u(k) * log(x)^3 >= c_A,
    c_A = 0.0486680000822.

So only the broad union
    [ lower_union, upper_union ]
of x below xcrit needs exact finite prime-gap verification.

This script uses an exact segmented sieve. No probabilistic primality test.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, getcontext
from math import isqrt
import json

getcontext().prec = 70

AXLER_C = Decimal("0.0486680000822")
K0 = 494_035
K1 = 500_000
SEGMENT_SIZE = 1_000_000


def A(k: int) -> int:
    return k**3


def U(k: int) -> int:
    return (k + 1) ** 3 - 1


def D(k: int) -> int:
    return isqrt(U(k) // 2)


def u_decimal(k: int) -> Decimal:
    K = Decimal(k)
    return Decimal(3) / K + Decimal(3) / (K * K)


def L_decimal(k: int) -> Decimal:
    """Smooth lower bound <= A/D <= A/q for all danger q."""
    K = Decimal(k)
    uu = Decimal(U(k))
    return Decimal(2).sqrt() * (K**3) / uu.sqrt()


def xcrit_decimal(k: int) -> Decimal:
    """Axler n=3 crossover: u(k) log(x)^3 = c_A."""
    u = u_decimal(k)
    root = ((AXLER_C / u).ln() / Decimal(3)).exp()
    return root.exp()


def simple_primes(limit: int) -> list[int]:
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n in range(2, limit + 1) if flags[n]]


def segmented_primes(lo: int, hi: int, base_primes: list[int]):
    """Yield exact primes in inclusive [lo, hi]."""
    start = max(2, lo)
    for seg_lo in range(start, hi + 1, SEGMENT_SIZE):
        seg_hi = min(hi, seg_lo + SEGMENT_SIZE - 1)
        flags = bytearray(b"\x01") * (seg_hi - seg_lo + 1)
        for p in base_primes:
            if p * p > seg_hi:
                break
            first = max(p * p, ((seg_lo + p - 1) // p) * p)
            if first <= seg_hi:
                flags[first - seg_lo : seg_hi - seg_lo + 1 : p] = b"\x00" * (
                    (seg_hi - first) // p + 1
                )
        for offset, flag in enumerate(flags):
            if flag:
                yield seg_lo + offset


def previous_prime(n: int, base_primes: list[int]) -> int:
    """Exact predecessor using bounded local segmented windows."""
    width = 10_000
    hi = n - 1
    while hi >= 2:
        lo = max(2, hi - width + 1)
        ps = list(segmented_primes(lo, hi, base_primes))
        if ps:
            return ps[-1]
        hi = lo - 1
        width *= 2
    raise RuntimeError("no predecessor prime")


def next_prime(n: int, base_primes: list[int]) -> int:
    """Exact successor using bounded local segmented windows."""
    width = 10_000
    lo = n + 1
    while True:
        hi = lo + width - 1
        ps = list(segmented_primes(lo, hi, base_primes))
        if ps:
            return ps[0]
        lo = hi + 1
        width *= 2


def main() -> None:
    L_values = [L_decimal(k) for k in range(K0, K1 + 1)]
    X_values = [xcrit_decimal(k) for k in range(K0, K1 + 1)]
    assert all(a <= b for a, b in zip(L_values, L_values[1:]))
    assert all(a <= b for a, b in zip(X_values, X_values[1:]))

    lower_real = min(L_values)
    upper_real = max(X_values)
    lower = int(lower_real.to_integral_value(rounding=ROUND_FLOOR))
    upper = int(upper_real.to_integral_value(rounding=ROUND_CEILING))

    base_limit = isqrt(upper + 1_000_000) + 2
    base_primes = simple_primes(base_limit)

    pred = previous_prime(lower, base_primes)
    succ = next_prime(upper, base_primes)

    primes = [pred]
    primes.extend(segmented_primes(lower, upper, base_primes))
    if primes[-1] != succ:
        primes.append(succ)

    assert primes[0] < lower
    assert primes[-1] > upper
    assert all(a < b for a, b in zip(primes, primes[1:]))

    AK = A(K1)
    deltaK = U(K1) - AK

    max_gap = -1
    max_gap_pair = None
    max_ratio_num = None
    max_ratio_den = None
    violating = []

    for a, b in zip(primes, primes[1:]):
        gap = b - a
        if gap > max_gap:
            max_gap = gap
            max_gap_pair = (a, b)

        lhs = gap * AK
        rhs = a * deltaK
        if max_ratio_num is None or gap * max_ratio_den > max_ratio_num * a:
            max_ratio_num = gap
            max_ratio_den = a
        if lhs > rhs:
            violating.append((a, b, gap, lhs - rhs))

    assert not violating

    min_x_minus_F = None
    min_x_record = None
    for k in range(K0, K1 + 1):
        f = isqrt(U(k))
        d = D(k)
        margin = A(k) // d + 1 - f
        if min_x_minus_F is None or margin < min_x_minus_F:
            min_x_minus_F = margin
            min_x_record = (k, margin, f, d)
    assert min_x_minus_F is not None and min_x_minus_F > 0

    max_gap_a, max_gap_b = max_gap_pair
    result = {
        "status": (
            "R005-A P3 POST-AXLER PRIME-GAP DUALITY CERTIFICATE / "
            "EXACT SEGMENTED SIEVE / NOT CANONICAL"
        ),
        "k_range": [K0, K1],
        "cofactor_union": {
            "lower_floor": lower,
            "upper_ceil": upper,
            "width": upper - lower + 1,
            "predecessor_prime": pred,
            "successor_prime": succ,
            "prime_count_inside_union": len(primes) - 2,
        },
        "axler_crossover": {
            "xcrit_K0": str(X_values[0]),
            "xcrit_K1": str(X_values[-1]),
            "L_K0": str(L_values[0]),
            "L_K1": str(L_values[-1]),
        },
        "relative_gap_threshold": {
            "u_at_K1_exact_num": deltaK,
            "u_at_K1_exact_den": AK,
            "u_at_K1_decimal": str(Decimal(deltaK) / Decimal(AK)),
        },
        "max_absolute_gap": {
            "a": max_gap_a,
            "b": max_gap_b,
            "gap": max_gap,
        },
        "max_relative_gap": {
            "gap_num": max_ratio_num,
            "left_prime_den": max_ratio_den,
            "decimal": str(Decimal(max_ratio_num) / Decimal(max_ratio_den)),
        },
        "all_relative_gaps_within_threshold": True,
        "minimum_floor_A_over_D_plus_1_minus_F": {
            "k": min_x_record[0],
            "margin": min_x_record[1],
            "F": min_x_record[2],
            "D": min_x_record[3],
        },
        "conclusion": (
            "Every p=3 danger witness is forced for every integer "
            f"{K0}<=k<={K1}; combined with the prior certificate, "
            "the p=3 divisor-witness language has a unique least safe basis "
            "for every 2<=k<=500000."
        ),
        "duality": {
            "gap_form": (
                "for consecutive cofactor primes a<b, e=1 failure at witness q "
                "is equivalent to q in (U/b, A/a]"
            ),
            "necessary_relative_gap": "b/a > U/A",
        },
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
