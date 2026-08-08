"""Integer focusing calculus for Enterprise Math P019.

This module builds only on finite cross-section cardinalities and the exact
branching-minus-collision decomposition from ``directed_expansion``.  It does
not implement the continuum Raychaudhuri equation.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable

from .directed_expansion import (
    branching_collision_decomposition,
    expansion_trajectory,
)

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]


def _positive(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _nonnegative(name: str, value: int) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")
    return value


def focusing_margin(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return C(A)-B(A), the negative of section expansion."""
    data = branching_collision_decomposition(vertices, edges, section)
    return data["collision_excess"] - data["branching_surplus"]


def strict_focusing_step(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
    minimum_margin: int = 1,
) -> bool:
    """Return whether collision exceeds branching by at least ``minimum_margin``."""
    _positive("minimum_margin", minimum_margin)
    return focusing_margin(vertices, edges, section) >= minimum_margin


def finite_focusing_step_bound(initial_size: int, minimum_margin: int = 1) -> int:
    """Return ceil(initial_size/minimum_margin) using integer arithmetic."""
    _positive("initial_size", initial_size)
    _positive("minimum_margin", minimum_margin)
    return (initial_size + minimum_margin - 1) // minimum_margin


def verify_strict_focusing_trajectory(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    initial_section: Iterable[Vertex],
    steps: int,
    minimum_margin: int = 1,
) -> dict[str, object]:
    """Verify the finite focusing bound along a generated future trajectory.

    The theorem is conditional: every nonempty transition inspected before
    extinction must satisfy ``C-B >= minimum_margin``.  When it does, section
    size drops by at least that integer margin at each step.
    """
    _nonnegative("steps", steps)
    _positive("minimum_margin", minimum_margin)
    sections, expansions = expansion_trajectory(vertices, edges, initial_section, steps)
    margins = tuple(-expansion for expansion in expansions)
    condition_holds = all(
        margin >= minimum_margin
        for index, margin in enumerate(margins)
        if sections[index]
    )
    bound = finite_focusing_step_bound(len(sections[0]), minimum_margin)
    extinct_index = next(
        (index for index, section in enumerate(sections) if not section),
        None,
    )
    if condition_holds and len(expansions) >= bound and extinct_index is None:
        raise AssertionError("strict focusing condition should force finite extinction")
    return {
        "sections": sections,
        "expansions": expansions,
        "margins": margins,
        "condition_holds": condition_holds,
        "bound": bound,
        "extinct_index": extinct_index,
    }


def relative_expansion_change_numerator(
    current_size: int,
    current_expansion: int,
    next_size: int,
    next_expansion: int,
) -> int:
    """Cross-multiplied sign of Xi_next/N_next - Xi_current/N_current.

    The sign of this integer equals the sign of the change in normalized
    expansion without storing either rational value.
    """
    _positive("current_size", current_size)
    _positive("next_size", next_size)
    if not isinstance(current_expansion, int) or not isinstance(next_expansion, int):
        raise TypeError("expansions must be integers")
    return current_size * next_expansion - next_size * current_expansion


def branching_collision_rate_numerators(
    current_size: int,
    next_size: int,
    current_branching: int,
    next_branching: int,
    current_collision: int,
    next_collision: int,
) -> dict[str, int]:
    """Decompose the normalized-expansion change numerator into B and C parts."""
    _positive("current_size", current_size)
    _positive("next_size", next_size)
    values = (
        current_branching,
        next_branching,
        current_collision,
        next_collision,
    )
    if any(not isinstance(value, int) for value in values):
        raise TypeError("branching and collision values must be integers")
    branch_numerator = current_size * next_branching - next_size * current_branching
    collision_numerator = current_size * next_collision - next_size * current_collision
    total = branch_numerator - collision_numerator
    return {
        "branch_numerator": branch_numerator,
        "collision_numerator": collision_numerator,
        "expansion_change_numerator": total,
    }


def no_sink_branch_clock_budget(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return branching surplus when every section vertex has a future continuation.

    This is only a candidate intrinsic causal-clock budget.  It is not identified
    with physical proper time or with the earlier Schwarzschild clock state.
    """
    vertex_tuple = tuple(vertices)
    vertex_set = set(vertex_tuple)
    section_set = frozenset(section)
    if not section_set:
        raise ValueError("cross-section must be nonempty")
    if not section_set.issubset(vertex_set):
        raise ValueError("cross-section contains a vertex outside the graph")
    edge_tuple = tuple(dict.fromkeys(edges))
    outdegree = Counter(source for source, target in edge_tuple if source in section_set)
    if any(outdegree[vertex] == 0 for vertex in section_set):
        raise ValueError("branch-clock budget requires at least one successor per state")
    return sum(outdegree[vertex] - 1 for vertex in section_set)


def branch_clock_focusing_identity(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> dict[str, int]:
    """Return Xi = K_branch - C when the no-sink branch budget is defined."""
    clock_budget = no_sink_branch_clock_budget(vertices, edges, section)
    data = branching_collision_decomposition(vertices, edges, section)
    if clock_budget != data["branching_surplus"]:
        raise AssertionError("branch-clock budget must equal branching surplus")
    if data["expansion"] != clock_budget - data["collision_excess"]:
        raise AssertionError("branch-clock focusing identity failed")
    return {
        "expansion": data["expansion"],
        "branch_clock_budget": clock_budget,
        "collision_excess": data["collision_excess"],
    }
