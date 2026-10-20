"""Generic p-power reciprocal-gap carry compiler for R005-B.

For a p-power basin ``k^p < n < (k+1)^p`` with p>=3, fix a consecutive
cofactor-prime gap a<b that lies strictly beyond the basin factor horizon.
This module compiles the exact integer reciprocal witness interval and its
activation thresholds.

The arithmetic is owner-local R005-B factor-horizon/carry structure.  Generic
forced-core, least-basis and hitting-set semantics remain R005-A/A2/A4.
"""

from .legendre import interior_hit_count, is_prime
from .prime_collapse_field import factor_horizon, interior_width, interior_width_carry
from .prime_horizon_gap import next_prime_after


def _ceil_div(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError("denominator must be positive")
    return -(-n // d)


def _previous_prime_at_most(n: int) -> int:
    if n < 2:
        raise ValueError("n must be at least 2")
    q = n
    while not is_prime(q):
        q -= 1
    return q


def _validate_pre(k: int, power: int, a: int) -> None:
    if k < 1:
        raise ValueError("k must be positive")
    if power < 3:
        raise ValueError("generic reciprocal carry currently requires power>=3")
    if a < 2 or not is_prime(a):
        raise ValueError("a must be prime")
    if factor_horizon(k, power) >= a:
        raise ValueError("a must lie strictly beyond the p-power factor horizon")


def _validate_gap(k: int, power: int, a: int, b: int) -> None:
    _validate_pre(k, power, a)
    if b <= a or not is_prime(b) or next_prime_after(a) != b:
        raise ValueError("a<b must be consecutive primes")


def reciprocal_real_gap_threshold(k: int, power: int, a: int) -> int:
    """Least integer g making the real reciprocal interval positive.

    With A=k^p, U=(k+1)^p-1 and b=a+g, the real interval

        U/b < q <= A/a

    has positive width exactly when

        g*A > a*(U-A) = a*L_p(k).

    Thus the least integer g is ``1+floor(a*L_p(k)/A)``.
    """
    _validate_pre(k, power, a)
    lower = k**power
    return 1 + a * interior_width(k, power) // lower


def reciprocal_endpoint_state(k: int, power: int, a: int) -> tuple[int, int, int, int]:
    """Return ``(m,r,d,r_next)`` for the p-power quotient endpoint.

    Write

        k^p = a*m+r,
        (k+1)^p = a*(m+d)+r_next.

    Since power>=3 and a is beyond the factor horizon, a>k+1; hence a does not
    divide (k+1)^p and d is exactly H_{p,a}(k).
    """
    _validate_pre(k, power, a)
    lower = k**power
    next_power = (k + 1) ** power
    m, r = divmod(lower, a)
    m_next, r_next = divmod(next_power, a)
    return m, r, m_next - m, r_next


def reciprocal_integer_depth(k: int, power: int, a: int, b: int) -> int:
    """Return terminal depth J of the exact integer reciprocal window.

    The captured integers are q=m-j for 0<=j<=J with

        J=m-ceil((k+1)^p/b).

    A negative J means that the positive real interval has no integer point.
    """
    _validate_gap(k, power, a, b)
    m = k**power // a
    return m - _ceil_div((k + 1) ** power, b)


def reciprocal_threshold(k: int, power: int, a: int, depth: int = 0) -> int:
    """Least right-gap length activating terminal depth ``depth``."""
    _validate_pre(k, power, a)
    if depth < 0:
        raise ValueError("depth must be nonnegative")
    m = k**power // a
    q = m - depth
    if q <= 0:
        raise ValueError("depth escapes the positive quotient endpoint")
    return _ceil_div((k + 1) ** power, q) - a


def reciprocal_jump_carry(k: int, power: int, a: int) -> tuple[int, int, int]:
    """Return ``(basin_jump, reciprocal_carry, depth_zero_threshold)``.

    If C=(k+1)^p=a(m+d)+r_next, then

        G_0 = d + ceil((d*(a-m)+r_next)/m).

    The jump d is the existing basin hit count H_{p,a}(k).
    """
    m, _, jump, r_next = reciprocal_endpoint_state(k, power, a)
    if m <= 0:
        raise ValueError("quotient endpoint must be positive")
    carry = _ceil_div(jump * (a - m) + r_next, m)
    return jump, carry, jump + carry


def reciprocal_three_layer_carry(
    k: int, power: int, a: int
) -> tuple[int, int, int, int]:
    """Return coarse-width, basin-bit, reciprocal-carry and exact threshold.

    This exposes

        G_0 = floor(L_p(k)/a) + epsilon_{p,a}(k) + eta_{p,a}(k).
    """
    jump, reciprocal_carry, threshold = reciprocal_jump_carry(k, power, a)
    coarse = interior_width(k, power) // a
    basin_bit = interior_width_carry(k, a, power)
    if jump != interior_hit_count(k, a, power):
        raise AssertionError("quotient jump disagrees with basin hit count")
    if jump != coarse + basin_bit:
        raise AssertionError("full-width carry decomposition failed")
    return coarse, basin_bit, reciprocal_carry, threshold


def reciprocal_threshold_ladder(
    k: int, power: int, a: int, max_depth: int
) -> tuple[int, ...]:
    """Return ``G_0,...,G_max_depth``."""
    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    return tuple(reciprocal_threshold(k, power, a, j) for j in range(max_depth + 1))


def reciprocal_boundary_prime(k: int, power: int, a: int, b: int) -> int | None:
    """Return the greatest prime in the reciprocal integer window, if present."""
    _validate_gap(k, power, a, b)
    m = k**power // a
    if m < 2:
        return None
    q = _previous_prime_at_most(m)
    return q if b * q >= (k + 1) ** power else None


def reciprocal_prime_lag_budget(
    k: int, power: int, a: int, b: int
) -> tuple[int, int, int, int]:
    """Return ``(Q,lag,slack,threshold_at_Q)`` for the boundary predecessor.

    With ``slack=(b-a)-G_0``, the universal ladder inequality

        G_{j+1} >= G_j+1

    implies that any captured predecessor prime Q=m-lag must satisfy

        lag <= slack.
    """
    _validate_gap(k, power, a, b)
    m = k**power // a
    if m < 2:
        raise ValueError("quotient endpoint has no predecessor prime")
    q = _previous_prime_at_most(m)
    lag = m - q
    g0 = reciprocal_threshold(k, power, a, 0)
    slack = (b - a) - g0
    return q, lag, slack, reciprocal_threshold(k, power, a, lag)
