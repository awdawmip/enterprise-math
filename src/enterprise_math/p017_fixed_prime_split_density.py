"""Finite audit helpers for the fixed-prime split-density theorem.

The theorem itself uses the classical density of the Beatty sequence for
sqrt(p) and equidistribution of irrational rotations.  This module stays in
integer arithmetic: it checks the exact Beatty-core inequality, the L068 split
criterion, and the finite primorial localization of every realizability failure.
"""

from __future__ import annotations

from .p017_root_split_mobius import root_split_mobius_counts
from .p017_root_split_overshoot import raw_root_branch_slot_counts
from .rough_interval_mobius import lower_primorial


def integer_beatty_core(k: int, prime: int) -> bool:
    """Integer form of ``k=floor(m*sqrt(p))`` for the next root boundary m.

    Since prime p is nonsquare, this is exactly

        k^2 < p*m^2 < (k+1)^2.
    """

    data = raw_root_branch_slot_counts(k, prime)
    boundary_state = int(data["boundary_state"])
    return k * k < boundary_state < (k + 1) * (k + 1)


def actual_fixed_prime_split(k: int, prime: int) -> bool:
    return bool(root_split_mobius_counts(k, prime)["realized_split"])


def split_failure_localization(k: int, prime: int) -> dict[str, object]:
    """Locate an actual failure inside one fixed-prime Beatty-core candidate.

    Any interval of ``P_<p`` consecutive integers contains every residue class
    modulo that primorial and hence a p-rough integer. Therefore if a Beatty-core
    candidate fails actual splitting, at least one raw branch has length strictly
    below ``P_<p``.
    """

    data = root_split_mobius_counts(k, prime)
    primorial = lower_primorial(prime)
    beatty = integer_beatty_core(k, prime)
    actual = bool(data["realized_split"])
    lower_slots = int(data["lower_slots"])
    upper_slots = int(data["upper_slots"])

    if beatty and not actual and not (lower_slots < primorial or upper_slots < primorial):
        raise AssertionError("fixed-prime split failure escaped finite primorial boundary layer")

    return {
        **data,
        "lower_primorial": primorial,
        "beatty_core": beatty,
        "actual_split": actual,
        "failure_localized": (not beatty) or actual or lower_slots < primorial or upper_slots < primorial,
    }


def fixed_prime_split_count(prime: int, max_k: int) -> int:
    """Finite regression count, not an asymptotic proof."""

    if max_k < prime:
        return 0
    return sum(actual_fixed_prime_split(k, prime) for k in range(prime, max_k + 1))
