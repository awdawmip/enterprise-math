"""Exact 1D partition of the collapse-generated material interaction shell.

The geometric positive-gap interaction shell at collapse factor ``d`` has
primitive clearances ``g=1..d-1`` and therefore thickness ``d-1``.  Calling all
of it a rebound layer is generally too coarse.  With a finite material return
branch and an incoming budget ``B``, the shell splits into at most four disjoint
positive-gap regions, ordered from the primitive core outward:

    UNDERRESOLVED -> REBOUND -> ZERO_RETURN -> RESOLVED exterior.

Including primitive contact ``g=0`` gives the five-zone picture

    primitive core
      -> underresolved inner shell
      -> true rebound band
      -> zero-return dead shell
      -> resolved exterior.

For a nondecreasing returning branch, represented depths are ``1..K'`` with
``K'=min(K,d-1)``.  If ``k_B`` is the first depth with ``B*R_k >= A``:

* underresolved thickness = ``d-1-K'``;
* rebound thickness = ``max(0, K'-k_B+1)`` when ``k_B`` exists;
* zero-return thickness is the remaining represented depth count.

The intervals are expressed in primitive positive clearance coordinates.  They
are effective dynamics zones of the declared finite world policy, not geometric
material thicknesses or continuum constitutive regions.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import MaterialCurveProfile
from .material_scale_phase_diagram import minimum_rebound_depth
from .material_scale_response import returning_branch_is_monotone

ClearanceInterval = tuple[int, int]


def _interval(lo: int, hi: int) -> ClearanceInterval | None:
    return None if lo > hi else (lo, hi)


@dataclass(frozen=True)
class EffectiveMaterialLayer1D:
    collapse_factor: int
    incoming_budget: int
    material_max_depth: int
    represented_max_depth: int
    minimum_rebound_depth: int | None
    geometric_shell_thickness: int
    underresolved_thickness: int
    rebound_thickness: int
    zero_return_thickness: int
    underresolved_clearances: ClearanceInterval | None
    rebound_clearances: ClearanceInterval | None
    zero_return_clearances: ClearanceInterval | None
    resolved_exterior_min_clearance: int

    @property
    def represented_thickness(self) -> int:
        return self.rebound_thickness + self.zero_return_thickness


def effective_material_layer_1d(
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> EffectiveMaterialLayer1D:
    """Partition all positive clearances collapsed by ``d`` under a monotone branch."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")
    if not profile.returning or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if not returning_branch_is_monotone(profile):
        raise ValueError("returning branch must be nondecreasing for contiguous layer partition")

    geometric = collapse_factor - 1
    max_depth = len(profile.returning) - 1
    represented_max = min(max_depth, geometric)
    underresolved = geometric - represented_max
    k_min_global = minimum_rebound_depth(incoming_budget, profile)
    k_min = (
        k_min_global
        if k_min_global is not None and k_min_global <= represented_max
        else None
    )

    if k_min is None:
        rebound = 0
        zero_return = represented_max
    else:
        rebound = represented_max - k_min + 1
        zero_return = k_min - 1

    if underresolved + rebound + zero_return != geometric:
        raise AssertionError("effective material shell partition lost clearance cells")

    # depth k=d-g, so deeper represented states lie closer to the primitive core.
    underresolved_interval = _interval(1, underresolved)
    represented_inner_gap = underresolved + 1
    if k_min is None:
        rebound_interval = None
        zero_interval = _interval(represented_inner_gap, geometric)
    else:
        # k in [k_min, represented_max] maps to
        # g in [d-represented_max, d-k_min].
        rebound_interval = _interval(
            collapse_factor - represented_max,
            collapse_factor - k_min,
        )
        zero_interval = _interval(collapse_factor - k_min + 1, geometric)

    def _length(interval: ClearanceInterval | None) -> int:
        return 0 if interval is None else interval[1] - interval[0] + 1

    if _length(underresolved_interval) != underresolved:
        raise AssertionError("underresolved interval length mismatch")
    if _length(rebound_interval) != rebound:
        raise AssertionError("rebound interval length mismatch")
    if _length(zero_interval) != zero_return:
        raise AssertionError("zero-return interval length mismatch")

    return EffectiveMaterialLayer1D(
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        material_max_depth=max_depth,
        represented_max_depth=represented_max,
        minimum_rebound_depth=k_min,
        geometric_shell_thickness=geometric,
        underresolved_thickness=underresolved,
        rebound_thickness=rebound,
        zero_return_thickness=zero_return,
        underresolved_clearances=underresolved_interval,
        rebound_clearances=rebound_interval,
        zero_return_clearances=zero_interval,
        resolved_exterior_min_clearance=collapse_factor,
    )
