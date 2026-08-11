"""Exact arithmetic bridge for the R005-B cubic combined finite theorem.

The module does not verify Oppermann's conjecture or the external prime-gap
database.  It freezes only the integer conversions used to compose those two
finite external certificates with the existing R005-A/R005-B theorems.
"""

from math import isqrt


OPPERMANN_INDEX_LIMIT = 70_500_000_000_000
COMBINED_K_MAX = 2_150_153_225
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


def combined_endpoint_arithmetic_holds() -> bool:
    """Return whether all frozen integer endpoint conversions hold."""
    k = COMBINED_K_MAX
    return (
        ceil_sqrt_half_cube(k) <= OPPERMANN_INDEX_LIMIT
        and ceil_sqrt_half_cube(k + 1) > OPPERMANN_INDEX_LIMIT
        and worst_q_gt_k_cofactor_floor(k) < PRIME_GAP_COVERAGE_LIMIT
        and upper_closed_by_uniform_gap_cap(OLD_COMPLETE_PREFIX_MAX + 1)
        and upper_closed_by_uniform_gap_cap(k)
    )
