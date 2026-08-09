"""Exact sampled phase spectrum for the E001 1D collapse-material wall toy world.

For a wall/body effective thickness ``H`` and a separated-side displacement
``s>=H``, every positive-clearance crossing phase is determined by

    g_pre + g_post = C = s-H+2,
    g_pre,g_post >= 1.

There are ``C-1`` such phases.  Let ``g=min(g_pre,g_post)``.  At spatial factor
``d``:

* ``g>=d`` transmits;
* ``g<d`` enters interaction-layer depth ``k=d-g`` and returns integer motion
  budget ``floor(B*R_k/A)`` from the declared RETURNING material branch.

This module counts phases by outcome exactly and also sums returned integer
budget over all represented phases.  Counts and sums are combinatorial; they are
not probabilities, energy, or expected values unless an external interpretation
is separately declared.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_kinematic_coupling import rebound_budget
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import Wall1D, minimum_positive_clearance_crossing_displacement


@dataclass(frozen=True)
class ReboundPhaseBin:
    """Number of crossing phases producing one integer returned budget."""

    returned_budget: int
    phase_count: int


@dataclass(frozen=True)
class MaterialPhaseSpectrum1D:
    """Exact transmission/rebound histogram for one finite parameter tuple."""

    wall_thickness: int
    body_diameter: int
    effective_thickness: int
    displacement: int
    collapse_factor: int
    incoming_budget: int
    positive_clearance_phases: int
    transmitting_phases: int
    rebound_phases: int
    rebound_bins: tuple[ReboundPhaseBin, ...]
    total_returned_budget_over_phases: int


def controlling_gap_phase_multiplicity(clearance_sum: int, controlling_gap: int) -> int:
    """Multiplicity of ``min(g_pre,g_post)=g`` for positive pairs summing to C."""
    if (
        isinstance(clearance_sum, bool)
        or not isinstance(clearance_sum, int)
        or clearance_sum < 2
    ):
        raise ValueError("clearance_sum must be an integer >=2")
    if (
        isinstance(controlling_gap, bool)
        or not isinstance(controlling_gap, int)
        or controlling_gap <= 0
    ):
        raise ValueError("controlling_gap must be a positive integer")
    if 2 * controlling_gap > clearance_sum:
        return 0
    return 1 if 2 * controlling_gap == clearance_sum else 2


def material_phase_spectrum(
    wall: Wall1D,
    radius: int,
    displacement: int,
    collapse_factor: int,
    incoming_budget: int,
    material_profile: MaterialCurveProfile,
) -> MaterialPhaseSpectrum1D:
    """Count exact positive-clearance crossing phases by finite material outcome."""
    for name, value, lower in (
        ("radius", radius, 0),
        ("displacement", displacement, 0),
        ("collapse_factor", collapse_factor, 1),
        ("incoming_budget", incoming_budget, 0),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < lower:
            raise ValueError(f"{name} must be an integer >= {lower}")

    effective = minimum_positive_clearance_crossing_displacement(wall, radius)
    clearance_sum = displacement - effective + 2
    if clearance_sum < 2:
        return MaterialPhaseSpectrum1D(
            wall_thickness=wall.thickness_cells,
            body_diameter=2 * radius + 1,
            effective_thickness=effective,
            displacement=displacement,
            collapse_factor=collapse_factor,
            incoming_budget=incoming_budget,
            positive_clearance_phases=0,
            transmitting_phases=0,
            rebound_phases=0,
            rebound_bins=(),
            total_returned_budget_over_phases=0,
        )

    if collapse_factor - 1 >= len(material_profile.returning):
        raise ValueError(
            "material return curve must represent every possible coarse layer depth"
        )

    positive_phases = clearance_sum - 1
    transmitting = 0
    rebound_counts: Counter[int] = Counter()
    max_gap = clearance_sum // 2
    counted = 0
    for gap in range(1, max_gap + 1):
        multiplicity = controlling_gap_phase_multiplicity(clearance_sum, gap)
        if multiplicity == 0:
            continue
        counted += multiplicity
        if gap >= collapse_factor:
            transmitting += multiplicity
            continue
        depth = collapse_factor - gap
        response_sample = material_profile.returning[depth]
        returned = rebound_budget(
            incoming_budget,
            response_sample,
            material_profile.amplitude,
        ).returned_budget
        rebound_counts[returned] += multiplicity

    if counted != positive_phases:
        raise AssertionError("controlling-gap multiplicities lost crossing phases")
    rebound_phases = sum(rebound_counts.values())
    if transmitting + rebound_phases != positive_phases:
        raise AssertionError("phase spectrum failed total-count conservation")

    bins = tuple(
        ReboundPhaseBin(returned_budget=budget, phase_count=count)
        for budget, count in sorted(rebound_counts.items())
    )
    total_returned = sum(
        item.returned_budget * item.phase_count for item in bins
    )
    return MaterialPhaseSpectrum1D(
        wall_thickness=wall.thickness_cells,
        body_diameter=2 * radius + 1,
        effective_thickness=effective,
        displacement=displacement,
        collapse_factor=collapse_factor,
        incoming_budget=incoming_budget,
        positive_clearance_phases=positive_phases,
        transmitting_phases=transmitting,
        rebound_phases=rebound_phases,
        rebound_bins=bins,
        total_returned_budget_over_phases=total_returned,
    )
