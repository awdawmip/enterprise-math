"""Exact cubic boundary-prime compression for R005-B.

This module specializes the cubic pure-horizon-cap existence question. The
complete non-forced witness list remains owned by the prime-slice compiler in
``prime_horizon_gap``. For the yes/no question "does the cubic pure cap contain
any non-forced witness?", only the nearest prime at or below the lower root and
the nearest prime above the factor horizon are required.

All routines are exact integer helpers. No density or prime-gap theorem is
implemented here.
"""

from math import isqrt

from .legendre import is_prime
from .prime_collapse_field import factor_horizon
from .prime_horizon_gap import next_prime_after


def previous_prime_at_most(n: int) -> int:
    """Return the greatest prime <= n."""
    if n < 2:
        raise ValueError("n must be at least 2")
    q = n
    while not is_prime(q):
        q -= 1
    return q


def cubic_boundary_primes(k: int) -> tuple[int, int]:
    """Return ``(Q,R)`` for the cubic pure-cap boundary-prime test.

    ``Q`` is the greatest prime at or below
    ``S=floor(sqrt(k^3))`` and ``R`` is the least prime strictly above
    ``F=floor(sqrt((k+1)^3-1))``.
    """
    if k < 3:
        raise ValueError("cubic boundary-prime compression requires k>=3")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    root_lower = isqrt(lower)
    horizon = isqrt(upper)
    return previous_prime_at_most(root_lower), next_prime_after(horizon)


def cubic_pure_cap_max_nonforced_candidate(k: int) -> int | None:
    """Return the canonical maximal cubic pure-cap obstruction, if one exists.

    For ``k>=3``, the cubic pure-cap non-forced set is nonempty iff its largest
    possible prime ``Q<=S`` satisfies both

        Q*F > A,
        Q*R > U,

    where ``A=k^3``, ``U=(k+1)^3-1``, ``F=isqrt(U)`` and
    ``R=nextprime(F)``. When these hold, ``Q`` itself is the largest
    non-forced pure-cap witness.
    """
    if k < 3:
        raise ValueError("cubic boundary-prime compression requires k>=3")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    horizon = factor_horizon(k, 3)
    q_left, r_right = cubic_boundary_primes(k)
    if q_left * horizon > lower and q_left * r_right > upper:
        return q_left
    return None


def cubic_boundary_gap_state(k: int) -> tuple[int, int, int, int]:
    """Return exact nearest-prime gaps and product margins.

    The tuple is

        (left_lag, right_gap, horizon_margin, overshoot_margin),

    where

        left_lag = S-Q,
        right_gap = R-F,
        horizon_margin = Q*F-A,
        overshoot_margin = Q*R-U.

    A cubic pure-cap obstruction exists exactly when both margins are positive.
    """
    if k < 3:
        raise ValueError("cubic boundary-prime compression requires k>=3")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    root_lower = isqrt(lower)
    horizon = factor_horizon(k, 3)
    q_left, r_right = cubic_boundary_primes(k)
    return (
        root_lower - q_left,
        r_right - horizon,
        q_left * horizon - lower,
        q_left * r_right - upper,
    )


def cubic_boundary_margin_identity(k: int) -> tuple[int, int]:
    """Return the two equivalent lag-form margins.

    If ``ell=S-Q``, then

        Q*F-A = (F*S-A) - ell*F,
        Q*R-U = (R*S-U) - ell*R.

    Returning the right-hand sides makes the exact two-nearest-prime criterion
    convenient to regression-test without floating point arithmetic.
    """
    if k < 3:
        raise ValueError("cubic boundary-prime compression requires k>=3")
    lower = k**3
    upper = (k + 1) ** 3 - 1
    root_lower = isqrt(lower)
    horizon = factor_horizon(k, 3)
    q_left, r_right = cubic_boundary_primes(k)
    lag = root_lower - q_left
    return (
        horizon * root_lower - lower - lag * horizon,
        r_right * root_lower - upper - lag * r_right,
    )
