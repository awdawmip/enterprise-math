"""Exact local relation diagnostics for finite minimal-vector systems.

The mother object here is not a root system.  It is a full finite set of
minimal nonzero vectors for an integer quadratic form.  Root systems are one
highly symmetric benchmark family.

Fix a primitive direction ``alpha``.  Every common primitive neighbor ``beta``
of the edge ``0--alpha`` has a complementary partner ``alpha-beta``.  These
partners form two-state fibers.  Between two distinct fibers, minimality forces
one of only two possibilities: no primitive adjacency, or exactly one perfect
matching.  Hence every primitive-edge context is a two-fold lift of a simple
base graph.  ADE simply-laced roots are the special case where this base graph
is complete.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

Vector = tuple[int, ...]
GramMatrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class MinimalVectorEdgeContext:
    primitive_norm: int
    common_neighbor_count: int
    complementary_fiber_count: int
    base_edges: tuple[tuple[int, int], ...]
    lift_matching_bits: tuple[tuple[int, int, int], ...]

    @property
    def base_edge_count(self) -> int:
        return len(self.base_edges)

    @property
    def complete_base(self) -> bool:
        n = self.complementary_fiber_count
        return self.base_edge_count == n * (n - 1) // 2


def _validate_gram(gram: GramMatrix, dimension: int) -> None:
    if len(gram) != dimension or any(len(row) != dimension for row in gram):
        raise ValueError("gram must be a square matrix matching vector dimension")
    for i in range(dimension):
        for j in range(dimension):
            if gram[i][j] != gram[j][i]:
                raise ValueError("gram must be symmetric")


def bilinear(left: Vector, right: Vector, gram: GramMatrix) -> int:
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimension")
    _validate_gram(gram, len(left))
    return sum(
        left[i] * gram[i][j] * right[j]
        for i in range(len(left))
        for j in range(len(right))
    )


def quadratic(vector: Vector, gram: GramMatrix) -> int:
    return bilinear(vector, vector, gram)


def subtract(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimension")
    return tuple(a - b for a, b in zip(left, right))


def minimal_vector_norm(vectors: tuple[Vector, ...], gram: GramMatrix) -> int:
    if not vectors:
        raise ValueError("vectors must be nonempty")
    norms = {quadratic(vector, gram) for vector in vectors}
    if len(norms) != 1:
        raise ValueError("all primitive vectors must have one common minimal norm")
    norm = norms.pop()
    if norm <= 0:
        raise ValueError("primitive norm must be positive")
    return norm


def primitive_adjacent(
    left: Vector,
    right: Vector,
    gram: GramMatrix,
    primitive_norm: int,
) -> bool:
    if left == right:
        return False
    return quadratic(subtract(left, right), gram) == primitive_norm


def edge_context_two_cover(
    vectors: tuple[Vector, ...],
    gram: GramMatrix,
    alpha: Vector,
) -> MinimalVectorEdgeContext:
    """Return the canonical two-cover profile around primitive edge ``0--alpha``.

    ``vectors`` must contain the complete primitive/minimal vector set needed by
    the local calculation, in particular every ``alpha-beta`` produced below.
    Matching bit 0 means representative-to-representative adjacency; bit 1
    means representative-to-complement adjacency.  Flipping a representative
    inside one fiber changes incident bits but not cycle parity.
    """
    vector_set = set(vectors)
    if alpha not in vector_set:
        raise ValueError("alpha must belong to the primitive vector set")
    norm = minimal_vector_norm(vectors, gram)
    common = tuple(
        beta
        for beta in vectors
        if primitive_adjacent(alpha, beta, gram, norm)
    )
    common_set = set(common)

    fibers: list[tuple[Vector, Vector]] = []
    seen: set[Vector] = set()
    for beta in common:
        if beta in seen:
            continue
        complement = subtract(alpha, beta)
        if complement not in common_set:
            raise ValueError("primitive set is not closed under edge complementation")
        if complement == beta:
            raise ValueError("edge complementation must be fixed-point free")
        fibers.append((beta, complement))
        seen.add(beta)
        seen.add(complement)

    base_edges: list[tuple[int, int]] = []
    bits: list[tuple[int, int, int]] = []
    for i, j in combinations(range(len(fibers)), 2):
        left, left_star = fibers[i]
        right, right_star = fibers[j]
        parallel = primitive_adjacent(left, right, gram, norm)
        crossed = primitive_adjacent(left, right_star, gram, norm)
        if parallel and crossed:
            raise AssertionError("minimality forbids both matchings simultaneously")
        if not parallel and not crossed:
            continue

        # Complementation symmetry forces the second edge of the same matching.
        if parallel and not primitive_adjacent(left_star, right_star, gram, norm):
            raise AssertionError("parallel matching must be complement-symmetric")
        if crossed and not primitive_adjacent(left_star, right, gram, norm):
            raise AssertionError("crossed matching must be complement-symmetric")
        base_edges.append((i, j))
        bits.append((i, j, 0 if parallel else 1))

    return MinimalVectorEdgeContext(
        primitive_norm=norm,
        common_neighbor_count=len(common),
        complementary_fiber_count=len(fibers),
        base_edges=tuple(base_edges),
        lift_matching_bits=tuple(bits),
    )


def triangle_loop_return_counts(context: MinimalVectorEdgeContext) -> tuple[int, int]:
    """Return ``(preserving, flipping)`` base-triangle lift counts.

    The XOR of the three matching bits around a base triangle is invariant
    under swapping the two labels in any complementary fiber.
    """
    bit = {(i, j): value for i, j, value in context.lift_matching_bits}
    preserving = 0
    flipping = 0
    for i, j, k in combinations(range(context.complementary_fiber_count), 3):
        keys = ((i, j), (i, k), (j, k))
        if any(key not in bit for key in keys):
            continue
        parity = bit[(i, j)] ^ bit[(i, k)] ^ bit[(j, k)]
        if parity:
            flipping += 1
        else:
            preserving += 1
    return preserving, flipping
