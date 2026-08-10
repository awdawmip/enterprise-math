"""Exact integer carry compiler for the cubic lower cofactor-gap knife edge.

This module refines the PRE_HORIZON reciprocal-gap layer from
``prime_cubic_gap_lifecycle``.  It separates the real reciprocal interval from
its integer lattice occupancy and exposes the exact activation threshold as a
cubic basin hit-count jump plus one further reciprocal carry.

Generic forced-core / hitting-set semantics remain R005-A/A2/A4 ownership.
All routines are exact integer helpers; no analytic prime-gap theorem is
implemented here.
"""

from .legendre import interior_hit_count, is_prime
from .prime_collapse_field import factor_horizon, interior_width_carry
from .prime_cubic_boundary import previous_prime_at_most
from .prime_horizon_gap import next_prime_after


def _ceil_div(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError("denominator must be positive")
    return -(-n // d)


def _validate_pre_horizon(a: int, k: int) -> None:
    if k < 3:
        raise ValueError("k must be at least 3")
    if a < 2 or not is_prime(a):
        raise ValueError("a must be prime")
    if factor_horizon(k, 3) >= a:
        raise ValueError("a must lie strictly beyond the cubic factor horizon")


def _validate_consecutive_gap(a: int, b: int, k: int) -> None:
    _validate_pre_horizon(a, k)
    if b <= a or not is_prime(b) or next_prime_after(a) != b:
        raise ValueError("a<b must be consecutive primes")


def cubic_real_gap_threshold(a: int, k: int) -> int:
    """Least integer gap length making the PRE reciprocal interval real-positive.

    The real interval ``U/(a+g) < q <= A/a`` has positive width exactly when

        g*k^2 > 3*a*(k+1).

    Hence this returns ``1+floor(3*a*(k+1)/k^2)``.
    """
    _validate_pre_horizon(a, k)
    return 1 + (3 * a * (k + 1)) // (k * k)


def cubic_reciprocal_endpoint_state(a: int, k: int) -> tuple[int, int, int, int]:
    """Return ``(m,r,d,r_next)`` for one cubic PRE state.

    Put

        A=k^3 = a*m + r,
        C=(k+1)^3 = a*(m+d) + r_next.

    Because PRE_HORIZON gives ``a>F_3(k)>k+1``, ``a`` cannot divide C and
    ``d`` is exactly the basin hit count ``H_{3,a}(k)``.
    """
    _validate_pre_horizon(a, k)
    lower = k**3
    next_cube = (k + 1) ** 3
    m, r = divmod(lower, a)
    m_next, r_next = divmod(next_cube, a)
    return m, r, m_next - m, r_next


def cubic_reciprocal_integer_depth(a: int, b: int, k: int) -> int:
    """Return the exact terminal depth J of the integer reciprocal q-window.

    Write ``m=floor(k^3/a)`` and ``C=(k+1)^3``.  Integers captured by the
    PRE gap are exactly

        q=m-j,  0<=j<=J,

    where

        J=m-ceil(C/b)=floor((b*m-C)/b).

    A negative J means that the real reciprocal interval contains no integer.
    """
    _validate_consecutive_gap(a, b, k)
    m = k**3 // a
    return m - _ceil_div((k + 1) ** 3, b)


def cubic_reciprocal_threshold(a: int, k: int, depth: int = 0) -> int:
    """Return the least right-gap length activating terminal depth ``depth``.

    For ``q=m-depth``, the condition ``(a+g)q >= (k+1)^3`` is equivalent to

        g >= ceil((k+1)^3/q) - a.
    """
    _validate_pre_horizon(a, k)
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    m = k**3 // a
    q = m - depth
    if q <= 0:
        raise ValueError("depth escapes the positive quotient endpoint")
    return _ceil_div((k + 1) ** 3, q) - a


def cubic_reciprocal_jump_carry(a: int, k: int) -> tuple[int, int, int]:
    """Return ``(jump, reciprocal_carry, threshold)`` at depth zero.

    If ``m=floor(k^3/a)``, ``d=floor((k+1)^3/a)-m`` and
    ``r_next=(k+1)^3 mod a``, then

        G_0 = d + ceil((d*(a-m)+r_next)/m).

    The jump d is exactly ``H_{3,a}(k)``.  Thus the integer critical gap is an
    existing cubic basin hit-count plus a second, quotient-side carry.
    """
    m, _, jump, r_next = cubic_reciprocal_endpoint_state(a, k)
    if m <= 0:
        raise ValueError("quotient endpoint must be positive")
    reciprocal_carry = _ceil_div(jump * (a - m) + r_next, m)
    threshold = jump + reciprocal_carry
    return jump, reciprocal_carry, threshold


def cubic_reciprocal_three_layer_carry(a: int, k: int) -> tuple[int, int, int, int]:
    """Return ``(coarse_width, basin_bit, reciprocal_carry, threshold)``.

    In PRE_HORIZON,

        jump = H_{3,a}(k)
             = floor((3k^2+3k)/a) + epsilon,

    with ``epsilon`` the existing one-bit full-width carry.  The depth-zero
    reciprocal threshold is then ``jump + reciprocal_carry``.
    """
    jump, reciprocal_carry, threshold = cubic_reciprocal_jump_carry(a, k)
    coarse_width = (3 * k * k + 3 * k) // a
    basin_bit = interior_width_carry(k, a, 3)
    if jump != interior_hit_count(k, a, 3):
        raise AssertionError("quotient jump disagrees with cubic basin hit count")
    if jump != coarse_width + basin_bit:
        raise AssertionError("cubic hit-count carry decomposition failed")
    return coarse_width, basin_bit, reciprocal_carry, threshold


def cubic_reciprocal_threshold_ladder(a: int, k: int, max_depth: int) -> tuple[int, ...]:
    """Return ``G_0,...,G_max_depth`` for the terminal reciprocal ladder."""
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    return tuple(cubic_reciprocal_threshold(a, k, j) for j in range(max_depth + 1))


def cubic_lower_boundary_prime(a: int, b: int, k: int) -> int | None:
    """Return the maximal prime captured by the PRE reciprocal integer window.

    If ``m=floor(k^3/a)`` and ``Q`` is the greatest prime <=m, the reciprocal
    integer slice contains a prime iff

        Q >= ceil((k+1)^3/b),

    equivalently ``b*Q >= (k+1)^3``.  Thus the yes/no occupancy question again
    compresses to one boundary prime.
    """
    _validate_consecutive_gap(a, b, k)
    m = k**3 // a
    if m < 2:
        return None
    q = previous_prime_at_most(m)
    return q if b * q >= (k + 1) ** 3 else None


def cubic_lower_full_nonforced_candidate(a: int, b: int, k: int) -> int | None:
    """Return the boundary prime when it is also a full lower-band obstruction.

    The PRE cofactor gap blocks the e=1 route.  When the captured boundary prime
    satisfies q>k, the cubic one-large-prime normal form excludes all remaining
    singleton-support forms, so q is fully non-forced.
    """
    q = cubic_lower_boundary_prime(a, b, k)
    return q if q is not None and q > k else None


def cubic_prime_lag_budget(a: int, b: int, k: int) -> tuple[int, int, int, int]:
    """Return ``(Q, lag, slack, threshold_at_Q)`` for the lower boundary prime.

    ``slack=(b-a)-G_0`` is the number of right-gap units above the depth-zero
    integer threshold.  In PRE_HORIZON the threshold ladder obeys

        G_{j+1} >= G_j + 1,

    so a necessary condition for the predecessor-prime lag ``lag=m-Q`` to be
    captured is ``lag<=slack``.
    """
    _validate_consecutive_gap(a, b, k)
    m = k**3 // a
    if m < 2:
        raise ValueError("quotient endpoint has no predecessor prime")
    q = previous_prime_at_most(m)
    lag = m - q
    g0 = cubic_reciprocal_threshold(a, k, 0)
    slack = (b - a) - g0
    return q, lag, slack, cubic_reciprocal_threshold(a, k, lag)
