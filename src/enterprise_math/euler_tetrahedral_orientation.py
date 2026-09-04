"""Exact tetrahedral orientation-local-system checker for Enterprise Euler geometry.

The checker uses only integer matrices and finite enumeration. It proves at the
selected FCC/tetrahedral carrier level that the four slice-local chiral cross
operators form an orientation local system:

    Q D_n Q^{-1} = det(Q) D_{Qn}.

Orientation-preserving tetrahedral symmetries therefore preserve the local
Euler generator J=D/sqrt(3), while orientation-reversing symmetries flip it.

No floating point, angle, numerical pi, or native-six-dimensional
identification is used.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations, product
from typing import Iterator, Sequence

Vector3 = tuple[int, int, int]
Matrix3 = tuple[
    tuple[int, int, int],
    tuple[int, int, int],
    tuple[int, int, int],
]
Permutation4 = tuple[int, int, int, int]

IDENTITY3: Matrix3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

TETRAHEDRAL_NORMALS: tuple[Vector3, ...] = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def _check_matrix(matrix: Matrix3) -> None:
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("matrix must be 3x3")


def dot(left: Vector3, right: Vector3) -> int:
    return sum(a * b for a, b in zip(left, right))


def cross(left: Vector3, right: Vector3) -> Vector3:
    a, b, c = left
    x, y, z = right
    return b * z - c * y, c * x - a * z, a * y - b * x


def negate(vector: Vector3) -> Vector3:
    return tuple(-x for x in vector)  # type: ignore[return-value]


def mat_vec(matrix: Matrix3, vector: Vector3) -> Vector3:
    _check_matrix(matrix)
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def mat_mul(left: Matrix3, right: Matrix3) -> Matrix3:
    _check_matrix(left)
    _check_matrix(right)
    return tuple(
        tuple(
            sum(left[row][k] * right[k][column] for k in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def transpose(matrix: Matrix3) -> Matrix3:
    _check_matrix(matrix)
    return tuple(
        tuple(matrix[column][row] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def determinant(matrix: Matrix3) -> int:
    _check_matrix(matrix)
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def permutation_sign(permutation: Sequence[int]) -> int:
    if sorted(permutation) != list(range(len(permutation))):
        raise ValueError("not a permutation")
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def signed_permutation_matrices() -> Iterator[Matrix3]:
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            yield tuple(
                tuple(
                    signs[row] if column == permutation[row] else 0
                    for column in range(3)
                )
                for row in range(3)
            )  # type: ignore[misc]


def induced_normal_permutation(matrix: Matrix3) -> Permutation4:
    images = tuple(mat_vec(matrix, normal) for normal in TETRAHEDRAL_NORMALS)
    if set(images) != set(TETRAHEDRAL_NORMALS):
        raise ValueError("matrix does not preserve the tetrahedral normal family")
    return tuple(TETRAHEDRAL_NORMALS.index(image) for image in images)  # type: ignore[return-value]


@dataclass(frozen=True)
class TetrahedralSymmetry:
    matrix: Matrix3
    permutation: Permutation4
    determinant: int

    @property
    def orientation_preserving(self) -> bool:
        return self.determinant == 1

    def maps_slice(self, source: int, target: int) -> bool:
        return self.permutation[source] == target


def tetrahedral_symmetries() -> tuple[TetrahedralSymmetry, ...]:
    symmetries: list[TetrahedralSymmetry] = []
    for matrix in signed_permutation_matrices():
        images = {mat_vec(matrix, normal) for normal in TETRAHEDRAL_NORMALS}
        if images != set(TETRAHEDRAL_NORMALS):
            continue
        permutation = induced_normal_permutation(matrix)
        det = determinant(matrix)
        if det not in (-1, 1):
            raise AssertionError("tetrahedral symmetry is not orthogonal")
        if mat_mul(matrix, transpose(matrix)) != IDENTITY3:
            raise AssertionError("signed permutation matrix failed orthogonality")
        if det != permutation_sign(permutation):
            raise AssertionError("determinant did not equal induced permutation sign")
        symmetries.append(TetrahedralSymmetry(matrix, permutation, det))
    symmetries.sort(key=lambda item: (item.permutation, item.matrix))
    if len(symmetries) != 24:
        raise AssertionError(
            f"expected 24 tetrahedral symmetries, found {len(symmetries)}"
        )
    return tuple(symmetries)


def cross_matrix(normal: Vector3) -> Matrix3:
    a, b, c = normal
    return ((0, -c, b), (c, 0, -a), (-b, a, 0))


def outer(left: Vector3, right: Vector3) -> Matrix3:
    return tuple(
        tuple(left[row] * right[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matrix_add(left: Matrix3, right: Matrix3) -> Matrix3:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def matrix_scalar_mul(scalar: int, matrix: Matrix3) -> Matrix3:
    return tuple(
        tuple(scalar * matrix[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def cross_square_certificate(normal: Vector3) -> tuple[Matrix3, Matrix3]:
    """Return the equal matrices D_n^2 and n n^T - ||n||^2 I."""

    operator = cross_matrix(normal)
    left = mat_mul(operator, operator)
    norm_sq = dot(normal, normal)
    right = matrix_add(
        outer(normal, normal),
        matrix_scalar_mul(-norm_sq, IDENTITY3),
    )
    if left != right:
        raise AssertionError("cross-square certificate failed")
    return left, right


def covariance_certificate(
    symmetry: TetrahedralSymmetry,
    normal_index: int,
) -> tuple[Matrix3, Matrix3]:
    """Verify Q D_n Q^T = det(Q) D_(Qn)."""

    if normal_index not in range(4):
        raise ValueError("normal_index must lie in range(4)")
    normal = TETRAHEDRAL_NORMALS[normal_index]
    image = mat_vec(symmetry.matrix, normal)
    left = mat_mul(
        mat_mul(symmetry.matrix, cross_matrix(normal)),
        transpose(symmetry.matrix),
    )
    right = matrix_scalar_mul(symmetry.determinant, cross_matrix(image))
    if left != right:
        raise AssertionError("twisted cross-operator covariance failed")
    return left, right


def primitive_unoriented(vector: Vector3) -> Vector3:
    """Canonical primitive representative of a nonzero unoriented integer line."""

    from math import gcd

    if vector == (0, 0, 0):
        raise ValueError("zero vector has no line direction")
    divisor = 0
    for coordinate in vector:
        divisor = gcd(divisor, abs(coordinate))
    primitive = tuple(coordinate // divisor for coordinate in vector)
    for coordinate in primitive:
        if coordinate:
            if coordinate < 0:
                primitive = tuple(-x for x in primitive)
            break
    return primitive  # type: ignore[return-value]


def shared_line_axes() -> dict[tuple[int, int], Vector3]:
    axes: dict[tuple[int, int], Vector3] = {}
    for source in range(4):
        for target in range(source + 1, 4):
            axis = primitive_unoriented(
                cross(TETRAHEDRAL_NORMALS[source], TETRAHEDRAL_NORMALS[target])
            )
            axes[(source, target)] = axis
    if len(set(axes.values())) != 6:
        raise AssertionError("the six slice pairs did not yield six line families")
    return axes


def incidence_ray(source: int, target: int) -> Vector3:
    if source == target or source not in range(4) or target not in range(4):
        raise ValueError("source and target must be distinct slice labels")
    return cross(TETRAHEDRAL_NORMALS[source], TETRAHEDRAL_NORMALS[target])


def even_transports(source: int, target: int) -> tuple[TetrahedralSymmetry, ...]:
    transports = tuple(
        symmetry
        for symmetry in tetrahedral_symmetries()
        if symmetry.orientation_preserving and symmetry.maps_slice(source, target)
    )
    if len(transports) != 3:
        raise AssertionError("expected exactly three A4 transports between two slices")
    return transports


def odd_transports(source: int, target: int) -> tuple[TetrahedralSymmetry, ...]:
    transports = tuple(
        symmetry
        for symmetry in tetrahedral_symmetries()
        if not symmetry.orientation_preserving and symmetry.maps_slice(source, target)
    )
    if len(transports) != 3:
        raise AssertionError("expected exactly three odd transports between two slices")
    return transports


def compose_symmetries(*symmetries: TetrahedralSymmetry) -> TetrahedralSymmetry:
    """Compose in application order: ``compose_symmetries(g,h)`` means h after g."""

    matrix = IDENTITY3
    for symmetry in symmetries:
        matrix = mat_mul(symmetry.matrix, matrix)
    permutation = induced_normal_permutation(matrix)
    det = determinant(matrix)
    result = TetrahedralSymmetry(matrix, permutation, det)
    known = {
        (item.matrix, item.permutation, item.determinant)
        for item in tetrahedral_symmetries()
    }
    if (result.matrix, result.permutation, result.determinant) not in known:
        raise AssertionError("symmetry composition left the tetrahedral group")
    return result


def stabilizer(
    slice_index: int,
    *,
    orientation_preserving: bool = True,
) -> tuple[TetrahedralSymmetry, ...]:
    items = tuple(
        symmetry
        for symmetry in tetrahedral_symmetries()
        if symmetry.maps_slice(slice_index, slice_index)
        and symmetry.orientation_preserving == orientation_preserving
    )
    if len(items) != 3:
        raise AssertionError(f"expected stabilizer size 3, found {len(items)}")
    return items


def triangle_loop_holonomies(
    first: int,
    second: int,
    third: int,
) -> Counter[Matrix3]:
    if len({first, second, third}) != 3:
        raise ValueError("triangle labels must be distinct")
    counter: Counter[Matrix3] = Counter()
    for q12 in even_transports(first, second):
        for q23 in even_transports(second, third):
            for q31 in even_transports(third, first):
                loop = compose_symmetries(q12, q23, q31)
                if not loop.maps_slice(first, first):
                    raise AssertionError("triangle transport did not close")
                if not loop.orientation_preserving:
                    raise AssertionError("A4 triangle loop reversed orientation")
                covariance_certificate(loop, first)
                counter[loop.matrix] += 1
    if set(counter) != {item.matrix for item in stabilizer(first)}:
        raise AssertionError("triangle holonomy did not fill the C3 stabilizer")
    if sum(counter.values()) != 27:
        raise AssertionError("unexpected number of triangle transport choices")
    return counter


def graph_cycle_holonomies(edge_bits: Sequence[int]) -> tuple[int, int, int]:
    """Independent triangle holonomies for K4 edge order 01,02,03,12,13,23."""

    if len(edge_bits) != 6 or any(bit not in (0, 1) for bit in edge_bits):
        raise ValueError("edge_bits must be six bits")
    e01, e02, e03, e12, e13, e23 = edge_bits
    return e01 ^ e12 ^ e02, e01 ^ e13 ^ e03, e02 ^ e23 ^ e03


def vertex_gauge(
    edge_bits: Sequence[int],
    vertex_bits: Sequence[int],
) -> tuple[int, ...]:
    if len(edge_bits) != 6 or any(bit not in (0, 1) for bit in edge_bits):
        raise ValueError("edge_bits must be six bits")
    if len(vertex_bits) != 4 or any(bit not in (0, 1) for bit in vertex_bits):
        raise ValueError("vertex_bits must be four bits")
    edges = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
    return tuple(
        bit ^ vertex_bits[left] ^ vertex_bits[right]
        for bit, (left, right) in zip(edge_bits, edges)
    )


def graph_sign_class_count() -> int:
    representatives: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for bits in product((0, 1), repeat=6):
        holonomy = graph_cycle_holonomies(bits)
        representatives.setdefault(holonomy, bits)
        for gauge in product((0, 1), repeat=4):
            if graph_cycle_holonomies(vertex_gauge(bits, gauge)) != holonomy:
                raise AssertionError("triangle holonomy was not gauge invariant")
    if len(representatives) != 8:
        raise AssertionError("expected H1(K4,F2) to have eight classes")
    return len(representatives)


def orientation_local_system_certificate() -> dict[str, object]:
    symmetries = tetrahedral_symmetries()
    even = tuple(item for item in symmetries if item.orientation_preserving)
    odd = tuple(item for item in symmetries if not item.orientation_preserving)

    for normal in TETRAHEDRAL_NORMALS:
        if dot(normal, normal) != 3:
            raise AssertionError("tetrahedral normal did not have norm squared three")
        cross_square_certificate(normal)

    if tuple(map(sum, zip(*TETRAHEDRAL_NORMALS))) != (0, 0, 0):
        raise AssertionError("tetrahedral normals did not sum to zero")
    for left in range(4):
        for right in range(4):
            expected = 3 if left == right else -1
            if dot(TETRAHEDRAL_NORMALS[left], TETRAHEDRAL_NORMALS[right]) != expected:
                raise AssertionError("tetrahedral Gram matrix mismatch")

    for symmetry in symmetries:
        for normal_index in range(4):
            covariance_certificate(symmetry, normal_index)

    for source in range(4):
        for target in range(4):
            even_transports(source, target)
            odd_transports(source, target)

    for source in range(4):
        for target in range(4):
            if source == target:
                continue
            if incidence_ray(target, source) != negate(incidence_ray(source, target)):
                raise AssertionError("incidence rays were not opposite")

    triangle_profiles = {}
    for triangle in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
        profile = triangle_loop_holonomies(*triangle)
        triangle_profiles["".join(map(str, triangle))] = sorted(profile.values())

    return {
        "normal_count": 4,
        "shared_line_count": len(shared_line_axes()),
        "symmetry_count": len(symmetries),
        "orientation_preserving_count": len(even),
        "orientation_reversing_count": len(odd),
        "induced_group": "S4",
        "orientation_preserving_subgroup": "A4",
        "determinant_equals_permutation_sign": True,
        "even_transport_count_per_ordered_pair": 3,
        "odd_transport_count_per_ordered_pair": 3,
        "cross_operator_covariance": "Q D_n Q^-1 = det(Q) D_(Qn)",
        "chirality_rule": "even preserves J; odd reverses J",
        "triangle_chirality_holonomy": 0,
        "triangle_frame_holonomy": "C3 stabilizer",
        "triangle_choice_profiles": triangle_profiles,
        "abstract_graph_sign_class_count": graph_sign_class_count(),
        "ambient_oriented_transport_class": (0, 0, 0),
        "status": "PASS",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(orientation_local_system_certificate(), indent=2, sort_keys=True))
