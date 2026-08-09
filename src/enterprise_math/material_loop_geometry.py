"""Exact integer lattice geometry of realized E001 material histories.

A finite material history gives integer vertices

    (deformation_index, response_sample).

For a closed path, the shoelace sum is an exact signed *twice area* in this
state lattice:

    A2 = sum_i (x_i*y_(i+1) - x_(i+1)*y_i).

No division, continuum integral, interpolation, or unvisited branch-table point
is required.  The quantity is a combinatorial state-loop area only; it does not
carry physical work/energy units unless a later explicit calibration law says
so.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_hysteresis import MaterialHistoryState


@dataclass(frozen=True)
class MaterialLoopGeometry:
    """Integer lattice geometry of one represented material-state history."""

    vertices: tuple[tuple[int, int], ...]
    closed: bool
    signed_twice_area: int | None
    absolute_twice_area: int | None
    boundary_lattice_steps: int | None


def _vertices(
    states: tuple[MaterialHistoryState, ...] | list[MaterialHistoryState],
) -> tuple[tuple[int, int], ...]:
    history = tuple(states)
    if not history:
        raise ValueError("material history must be nonempty")
    return tuple(
        (state.deformation_index, state.response_sample) for state in history
    )


def signed_twice_lattice_area(vertices: tuple[tuple[int, int], ...]) -> int:
    """Return exact shoelace signed twice-area of a closed vertex cycle."""
    if not vertices:
        raise ValueError("vertices must be nonempty")
    if vertices[0] != vertices[-1]:
        raise ValueError("lattice area requires a closed path")
    return sum(
        x0 * y1 - x1 * y0
        for (x0, y0), (x1, y1) in zip(vertices, vertices[1:])
    )


def boundary_lattice_steps(vertices: tuple[tuple[int, int], ...]) -> int:
    """Sum gcd(|dx|,|dy|) over closed polygonal edges.

    This counts primitive lattice segments along the represented closed path.
    It does not assume the path is simple, so no Pick-theorem interior claim is
    made here.
    """
    if not vertices:
        raise ValueError("vertices must be nonempty")
    if vertices[0] != vertices[-1]:
        raise ValueError("boundary count requires a closed path")
    return sum(
        gcd(abs(x1 - x0), abs(y1 - y0))
        for (x0, y0), (x1, y1) in zip(vertices, vertices[1:])
    )


def material_loop_geometry(
    states: tuple[MaterialHistoryState, ...] | list[MaterialHistoryState],
) -> MaterialLoopGeometry:
    """Return path vertices and exact closed-loop lattice diagnostics when available."""
    vertices = _vertices(states)
    closed = vertices[0] == vertices[-1]
    if not closed:
        return MaterialLoopGeometry(
            vertices=vertices,
            closed=False,
            signed_twice_area=None,
            absolute_twice_area=None,
            boundary_lattice_steps=None,
        )
    signed = signed_twice_lattice_area(vertices)
    return MaterialLoopGeometry(
        vertices=vertices,
        closed=True,
        signed_twice_area=signed,
        absolute_twice_area=abs(signed),
        boundary_lattice_steps=boundary_lattice_steps(vertices),
    )
