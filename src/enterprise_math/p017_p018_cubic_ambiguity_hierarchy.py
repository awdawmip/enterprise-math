"""P017/P018 bridge: nested ambiguity frontiers inside the cubic low-partner zone.

This module refines the exact partner-ambiguity cutoff with the affine-cell
spacing discovered on P017 #150.

Let

    H = R_3(2*k^2-1)+1

be the P018 candidate-channel horizon. If a residual hard-core pair ``d<e``
has the larger-core base root at or below H, then the exact square-root
inequality forces

    e >= L(k) = floor(k^2/(H+1)^2) + 1.

The preceding bridge also forces ``d<=D(k)``. Combining the lower bound on ``e``
with the P017 #150 parity-cell spacing gives nested frontiers

    E_2(k) = floor((k-1)/(2*L(k))),
    E_6(k) = floor((k-1)/(6*L(k))).

If ``d>E_2(k)``, then ``2de>=k``. Therefore the parity-compatible full-core
cell (one residue class modulo ``2de`` in #150) has at most one bounded radius
in ``1<=r<k``.

In the generic mod-3 branch of #150, two prime-tail lifts require ``6de<k``.
Thus ``d>E_6(k)`` makes a second prime-tail lift impossible whenever
``3`` does not divide ``M*de``.

This does not contradict the local-admissibility negative boundary of #150:
it localizes where repeated ambiguity can live; it does not claim a fixed CRT
wheel kills every cell.
"""

from __future__ import annotations

from .p017_p018_cubic_high_channel import cubic_candidate_horizon
from .p017_p018_cubic_pair_resolution import (
    cubic_partner_ambiguity_cutoff,
    residual_pair_cubic_resolution,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def low_partner_core_floor(k: int) -> int:
    """Return L(k), the minimum possible larger core in the low-partner zone."""
    _require_int("k", k)
    if k < 2:
        raise ValueError("k must be at least 2")
    horizon = cubic_candidate_horizon(k)
    return (k * k) // ((horizon + 1) ** 2) + 1


def parity_multilift_small_core_cutoff(k: int) -> int:
    """Return E_2(k): only d<=E_2 can have 2de<k in a low-partner cell."""
    lower = low_partner_core_floor(k)
    return (k - 1) // (2 * lower)


def ternary_multilift_small_core_cutoff(k: int) -> int:
    """Return E_6(k): generic two-prime-tail cells need d<=E_6."""
    lower = low_partner_core_floor(k)
    return (k - 1) // (6 * lower)


def low_partner_ambiguity_hierarchy(k: int, d: int, e: int) -> dict[str, object]:
    """Classify one residual pair inside/outside the nested ambiguity layers."""
    data = residual_pair_cubic_resolution(k, d, e)
    horizon = int(data["cubic_horizon"])
    larger_root = int(data["larger_base_root"])
    if larger_root > horizon:
        raise ValueError("pair is already fully cubic-high; no low-partner ambiguity remains")

    lower = low_partner_core_floor(k)
    e2 = parity_multilift_small_core_cutoff(k)
    e6 = ternary_multilift_small_core_cutoff(k)
    center = k * (k + 1)
    product = d * e

    if e < lower:
        raise AssertionError("low partner root failed to force e>=L(k)")
    if d > int(data["ambiguity_cutoff"]):
        raise AssertionError("low partner root escaped D(k)")

    parity_can_repeat = 2 * product < k
    if parity_can_repeat and d > e2:
        raise AssertionError("parity multi-lift cell escaped E_2(k)")

    generic_mod3 = (center * product) % 3 != 0
    ternary_can_repeat = generic_mod3 and 6 * product < k
    if ternary_can_repeat and d > e6:
        raise AssertionError("generic ternary multi-prime cell escaped E_6(k)")

    return {
        **data,
        "low_partner_core_floor": lower,
        "parity_multilift_cutoff": e2,
        "ternary_multilift_cutoff": e6,
        "larger_core_floor_margin": e - lower,
        "parity_cell_can_have_multiple_lifts": parity_can_repeat,
        "generic_mod3_cell": generic_mod3,
        "generic_mod3_cell_can_have_multiple_prime_lifts": ternary_can_repeat,
        "ternary_exception": not generic_mod3,
    }


def hierarchy_summary(k: int) -> dict[str, int]:
    """Return the four exact scale cutoffs D,L,E2,E6 for one parent k."""
    _require_int("k", k)
    if k < 16:
        raise ValueError("residual odd hard-core pairs require k>=16")
    return {
        "k": k,
        "partner_ambiguity_cutoff": cubic_partner_ambiguity_cutoff(k),
        "low_partner_core_floor": low_partner_core_floor(k),
        "parity_multilift_cutoff": parity_multilift_small_core_cutoff(k),
        "ternary_multilift_cutoff": ternary_multilift_small_core_cutoff(k),
    }
