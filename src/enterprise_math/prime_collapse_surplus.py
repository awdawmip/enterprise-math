"""Exact R005-B prime-surplus decomposition primitives.

This module refines the p-power basin Moebius decomposition from
``prime_collapse_field``.  The routines are finite exact identities for bounded
research use.  The naive Moebius sums remain exponential in the number of
screening primes and are not proposed as a competitive prime-counting method.

Square centered-shell / fixed-gap factor certificates are intentionally not
reimplemented here: the equivalent theorem is already owned canonically by
P018-T71.
"""

from math import comb

from .legendre import primes_up_to, squarefree_divisors_with_mu
from .prime_collapse_field import factor_horizon, polynomial_carry


def post_horizon_prime_count(horizon: int, limit: int) -> int:
    """Count primes q with ``horizon < q <= limit`` exactly."""
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if limit <= horizon:
        return 0
    return sum(q > horizon for q in primes_up_to(limit))


def mobius_survivor_count(limit: int, horizon: int) -> int:
    """Count positive integers <= limit surviving primes <= horizon.

    This is the classical partial-sieve count written by exact inclusion-
    exclusion over the square-free divisors of the primorial through horizon.
    It is deliberately small-scale because the divisor enumeration is
    exponential in ``pi(horizon)``.
    """
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if limit == 0:
        return 0
    return sum(
        mu * (limit // d)
        for d, mu in squarefree_divisors_with_mu(primes_up_to(horizon))
    )


def subsquare_survivor_count(limit: int, horizon: int) -> int:
    """Return the exact survivor count below the next horizon square.

    If ``1 <= limit < (horizon+1)^2``, every survivor above 1 after removing
    all prime divisors <= horizon must itself be a prime > horizon.  Hence the
    count is exactly ``1 + # {q prime : horizon < q <= limit}``.
    """
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if limit == 0:
        return 0
    if limit >= (horizon + 1) ** 2:
        raise ValueError("limit must lie strictly below (horizon+1)^2")
    return 1 + post_horizon_prime_count(horizon, limit)


def mobius_polynomial_carry_sum(k: int, power: int) -> int:
    """Return the exact Moebius sum of residue-local polynomial carries."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if power < 2:
        raise ValueError("power must be at least 2")
    horizon = factor_horizon(k, power)
    return sum(
        mu * polynomial_carry(k, d, power)
        for d, mu in squarefree_divisors_with_mu(primes_up_to(horizon))
    )


def prime_degree_surplus_terms(k: int, power: int) -> tuple[tuple[int, int, int], ...]:
    """Return ``(degree, binomial_weight, post-horizon-prime-count)`` terms."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if power < 2:
        raise ValueError("power must be at least 2")
    horizon = factor_horizon(k, power)
    return tuple(
        (j, comb(power, j), post_horizon_prime_count(horizon, k**j))
        for j in range(1, power)
    )


def prime_degree_surplus(k: int, power: int) -> int:
    """Return the weighted post-horizon prime surplus across width degrees."""
    return sum(
        coefficient * count
        for _, coefficient, count in prime_degree_surplus_terms(k, power)
    )


def prime_surplus_power_interval_prime_count(k: int, power: int) -> int:
    """Recover the exact p-basin prime count from surplus plus local carry.

    For ``k>=2`` and ``p>=2`` this implements

        P_p(k) = (2^p-2)
                 + sum_{j=1}^{p-1} C(p,j) * #{F_p(k)<q<=k^j : q prime}
                 + sum_{d|Q_F} mu(d) * chi_{p,d}(k).

    The formula is exact.  This implementation is only a bounded explorer
    because the final Moebius carry sum enumerates all square-free divisors of
    the primorial through the factor horizon.
    """
    if k < 2:
        raise ValueError("k must be at least 2")
    if power < 2:
        raise ValueError("power must be at least 2")
    return (
        2**power - 2
        + prime_degree_surplus(k, power)
        + mobius_polynomial_carry_sum(k, power)
    )
