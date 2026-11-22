"""Finite oracle for the square-diagonal Möbius bilinear parity target.

The analytic target is recorded in
`P017_P018_SQUARE_DIAGONAL_G3B_PARITY_BILINEAR_TARGET.md`.  This module does not
prove any bilinear cancellation.  It only fixes the exact integer geometry and
weights so future analytic work cannot drift back into an unsigned surrogate.
"""

from __future__ import annotations

from math import gcd, isqrt

from .legendre import primes_up_to
from .p017_p018_buchstab_cutoff_ladder import almost_prime_cutoff, square_interval_upper


def mobius(value: int) -> int:
    """Return the classical Möbius function using exact integer factorization."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    remaining = value
    sign = 1
    for p in primes_up_to(isqrt(value) + 1):
        if remaining % p:
            continue
        remaining //= p
        sign = -sign
        if remaining % p == 0:
            return 0
        while remaining % p == 0:
            remaining //= p
        if remaining == 1:
            break
        if p * p > remaining:
            break
    if remaining > 1:
        sign = -sign
    return sign


def truncated_mobius_divisor_sum(value: int, cutoff: int) -> int:
    """Return gamma(value,cutoff)=sum_{d|value,d<=cutoff} mu(d)."""
    for name, item in (("value", value), ("cutoff", cutoff)):
        if isinstance(item, bool) or not isinstance(item, int):
            raise ValueError(f"{name} must be an integer")
    if value < 1 or cutoff < 1:
        raise ValueError("value and cutoff must be positive")
    return sum(mobius(d) for d in range(1, min(value, cutoff) + 1) if value % d == 0)


def square_shell_factor_fiber(k: int, n: int) -> dict[str, int]:
    """Return the exact m-fiber with k^2 < m*n <= k^2+2k."""
    for name, value in (("k", k), ("n", n)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if k < 1 or n < 1:
        raise ValueError("k and n must be positive")
    lower = k * k
    upper = square_interval_upper(k)
    m_min = lower // n + 1
    m_max = upper // n
    count = max(0, m_max - m_min + 1)
    floor_difference = upper // n - lower // n
    if count != floor_difference:
        raise AssertionError("factor-fiber cardinality disagreed with floor difference")
    return {
        "k": k,
        "n": n,
        "lower": lower,
        "upper": upper,
        "m_min": m_min,
        "m_max": m_max,
        "fiber_count": count,
    }


def p2_rough_wheel(k: int) -> tuple[int, int]:
    """Return (z2,P_z2) for the exact minimal-P2 root cutoff."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 3:
        raise ValueError("k must be an integer >=3")
    z2 = int(almost_prime_cutoff(k, 2)["cutoff"])
    wheel = 1
    for p in primes_up_to(z2):
        wheel *= p
    return z2, wheel


def square_shell_parity_bilinear_slice(
    k: int,
    n_lo: int,
    n_hi: int,
    gamma_cutoff: int,
    *,
    p2_rough_only: bool = True,
) -> dict[str, object]:
    """Evaluate one finite FI-shaped Möbius bilinear slice.

    The returned quantity is

        sum_m | sum_{n_lo < n <= n_hi, k^2 < mn <= U}
                    gamma(n,C) mu(mn) 1_rough(mn) |.

    It is an exact finite research oracle only.  No asymptotic bound is claimed.
    """
    for name, value in (
        ("k", k),
        ("n_lo", n_lo),
        ("n_hi", n_hi),
        ("gamma_cutoff", gamma_cutoff),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if k < 3 or n_lo < 0 or n_hi <= n_lo or gamma_cutoff < 1:
        raise ValueError("require k>=3, 0<=n_lo<n_hi and gamma_cutoff>=1")

    z2, wheel = p2_rough_wheel(k)
    lower = k * k
    upper = square_interval_upper(k)

    outer: dict[int, int] = {}
    term_count = 0
    signed_term_sum = 0
    for n in range(n_lo + 1, n_hi + 1):
        gamma = truncated_mobius_divisor_sum(n, gamma_cutoff)
        if gamma == 0:
            continue
        fiber = square_shell_factor_fiber(k, n)
        for m in range(fiber["m_min"], fiber["m_max"] + 1):
            state = m * n
            if not lower < state <= upper:
                raise AssertionError("fiber emitted a state outside the square shell")
            if p2_rough_only and gcd(state, wheel) != 1:
                continue
            weight = gamma * mobius(state)
            outer[m] = outer.get(m, 0) + weight
            term_count += 1
            signed_term_sum += weight

    absolute_outer_sum = sum(abs(value) for value in outer.values())
    return {
        "k": k,
        "n_interval": (n_lo, n_hi),
        "gamma_cutoff": gamma_cutoff,
        "p2_cutoff": z2,
        "p2_rough_only": p2_rough_only,
        "term_count": term_count,
        "signed_term_sum_before_outer_absolute_values": signed_term_sum,
        "outer_fiber_sums": tuple(sorted(outer.items())),
        "bilinear_absolute_outer_sum": absolute_outer_sum,
        "status": "FINITE_PARITY_BILINEAR_ORACLE_ONLY",
    }
