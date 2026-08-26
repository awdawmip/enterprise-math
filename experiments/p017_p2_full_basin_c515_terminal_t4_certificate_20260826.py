#!/usr/bin/env python3
"""Exact certificate for the c=103/20 terminal T4 Rosser remainder.

At the Tier-A full-basin splice, use

    W = K0 + 1,
    D = W^(10/9),
    a = 6, b = 93/20, c = 103/20,
    A = D^(b/a) = W^(31/36),
    C = D^(c/a) = W^(103/108).

For the upper Rosser-Iwaniec weight with beta=2, descending prime factors
p_1>...>p_r satisfy the odd-position support conditions

    p_1...p_{j-1} p_j^3 < Q  (j odd),

where Q=D/p for the external terminal prime.  At Q_max=W^(1/4), this
forces p_1<=23; exact enumeration gives 68 support states.  Reindexing each
state by its activation threshold qcrit reduces the terminal remainder to 68
weighted prime sums.

Dusart's unconditional bounds

    pi(x) >= x/(log x - 1)      for x >= 5393,
    pi(x) <= x/(log x - 1.1)   for x >= 60184

and partial summation then give a fully explicit upper bound.  The remaining
integral is bounded by a 16-panel upper Riemann sum for the decreasing function
1/(log t - 1.1).  All logarithms are enclosed by exact Fraction arithmetic via
binary range reduction and the atanh series.

The final assertion is

    R_T4 / (2 K0) < 1/800 = 0.00125.

No floating-point value is used to establish the certificate.
"""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import isqrt

K0 = 116_009_280_740_973_308
W = K0 + 1
PANELS = 16
LOG_DEGREE = 28

A_SIEVE = Q(6)
B_TERM = Q(93, 20)
C_TERM = Q(103, 20)
DENOMINATOR = 2 * C_TERM - B_TERM - 1
COEFF = Q(27, 5)  # 6/log D = (27/5)/log W because D=W^(10/9)

assert DENOMINATOR == Q(93, 20)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def strict_floor_power(base: int, numerator: int, denominator: int) -> int:
    """Largest n with n^denominator < base^numerator, by integer arithmetic."""
    target = base**numerator
    lo, hi = 0, 1
    while hi**denominator < target:
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**denominator < target:
            lo = mid
        else:
            hi = mid
    return lo


def strict_floor_D_over_q(q: int) -> int:
    """Largest n with n < D/q for D=W^(10/9)."""
    target = W**10
    lo, hi = 0, 1
    while (q * hi) ** 9 < target:
        lo, hi = hi, 2 * hi
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if (q * mid) ** 9 < target:
            lo = mid
        else:
            hi = mid
    return lo


def atanh_log_bounds(x: Q, degree: int = LOG_DEGREE) -> tuple[Q, Q]:
    """Rigorous bounds for log(x), used only for 1<=x<=2."""
    if not (1 <= x <= 2):
        raise ValueError("range-reduced logarithm expects 1 <= x <= 2")
    z = (x - 1) / (x + 1)
    partial = Q(0)
    for k in range(degree + 1):
        partial += 2 * z ** (2 * k + 1) / (2 * k + 1)
    tail = 2 * z ** (2 * degree + 3) / (
        (2 * degree + 3) * (1 - z * z)
    )
    return partial, partial + tail


LOG2_LO, LOG2_HI = atanh_log_bounds(Q(2))


