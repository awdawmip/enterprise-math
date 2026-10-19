"""Exact proper-versus-reflective tetrahedral Euler transport classification.

A fully S4-equivariant involutive transport assigned to an overlap edge and
required to exchange that edge's endpoints has exactly two possibilities:

* the endpoint transposition, an improper/reflection-type transport;
* the endpoint transposition times the complementary transposition, a proper
  tetrahedral half-turn.

The first yields the uniform all-face chirality twist and endpoint torsion.
The second has exact identity face transport and yields the flat phase.

The checker uses only finite permutations and exact integer matrices.  No
floating point, angle, trigonometry, or numerical value of pi is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Iterable, Iterator

from enterprise_math.euler_c12_root_torsor import (
    EdgeBits,
    face_holonomies,
    holonomy_code,
)
from enterprise_math.euler_holonomy_residual_duality import (
    TORSION_RESIDUAL,
    ZERO_RESIDUAL,
    edge_to_residual,
)
from enterprise_math.euler_twisted_endpoint_cohomology import determinant

Permutation = tuple[int, int, int, int]
Edge = tuple[int, int]
Face = tuple[int, int, int]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

VERTICES = (0, 1, 2, 3)
EDGES: tuple[Edge, ...] = tuple(combinations(VERTICES, 2))
FACES: tuple[Face, ...] = tuple(combinations(VERTICES, 3))
IDENTITY: Permutation = (0, 1, 2, 3)
STANDARD_GRAM: Matrix3 = ((2, 1, 1), (1, 2, 1), (1, 1, 2))


def validate_permutation(value: Iterable[int]) -> Permutation:
    result = tuple(value)
    if len(result) != 4 or set(result) != set(VERTICES):
        raise ValueError("expected a permutation of 0,1,2,3")
    return result  # type: ignore[return-value]


def all_permutations() -> Iterator[Permutation]:
    for value in permutations(VERTICES):
        yield value  # type: ignore[misc]


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Composition `left after right`."""

    left = validate_permutation(left)
    right = validate_permutation(right)
    return tuple(left[right[index]] for index in VERTICES)  # type: ignore[return-value]


def inverse(permutation: Permutation) -> Permutation:
    permutation = validate_permutation(permutation)
    result = [0] * 4
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)  # type: ignore[return-value]


def conjugate(group_element: Permutation, value: Permutation) -> Permutation:
    return compose(group_element, compose(value, inverse(group_element)))


def transposition(left: int, right: int) -> Permutation:
    if left not in VERTICES or right not in VERTICES or left == right:
        raise ValueError("transposition requires two distinct tetrahedral vertices")
    result = list(IDENTITY)
    result[left], result[right] = result[right], result[left]
    return tuple(result)  # type: ignore[return-value]


def permutation_sign(permutation: Permutation) -> int:
    permutation = validate_permutation(permutation)
    inversions = sum(
        permutation[left] > permutation[right]
        for left in VERTICES
        for right in range(left + 1, 4)
    )
    return -1 if inversions % 2 else 1


def is_involution(permutation: Permutation) -> bool:
    return compose(permutation, permutation) == IDENTITY


def normalize_edge(edge: Edge) -> Edge:
    left, right = edge
    if left not in VERTICES or right not in VERTICES or left == right:
        raise ValueError("edge must contain two distinct tetrahedral vertices")
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def complement_edge(edge: Edge) -> Edge:
    edge = normalize_edge(edge)
    return tuple(vertex for vertex in VERTICES if vertex not in edge)  # type: ignore[return-value]


def permute_edge(permutation: Permutation, edge: Edge) -> Edge:
    permutation = validate_permutation(permutation)
    left, right = normalize_edge(edge)
    return normalize_edge((permutation[left], permutation[right]))


def reflection_transport(edge: Edge) -> Permutation:
    """Improper transport: swap only the overlap endpoints."""

    left, right = normalize_edge(edge)
    return transposition(left, right)


