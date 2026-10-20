"""Exact arithmetic bridge for R005-B cubic finite certificate composition.

The module does not verify Oppermann's conjecture, Kadiri--Lumley's or
Cully--Hugill--Lee's effective prime-interval theorems, or the external
prime-gap database.  It freezes only the integer conversions used to compose
those external certificates with the existing R005-A/R005-B theorems.
"""

from math import isqrt


OPPERMANN_INDEX_LIMIT = 70_500_000_000_000
OPPERMANN_ONLY_K_MAX = 2_150_153_225
KADIRI_LUMLEY_E59_DELTA = 1_946_282_821
KADIRI_LUMLEY_E59_K_MAX = 5_838_848_460
CULLY_HUGILL_LEE_E55_DELTA = 10_288_400_000
CULLY_HUGILL_LEE_E60_DELTA = 76_918_400_000
CULLY_HUGILL_LEE_E60_FIT_K_MAX = 230_755_199_997
PRIME_GAP_COVERAGE_LIMIT = 10**20
PRIME_GAP_CAP = 1724
CURRENT_COMPLETE_CLASSIFICATION_K_MAX = 10_000_000_000
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
    """Check the exact size complement behind the effective-interval bridge.

    If finite Oppermann coverage fails, q*N^2<k^3.  Hence for
    U=(k+1)^3-1 the cofactor upper endpoint y=U/q satisfies y>N^2.
    This routine freezes that integer implication.  The external comparison
    N^2>e^60 belongs to the cited effective prime-interval input.
    """
    if k < 1 or q < 1:
        raise ValueError("k and q must be positive")
    if oppermann_index_covered(k, q):
        return True
    upper = (k + 1) ** 3 - 1
    return upper > q * OPPERMANN_INDEX_LIMIT**2


def effective_relative_interval_fits(k: int, delta: int) -> bool:
    """Check whether a relative prime interval with parameter delta fits.

    A theorem supplying a prime in

        (y*(1-1/delta), y],  y=U/q,

    fits strictly above the cubic lower cofactor endpoint A/q exactly when

        U*(1-1/delta) > A,

    equivalently

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


def horizontal_gap_database_covered(k: int) -> bool:
    """Return whether every q>k cofactor point lies below the frozen data cap."""
    return worst_q_gt_k_cofactor_floor(k) < PRIME_GAP_COVERAGE_LIMIT


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
        and horizontal_gap_database_covered(k)
    )


def kadiri_lumley_e59_endpoint_arithmetic_holds() -> bool:
    """Return whether the historical e^59 bridge endpoint conversions hold."""
    k = KADIRI_LUMLEY_E59_K_MAX
    return (
        effective_relative_interval_fits(k, KADIRI_LUMLEY_E59_DELTA)
        and not effective_relative_interval_fits(k + 1, KADIRI_LUMLEY_E59_DELTA)
        and horizontal_gap_database_covered(k)
        and upper_closed_by_uniform_gap_cap(k)
    )


def cully_hugill_lee_e60_fit_endpoint_arithmetic_holds() -> bool:
    """Check the corrected CHL log(x0)=60 row's exact cubic fit endpoint."""
    k = CULLY_HUGILL_LEE_E60_FIT_K_MAX
    delta = CULLY_HUGILL_LEE_E60_DELTA
    return (
        effective_relative_interval_fits(k, delta)
        and not effective_relative_interval_fits(k + 1, delta)
    )


def current_complete_classification_endpoint_arithmetic_holds() -> bool:
    """Check the current 10^20-data-limited cubic endpoint packet.

    The corrected Cully--Hugill--Lee e^60 row still fits far beyond this point;
    the active finite endpoint is exactly the q>k horizontal data boundary.
    """
    k = CURRENT_COMPLETE_CLASSIFICATION_K_MAX
    return (
        effective_relative_interval_fits(k, CULLY_HUGILL_LEE_E60_DELTA)
        and horizontal_gap_database_covered(k)
        and not horizontal_gap_database_covered(k + 1)
        and upper_closed_by_uniform_gap_cap(k)
    )
