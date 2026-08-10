"""Next-p-square overshoot calculus for P017 factor->root shell splitting.

For a fixed square basin k and prime divisor p, the exact open cofactor window is
split by the next p-weighted square boundary above k^2.  The overshoot

    tau_p = p*m_p^2 - k^2,

where m_p is the least integer with p*m_p^2 > k^2, determines the raw number of
quotient slots on both sides of the root boundary exactly.  Actual least-prime
shell splitting is obtained by applying the p-rough realizability predicate to
those two subwindows.
"""

from __future__ import annotations

from math import isqrt

from .legendre import primes_up_to
from .p017_cofactor_window import centered_cofactor_window, is_p_rough


def ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -(-numerator // denominator)


def next_p_square_overshoot(k: int, prime: int) -> dict[str, int]:
    """Return the next p*square boundary above k^2 and its positive overshoot."""

    if isinstance(k, bool) or not isinstance(k, int) or k < 2:
        raise ValueError("k must be an integer >=2")
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <=k")

    base_quotient = (k * k) // prime
    lower_root = isqrt(base_quotient)
    boundary_root = lower_root + 1
    boundary_state = prime * boundary_root * boundary_root
    tau = boundary_state - k * k
    if tau <= 0:
        raise AssertionError("next p-square boundary did not lie above k^2")

    return {
        "k": k,
        "prime": prime,
        "lower_root": lower_root,
        "boundary_root": boundary_root,
        "boundary_quotient": boundary_root * boundary_root,
        "boundary_state": boundary_state,
        "overshoot": tau,
    }


def raw_root_branch_slot_counts(k: int, prime: int) -> dict[str, int | bool]:
    """Exact raw quotient-slot counts below and above the next root boundary.

    If tau is the next-p-square overshoot, then

        lower_slots = ceil(tau/p)-1,
        upper_slots = floor((2k-tau)/p)+1 when tau<=2k, else 0.

    Hence the open exact quotient window meets both adjacent root basins iff

        p < tau <= 2k.
    """

    data = next_p_square_overshoot(k, prime)
    tau = int(data["overshoot"])
    lower_slots = ceil_div(tau, prime) - 1
    upper_slots = max(0, (2 * k - tau) // prime + 1) if tau <= 2 * k else 0

    window = centered_cofactor_window(k, prime)
    boundary = int(data["boundary_quotient"])
    lo = int(window["q_min"])
    hi = int(window["q_max"])
    direct_lower = max(0, min(hi, boundary - 1) - lo + 1)
    direct_upper = max(0, hi - max(lo, boundary) + 1)
    if lower_slots != direct_lower or upper_slots != direct_upper:
        raise AssertionError("overshoot slot formulas disagree with exact cofactor window")

    raw_split = lower_slots > 0 and upper_slots > 0
    if raw_split != (prime < tau <= 2 * k):
        raise AssertionError("raw split criterion disagrees with overshoot interval")

    return {
        **data,
        "q_min": lo,
        "q_max": hi,
        "lower_slots": lower_slots,
        "upper_slots": upper_slots,
        "raw_split": raw_split,
    }


def realized_root_branch_occupancy(k: int, prime: int) -> dict[str, object]:
    """Apply the p-rough realizability filter to both raw root subwindows."""

    raw = raw_root_branch_slot_counts(k, prime)
    lo = int(raw["q_min"])
    hi = int(raw["q_max"])
    boundary = int(raw["boundary_quotient"])

    lower_values = tuple(
        q
        for q in range(lo, min(hi, boundary - 1) + 1)
        if is_p_rough(q, prime)
    )
    upper_values = tuple(
        q
        for q in range(max(lo, boundary), hi + 1)
        if is_p_rough(q, prime)
    )
    realized_split = bool(lower_values and upper_values)

    return {
        **raw,
        "lower_rough_values": lower_values,
        "upper_rough_values": upper_values,
        "realized_split": realized_split,
    }


def raw_split_primes(k: int) -> tuple[int, ...]:
    return tuple(
        p for p in primes_up_to(k) if bool(raw_root_branch_slot_counts(k, p)["raw_split"])
    )


def realized_split_primes(k: int) -> tuple[int, ...]:
    return tuple(
        p
        for p in primes_up_to(k)
        if bool(realized_root_branch_occupancy(k, p)["realized_split"])
    )