@lru_cache(maxsize=None)
def log_int_bounds(n: int) -> tuple[Q, Q]:
    """Rigorous Fraction bounds for log(n) by binary range reduction."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return Q(0), Q(0)
    k = n.bit_length() - 1
    reduced = Q(n, 1 << k)
    lo, hi = atanh_log_bounds(reduced)
    return k * LOG2_LO + lo, k * LOG2_HI + hi


LOGW_LO, LOGW_HI = log_int_bounds(W)
ALPHA_UPPER = COEFF / LOGW_LO


def phi_upper(n: int) -> Q:
    log_lo, _ = log_int_bounds(n)
    ratio_lower = log_lo / LOGW_HI
    return C_TERM - COEFF * ratio_lower


def phi_lower(n: int) -> Q:
    _, log_hi = log_int_bounds(n)
    ratio_upper = log_hi / LOGW_LO
    return C_TERM - COEFF * ratio_upper


def pi_upper(n: int) -> Q:
    """Dusart: pi(n) <= n/(log n - 1.1), n>=60184."""
    log_lo, _ = log_int_bounds(n)
    return Q(n) / (log_lo - Q(11, 10))


def pi_lower(n: int) -> Q:
    """Dusart: pi(n) >= n/(log n - 1), n>=5393."""
    _, log_hi = log_int_bounds(n)
    return Q(n) / (log_hi - 1)


def integral_upper(a: int, b: int) -> Q:
    """Upper-bound int_a^b dt/(log t-1.1) by monotone left rectangles."""
    if b <= a:
        return Q(0)
    points = [a + (b - a) * j // PANELS for j in range(PANELS)] + [b]
    total = Q(0)
    for x0, x1 in zip(points, points[1:]):
        if x1 == x0:
            continue
        log_lo, _ = log_int_bounds(x0)
        total += Q(x1 - x0) / (log_lo - Q(11, 10))
    return total


def upper_rosser_states(qmax: int) -> list[tuple[int, int, tuple[int, ...]]]:
    """Enumerate the beta=2 upper-Rosser positional support at maximal Q.

    Returns (d, qcrit, descending_prime_tuple), where

        qcrit = max_{j odd} p1...p_{j-1} p_j^3.
    """
    # The j=1 condition p1^3<qmax forces p1<=23 here.
    candidate_primes = [
        p for p in primes_up_to(1439) if p >= 3 and p**3 < qmax
    ]
    assert candidate_primes == [3, 5, 7, 11, 13, 17, 19, 23]

    states: list[tuple[int, int, tuple[int, ...]]] = []
    for r in range(len(candidate_primes) + 1):
        for chosen in combinations(candidate_primes, r):
            descending = tuple(sorted(chosen, reverse=True))
            prefix = 1
            qcrit = 1
            for j, p in enumerate(descending, start=1):
                if j % 2 == 1:
                    qcrit = max(qcrit, prefix * p**3)
                prefix *= p
            if qcrit < qmax:
                states.append((prefix, qcrit, descending))
    return states


def main() -> None:
    # Terminal endpoints and maximal inner upper-sieve level.
    a0 = strict_floor_power(W, 31, 36)       # floor(W^(31/36)), strict
    c0 = strict_floor_power(W, 103, 108)     # floor(W^(103/108)), strict
    qmax = strict_floor_power(W, 1, 4)       # floor(W^(1/4)), strict

    assert a0 == 494_793_856_728_459
    assert c0 == 18_813_514_064_055_713
    assert qmax == 18_455
    assert a0 > 60_184

    states = upper_rosser_states(qmax)
    assert len(states) == 68

    by_omega: dict[int, int] = {}
    for _, _, primes in states:
        by_omega[len(primes)] = by_omega.get(len(primes), 0) + 1
    assert by_omega == {0: 1, 1: 8, 2: 28, 3: 26, 4: 5}

    critical_values = sorted({qcrit for _, qcrit, _ in states})
    assert critical_values == [
        1,
        27,
        125,
        343,
        945,
        1331,
        1485,
        2079,
        2197,
        2457,
        3861,
        4913,
        5049,
        5967,
        6859,
        8721,
        9625,
        11375,
        12167,
        14875,
        16625,
        17875,
    ]

    phi_a_lower = phi_lower(a0)
    pi_a_lower = pi_lower(a0)

    total = Q(0)
    active_states = 0
    for _, qcrit, _ in states:
        bq = strict_floor_D_over_q(qcrit)
        b0 = min(c0, bq)
        if b0 <= a0:
            continue
        active_states += 1

        # Partial summation for sum_{a0<p<=b0} phi(p), with
        # phi'(t)=-(27/5)/(t log W), and Dusart's upper/lower pi bounds.
        state_upper = (
            phi_upper(b0) * pi_upper(b0)
            - phi_a_lower * pi_a_lower
            + ALPHA_UPPER * integral_upper(a0, b0)
        )
        assert state_upper > 0
        total += state_upper

    assert active_states == 68

    # T4 appears inside W with prefactor 1/(2c-b-1)=20/93.
    terminal_remainder = total / DENOMINATOR
    ratio = terminal_remainder / (2 * K0)

    assert ratio < Q(1, 800)

    print("P017 c=103/20 terminal T4 certificate: PASS")
    print("upper Rosser states =", len(states))
    print("omega layers =", by_omega)
    print("critical Q values =", critical_values)
    print("rigorous T4/(2K) bound ~=", float(ratio))
    print("T4/(2K) < 1/800 = 0.00125")


if __name__ == "__main__":
    main()
