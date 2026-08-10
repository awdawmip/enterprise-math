"""Intrinsic hierarchy geometry induced only by finite precision refinement.

Nested distinguishability signatures canonically determine a finite ultrametric:
for distinct states at the current finest layer, find the finest earlier scale
at which they still have the same coarse image.  The distance is the exact
integer refinement factor from that common scale to the current scale.

This is established hierarchical/ultrametric mathematics used as an R004
pressure test.  It shows both a positive result (precision hierarchy alone can
induce intrinsic geometry) and a negative boundary (the induced geometry is
hierarchical and need not resemble connected local/Euclidean space).
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Hashable

State = Hashable


def validate_scale_chain(scales: Sequence[int]) -> tuple[int, ...]:
    chain = tuple(scales)
    if not chain:
        raise ValueError("scale chain must be nonempty")
    if any(isinstance(scale, bool) or not isinstance(scale, int) or scale <= 0 for scale in chain):
        raise ValueError("scales must be positive integers")
    if any(right % left for left, right in zip(chain, chain[1:])):
        raise ValueError("scales must form a divisibility chain")
    return chain


def validate_signatures(
    scales: Sequence[int], signatures: Mapping[State, Sequence[Hashable]]
) -> tuple[int, ...]:
    chain = validate_scale_chain(scales)
    if not signatures:
        raise ValueError("signatures must be nonempty")
    width = len(chain)
    normalized = {state: tuple(signature) for state, signature in signatures.items()}
    if any(len(signature) != width for signature in normalized.values()):
        raise ValueError("every signature must contain one coordinate per scale")

    roots = {signature[0] for signature in normalized.values()}
    if len(roots) != 1:
        raise ValueError("R004 hierarchy signatures need one precision-one root class")

    final_coordinates = [signature[-1] for signature in normalized.values()]
    if len(final_coordinates) != len(set(final_coordinates)):
        raise ValueError("final coordinates must distinguish declared current states")

    states = tuple(normalized)
    for index, left in enumerate(states):
        for right in states[index + 1 :]:
            left_signature = normalized[left]
            right_signature = normalized[right]
            for level in range(width - 1):
                if (
                    left_signature[level + 1] == right_signature[level + 1]
                    and left_signature[level] != right_signature[level]
                ):
                    raise ValueError("signature equivalence classes must be nested")
    return chain


def last_common_level(
    signatures: Mapping[State, Sequence[Hashable]], left: State, right: State
) -> int:
    if left not in signatures or right not in signatures:
        raise ValueError("unknown state")
    left_signature = tuple(signatures[left])
    right_signature = tuple(signatures[right])
    common = [
        index
        for index, (a, b) in enumerate(zip(left_signature, right_signature))
        if a == b
    ]
    if not common:
        raise ValueError("states need a common precision-one ancestor")
    return max(common)


def hierarchy_distance(
    scales: Sequence[int],
    signatures: Mapping[State, Sequence[Hashable]],
    left: State,
    right: State,
) -> int:
    """Return the exact divisibility-weighted hierarchy ultrametric distance."""
    chain = validate_signatures(scales, signatures)
    if left not in signatures or right not in signatures:
        raise ValueError("unknown state")
    if left == right:
        return 0
    level = last_common_level(signatures, left, right)
    if level == len(chain) - 1:
        raise ValueError("distinct states cannot share the final coordinate")
    return chain[-1] // chain[level]


def hierarchy_ball(
    scales: Sequence[int],
    signatures: Mapping[State, Sequence[Hashable]],
    center: State,
    radius: int,
) -> frozenset[State]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    validate_signatures(scales, signatures)
    return frozenset(
        state
        for state in signatures
        if hierarchy_distance(scales, signatures, center, state) <= radius
    )


def hierarchy_shell(
    scales: Sequence[int],
    signatures: Mapping[State, Sequence[Hashable]],
    center: State,
    radius: int,
) -> frozenset[State]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    validate_signatures(scales, signatures)
    return frozenset(
        state
        for state in signatures
        if hierarchy_distance(scales, signatures, center, state) == radius
    )


def ultrametric_holds(
    scales: Sequence[int], signatures: Mapping[State, Sequence[Hashable]]
) -> bool:
    validate_signatures(scales, signatures)
    states = tuple(signatures)
    for x in states:
        for y in states:
            for z in states:
                if hierarchy_distance(scales, signatures, x, z) > max(
                    hierarchy_distance(scales, signatures, x, y),
                    hierarchy_distance(scales, signatures, y, z),
                ):
                    return False
    return True


def minimum_distance_adjacency(
    scales: Sequence[int], signatures: Mapping[State, Sequence[Hashable]]
) -> frozenset[frozenset[State]]:
    """Connect distinct states only at the smallest nonzero hierarchy distance."""
    validate_signatures(scales, signatures)
    states = tuple(signatures)
    distances = [
        hierarchy_distance(scales, signatures, left, right)
        for index, left in enumerate(states)
        for right in states[index + 1 :]
    ]
    if not distances:
        return frozenset()
    minimum = min(distances)
    return frozenset(
        frozenset((left, right))
        for index, left in enumerate(states)
        for right in states[index + 1 :]
        if hierarchy_distance(scales, signatures, left, right) == minimum
    )
