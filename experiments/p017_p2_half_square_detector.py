"""Finite verifier for the sharp P017 half-visible/half-square P2 detector.

Research owner artifact only.  It checks exact finite instances of
P2-R06--P2-R11 in
`docs/P017_P2_CHEN_CARRY_BRIDGE_SUPPLEMENT_01_20260824.md`.
It is not an asymptotic proof and makes no all-K P2 claim.
"""

from __future__ import annotations

from math import ceil, isqrt


def hit_count(k: int, m: int) -> int:
    if isinstance(k, bool) or not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    if isinstance(m, bool) or not isinstance(m, int) or m < 1:
        raise ValueError("m must be a positive integer")
    return (k * k + 2 * k) // m - (k * k) // m


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    x = n
    rows: list[tuple[int, int]] = []
    p = 2
    while p * p <= x:
        exponent = 0
        while x % p == 0:
            x //= p
            exponent += 1
        if exponent:
            rows.append((p, exponent))
        p += 1 if p == 2 else 2
    if x > 1:
        rows.append((x, 1))
    return tuple(rows)


def big_omega(n: int) -> int:
    return sum(exponent for _, exponent in factorization(n))


def half_square_detector_numerator(k: int, n: int) -> int:
    """Return twice the exact detector weight.

    2*w_K(n) = 2 - omega_<W(n) - 1_(n is not squarefree).
    """
    w = k + 1
    if not (k >= 2 and k * k < n < w * w):
        raise ValueError("n must lie in the open consecutive-square basin")
    rows = factorization(n)
    visible_distinct = sum(1 for prime, _ in rows if prime < w)
    squarefull = int(any(exponent >= 2 for _, exponent in rows))
    return 2 - visible_distinct - squarefull


def sieve_minorant_numerator(k: int, n: int) -> int:
    """Return twice the sieve-compatible sum-of-square-incidences minorant."""
    w = k + 1
    if not (k >= 2 and k * k < n < w * w):
        raise ValueError("n must lie in the open consecutive-square basin")
    rows = factorization(n)
    visible_distinct = sum(1 for prime, _ in rows if prime < w)
    visible_square_count = sum(
        1 for prime, exponent in rows if prime < w and exponent >= 2
    )
    return 2 - visible_distinct - visible_square_count


def primes_up_to(limit: int) -> tuple[int, ...]:
    if limit < 2:
        return ()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return tuple(index for index in range(2, limit + 1) if sieve[index])


def power_incidence_sum(k: int, z: int, exponent: int) -> int:
    if exponent < 2:
        raise ValueError("exponent must be at least two")
    return sum(
        hit_count(k, prime**exponent)
        for prime in primes_up_to(k)
        if prime >= z
    )


def power_incidence_bound(k: int, z: int, exponent: int) -> float:
    """P2-R08 bound with the root-balanced integer split Y."""
    if not (k >= 2 and 2 <= z <= k + 1 and exponent >= 2):
        raise ValueError("invalid k, z, or exponent")
    w = k + 1
    y = max(z, ceil(w ** (2 / (exponent + 1))))
    return (
        2 * k / ((exponent - 1) * (z - 1) ** (exponent - 1))
        + y
        + w * w / y**exponent
    )


def odd_quotient_count(k: int, m: int) -> int:
    return hit_count(k, m) - hit_count(k, 2 * m)


def direct_odd_quotient_window_count(k: int, m: int) -> int:
    lower = k * k // m + 1
    upper = (k * k + 2 * k) // m
    return sum(quotient % 2 for quotient in range(lower, upper + 1))


def shallow_switch_rows(k: int, upper_m: int) -> tuple[tuple[int, int], ...]:
    """Return every super-root binary incidence (m,q) with m<=upper_m."""
    if upper_m <= k:
        return ()
    rows: list[tuple[int, int]] = []
    for m in range(k + 1, upper_m + 1):
        lower = k * k // m + 1
        upper = (k * k + 2 * k) // m
        for quotient in range(lower, upper + 1):
            if quotient % 2:
                rows.append((m, quotient))
    return tuple(rows)


def verify(limit_k: int = 300, limit_m: int = 1000) -> None:
    for k in range(2, limit_k + 1):
        w = k + 1
        for n in range(k * k + 1, w * w):
            is_p2 = big_omega(n) <= 2
            assert (half_square_detector_numerator(k, n) > 0) == is_p2
            assert (sieve_minorant_numerator(k, n) > 0) == is_p2
            assert sieve_minorant_numerator(k, n) <= half_square_detector_numerator(k, n)

        for m in range(1, limit_m + 1):
            assert odd_quotient_count(k, m) == direct_odd_quotient_window_count(k, m)
            if m > k:
                assert odd_quotient_count(k, m) in (0, 1)

    # Componentwise sharpness witnesses.
    assert factorization(42) == ((2, 1), (3, 1), (7, 1))
    assert half_square_detector_numerator(6, 42) == 0
    assert factorization(8) == ((2, 3),)
    assert half_square_detector_numerator(2, 8) == 0

    # Finite checks of the general power-incidence envelope.
    for k in range(10, limit_k + 1):
        test_cutoffs = {
            2,
            3,
            max(2, isqrt(k) // 2),
            max(2, isqrt(k)),
        }
        for z in sorted(min(cutoff, k) for cutoff in test_cutoffs):
            for exponent in (2, 3):
                assert power_incidence_sum(k, z, exponent) <= power_incidence_bound(
                    k, z, exponent
                )

    # P2-R11 shallow switching and its quotient range.
    for k in range(8, min(limit_k, 160) + 1):
        # eta=1/4, rounded down at the integer endpoint.
        upper_m = max(k + 1, int(k ** 1.25))
        lower_q_real = k ** 0.75
        for m, quotient in shallow_switch_rows(k, upper_m):
            assert k < m <= upper_m
            assert quotient % 2 == 1
            assert lower_q_real < quotient <= k
            assert k * k < m * quotient < (k + 1) ** 2


if __name__ == "__main__":
    verify()
    print("P017 half-square P2 detector verifier: PASS")
