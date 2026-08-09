"""Exact sampled phase spectrum for the E001 1D collapse-material wall toy world.

For a wall/body effective thickness ``H`` and a separated-side displacement
``s>=H``, every positive-clearance crossing phase is determined by

    g_pre + g_post = C = s-H+2,
    g_pre,g_post >= 1.

There are ``C-1`` such phases.  Let ``g=min(g_pre,g_post)``.  At spatial factor
``d``:

* ``g>=d`` transmits;
* ``g<d`` enters interaction-layer depth ``k=d-g``;
* if ``k`` exceeds the finite material branch, that phase is explicitly
  ``UNDERRESOLVED`` rather than clamped or rejected;
* a represented interaction with returned budget 0 is ``ZERO_RETURN``;
* only strictly positive returned budget contributes to ``REBOUND`` phase mass.

Thus every positive-clearance phase is conserved exactly as

    TRANSMIT + UNDERRESOLVED + ZERO_RETURN + REBOUND.

Counts and sums are combinatorial; they are not probabilities, energy, or
expected values unless an external interpretation is separately declared.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_kinematic_coupling import rebound_budget
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import Wall1D, minimum_positive_clearance_crossing_displacement


@dataclass(frozen=True)
class ReboundPhaseBin:
    """Number of crossing phases producing one strictly positive returned budget."""

    returned_budget: int
    phase_count: int


@dataclass(frozen=True)
class MaterialPhaseSpectrum1D:
    """Exact four-way phase histogram for one finite material/world tuple."""

    wall_thickness: int
    body_diameter: int
    effective_thickness: int
    displacement: int
    collapse_factor: int
    incoming_budget: int
    positive_clearance_phases: int
    transmitting_phases: int
    underresolved_phases: int
    zero_return_phases: int
    rebound_phases: int
    rebound_bins: tuple[ReboundPhaseBin, ...]
    total_returned_budget_over_phases: int

    @property
    def interaction_phases(self) -> int:
        return self.underresolved_phases + self.zero_return_phases + self.rebound_phases


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
    """Count positive-clearance crossing phases by finite material outcome."""
    for name, value, lower in (
        ("radius", radius, 0),
        ("displacement", displacement, 0),
        ("collapse_factor", collapse_factor, 1),
        ("incoming_budget", incoming_budget, 0),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < lower:
            raise ValueError(f"{name} must be an integer >= {lower}")
    if not material_profile.returning or len(material_profile.loading) != len(material_profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")

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
            underresolved_phases=0,
            zero_return_phases=0,
            rebound_phases=0,
            rebound_bins=(),
            total_returned_budget_over_phases=0,
        )

    positive_phases = clearance_sum - 1
    transmitting = 0
    underresolved = 0
    zero_return = 0
    rebound_counts: Counter[int] = Counter()
    max_gap = clearance_sum // 2
    max_depth = len(material_profile.returning) - 1
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
        if depth > max_depth:
            underresolved += multiplicity
            continue
        response_sample = material_profile.returning[depth]
        returned = rebound_budget(
            incoming_budget,
            response_sample,
            material_profile.amplitude,
        ).returned_budget
        if returned == 0:
            zero_return += multiplicity
        else:
            rebound_counts[returned] += multiplicity

    if counted != positive_phases:
        raise AssertionError("controlling-gap multiplicities lost crossing phases")
    rebound_phases = sum(rebound_counts.values())
    if transmitting + underresolved + zero_return + rebound_phases != positive_phases:
        raise AssertionError("phase spectrum failed four-way count conservation")

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
        underresolved_phases=underresolved,
        zero_return_phases=zero_return,
        rebound_phases=rebound_phases,
        rebound_bins=bins,
        total_returned_budget_over_phases=total_returned,
    )