def proper_half_turn_transport(edge: Edge) -> Permutation:
    """Proper transport: swap the edge endpoints and the complementary pair."""

    left, right = normalize_edge(edge)
    other_left, other_right = complement_edge(edge)
    return compose(transposition(left, right), transposition(other_left, other_right))


def edge_stabilizer(edge: Edge) -> tuple[Permutation, ...]:
    edge = normalize_edge(edge)
    return tuple(permutation for permutation in all_permutations() if permute_edge(permutation, edge) == edge)


def commutes(left: Permutation, right: Permutation) -> bool:
    return compose(left, right) == compose(right, left)


def base_transport_candidates() -> tuple[Permutation, ...]:
    base = (0, 1)
    stabilizer = edge_stabilizer(base)
    candidates = tuple(
        permutation
        for permutation in all_permutations()
        if is_involution(permutation)
        and permutation[0] == 1
        and permutation[1] == 0
        and all(commutes(permutation, stabilizer_element) for stabilizer_element in stabilizer)
    )
    return candidates


def transport_assignment(kind: str) -> dict[Edge, Permutation]:
    if kind == "reflection":
        transport = reflection_transport
    elif kind == "proper":
        transport = proper_half_turn_transport
    else:
        raise ValueError("kind must be 'reflection' or 'proper'")
    return {edge: transport(edge) for edge in EDGES}


def assignment_is_equivariant(kind: str) -> bool:
    assignment = transport_assignment(kind)
    return all(
        assignment[permute_edge(permutation, edge)]
        == conjugate(permutation, assignment[edge])
        for permutation in all_permutations()
        for edge in EDGES
    )


def face_transport(kind: str, face: Face) -> Permutation:
    i, j, k = face
    assignment = transport_assignment(kind)
    # travel i -> j -> k -> i
    return compose(
        assignment[normalize_edge((k, i))],
        compose(
            assignment[normalize_edge((j, k))],
            assignment[normalize_edge((i, j))],
        ),
    )


def assignment_edge_bits(kind: str) -> EdgeBits:
    assignment = transport_assignment(kind)
    return tuple(0 if permutation_sign(assignment[edge]) == 1 else 1 for edge in EDGES)  # type: ignore[return-value]


