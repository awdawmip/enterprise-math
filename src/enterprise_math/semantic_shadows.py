"""Compositional shadows from non-negative count semantics to existence semantics.

Positive support maps natural-number matrix/count algebra to Boolean relation
algebra.  At the graded path-cost layer, positive coefficient support followed
by Pareto pruning yields the existence-only antichain state.

These helpers deliberately reject signed count matrices because cancellation
breaks the positive-support homomorphism used by the bridge theorem.
"""

from __future__ import annotations

from .equitable_count_quotient import IntMatrix, matrix_product
from .multistage_support_frontier import (
    MultiFrontier,
    MultiFrontierMatrix,
    convolve_frontier_matrices,
    pareto_minimal_vectors,
)
from .multistage_witness_counts import (
    CountHistogram,
    CountHistogramMatrix,
    convolve_count_matrices,
)

Relation = frozenset[tuple[int, int]]


def positive_support_relation(matrix: IntMatrix) -> Relation:
    """Entrywise positive support of a non-negative integer square matrix."""
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be non-negative integers")
    return frozenset(
        (source, target)
        for source in range(size)
        for target in range(size)
        if matrix[source][target] > 0
    )


def compose_relations(left: Relation, right: Relation) -> Relation:
    """Boolean relational composition."""
    right_by_source: dict[int, set[int]] = {}
    for source, target in right:
        right_by_source.setdefault(source, set()).add(target)
    return frozenset(
        (source, target)
        for source, middle in left
        for target in right_by_source.get(middle, ())
    )


def support_product_commutes(left: IntMatrix, right: IntMatrix) -> bool:
    """Audit supp(AB)=supp(A)∘supp(B) over non-negative integers."""
    return positive_support_relation(matrix_product(left, right)) == compose_relations(
        positive_support_relation(left), positive_support_relation(right)
    )


def count_histogram_positive_support(histogram: CountHistogram) -> tuple[tuple[int, ...], ...]:
    """Return exact positive cost support, forgetting coefficient magnitudes."""
    if not histogram or any(count <= 0 for _cost, count in histogram):
        raise ValueError("histogram must have positive coefficients")
    return tuple(sorted(cost for cost, _count in histogram))


def count_histogram_frontier(histogram: CountHistogram) -> MultiFrontier:
    """Pareto-minimal existence shadow of a count-complete cost histogram."""
    return pareto_minimal_vectors(count_histogram_positive_support(histogram))


def count_matrix_frontier_shadow(matrix: CountHistogramMatrix) -> MultiFrontierMatrix:
    """Project each count histogram entry to its Pareto existence frontier."""
    return tuple(
        tuple(count_histogram_frontier(histogram) for histogram in row)
        for row in matrix
    )


def coefficient_to_antichain_composition_commutes(
    left: CountHistogramMatrix, right: CountHistogramMatrix
) -> bool:
    """Audit Pareto(supp(H*K))=Pareto(supp(H))*Pareto(supp(K))."""
    composed_counts = convolve_count_matrices(left, right)
    projected_after = count_matrix_frontier_shadow(composed_counts)
    projected_before = convolve_frontier_matrices(
        count_matrix_frontier_shadow(left),
        count_matrix_frontier_shadow(right),
    )
    return projected_after == projected_before
