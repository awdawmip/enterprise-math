"""Sharp radius/volume bounds for one binary-helper action support.

For one declared helper action q in an acyclic helper dependency graph where
every helper has at most two helper predecessors, let h be the maximum reverse
dependency distance from an ancestor helper to q.  Then

    h + 1 <= |down(q)| <= 2^(h+1) - 1.

The lower bound is a longest dependency path.  The upper bound follows because
reverse shell t has at most 2^t helpers.  A sequential helper chain attains the
lower bound; a perfect binary helper subtree attains the upper bound.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_synergy_depth import synergy_chain
from .closure_support_horizon_geometry import support_horizon_geometry
from .closure_action_support_cost import largest_single_action_support


@dataclass(frozen=True)
class SupportRadiusVolumeExtremes:
    horizon: int
    lower_bound: int
    upper_bound: int
    sequential_arity: int
    sequential_support_count: int
    balanced_arity: int
    balanced_support_count: int
    lower_sharp: bool
    upper_sharp: bool


def sequential_top_helper_support_count(arity: int) -> tuple[int, int]:
    """Return (reverse horizon, helper support count) for top sequential helper."""
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 3:
        raise ValueError("arity must be an integer >= 3")
    compiler = synergy_chain(arity)
    helpers = compiler.helpers
    if not helpers:
        return 0, 0
    # e_(k-1) depends on the chain e2 -> e3 -> ... -> e_(k-1).
    return arity - 3, len(helpers)


def support_radius_volume_extremes(horizon: int) -> SupportRadiusVolumeExtremes:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a nonnegative integer")
    lower = horizon + 1
    upper = (1 << (horizon + 1)) - 1

    sequential_arity = horizon + 3
    seq_h, seq_count = sequential_top_helper_support_count(sequential_arity)
    if seq_h != horizon:
        raise AssertionError("sequential chain must realize the requested horizon")

    # Perfect balanced top helper has H_supp=log2(k)-2.  Therefore k=2^(h+2).
    balanced_arity = 1 << (horizon + 2)
    top = largest_single_action_support(balanced_arity)
    geometry = support_horizon_geometry(balanced_arity, top.support_generators)
    if geometry.horizon != horizon:
        raise AssertionError("perfect tree must realize the requested horizon")
    balanced_count = top.dependency_support_count

    return SupportRadiusVolumeExtremes(
        horizon=horizon,
        lower_bound=lower,
        upper_bound=upper,
        sequential_arity=sequential_arity,
        sequential_support_count=seq_count,
        balanced_arity=balanced_arity,
        balanced_support_count=balanced_count,
        lower_sharp=seq_count == lower,
        upper_sharp=balanced_count == upper,
    )
