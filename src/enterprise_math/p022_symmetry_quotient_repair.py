"""Symmetry-quotient path lifting behind the Barlow repair theorem.

For any transition graph with an equitable partition, the number of microscopic
continuations from one quotient block to another is independent of the chosen
representative.  A fixed quotient path therefore has a lift count equal to the
product of its edge multiplicities.

Group-orbit partitions of a graph by automorphisms are automatically equitable.
The two-sided Barlow coordination quotient is the orbit space of the signed-
permutation group acting on the signed drift lattice; its edge multiplicities
are 1, 2, or 4 and reproduce the exact 2^(E+B) repair fiber.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Mapping, Sequence
from math import prod

Vertex = Hashable
Block = Hashable
QuotientEdge = tuple[Block, Block]


def equitable_transition_multiplicities(
    adjacency: Mapping[Vertex, Sequence[Vertex]],
    block_of: Mapping[Vertex, Block],
) -> dict[QuotientEdge, int]:
    """Return block-to-block continuation counts for an equitable partition.

    Raises ``ValueError`` if two vertices in the same source block have
    different numbers of outgoing neighbors in any target block.
    """
    vertices = tuple(adjacency)
    if set(vertices) != set(block_of):
        raise ValueError("block_of must label exactly the adjacency vertices")
    blocks = tuple(dict.fromkeys(block_of[vertex] for vertex in vertices))
    representatives: dict[Block, dict[Block, int]] = {}

    for vertex in vertices:
        source = block_of[vertex]
        counts = Counter(block_of[neighbor] for neighbor in adjacency[vertex])
        row = {target: counts.get(target, 0) for target in blocks}
        if source in representatives and representatives[source] != row:
            raise ValueError("partition is not equitable for the transition graph")
        representatives[source] = row

    return {
        (source, target): count
        for source, row in representatives.items()
        for target, count in row.items()
        if count
    }


def quotient_path_lift_count(
    quotient_path: tuple[Block, ...],
    edge_multiplicities: Mapping[QuotientEdge, int],
) -> int:
    """Microscopic lifts of a quotient path from one fixed microscopic start.

    For ``A_0,...,A_n`` each lift prefix ending in block ``A_i`` has exactly
    ``m(A_i,A_(i+1))`` continuations into the next block, so induction gives the
    product of edge multiplicities.
    """
    if not isinstance(quotient_path, tuple) or not quotient_path:
        raise ValueError("quotient_path must be a nonempty tuple")
    factors = []
    for left, right in zip(quotient_path, quotient_path[1:], strict=True):
        factor = edge_multiplicities.get((left, right), 0)
        if factor <= 0:
            return 0
        factors.append(factor)
    return prod(factors) if factors else 1


def barlow_orbit_edge_multiplicity(
    previous: tuple[int, int], current: tuple[int, int]
) -> int:
    """Signed-drift lift multiplicity of one unordered absolute Barlow step.

    States are sorted pairs ``0<=a<=b``.  One factor two is created for every
    zero coordinate in the previous state (choice of sign when leaving zero),
    plus one factor two when an equal pair splits into unequal successors
    (choice of which labelled side takes the larger absolute value).
    """
    if (
        len(previous) != 2
        or len(current) != 2
        or previous[0] < 0
        or previous[0] > previous[1]
        or current[0] < 0
        or current[0] > current[1]
    ):
        raise ValueError("Barlow quotient states must satisfy 0<=a<=b")

    a, b = previous
    c, d = current
    candidates = {
        tuple(sorted((abs(a + sa), abs(b + sb))))
        for sa in (-1, 1)
        for sb in (-1, 1)
    }
    if current not in candidates:
        raise ValueError("current is not a legal quotient successor")

    zero_bits = int(a == 0) + int(b == 0)
    split_bit = int(a == b and c != d)
    predicted = 2 ** (zero_bits + split_bit)

    # Independent microscopic step count from one canonical signed
    # representative (a,b).  Signed permutations of the representative give
    # the same count by symmetry.
    direct = sum(
        1
        for sa in (-1, 1)
        for sb in (-1, 1)
        if tuple(sorted((abs(a + sa), abs(b + sb)))) == current
    )
    if direct != predicted:
        raise AssertionError("boundary-event formula must equal orbit edge multiplicity")
    return direct


def barlow_quotient_path_lift_count(
    pair_history: tuple[tuple[int, int], ...],
) -> int:
    """Exact microscopic word-pair fiber of one Barlow coordination history."""
    path = ((0, 0),) + pair_history
    return prod(
        barlow_orbit_edge_multiplicity(left, right)
        for left, right in zip(path, path[1:], strict=True)
    )


def non_equitable_counterexample() -> tuple[
    dict[str, tuple[str, ...]], dict[str, str]
]:
    """Minimal partition where quotient edge multiplicity depends on representative."""
    adjacency = {
        "a1": ("b1", "b2"),
        "a2": ("b1",),
        "b1": (),
        "b2": (),
    }
    block_of = {"a1": "A", "a2": "A", "b1": "B", "b2": "B"}
    return adjacency, block_of
