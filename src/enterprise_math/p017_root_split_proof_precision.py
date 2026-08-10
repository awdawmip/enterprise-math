"""Bonferroni proof precision for actual P017 factor->root shell splitting.

L069 makes each branch occupancy an exact p-rough interval count.  This module
asks how many inclusion-exclusion orders are sufficient to *prove* positivity.
The resulting depth is proof precision, not part of the represented number state.
"""

from __future__ import annotations

from .p017_root_split_mobius import root_split_mobius_counts
from .rough_bonferroni import minimum_positive_bonferroni_depth


def split_branch_proof_depths(k: int, prime: int) -> dict[str, object]:
    """Return minimum odd Bonferroni depths for both occupied root branches."""

    data = root_split_mobius_counts(k, prime)
    if not bool(data["realized_split"]):
        return {
            **data,
            "lower_proof_depth": None,
            "upper_proof_depth": None,
            "split_proof_depth": None,
        }

    lower = data["lower_interval"]
    upper = data["upper_interval"]
    if lower is None or upper is None:
        raise AssertionError("realized split lost a raw branch interval")

    lower_depth = minimum_positive_bonferroni_depth(int(lower[0]), int(lower[1]), prime)
    upper_depth = minimum_positive_bonferroni_depth(int(upper[0]), int(upper[1]), prime)

    # A missing odd Bonferroni certificate is allowed: exact inclusion-exclusion
    # can still prove positivity.  Mark the combined shallow proof depth as None
    # in that case rather than inventing an even-depth lower bound.
    split_depth = (
        None
        if lower_depth is None or upper_depth is None
        else max(lower_depth, upper_depth)
    )
    return {
        **data,
        "lower_proof_depth": lower_depth,
        "upper_proof_depth": upper_depth,
        "split_proof_depth": split_depth,
    }
