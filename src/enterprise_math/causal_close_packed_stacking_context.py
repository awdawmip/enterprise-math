"""Close-packed stacking as a two-bit local causal continuation law.

A close-packed layer registry lives in Z/3Z.  Each transition z->z+1 changes the
registry by a sign delta_z in {+1,-1}; equal adjacent registries are forbidden.
The local contact environment of a center in layer z depends only on the two
adjacent continuation signs delta_(z-1), delta_z.

Exact integer contact-graph enumeration gives:

    delta_(z-1) == delta_z : 12 bonds of the FCC-like 421 graph context;
    delta_(z-1) != delta_z : 6 bonds 421 and 6 in-layer bonds 422.

Thus FCC/HCP are periodic trajectories of one support law rather than primitive
lattice labels in this representation.  Arbitrary sign words encode stacking
fault/polytype candidates.  This is a combinatorial structural model, not a
claim about thermodynamic stability.
"""

from __future__ import annotations

from collections import Counter
from typing import Mapping

from .causal_close_packed_contact import (
    BondSignature,
    bond_common_neighbor_signature,
    close_packed_point,
    local_close_packed_points,
    point_neighbors,
)


FCC_CONTEXT: BondSignature = (4, 2, (2, 2), (1, 1, 1, 1))
HCP_IN_PLANE_CONTEXT: BondSignature = (4, 2, (3, 1), (0, 1, 1, 2))


def _require_sign(value: int) -> int:
    if value not in (-1, 1):
        raise ValueError("stacking continuation signs must be +/-1")
    return value


def registry_sequence_from_signs(
    transition_signs: Mapping[int, int],
    minimum_layer: int,
    maximum_layer: int,
    origin_registry: int = 0,
) -> dict[int, int]:
    """Recover exact Z/3Z layer registries from transition signs.

    `transition_signs[z]` is the signed registry step from layer z to z+1.
    The requested range must contain layer zero.
    """
    if minimum_layer > 0 or maximum_layer < 0 or minimum_layer > maximum_layer:
        raise ValueError("layer range must contain zero")
    if origin_registry not in (0, 1, 2):
        raise ValueError("origin registry must lie in Z/3Z")
    for layer in range(minimum_layer, maximum_layer):
        if layer not in transition_signs:
            raise ValueError("a transition sign is required across every requested layer gap")
        _require_sign(transition_signs[layer])

    registries = {0: origin_registry}
    for layer in range(0, maximum_layer):
        registries[layer + 1] = (registries[layer] + transition_signs[layer]) % 3
    for layer in range(-1, minimum_layer - 1, -1):
        registries[layer] = (registries[layer + 1] - transition_signs[layer]) % 3
    return registries


def stacking_registry_function(
    transition_signs: Mapping[int, int],
    minimum_layer: int,
    maximum_layer: int,
):
    registries = registry_sequence_from_signs(
        transition_signs, minimum_layer, maximum_layer
    )
    return lambda layer: registries[layer]


def local_hcp_indicator(previous_sign: int, next_sign: int) -> int:
    _require_sign(previous_sign)
    _require_sign(next_sign)
    return int(previous_sign != next_sign)


def predicted_local_bond_context_histogram(
    previous_sign: int,
    next_sign: int,
) -> dict[BondSignature, int]:
    if local_hcp_indicator(previous_sign, next_sign) == 0:
        return {FCC_CONTEXT: 12}
    return {FCC_CONTEXT: 6, HCP_IN_PLANE_CONTEXT: 6}


def exact_local_bond_context_histogram(
    transition_signs: Mapping[int, int],
    center_layer: int = 0,
) -> dict[BondSignature, int]:
    """Enumerate the exact integer contact graph around one layer center."""
    needed_min = center_layer - 3
    needed_max = center_layer + 3
    registry = stacking_registry_function(
        transition_signs, needed_min, needed_max
    )
    points = local_close_packed_points(registry, 4, 3)
    center = close_packed_point(0, 0, center_layer, registry)
    neighbors = point_neighbors(center, points)
    if len(neighbors) != 12:
        raise AssertionError("a valid close-packed center must have twelve contacts")
    return dict(
        Counter(
            bond_common_neighbor_signature(center, neighbor, points)
            for neighbor in neighbors
        )
    )


def local_context_is_determined_by_two_signs(
    transition_signs: Mapping[int, int],
    center_layer: int = 0,
) -> bool:
    previous = transition_signs[center_layer - 1]
    following = transition_signs[center_layer]
    return exact_local_bond_context_histogram(
        transition_signs, center_layer
    ) == predicted_local_bond_context_histogram(previous, following)


def all_fcc_signs(start: int, stop: int, sign: int = 1) -> dict[int, int]:
    _require_sign(sign)
    return {layer: sign for layer in range(start, stop)}


def alternating_hcp_signs(start: int, stop: int, first_sign: int = 1) -> dict[int, int]:
    _require_sign(first_sign)
    return {
        layer: first_sign if (layer - start) % 2 == 0 else -first_sign
        for layer in range(start, stop)
    }