def standard_representation_matrix(permutation: Permutation) -> Matrix3:
    """Matrix on the sum-zero subspace of Z^4 in basis e0-e3,e1-e3,e2-e3."""

    permutation = validate_permutation(permutation)
    columns: list[tuple[int, int, int]] = []
    for basis_vertex in range(3):
        vector = [0, 0, 0, 0]
        vector[permutation[basis_vertex]] += 1
        vector[permutation[3]] -= 1
        # A sum-zero vector x has coordinates (x0,x1,x2) in this basis.
        columns.append((vector[0], vector[1], vector[2]))
    return tuple(
        tuple(columns[column][row] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix3) -> Matrix3:
    return tuple(tuple(matrix[column][row] for column in range(3)) for row in range(3))  # type: ignore[return-value]


def matrix_multiply(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(sum(left[row][index] * right[index][column] for index in range(3)) for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def standard_representation_is_orthogonal(permutation: Permutation) -> bool:
    matrix = standard_representation_matrix(permutation)
    return matrix_multiply(transpose(matrix), matrix_multiply(STANDARD_GRAM, matrix)) == STANDARD_GRAM


@dataclass(frozen=True)
class TransportDichotomyReport:
    candidate_count: int
    candidates: tuple[Permutation, ...]
    proper_edge_bits: EdgeBits
    reflection_edge_bits: EdgeBits
    proper_face_transports: tuple[Permutation, ...]
    reflection_face_transports: tuple[Permutation, ...]
    proper_residual: object
    reflection_residual: object
    permutation_representation_checks: int


def verify_transport_dichotomy() -> TransportDichotomyReport:
    candidates = base_transport_candidates()
    expected_candidates = (
        reflection_transport((0, 1)),
        proper_half_turn_transport((0, 1)),
    )
    if set(candidates) != set(expected_candidates) or len(candidates) != 2:
        raise AssertionError("the equivariant base-edge transport classification is not two-valued")

    for kind in ("proper", "reflection"):
        assignment = transport_assignment(kind)
        if not assignment_is_equivariant(kind):
            raise AssertionError(f"{kind} transport assignment is not S4-equivariant")
        for edge, transport in assignment.items():
            left, right = edge
            if transport[left] != right or transport[right] != left:
                raise AssertionError(f"{kind} transport does not exchange edge endpoints")
            if not is_involution(transport):
                raise AssertionError(f"{kind} transport is not involutive")

    proper_bits = assignment_edge_bits("proper")
    reflection_bits = assignment_edge_bits("reflection")
    if proper_bits != (0, 0, 0, 0, 0, 0):
        raise AssertionError("proper transport should have zero chirality bits")
    if reflection_bits != (1, 1, 1, 1, 1, 1):
        raise AssertionError("reflection transport should have uniform chirality bits")

    proper_faces = tuple(face_transport("proper", face) for face in FACES)
    reflection_faces = tuple(face_transport("reflection", face) for face in FACES)
    if any(transport != IDENTITY for transport in proper_faces):
        raise AssertionError("proper face transport does not close exactly")
    if any(permutation_sign(transport) != -1 for transport in reflection_faces):
        raise AssertionError("reflective face transport should be orientation reversing")

    if face_holonomies(proper_bits) != (0, 0, 0, 0):
        raise AssertionError("proper transport is not face-flat")
    if face_holonomies(reflection_bits) != (1, 1, 1, 1):
        raise AssertionError("reflective transport is not uniformly twisted")
    if edge_to_residual(proper_bits) != ZERO_RESIDUAL:
        raise AssertionError("proper transport did not map to zero residual")
    if edge_to_residual(reflection_bits) != TORSION_RESIDUAL:
        raise AssertionError("reflective transport did not map to endpoint torsion")

    representation_checks = 0
    for permutation in all_permutations():
        matrix = standard_representation_matrix(permutation)
        if determinant(matrix) != permutation_sign(permutation):
            raise AssertionError("standard tetrahedral determinant is not permutation sign")
        if not standard_representation_is_orthogonal(permutation):
            raise AssertionError("standard tetrahedral representation did not preserve its Gram form")
        representation_checks += 1

    return TransportDichotomyReport(
        candidate_count=len(candidates),
        candidates=candidates,
        proper_edge_bits=proper_bits,
        reflection_edge_bits=reflection_bits,
        proper_face_transports=proper_faces,
        reflection_face_transports=reflection_faces,
        proper_residual=edge_to_residual(proper_bits),
        reflection_residual=edge_to_residual(reflection_bits),
        permutation_representation_checks=representation_checks,
    )


def complete_transport_certificate() -> dict[str, object]:
    report = verify_transport_dichotomy()
    return {
        "candidate_count": report.candidate_count,
        "base_edge_candidates": report.candidates,
        "proper_phase": {
            "transport": "(ij)(kl)",
            "parity": 1,
            "edge_bits": report.proper_edge_bits,
            "face_holonomies": face_holonomies(report.proper_edge_bits),
            "face_transport_identity": True,
            "endpoint_residual": {"p": 0, "q": 0, "e": 0},
        },
        "reflective_phase": {
            "transport": "(ij)",
            "parity": -1,
            "edge_bits": report.reflection_edge_bits,
            "face_holonomies": face_holonomies(report.reflection_edge_bits),
            "face_transport_orientation": -1,
            "endpoint_residual": {"p": 0, "q": 0, "e": 1},
        },
        "standard_representation_checks": report.permutation_representation_checks,
        "selection_rule": (
            "orientation-preserving carrier transport selects the flat global-J phase; "
            "reflection-type transport selects the uniformly twisted projective-Euler phase"
        ),
        "boundary": (
            "The classification is exact for S4-equivariant involutive edge transports. "
            "Current P000 does not yet specify which determinant type is realized by native Cell transport."
        ),
    }
