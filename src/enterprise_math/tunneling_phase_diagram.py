"""E001.10 exact discrete phase counts for sampled wall tunneling.

Let a 1D wall occupy ``T`` primitive cells and a moving interval body occupy
``D=2r+1`` primitive cells.  Define effective obstruction thickness

    H = T + D.

For a fixed left-to-right center displacement ``s``, a sampled transition whose
pre/post body supports lie on opposite sides with positive primitive clearances
``g_pre,g_post>=1`` satisfies the exact identity

    g_pre + g_post = s - H + 2.

Therefore, when ``s>=H``, the number of integer phase choices with positive
clearance at both represented endpoints is

    N_sep = s - H + 1.

At spatial collapse factor ``d``, sampled-state transmission requires both
endpoint clearances to survive collapse:

    g_pre>=d and g_post>=d.

The exact number of transmitting phases is

    N_trans(d) = max(0, s - H - 2*d + 3).

Hence at least one sampled transmitting phase exists iff

    s >= H + 2*(d-1).

The remaining positive-clearance crossing phases are macro-contact phases at
that scale.  These are combinatorial counts, not probabilities unless an
external phase distribution is separately supplied.
"""

from __future__ import annotations

from dataclasses import dataclass

from .scale_tunneling_1d import Wall1D, minimum_positive_clearance_crossing_displacement


@dataclass(frozen=True)
class TunnelingPhaseDiagram1D:
    """Exact phase counts for one wall/body/displacement/spatial-factor tuple."""

    wall_thickness: int
    body_diameter: int
    effective_thickness: int
    displacement: int
    collapse_factor: int
    positive_clearance_crossing_phases: int
    transmitting_phases: int
    macro_contact_phases: int
    transmission_start_clearance_range: tuple[int, int] | None
    minimum_displacement_for_any_transmission: int


def tunneling_phase_diagram(
    wall: Wall1D,
    radius: int,
    displacement: int,
    collapse_factor: int,
) -> TunnelingPhaseDiagram1D:
    """Return exact sampled tunneling phase counts for one integer parameter tuple."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if isinstance(displacement, bool) or not isinstance(displacement, int) or displacement < 0:
        raise ValueError("displacement must be a non-negative integer")
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")

    body_diameter = 2 * radius + 1
    effective = minimum_positive_clearance_crossing_displacement(wall, radius)
    if effective != wall.thickness_cells + body_diameter:
        raise AssertionError("effective wall/body thickness identity failed")

    positive_phases = max(0, displacement - effective + 1)
    transmitting = max(0, displacement - effective - 2 * collapse_factor + 3)
    if transmitting > positive_phases:
        raise AssertionError("transmitting phase count exceeded positive-clearance phases")
    macro_contact = positive_phases - transmitting

    if transmitting:
        clearance_sum = displacement - effective + 2
        transmission_range = (
            collapse_factor,
            clearance_sum - collapse_factor,
        )
        if transmission_range[1] < transmission_range[0]:
            raise AssertionError("nonempty transmitting count produced empty phase range")
        if transmission_range[1] - transmission_range[0] + 1 != transmitting:
            raise AssertionError("transmission range cardinality disagrees with formula")
    else:
        transmission_range = None

    minimum_transmission_displacement = effective + 2 * (collapse_factor - 1)
    return TunnelingPhaseDiagram1D(
        wall_thickness=wall.thickness_cells,
        body_diameter=body_diameter,
        effective_thickness=effective,
        displacement=displacement,
        collapse_factor=collapse_factor,
        positive_clearance_crossing_phases=positive_phases,
        transmitting_phases=transmitting,
        macro_contact_phases=macro_contact,
        transmission_start_clearance_range=transmission_range,
        minimum_displacement_for_any_transmission=minimum_transmission_displacement,
    )


def enumerate_positive_clearance_phases(
    wall: Wall1D,
    radius: int,
    displacement: int,
) -> tuple[tuple[int, int], ...]:
    """Enumerate ``(g_pre,g_post)`` phase pairs for differential validation."""
    effective = minimum_positive_clearance_crossing_displacement(wall, radius)
    clearance_sum = displacement - effective + 2
    if clearance_sum < 2:
        return ()
    return tuple(
        (pre, clearance_sum - pre)
        for pre in range(1, clearance_sum)
    )
