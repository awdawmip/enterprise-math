"""Exact arithmetic bridge for R005-B cubic finite certificate composition.

The module does not verify Oppermann's conjecture, Kadiri--Lumley's effective
prime-interval theorem, or the external prime-gap database.  It freezes only
the integer conversions used to compose those external certificates with the
existing R005-A/R005-B theorems.
"""

from math import isqrt


OPPERMANN_INDEX_LIMIT = 70_500_000_000_000
OPPERMANN_ONLY_K_MAX = 2_150_153_225
KADIRI_LUMLEY_E59_DELTA = 1_946_282_821
KADIRI_LUMLEY_E59_K_MAX = 5_838_848_460
PRIME_GAP_COVERAGE_LIMIT = 10**20
PRIME_GAP_CAP = 1724
OLD_COMPLETE_PREFIX_MAX = 5_848_035


def ceil_sqrt_half_cube(k: int) -> int:
    """Return ceil(sqrt(k^3/2)) exactly."""
    if k < 1:
        raise ValueError("k must be positive")
    n = k**3
    t = isqrt(n // 2)
    while 2 * t * t < n:
        t += 1
    while t > 0 and 2 * (t - 1) * (t - 1) >= n:
        t -= 1
    return t


def oppermann_index_covered(k: int, q: int) -> bool:
    """Return the exact arithmetic condition t(q)<=N for finite Oppermann data.

    For t(q)=ceil(sqrt(k^3/q)), coverage is equivalent to

        k^3 <= q*N^2.
    """
    if k < 1 or q < 1:
        raise ValueError("k and q must be positive")
    return k**3 <= q * OPPERMANN_INDEX_LIMIT**2


def oppermann_escape_forces_large_effective_scale(k: int, q: int) -> bool:
    """Check the exact scale complement behind the Kadiri--Lumley bridge.

    If finite Oppermann coverage fails, q*N^2<k^3.  Hence for
    U=(k+1)^3-1 the cofactor upper endpoint y=U/q satisfies y>N^2.
    This routine checks the integer inequality q*N^2<k^3 => U>q*N^2.
    The external comparison N^2>e^59 is not encoded as integer theorem data.
    """
    if k < 1 or q < 1:
        raise ValueError("k and q must be positive")
    if oppermann_index_covered(k, q):
        return True
    upper = (k + 1) ** 3 - 1
    return upper > q * OPPERMANN_INDEX_LIMIT**2


def effective_relative_interval_fits(k: int, delta: int) -> bool:
    """Check whether a relative prime interval with parameter delta fits.

    Applying a theorem that supplies a prime in

        (y*(1-1/delta), y), y=U/q,

    fits inside the cubic cofactor interval (A/q,U/q) exactly when

        3*(k+1)*(delta-1) > k^2.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if delta <= 1:
        raise ValueError("delta must exceed 1")
    return 3 * (k + 1) * (delta - 1) > k * k


def worst_q_gt_k_cofactor_floor(k: int) -> int:
    """Return max floor(k^3/q) over integer q>k.

    The maximum is attained at q=k+1 and equals k^2-k because

        (k+1)(k^2-k+1)=k^3+1.
    """
    if k < 1:
        raise ValueError("k must be positive")
    return k * k - k


def cubic_root_horizon_pair(k: int) -> tuple[int, int, int]:
    """Return (S,F,U) for the cubic basin."""
    if k < 1:
        raise ValueError("k must be positive")
    upper = (k + 1) ** 3 - 1
    return isqrt(k**3), isqrt(upper), upper


def upper_closed_by_uniform_gap_cap(k: int, gap_cap: int = PRIME_GAP_CAP) -> bool:
    """Check the exact sufficient upper-horizon closing inequality.

    If every consecutive prime gap containing F is at most gap_cap, then
    R=nextprime(F) satisfies R<=F+gap_cap.  The upper raw window is closed when

        (F+gap_cap)*S <= U.
    """
    if gap_cap < 0:
        raise ValueError("gap_cap must be nonnegative")
    s, f, upper = cubic_root_horizon_pair(k)
    return (f + gap_cap) * s <= upper


def oppermann_endpoint_arithmetic_holds() -> bool:
    """Return whether the frozen finite-Oppermann endpoint conversion holds."""
    k = OPPERMANN_ONLY_K_MAX
    return (
        ceil_sqrt_half_cube(k) <= OPPERMANN_INDEX_LIMIT
        and ceil_sqrt_half_cube(k + 1) > OPPERMANN_INDEX_LIMIT
        and worst_q_gt_k_cofactor_floor(k) < PRIME_GAP_COVERAGE_LIMIT
    )


def kadiri_lumley_e59_endpoint_arithmetic_holds() -> bool:
    """Return whether the e^59 effective-row endpoint conversions hold."""
    k = KADIRI_LUMLEY_E59_K_MAX
    return (
        effective_relative_interval_fits(k, KADIRI_LUMLEY_E59_DELTA)
        and not effective_relative_interval_fits(k + 1, KADIRI_LUMLEY_E59_DELTA)
        and worst_q_gt_k_cofactor_floor(k) < PRIME_GAP_COVERAGE_LIMIT
        and upper_closed_by_uniform_gap_cap(OLD_COMPLETE_PREFIX_MAX + 1)
        and upper_closed_by_uniform_gap_cap(k)
    )
