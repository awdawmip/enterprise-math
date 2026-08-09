"""Separate intrinsic material dead zones from kinematic quantization dead zones.

A ZERO_RETURN state can arise for two different finite reasons:

1. **material-zero**: the represented return-branch sample itself is exactly zero;
2. **kinematic-zero**: the material sample is positive, but the incoming budget
   is too small to resolve one returned motion quantum.

For a nondecreasing returning branch let

    k_0 = min { k>=1 : R_k > 0 }

be the first intrinsically positive material depth, and for incoming budget B let

    k_B = min { k>=1 : B*R_k >= A }

be the first depth with nonzero kinematic return.  Whenever ``k_B`` exists,
``k_B>=k_0``.  As B increases, ``k_B`` can move inward only toward ``k_0``; it
can never erase an intrinsic material-zero shell.  Thus the outer zero-return
region decomposes into a persistent material dead zone plus a budget-dependent
kinematic quantization zone.

The nD state-mass formulas below telescope over clearance depth shells.  They are
finite multiplicities, not physical continuum volumes.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_clearance_response_spectrum import material_clearance_coverage
from .material_response import MaterialCurveProfile
from .material_scale_phase_diagram import minimum_rebound_depth
from .material_scale_response import returning_branch_is_monotone


def first_positive_return_depth(profile: MaterialCurveProfile) -> int | None:
    """First positive-depth return sample that is intrinsically nonzero."""
    for depth, sample in enumerate(profile.returning[1:], start=1):
        if sample > 0:
            return depth
    return None


@dataclass(frozen=True)
class ZeroReturnDecompositionND:
    dimension: int
    collapse_factor: int
    incoming_budget: int
    represented_max_depth: int
    first_positive_material_depth: int | None
    first_nonzero_kinematic_depth: int | None
    material_zero_states: int
    kinematic_quantization_zero_states: int
    rebound_states: int
    underresolved_states: int
    coarse_only_states: int

    @property
    def zero_return_states(self) -> int:
        return self.material_zero_states + self.kinematic_quantization_zero_states


def zero_return_decomposition_nd(
    dimension: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> ZeroReturnDecompositionND:
    """Split represented zero-return state mass into material and budget causes."""
    for name, value in (("dimension", dimension), ("collapse_factor", collapse_factor)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if (
        isinstance(incoming_budget, bool)
        or not isinstance(incoming_budget, int)
        or incoming_budget < 0
    ):
        raise ValueError("incoming_budget must be a non-negative integer")
    if not profile.returning or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")
    if not returning_branch_is_monotone(profile):
        raise ValueError("returning branch must be nondecreasing for contiguous dead zones")

    max_depth = len(profile.returning) - 1
    coverage = material_clearance_coverage(
        dimension,
        collapse_factor,
        max_depth,
    )
    represented_max = coverage.effective_represented_depth
    k0_global = first_positive_return_depth(profile)
    k0 = (
        k0_global
        if k0_global is not None and k0_global <= represented_max
        else None
    )
    kB_global = minimum_rebound_depth(incoming_budget, profile)
    kB = (
        kB_global
        if kB_global is not None and kB_global <= represented_max
        else None
    )
    if kB is not None and (k0 is None or kB < k0):
        raise AssertionError("kinematic nonzero return appeared before positive material response")

    d = collapse_factor
    inner_side = d - represented_max
    if k0 is None:
        material_zero = coverage.represented_states
        kinematic_zero = 0
        rebound = 0
    else:
        positive_outer_side = d - k0 + 1
        material_zero = d**dimension - positive_outer_side**dimension
        positive_material_states = positive_outer_side**dimension - inner_side**dimension
        if kB is None:
            kinematic_zero = positive_material_states
            rebound = 0
        else:
            rebound_outer_side = d - kB + 1
            kinematic_zero = positive_outer_side**dimension - rebound_outer_side**dimension
            rebound = rebound_outer_side**dimension - inner_side**dimension

    if material_zero + kinematic_zero + rebound != coverage.represented_states:
        raise AssertionError("zero-return cause decomposition lost represented states")
    if material_zero + kinematic_zero + rebound + coverage.underresolved_states != coverage.coarse_only_states:
        raise AssertionError("zero-return cause decomposition failed coarse-box conservation")
    return ZeroReturnDecompositionND(
        dimension=dimension,
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        represented_max_depth=represented_max,
        first_positive_material_depth=k0,
        first_nonzero_kinematic_depth=kB,
        material_zero_states=material_zero,
        kinematic_quantization_zero_states=kinematic_zero,
        rebound_states=rebound,
        underresolved_states=coverage.underresolved_states,
        coarse_only_states=coverage.coarse_only_states,
    )
