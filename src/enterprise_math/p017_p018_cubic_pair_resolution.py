"""P017/P018 bridge: cubic-root localization of residual core-pair ambiguity.

The preceding cubic-high bridge proves that in every residual hard-core pair
``3<=d<e``, ``d*e<k``, the smaller full core ``d`` has its complete candidate
root channel strictly above the P018 cubic candidate horizon

    H = R_3(2*k^2-1) + 1.

This module asks when the *larger* core ``e`` is also forced above that horizon.
Define the exact ambiguity cutoff

    D(k) = floor(((H+1)^2 - 1) / k).

If the larger-core base root ``j_e=R_2(floor(k^2/e))`` is at most H, then

    floor(k^2/e) < (H+1)^2,

hence

    k^2 < e(H+1)^2.

Multiplying by d and using d*e<=k-1 gives

    d k^2 < (k-1)(H+1)^2 < k(H+1)^2,

so

    d k < (H+1)^2

and therefore ``d<=D(k)``.

Contrapositive: if ``d>D(k)``, both odd full-core channels lie strictly above
H.  Consuming the P018 odd-channel injectivity theorem, both full-core labels
are then recoverable from their two root channels.  All possible partner-core
channel ambiguity is confined to the odd small-core cells ``3<=d<=D(k)``.

The cutoff is sharp on the existing P017/P018 prime-tail witness:

    k=64, H=21, D=7, (d,e)=(7,9), (j_d,j_e)=(24,21).

Thus the larger-core channel can hit the cubic horizon exactly when the smaller
core sits at the cutoff.  This is a bridge theorem, not a new P018 mother result
and not a P017 L-number.
"""

from __future__ import annotations

from .p017_p018_cubic_high_channel import (
    cubic_candidate_horizon,
    transverse_small_endpoint_cubic_channel,
)
from .p017_p018_hard_core_bridge import base_root_index


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def cubic_partner_ambiguity_cutoff(k: int) -> int:
    """Return D(k)=floor(((H_c(k)+1)^2-1)/k)."""
    _require_int("k", k)
    if k < 2:
        raise ValueError("k must be at least 2")
    horizon = cubic_candidate_horizon(k)
    return ((horizon + 1) ** 2 - 1) // k


def odd_ambiguity_cell_count_bound(k: int) -> int:
    """Return the number of possible odd cells 3<=d<=D(k)."""
    cutoff = cubic_partner_ambiguity_cutoff(k)
    if cutoff < 3:
        return 0
    return (cutoff - 1) // 2


def residual_pair_cubic_resolution(k: int, d: int, e: int) -> dict[str, object]:
    """Classify whether one residual core pair is fully root-channel resolved.

    The input uses the same transverse hard-core assumptions as the preceding
    bridge.  The smaller channel is proved cubic-high there.  This function
    proves that a low larger-core channel can occur only when d<=D(k).
    """
    for name, value in (("k", k), ("d", d), ("e", e)):
        _require_int(name, value)

    small_route = transverse_small_endpoint_cubic_channel(k, d, e)
    horizon = int(small_route["cubic_horizon"])
    cutoff = cubic_partner_ambiguity_cutoff(k)
    larger_root = base_root_index(k, e)
    larger_channel = (larger_root, larger_root + 1)
    larger_is_high = larger_root > horizon

    if not larger_is_high:
        # j_e<=H means floor(k^2/e)<(H+1)^2, equivalently
        # k^2<e(H+1)^2.  Multiplying by d and using de<=k-1 yields the
        # exact cutoff inequality d*k<(H+1)^2.
        if not k * k < e * (horizon + 1) ** 2:
            raise AssertionError("low larger-root channel missed its square upper bound")
        if not d * e <= k - 1:
            raise AssertionError("d*e<k lost its integer product bound")
        if not d * k < (horizon + 1) ** 2:
            raise AssertionError("low partner channel failed the ambiguity cutoff inequality")
        if d > cutoff:
            raise AssertionError("low partner channel escaped the exact cutoff D(k)")
    elif d > cutoff and larger_root <= horizon:
        raise AssertionError("contrapositive cubic resolution failed")

    return {
        **small_route,
        "ambiguity_cutoff": cutoff,
        "odd_ambiguity_cell_bound": odd_ambiguity_cell_count_bound(k),
        "larger_base_root": larger_root,
        "larger_candidate_channel": larger_channel,
        "larger_channel_is_high": larger_is_high,
        "fully_core_pair_root_resolved": larger_is_high,
        "small_core_inside_ambiguity_frontier": d <= cutoff,
    }


def high_small_core_forces_full_pair_resolution(k: int, d: int, e: int) -> dict[str, object]:
    """Require d>D(k) and certify that both odd-core channels are cubic-high."""
    cutoff = cubic_partner_ambiguity_cutoff(k)
    if d <= cutoff:
        raise ValueError("require smaller core d above the ambiguity cutoff")
    data = residual_pair_cubic_resolution(k, d, e)
    if not data["larger_channel_is_high"]:
        raise AssertionError("d>D(k) failed to force the larger channel high")
    if not all(
        root > data["cubic_horizon"] for root in data["larger_candidate_channel"]
    ):
        raise AssertionError("larger candidate channel is not wholly cubic-high")
    return data
