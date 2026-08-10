"""Mobius exactification of the P017 root-split occupancy statistic.

L068 isolates two consecutive quotient subwindows around the next p-square root
boundary.  A p-rough integer is exactly an integer coprime to the product of all
primes below p, so each branch occupancy is the positivity of one finite Mobius
interval count.
"""

from __future__ import annotations

from .legendre import primes_up_to
from .p017_root_split_overshoot import raw_root_branch_slot_counts
from .rough_interval_mobius import rough_interval_mobius_count


def root_split_branch_intervals(k: int, prime: int) -> dict[str, object]:
    """Return the two raw quotient intervals separated by the p-square boundary."""

    raw = raw_root_branch_slot_counts(k, prime)
    lo = int(raw["q_min"])
    hi = int(raw["q_max"])
    boundary = int(raw["boundary_quotient"])

    lower = None
    lower_hi = min(hi, boundary - 1)
    if lo <= lower_hi:
        lower = (lo, lower_hi)

    upper = None
    upper_lo = max(lo, boundary)
    if upper_lo <= hi:
        upper = (upper_lo, hi)

    return {**raw, "lower_interval": lower, "upper_interval": upper}


def root_split_mobius_counts(k: int, prime: int) -> dict[str, object]:
    """Exact p-rough branch counts and the resulting realized split bit."""

    data = root_split_branch_intervals(k, prime)
    lower = data["lower_interval"]
    upper = data["upper_interval"]

    lower_count = (
        0
        if lower is None
        else rough_interval_mobius_count(int(lower[0]), int(lower[1]), prime)
    )
    upper_count = (
        0
        if upper is None
        else rough_interval_mobius_count(int(upper[0]), int(upper[1]), prime)
    )
    realized_split = lower_count > 0 and upper_count > 0

    return {
        **data,
        "lower_rough_count": lower_count,
        "upper_rough_count": upper_count,
        "realized_split": realized_split,
    }


def split_shell_count_by_mobius(k: int) -> int:
    """Exact L067 split-shell count S(k) from local Mobius positivity only."""

    return sum(
        bool(root_split_mobius_counts(k, prime)["realized_split"])
        for prime in primes_up_to(k)
    )
