"""High-displacement saturation of the endpoint-only 1D interaction phase spectrum.

For positive endpoint-clearance sum ``C`` and spatial collapse factor ``d``, an
interaction phase has controlling gap ``g<d``.  The multiplicity of one gap is
2 except at the symmetric center ``2g=C``, where it is 1.

Therefore, once

    C >= 2d-1,

every possible interaction gap ``g=1,...,d-1`` lies strictly before the center
and has multiplicity exactly 2.  Equivalently every interaction depth
``k=d-g=1,...,d-1`` appears in one left-heavy and one right-heavy saved-state
phase.  The interaction spectrum has saturated:

    N_interaction = 2(d-1),
    N_transmit = C-2d+1.

Further displacement can only add transmission phases.  It cannot add new
interaction phase mass at the same spatial precision.

For a finite material return branch, each represented depth therefore contributes
exactly two copies of its kinematic return class, while every unrepresented depth
contributes exactly two UNDERRESOLVED phases.  This factorization requires no
monotonicity assumption on the material branch.

This is an endpoint-only saved-state theorem.  No hidden path sweep is inserted.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .material_kinematic_coupling import rebound_budget
from .material_phase_spectrum import material_phase_spectrum
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import Wall1D, minimum_positive_clearance_crossing_displacement


@dataclass(frozen=True, order=True)
class SaturatedReturnedBudgetBin:
    returned_budget: int
    phase_count: int


@dataclass(frozen=True)
class SaturatedInteractionPhaseSpectrum1D:
    collapse_factor: int
    incoming_budget: int
    material_max_depth: int
    interaction_phases: int
    underresolved_phases: int
    zero_return_phases: int
    rebound_phases: int
    rebound_bins: tuple[SaturatedReturnedBudgetBin, ...]


def saturated_interaction_phase_spectrum(
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> SaturatedInteractionPhaseSpectrum1D:
    """Factorized interaction spectrum valid once ``C>=2d-1``."""
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

    d = collapse_factor
    interaction = 2 * (d - 1)
    max_depth = len(profile.returning) - 1
    represented_max = min(max_depth, d - 1)
    underresolved = 2 * ((d - 1) - represented_max)
    zero_return = 0
    counts: Counter[int] = Counter()
    for depth in range(1, represented_max + 1):
        returned = rebound_budget(
            incoming_budget,
            profile.returning[depth],
            profile.amplitude,
        ).returned_budget
        if returned == 0:
            zero_return += 2
        else:
            counts[returned] += 2
    rebound = sum(counts.values())
    if underresolved + zero_return + rebound != interaction:
        raise AssertionError("saturated interaction depth factorization lost phase mass")
    return SaturatedInteractionPhaseSpectrum1D(
        collapse_factor=d,
        incoming_budget=incoming_budget,
        material_max_depth=max_depth,
        interaction_phases=interaction,
        underresolved_phases=underresolved,
        zero_return_phases=zero_return,
        rebound_phases=rebound,
        rebound_bins=tuple(
            SaturatedReturnedBudgetBin(returned_budget=budget, phase_count=count)
            for budget, count in sorted(counts.items())
        ),
    )


def saturation_clearance_sum_threshold(collapse_factor: int) -> int:
    """Smallest ``C`` for which every interaction depth has multiplicity two."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    return 2 * collapse_factor - 1


def verify_saturated_wall_phase_spectrum(
    wall: Wall1D,
    radius: int,
    displacement: int,
    collapse_factor: int,
    incoming_budget: int,
    profile: MaterialCurveProfile,
) -> bool:
    """Check the factorized theorem against the full endpoint phase enumerator."""
    effective = minimum_positive_clearance_crossing_displacement(wall, radius)
    clearance_sum = displacement - effective + 2
    if clearance_sum < saturation_clearance_sum_threshold(collapse_factor):
        raise ValueError("wall jump has not reached the phase-saturation threshold")
    full = material_phase_spectrum(
        wall,
        radius,
        displacement,
        collapse_factor,
        incoming_budget,
        profile,
    )
    saturated = saturated_interaction_phase_spectrum(
        collapse_factor,
        incoming_budget,
        profile,
    )
    return (
        full.interaction_phases == saturated.interaction_phases
        and full.underresolved_phases == saturated.underresolved_phases
        and full.zero_return_phases == saturated.zero_return_phases
        and full.rebound_phases == saturated.rebound_phases
        and tuple((item.returned_budget, item.phase_count) for item in full.rebound_bins)
        == tuple((item.returned_budget, item.phase_count) for item in saturated.rebound_bins)
        and full.transmitting_phases == clearance_sum - 2 * collapse_factor + 1
    )
