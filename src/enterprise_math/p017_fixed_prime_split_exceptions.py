"""Finite audit of Pell-type exceptions to fixed-prime P017 split density.

For a fixed prime p, Beatty-core candidates are k=floor(m*sqrt(p)).  Any actual
split failure inside that core must have one raw branch shorter than the fixed
primorial P_<p.  This forces one of two bounded Pell defects:

    p*m^2 - k^2 = N,
    (k+1)^2 - p*m^2 = N.

The theorem that each fixed generalized Pell equation has only O(log K)
solutions up to K is classical; this module only records and checks the exact
finite defects for bounded audits.
"""

from __future__ import annotations

from .p017_fixed_prime_split_density import (
    actual_fixed_prime_split,
    integer_beatty_core,
)
from .p017_root_split_overshoot import raw_root_branch_slot_counts
from .rough_interval_mobius import lower_primorial


def fixed_prime_failure_defect(k: int, prime: int) -> dict[str, int | bool | None]:
    """Classify one Beatty-core actual failure by its bounded Pell defect."""

    raw = raw_root_branch_slot_counts(k, prime)
    beatty = integer_beatty_core(k, prime)
    actual = actual_fixed_prime_split(k, prime)
    if not beatty or actual:
        return {
            "beatty_core": beatty,
            "actual_split": actual,
            "failure": False,
            "lower_defect": None,
            "upper_defect": None,
        }

    primorial = lower_primorial(prime)
    m = int(raw["boundary_root"])
    lower_defect = prime * m * m - k * k
    upper_defect = (k + 1) * (k + 1) - prime * m * m

    lower_short = int(raw["lower_slots"]) < primorial
    upper_short = int(raw["upper_slots"]) < primorial
    if not (lower_short or upper_short):
        raise AssertionError("actual fixed-prime failure escaped short-branch localization")
    if lower_short and not (1 <= lower_defect <= prime * primorial):
        raise AssertionError("lower Pell defect escaped finite bound")
    if upper_short and not (1 <= upper_defect <= prime * max(primorial - 1, 0)):
        raise AssertionError("upper Pell defect escaped finite bound")

    return {
        "beatty_core": True,
        "actual_split": False,
        "failure": True,
        "lower_defect": lower_defect if lower_short else None,
        "upper_defect": upper_defect if upper_short else None,
        "lower_primorial": primorial,
    }


def fixed_prime_failure_count(prime: int, max_k: int) -> int:
    if max_k < prime:
        return 0
    return sum(
        bool(fixed_prime_failure_defect(k, prime)["failure"])
        for k in range(prime, max_k + 1)
    )
