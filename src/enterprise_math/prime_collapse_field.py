"""Exact integer tools for R005-B prime/collapse factor-horizon experiments.

The functions here expose finite identities only. They do not assert an
asymptotic theorem about primes in short intervals, nor a proof of Legendre's
conjecture. ``factor_horizon`` is the universal square-root screening horizon
for a complete p-power basin, not necessarily the smallest basin-specific
factor bound after the actual composite population is known.
"""

from math import comb, isqrt

from .legendre import (
    interior_hit_count,
    is_prime,
    power_gap,
    primes_up_to,
    square_carry,
    squarefree_divisors_with_mu,
)


def factor_horizon(k: int, power: int = 2) -> int:
    """Return floor(sqrt((k+1)^power - 1)) exactly."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if power < 2:
        raise ValueError("power must be at least 2")
    return isqrt((k + 1) ** power - 1)


def interior_width(k: int, power: int = 2) -> int:
    """Return the number of integers strictly inside the p-power basin."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if power < 1:
        raise ValueError("power must be positive")
    return power_gap(k, power) - 1


def interior_width_carry(k: int, d: int, power: int = 2) -> int:
    """Return the exact 0/1 boundary carry relative to floor(width/d).

    With L=(k+1)^p-k^p-1, this is the epsilon in

        H_{p,d}(k) = floor(L/d) + epsilon.
    """
    if k < 0:
        raise ValueError("k must be nonnegative")
    if d <= 0:
        raise ValueError("d must be positive")
    if power < 1:
        raise ValueError("power must be positive")
    width = interior_width(k, power)
    return int((k**power % d) + (width % d) >= d)


def polynomial_hit_baseline(k: int, d: int, power: int = 2) -> int:
    """Return the separated-floor polynomial baseline for H_{p,d}(k)."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if d <= 0:
        raise ValueError("d must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    return sum(comb(power, j) * (k**j // d) for j in range(1, power))


def polynomial_carry(k: int, d: int, power: int = 2) -> int:
    """Return the residue-local correction to ``polynomial_hit_baseline``.

    The value depends only on ``k mod d`` and obeys
    ``0 <= carry <= 2**power - 2`` for fixed ``power``.
    At power=2 it is exactly the existing square-carry correction.
    """
    if k < 0:
        raise ValueError("k must be nonnegative")
    if d <= 0:
        raise ValueError("d must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    residue_sum = sum(
        comb(power, j) * pow(k, j, d) for j in range(1, power)
    )
    return residue_sum // d + interior_width_carry(k, d, power)


def forced_visibility_degree(power: int) -> int:
    """Return the degree range forced below every p-basin factor horizon."""
    if power < 2:
        raise ValueError("power must be at least 2")
    return power // 2


def direct_power_interval_prime_count(k: int, power: int = 2) -> int:
    """Count primes strictly between k^p and (k+1)^p by direct testing."""
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    lower = k**power
    upper = (k + 1) ** power
    return sum(is_prime(n) for n in range(lower + 1, upper))


def mobius_power_interval_prime_count(k: int, power: int = 2) -> int:
    """Return the exact finite Moebius screening identity for one p-basin.

    This routine is intentionally an exact small-scale explorer: enumerating
    all square-free divisors of the product of primes <= factor_horizon is
    exponential in the number of those primes.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if power < 2:
        raise ValueError("power must be at least 2")
    horizon = factor_horizon(k, power)
    total = sum(
        mu * interior_hit_count(k, d, power)
        for d, mu in squarefree_divisors_with_mu(primes_up_to(horizon))
    )
    lower = k**power
    if horizon > lower:
        total += sum(is_prime(q) for q in range(lower + 1, horizon + 1))
    return total


def square_alignment_holds(k: int) -> bool:
    """Return the exact p=2 factor-horizon self-alignment check."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    return factor_horizon(k, 2) == k


def even_power_horizon_closed_form(k: int, power: int) -> int:
    """Return the exact closed form for an even collapse exponent."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    if power < 2 or power % 2:
        raise ValueError("power must be an even integer at least 2")
    return (k + 1) ** (power // 2) - 1


def square_carry_compatibility(k: int, d: int) -> bool:
    """Check that the general polynomial carry specializes to square_carry."""
    return polynomial_carry(k, d, 2) == square_carry(k, d)
