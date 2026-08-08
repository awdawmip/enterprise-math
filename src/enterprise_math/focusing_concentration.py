"""Higher-order focusing concentration observables for Enterprise Math P019.

These observables refine the total focusing excess C using the existing P011
collision spectrum of the outgoing-incidence target map.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable
from math import comb

from .directed_expansion import (
    branching_surplus,
    collision_excess,
    local_collision_spectrum,
    section_expansion,
    successor_multiplicities,
)

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]


def higher_order_concentration(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return H=J2-C=sum_w binom(m_w-1,2).

    H is zero exactly when every reached future target has multiplicity at most
    two.  It detects focusing concentrated beyond pairwise overlap.
    """
    collision = collision_excess(vertices, edges, section)
    pair_load = local_collision_spectrum(vertices, edges, section, 2)
    result = pair_load - collision
    multiplicities = successor_multiplicities(vertices, edges, section)
    direct = sum(comb(multiplicity - 1, 2) for multiplicity in multiplicities.values())
    if result != direct:
        raise AssertionError("higher-order concentration identity failed")
    return result


def quadratic_focusing_concentration(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> int:
    """Return Q=2*J2-C=sum_w (m_w-1)^2."""
    collision = collision_excess(vertices, edges, section)
    pair_load = local_collision_spectrum(vertices, edges, section, 2)
    result = 2 * pair_load - collision
    multiplicities = successor_multiplicities(vertices, edges, section)
    direct = sum((multiplicity - 1) ** 2 for multiplicity in multiplicities.values())
    if result != direct:
        raise AssertionError("quadratic focusing concentration identity failed")
    return result


def focusing_profile(
    vertices: Iterable[Vertex],
    edges: Iterable[DirectedEdge],
    section: Iterable[Vertex],
) -> dict[str, object]:
    """Return coarse and higher-order focusing data for one finite section."""
    section_tuple = tuple(dict.fromkeys(section))
    if not section_tuple:
        raise ValueError("section must be nonempty")
    multiplicities = successor_multiplicities(vertices, edges, section_tuple)
    collision = collision_excess(vertices, edges, section_tuple)
    branching = branching_surplus(vertices, edges, section_tuple)
    expansion = section_expansion(vertices, edges, section_tuple)
    spectrum = tuple(
        local_collision_spectrum(vertices, edges, section_tuple, order)
        for order in range(1, len(section_tuple) + 1)
    )
    return {
        "section_size": len(section_tuple),
        "branching_surplus": branching,
        "collision_excess": collision,
        "expansion": expansion,
        "collision_spectrum": spectrum,
        "maximum_target_multiplicity": max(multiplicities.values(), default=0),
        "higher_order_concentration": higher_order_concentration(
            vertices, edges, section_tuple
        ),
        "quadratic_focusing_concentration": quadratic_focusing_concentration(
            vertices, edges, section_tuple
        ),
    }


def pairwise_regime_reconstruction(
    section_size: int,
    branching_surplus_value: int,
    collision_excess_value: int,
) -> dict[str, int]:
    """Reconstruct target multiplicities when section_size<=2.

    With at most two sources every reached target has multiplicity 1 or 2.
    Therefore C is exactly the number of double-hit targets.  Given N and B,
    the total incidence count is E=N+B and future target count is F=E-C.
    """
    if not isinstance(section_size, int) or not isinstance(branching_surplus_value, int):
        raise TypeError("section size and branching surplus must be integers")
    if not isinstance(collision_excess_value, int):
        raise TypeError("collision excess must be an integer")
    if section_size < 1 or section_size > 2:
        raise ValueError("pairwise reconstruction applies only to one or two sources")
    if collision_excess_value < 0:
        raise ValueError("collision excess must be nonnegative")
    incidences = section_size + branching_surplus_value
    if incidences < 0:
        raise ValueError("incidence count must be nonnegative")
    future_targets = incidences - collision_excess_value
    double_targets = collision_excess_value
    single_targets = future_targets - double_targets
    if single_targets < 0:
        raise ValueError("coarse data are incompatible with multiplicity at most two")
    return {
        "incidences": incidences,
        "future_targets": future_targets,
        "single_targets": single_targets,
        "double_targets": double_targets,
    }
