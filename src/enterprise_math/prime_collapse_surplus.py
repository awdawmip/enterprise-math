"""Exact R005-B prime-surplus and square-gap bridge primitives.

This module refines the p-power basin Moebius decomposition from
``prime_collapse_field``.  The routines are finite exact identities for bounded
research use.  The naive Moebius sums remain exponential in the number of
screening primes and are not proposed as a competitive prime-counting method.

The square-gap certificate helper records an arithmetic factor-support
certificate only.  Generic forced/mandatory witness semantics remain owned by
the R005-A witness layer.
"""

from math import comb

from .legendre import is_prime, primes_up_to, squarefree_divisors_with_mu
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


def square_gap_target(q: int, offset: int) -> int:
    """Return the fixed even-gap target ``q + 2*offset + 2``."""
    if offset < 0:
        raise ValueError("offset must be nonnegative")
    return q + 2 * offset + 2


def square_gap_exclusive_certificate(q: int, offset: int) -> int | None:
    """Return the square-basin exclusive-factor certificate when it exists.

    Assume q is an odd prime and ``q > offset^2 + 2*offset``.  Put
    ``k=q+offset``.  Under exactly these hypotheses, a basin integer whose
    candidate prime-divisor support is the singleton ``{q}`` exists iff
    ``r=q+2*offset+2`` is prime.  When it exists the explicit certificate is
    ``n=q*r``; otherwise return ``None``.

    This is a factor-support certificate.  Interpreting singleton support as a
    forced/mandatory witness is the R005-A bridge theorem, not redefined here.
    """
    if offset < 0:
        raise ValueError("offset must be nonnegative")
    if q < 3 or q % 2 == 0 or not is_prime(q):
        raise ValueError("q must be an odd prime")
    if q <= offset * offset + 2 * offset:
        raise ValueError("q must exceed offset^2 + 2*offset")
    r = square_gap_target(q, offset)
    if not is_prime(r):
        return None
    k = q + offset
    certificate = q * r
    if not (k * k < certificate < (k + 1) * (k + 1)):
        raise AssertionError("derived certificate escaped its square basin")
    return certificate
