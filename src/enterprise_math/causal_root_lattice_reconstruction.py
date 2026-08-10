"""Global simply-laced translation structure from a local primitive causal graph.

For a primitive graph in the A/D/E regime, `causal_graph_gram_rank` reconstructs
an integer pair-grade matrix C using only graph relations.  Give every primitive
direction one formal integer generator, F=Z^R, and collapse the formal
combinations invisible to all pair probes:

    K = {x in Z^R : C x = 0}.

The causal translation module is F/K.  K is saturated because it is the kernel of
a homomorphism from a free abelian group to the torsion-free group Z^R; hence F/K
is torsion-free.  By the first isomorphism theorem it is isomorphic to im(C), so
its free rank is rank_Q(C).

For the simply-laced root graphs checked here, antipodes and primitive difference
relations are also recovered internally from C-columns.  Thus local primitive
relation data generates the same global root-lattice addition law without using
an ambient Euclidean coordinate space as ontology.

This theorem is deliberately restricted to graphs passing the simply-laced Gram
reconstruction contract.  Arbitrary laminated/Kappa shells require deeper causal
pair refinement before a traditional pair grade can be attached.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_graph_gram_rank import (
    causal_simply_laced_gram,
    graph_antipodes,
    rational_matrix_rank,
)
from .causal_primitive_link_profile import Adjacency, Vector


@dataclass(frozen=True)
class CausalTranslationModuleSummary:
    primitive_generator_count: int
    invisible_relation_rank: int
    translation_rank: int
    antipode_relations_verified: bool
    primitive_difference_relations_verified: bool


def _column(matrix: tuple[tuple[int, ...], ...], index: int) -> tuple[int, ...]:
    return tuple(row[index] for row in matrix)


def _subtract(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(left, right))


def _add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def causal_translation_rank(adjacency: Adjacency) -> int:
    return rational_matrix_rank(causal_simply_laced_gram(adjacency))


def invisible_relation_rank(adjacency: Adjacency) -> int:
    return len(adjacency) - causal_translation_rank(adjacency)


def antipode_column_relations_hold(adjacency: Adjacency) -> bool:
    vertices = tuple(adjacency)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    antipode = graph_antipodes(adjacency)
    matrix = causal_simply_laced_gram(adjacency)
    zero = (0,) * len(vertices)
    return all(
        _add(_column(matrix, index[vertex]), _column(matrix, index[antipode[vertex]])) == zero
        for vertex in vertices
    )


def primitive_difference_target(
    adjacency: Adjacency,
    left: Vector,
    right: Vector,
) -> Vector:
    """Unique primitive generator representing [right]-[left] for adjacent pair."""
    if left not in adjacency or right not in adjacency[left]:
        raise ValueError("left and right must be primitive-adjacent directions")
    vertices = tuple(adjacency)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    matrix = causal_simply_laced_gram(adjacency)
    target_column = _subtract(
        _column(matrix, index[right]),
        _column(matrix, index[left]),
    )
    matches = tuple(
        vertex
        for vertex in vertices
        if _column(matrix, index[vertex]) == target_column
    )
    if len(matches) != 1:
        raise ValueError("adjacent direction difference does not have one primitive target")
    return matches[0]


def primitive_difference_relations_hold(adjacency: Adjacency) -> bool:
    for left in adjacency:
        for right in adjacency[left]:
            try:
                primitive_difference_target(adjacency, left, right)
            except ValueError:
                return False
    return True


def causal_translation_module_summary(adjacency: Adjacency) -> CausalTranslationModuleSummary:
    rank = causal_translation_rank(adjacency)
    return CausalTranslationModuleSummary(
        primitive_generator_count=len(adjacency),
        invisible_relation_rank=len(adjacency) - rank,
        translation_rank=rank,
        antipode_relations_verified=antipode_column_relations_hold(adjacency),
        primitive_difference_relations_verified=primitive_difference_relations_hold(adjacency),
    )
