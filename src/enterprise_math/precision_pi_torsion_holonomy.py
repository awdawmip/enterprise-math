"""Exact finite certificates for the tetrahedral precision-pi normalization.

This module connects three carrier-level structures:

* the A3 and A5 balanced state lattices;
* the order-two saturation defect of the K4 endpoint-sum map;
* the elementary FCC spherical-face half-turn holonomy.

Only integer and Fraction arithmetic is used.  Classical pi enters only in the
separate local-CLT/spherical-area interpretation, not in these certificates.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import factorial, gcd
from typing import Iterable, Mapping, Sequence

Vertex = str
Edge = tuple[Vertex, Vertex]
Matrix = tuple[tuple[int, ...], ...]
EdgeState = Mapping[Edge, int]

VERTICES: tuple[Vertex, ...] = ("A", "B", "C", "D")
EDGES: tuple[Edge, ...] = (
    ("A", "B"),
    ("A", "C"),
    ("A", "D"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
)
OPPOSITE_MATCHINGS: tuple[tuple[Edge, Edge], ...] = (
    (("A", "B"), ("C", "D")),
    (("A", "C"), ("B", "D")),
    (("A", "D"), ("B", "C")),
)


def canonical_edge(left: Vertex, right: Vertex) -> Edge:
    if left == right or left not in VERTICES or right not in VERTICES:
        raise ValueError("an edge requires two distinct tetrahedral vertices")
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    """Exact Bareiss determinant for a square integer matrix."""

    rows = [list(map(int, row)) for row in matrix]
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("determinant requires a square matrix")
    if size == 0:
        return 1
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if rows[pivot_index][pivot_index] == 0:
            swap = next(
                (index for index in range(pivot_index + 1, size)
                 if rows[index][pivot_index] != 0),
                None,
            )
            if swap is None:
                return 0
            rows[pivot_index], rows[swap] = rows[swap], rows[pivot_index]
            sign *= -1
        pivot = rows[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    rows[row][column] * pivot
                    - rows[row][pivot_index] * rows[pivot_index][column]
                )
                if numerator % previous:
                    raise AssertionError("Bareiss division lost exactness")
                rows[row][column] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            rows[row][pivot_index] = 0
    return sign * rows[-1][-1]


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column] for row in range(len(matrix)))
                 for column in range(len(matrix[0])))


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column]
                for index in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def scalar_matrix_multiply(scalar: int, matrix: Matrix) -> Matrix:
    return tuple(tuple(scalar * entry for entry in row) for row in matrix)


def root_lattice_gram(rank: int) -> Matrix:
    """Gram matrix of A_rank in the basis e_i-e_(rank+1)."""

    if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 0:
        raise ValueError("rank must be a positive integer")
    return tuple(
        tuple(2 if row == column else 1 for column in range(rank))
        for row in range(rank)
    )


def endpoint_sum_matrix() -> Matrix:
    """Matrix of delta:A3->A5 in standard root-lattice bases."""

    return (
        (1, 1, 0),
        (1, 0, 1),
        (0, -1, -1),
        (0, 1, 1),
        (-1, 0, -1),
    )


def maximal_minors(matrix: Matrix) -> tuple[int, ...]:
    row_count = len(matrix)
    column_count = len(matrix[0])
    if row_count < column_count:
        raise ValueError("maximal-row minors require rows >= columns")
    return tuple(
        determinant(tuple(matrix[index] for index in rows))
        for rows in combinations(range(row_count), column_count)
    )


def saturation_index() -> int:
    values = maximal_minors(endpoint_sum_matrix())
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def edge_total(state: EdgeState) -> int:
    return sum(state[edge] for edge in EDGES)


def matching_sums(state: EdgeState) -> tuple[int, int, int]:
    return tuple(state[left] + state[right] for left, right in OPPOSITE_MATCHINGS)  # type: ignore[return-value]


def star_sum(state: EdgeState, vertex: Vertex) -> int:
    if vertex not in VERTICES:
        raise ValueError("unknown tetrahedral vertex")
    return sum(value for edge, value in state.items() if vertex in edge)


def endpoint_sum(vertex_state: Mapping[Vertex, int]) -> dict[Edge, int]:
    if set(vertex_state) != set(VERTICES):
        raise ValueError("vertex state must contain A, B, C, and D exactly")
    return {
        edge: vertex_state[edge[0]] + vertex_state[edge[1]]
        for edge in EDGES
    }


def add_edge_states(left: EdgeState, right: EdgeState, scale_right: int = 1) -> dict[Edge, int]:
    return {edge: left[edge] + scale_right * right[edge] for edge in EDGES}


def scale_edge_state(scalar: int, state: EdgeState) -> dict[Edge, int]:
    return {edge: scalar * state[edge] for edge in EDGES}


def face_contrast(omitted_vertex: Vertex) -> dict[Edge, int]:
    """+1 on the opposite face and -1 on the omitted vertex star."""

    if omitted_vertex not in VERTICES:
        raise ValueError("unknown tetrahedral vertex")
    return {
        edge: -1 if omitted_vertex in edge else 1
        for edge in EDGES
    }


def face_double_lift(omitted_vertex: Vertex) -> dict[Vertex, int]:
    """Balanced vertex potential whose endpoint sum is twice the face contrast."""

    if omitted_vertex not in VERTICES:
        raise ValueError("unknown tetrahedral vertex")
    return {
        vertex: -3 if vertex == omitted_vertex else 1
        for vertex in VERTICES
    }


def face_difference_lift(source: Vertex, target: Vertex) -> dict[Vertex, int]:
    """Potential lifting x_target-x_source."""

    if source == target or source not in VERTICES or target not in VERTICES:
        raise ValueError("source and target must be distinct tetrahedral vertices")
    return {
        vertex: 2 if vertex == source else (-2 if vertex == target else 0)
        for vertex in VERTICES
    }


def torsion_bit_on_zero_matching(state: EdgeState) -> int:
    """The common star parity on the zero-matching residual fiber."""

    if edge_total(state) != 0 or matching_sums(state) != (0, 0, 0):
        raise ValueError("torsion bit is defined here only on the zero-matching fiber")
    parities = {star_sum(state, vertex) % 2 for vertex in VERTICES}
    if len(parities) != 1:
        raise AssertionError("zero matching did not give a common star parity")
    return parities.pop()


def residual_holonomy_sign(state: EdgeState) -> int:
    """Map the residual torsion bit to the central tangent holonomy +/-1."""

    return -1 if torsion_bit_on_zero_matching(state) else 1


def normalization_square() -> Fraction:
    """Square of sqrt(3/8)=covol(A5)/(2*covol(A3))."""

    return Fraction(3, 8)


def normalized_covolume_ratio_square() -> Fraction:
    """Square of sqrt(3/8)*covol(A3)/covol(A5), equal to 1/4."""

    return normalization_square() * Fraction(determinant(root_lattice_gram(3)), determinant(root_lattice_gram(5)))


def balanced_probability(k: int, n: int) -> Fraction:
    if k < 2 or n < 0:
        raise ValueError("require k>=2 and n>=0")
    return Fraction(factorial(k * n), factorial(n) ** k * k ** (k * n))


def beta_integer(p: int, q: int) -> Fraction:
    if p <= 0 or q <= 0:
        raise ValueError("integer beta parameters must be positive")
    return Fraction(factorial(p - 1) * factorial(q - 1), factorial(p + q - 1))


def beta_factorized_ratio(n: int) -> Fraction:
    """Exact two-beta form of P4(n)/(n P6(n))."""

    if n <= 0:
        raise ValueError("n must be positive")
    return (
        2
        * (2 * n + 1)
        * Fraction(729, 4) ** n
        * beta_integer(4 * n + 1, 2 * n)
        * beta_integer(n + 1, n + 1)
    )


def direct_probability_ratio(n: int) -> Fraction:
    if n <= 0:
        raise ValueError("n must be positive")
    return balanced_probability(4, n) / (n * balanced_probability(6, n))


def beta_kernel(x: int | Fraction, y: int | Fraction) -> Fraction:
    x_value = Fraction(x)
    y_value = Fraction(y)
    return (
        Fraction(729, 4)
        * x_value**4
        * (1 - x_value) ** 2
        * y_value
        * (1 - y_value)
    )


def saddle_certificate() -> dict[str, object]:
    x = Fraction(2, 3)
    y = Fraction(1, 2)
    return {
        "point": (x, y),
        "kernel_value": beta_kernel(x, y),
        "negative_log_hessian": ((27, 0), (0, 8)),
        "hessian_determinant": 216,
    }


def exact_certificate(beta_depth: int = 24) -> dict[str, object]:
    gram3 = root_lattice_gram(3)
    gram5 = root_lattice_gram(5)
    matrix = endpoint_sum_matrix()
    image_gram = matrix_multiply(matrix_multiply(transpose(matrix), gram5), matrix)

    if determinant(gram3) != 4 or determinant(gram5) != 6:
        raise AssertionError("root-lattice Gram determinant certificate failed")
    if image_gram != scalar_matrix_multiply(2, gram3):
        raise AssertionError("endpoint-sum metric scaling certificate failed")
    if determinant(image_gram) != 32:
        raise AssertionError("endpoint-sum image Gram determinant failed")
    if saturation_index() != 2:
        raise AssertionError("endpoint-sum saturation index is not two")
    if normalized_covolume_ratio_square() != Fraction(1, 4):
        raise AssertionError("torsion-normalized covolume coefficient is not one half")

    for omitted in VERTICES:
        contrast = face_contrast(omitted)
        if edge_total(contrast) != 0 or matching_sums(contrast) != (0, 0, 0):
            raise AssertionError("face contrast does not lie in the torsion fiber")
        if torsion_bit_on_zero_matching(contrast) != 1:
            raise AssertionError("face contrast is not the nontrivial torsion class")
        if residual_holonomy_sign(contrast) != -1:
            raise AssertionError("face contrast does not map to half-turn holonomy")
        lift = face_double_lift(omitted)
        if sum(lift.values()) != 0:
            raise AssertionError("face double lift is not balanced")
        if endpoint_sum(lift) != scale_edge_state(2, contrast):
            raise AssertionError("face double lift certificate failed")

    for source, target in combinations(VERTICES, 2):
        difference = add_edge_states(face_contrast(target), face_contrast(source), -1)
        lift = face_difference_lift(source, target)
        if sum(lift.values()) != 0 or endpoint_sum(lift) != difference:
            raise AssertionError("face contrasts do not define one quotient class")

    for n in range(1, beta_depth + 1):
        if direct_probability_ratio(n) != beta_factorized_ratio(n):
            raise AssertionError(f"two-beta identity failed at n={n}")

    saddle = saddle_certificate()
    if saddle["kernel_value"] != 1 or saddle["hessian_determinant"] != 216:
        raise AssertionError("two-beta saddle certificate failed")

    return {
        "det_A3_gram": 4,
        "det_A5_gram": 6,
        "det_endpoint_image_gram": 32,
        "endpoint_metric_scale_squared": 2,
        "saturation_index": 2,
        "residual_torsion_order": 2,
        "normalization_square": normalization_square(),
        "normalized_covolume_ratio_square": normalized_covolume_ratio_square(),
        "face_contrasts_checked": len(VERTICES),
        "beta_identity_depth": beta_depth,
        "saddle": saddle,
        "status": "PASS",
    }
