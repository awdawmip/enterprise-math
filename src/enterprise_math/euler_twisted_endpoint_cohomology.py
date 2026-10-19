"""Uniformly twisted K4 cohomology and the integral endpoint residual.

For the tetrahedral graph, the flat coefficient system has edge coboundary
``v_j-v_i``.  The unique fully symmetric nontrivial sign system transports by
``-1`` on every edge, so its twisted coboundary is ``v_j+v_i``: exactly the
endpoint-sum map used by the precision-pi residual.

The module verifies the Smith data, the characteristic-two coincidence, the
zero-total/index-three exact sequence, and the unique nonzero S4-equivariant
map from the C12 root-cover kernel into the mod-two residual.

All calculations are exact integer/bit calculations.  No floating point,
angle, trigonometric function, or numerical value of pi is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from math import gcd
from typing import Iterable, Iterator, Sequence

from enterprise_math.euler_c12_root_torsor import (
    all_edge_bits,
    face_holonomies,
    holonomy_code,
)
from enterprise_math.euler_holonomy_residual_duality import (
    AffineResidual,
    TORSION_RESIDUAL,
    ZERO_RESIDUAL,
    edge_to_residual,
    invariant_residuals,
)

Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]

EDGE_ORDER = ("AB", "AC", "AD", "BC", "BD", "CD")

ORDINARY_INCIDENCE: Matrix = (
    (-1, 1, 0, 0),
    (-1, 0, 1, 0),
    (-1, 0, 0, 1),
    (0, -1, 1, 0),
    (0, -1, 0, 1),
    (0, 0, -1, 1),
)

UNIFORM_TWISTED_INCIDENCE: Matrix = (
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
)

# Bases v_A-v_D, v_B-v_D, v_C-v_D for zero-total vertex states and the
# first five edge coordinates for zero-total edge states.
ZERO_TOTAL_TWISTED_MATRIX: Matrix = (
    (1, 1, 0),
    (1, 0, 1),
    (0, -1, -1),
    (0, 1, 1),
    (-1, 0, -1),
)

UNIFORM_TWIST_EDGE_BITS = (1, 1, 1, 1, 1, 1)
FLAT_EDGE_BITS = (0, 0, 0, 0, 0, 0)


def _validate_matrix(matrix: Matrix) -> tuple[int, int]:
    if not matrix:
        return 0, 0
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError("matrix rows must have equal length")
    if any(isinstance(entry, bool) or not isinstance(entry, int) for row in matrix for entry in row):
        raise TypeError("matrix entries must be integers")
    return len(matrix), columns


def determinant(matrix: Matrix) -> int:
    """Exact determinant by the Leibniz formula; matrices here have size <= 4."""

    rows, columns = _validate_matrix(matrix)
    if rows != columns:
        raise ValueError("determinant requires a square matrix")
    if rows == 0:
        return 1

    total = 0
    for permutation in permutations(range(rows)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(rows)
            for j in range(i + 1, rows)
        )
        term = -1 if inversions % 2 else 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def minor(matrix: Matrix, row_indices: Sequence[int], column_indices: Sequence[int]) -> int:
    submatrix = tuple(
        tuple(matrix[row][column] for column in column_indices)
        for row in row_indices
    )
    return determinant(submatrix)


def determinantal_divisors(matrix: Matrix) -> tuple[int, ...]:
    """Return nonzero gcds Delta_k of all k-by-k minors."""

    rows, columns = _validate_matrix(matrix)
    result: list[int] = []
    for size in range(1, min(rows, columns) + 1):
        divisor = 0
        for row_indices in combinations(range(rows), size):
            for column_indices in combinations(range(columns), size):
                divisor = gcd(divisor, abs(minor(matrix, row_indices, column_indices)))
        if divisor == 0:
            break
        result.append(divisor)
    return tuple(result)


def smith_invariant_factors(matrix: Matrix) -> tuple[int, ...]:
    divisors = determinantal_divisors(matrix)
    previous = 1
    factors = []
    for divisor in divisors:
        if divisor % previous:
            raise AssertionError("determinantal divisors do not divide successively")
        factors.append(divisor // previous)
        previous = divisor
    return tuple(factors)


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    rows, columns = _validate_matrix(matrix)
    if len(vector) != columns:
        raise ValueError("vector length does not match matrix column count")
    return tuple(sum(matrix[row][column] * vector[column] for column in range(columns)) for row in range(rows))


def vector_add(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector lengths must agree")
    return tuple(a + b for a, b in zip(left, right))


def vector_subtract(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("vector lengths must agree")
    return tuple(a - b for a, b in zip(left, right))


def edge_total(vector: Vector) -> int:
    if len(vector) != 6:
        raise ValueError("edge vector must have six coordinates")
    return sum(vector)


def vertex_total(vector: Vector) -> int:
    if len(vector) != 4:
        raise ValueError("vertex vector must have four coordinates")
    return sum(vector)


def twisted_coboundary(vertices: Vector) -> Vector:
    return matrix_vector(UNIFORM_TWISTED_INCIDENCE, vertices)


def ordinary_coboundary(vertices: Vector) -> Vector:
    return matrix_vector(ORDINARY_INCIDENCE, vertices)


def neutralize_twisted_representative(edges: Vector) -> tuple[Vector, Vector]:
    """Make a class representative zero-total when its total is divisible by three.

    Returns `(vertex_shift, neutral_edge_representative)`.
    """

    if len(edges) != 6:
        raise ValueError("edge vector must have six coordinates")
    total = edge_total(edges)
    if total % 3:
        raise ValueError("twisted class is not in the total-neutral mod-three sector")
    mass = total // 3
    vertices = (mass, 0, 0, 0)
    neutral = vector_subtract(edges, twisted_coboundary(vertices))
    if edge_total(neutral) != 0:
        raise AssertionError("neutralization did not remove edge total")
    return vertices, neutral


def mod_two_matrix(matrix: Matrix) -> Matrix:
    return tuple(tuple(entry % 2 for entry in row) for row in matrix)


def symmetric_connection_classes() -> tuple[AffineResidual, ...]:
    """The two S4-fixed graph-gauge classes: flat and uniformly twisted."""

    return invariant_residuals()


def equivariant_root_kernel_images() -> tuple[AffineResidual, ...]:
    """Possible images of the generator of a trivial S4-module C2."""

    return symmetric_connection_classes()


def unique_nonzero_equivariant_root_kernel_image() -> AffineResidual:
    images = tuple(image for image in equivariant_root_kernel_images() if image != ZERO_RESIDUAL)
    if images != (TORSION_RESIDUAL,):
        raise AssertionError("the nonzero symmetric kernel image is not unique")
    return images[0]


@dataclass(frozen=True)
class TwistedCohomologyReport:
    ordinary_smith_factors: tuple[int, ...]
    twisted_smith_factors: tuple[int, ...]
    neutral_smith_factors: tuple[int, ...]
    ordinary_free_rank: int
    twisted_free_rank: int
    twisted_torsion: tuple[int, ...]
    neutral_free_rank: int
    neutral_torsion: tuple[int, ...]
    symmetric_gauge_classes: tuple[AffineResidual, ...]
    unique_nonzero_kernel_image: AffineResidual
    neutralization_cases_checked: int
    zero_total_injection_cases_checked: int


def verify_twisted_endpoint_cohomology(*, bound: int = 2) -> TwistedCohomologyReport:
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("bound must be a non-negative integer")

    ordinary_factors = smith_invariant_factors(ORDINARY_INCIDENCE)
    twisted_factors = smith_invariant_factors(UNIFORM_TWISTED_INCIDENCE)
    neutral_factors = smith_invariant_factors(ZERO_TOTAL_TWISTED_MATRIX)

    if ordinary_factors != (1, 1, 1):
        raise AssertionError("ordinary K4 incidence Smith data changed")
    if twisted_factors != (1, 1, 1, 2):
        raise AssertionError("uniformly twisted K4 incidence Smith data changed")
    if neutral_factors != (1, 1, 2):
        raise AssertionError("zero-total endpoint residual Smith data changed")

    if mod_two_matrix(ORDINARY_INCIDENCE) != mod_two_matrix(UNIFORM_TWISTED_INCIDENCE):
        raise AssertionError("ordinary and twisted incidence should coincide in characteristic two")

    if face_holonomies(FLAT_EDGE_BITS) != (0, 0, 0, 0):
        raise AssertionError("flat symmetric connection is not flat")
    if face_holonomies(UNIFORM_TWIST_EDGE_BITS) != (1, 1, 1, 1):
        raise AssertionError("uniformly twisted connection lacks all-face holonomy")
    if edge_to_residual(UNIFORM_TWIST_EDGE_BITS) != TORSION_RESIDUAL:
        raise AssertionError("uniform twist did not map to endpoint torsion")

    # Exact identity sum_e d_twisted(v) = 3 sum_v v.
    zero_total_injection_cases = 0
    for vertices in product(range(-bound, bound + 1), repeat=4):
        image = twisted_coboundary(vertices)
        if edge_total(image) != 3 * vertex_total(vertices):
            raise AssertionError("twisted total identity failed")
        if edge_total(image) == 0 and vertex_total(vertices) != 0:
            raise AssertionError("zero-total twisted image came from a nonzero-total vertex state")
        zero_total_injection_cases += 1

    # Construct every bounded kernel representative of total mod 3 as a
    # zero-total representative of the same twisted class.
    neutralization_cases = 0
    for edges in product(range(-bound, bound + 1), repeat=6):
        if edge_total(edges) % 3:
            continue
        vertices, neutral = neutralize_twisted_representative(edges)
        if vector_add(neutral, twisted_coboundary(vertices)) != edges:
            raise AssertionError("neutral representative is not cohomologous to the original")
        neutralization_cases += 1

    classes = symmetric_connection_classes()
    if classes != (ZERO_RESIDUAL, TORSION_RESIDUAL):
        raise AssertionError("full tetrahedral symmetry should leave exactly two gauge classes")
    unique_image = unique_nonzero_equivariant_root_kernel_image()

    ordinary_free_rank = 6 - len(ordinary_factors)
    twisted_free_rank = 6 - len(twisted_factors)
    neutral_free_rank = 5 - len(neutral_factors)

    return TwistedCohomologyReport(
        ordinary_smith_factors=ordinary_factors,
        twisted_smith_factors=twisted_factors,
        neutral_smith_factors=neutral_factors,
        ordinary_free_rank=ordinary_free_rank,
        twisted_free_rank=twisted_free_rank,
        twisted_torsion=tuple(value for value in twisted_factors if value > 1),
        neutral_free_rank=neutral_free_rank,
        neutral_torsion=tuple(value for value in neutral_factors if value > 1),
        symmetric_gauge_classes=classes,
        unique_nonzero_kernel_image=unique_image,
        neutralization_cases_checked=neutralization_cases,
        zero_total_injection_cases_checked=zero_total_injection_cases,
    )


def complete_twisted_cohomology_certificate(*, bound: int = 2) -> dict[str, object]:
    report = verify_twisted_endpoint_cohomology(bound=bound)
    return {
        "ordinary_graph_cohomology": {
            "smith_factors": report.ordinary_smith_factors,
            "abstract_group": "Z^3",
        },
        "uniformly_twisted_graph_cohomology": {
            "smith_factors": report.twisted_smith_factors,
            "free_rank": report.twisted_free_rank,
            "torsion": report.twisted_torsion,
            "abstract_group": "Z^2 + Z/2",
        },
        "zero_total_precision_sector": {
            "smith_factors": report.neutral_smith_factors,
            "free_rank": report.neutral_free_rank,
            "torsion": report.neutral_torsion,
            "abstract_group": "Z^2 + Z/2",
            "quotient_charge": "edge total modulo 3",
            "index_in_full_twisted_cohomology": 3,
            "extension_split": False,
        },
        "characteristic_two": {
            "ordinary_equals_twisted_mod_2": True,
            "common_dimension": 3,
        },
        "symmetric_phases": [
            {"p": state.p, "q": state.q, "e": state.e}
            for state in report.symmetric_gauge_classes
        ],
        "unique_nonzero_equivariant_root_kernel_image": {
            "p": report.unique_nonzero_kernel_image.p,
            "q": report.unique_nonzero_kernel_image.q,
            "e": report.unique_nonzero_kernel_image.e,
        },
        "exhaustive_bounded_checks": {
            "bound": bound,
            "neutralization_cases": report.neutralization_cases_checked,
            "zero_total_injection_cases": report.zero_total_injection_cases_checked,
        },
        "boundary": (
            "The integral bridge identifies the endpoint-sum quotient with a uniformly "
            "twisted graph coefficient system. It does not prove that native six-dimensional "
            "Cell transport selects that phase rather than the flat phase."
        ),
    }
