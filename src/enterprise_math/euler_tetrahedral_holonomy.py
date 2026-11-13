"""Exact tetrahedral slice transport and Euler half-turn holonomy.

All matrix computations use ``Fraction`` and all spinor computations use
integer quaternions.  Classical angles, trigonometric functions, and a
numerical value of pi are absent from the finite core.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from typing import Iterable

Vec3 = tuple[int, int, int]
RatVec3 = tuple[Fraction, Fraction, Fraction]
Mat3 = tuple[RatVec3, RatVec3, RatVec3]
Quat = tuple[int, int, int, int]

NORMALS: tuple[Vec3, ...] = (
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, 1, 1),
)


def dot(left: Iterable[int | Fraction], right: Iterable[int | Fraction]) -> Fraction:
    return sum((Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0))


def cross(left: Vec3, right: Vec3) -> Vec3:
    ax, ay, az = left
    bx, by, bz = right
    return (ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)


def scale_vec(scale: int | Fraction, vector: Iterable[int | Fraction]) -> RatVec3:
    scalar = Fraction(scale)
    x, y, z = vector
    return scalar * Fraction(x), scalar * Fraction(y), scalar * Fraction(z)


def add_vec(left: Iterable[int | Fraction], right: Iterable[int | Fraction]) -> RatVec3:
    a, b, c = left
    x, y, z = right
    return Fraction(a) + Fraction(x), Fraction(b) + Fraction(y), Fraction(c) + Fraction(z)


def determinant(left: Vec3, middle: Vec3, right: Vec3) -> int:
    return int(dot(left, cross(middle, right)))


def identity_matrix() -> Mat3:
    return (
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )


def transpose(matrix: Mat3) -> Mat3:
    return tuple(tuple(matrix[row][column] for row in range(3)) for column in range(3))  # type: ignore[return-value]


def mat_add(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def mat_scale(scale: int | Fraction, matrix: Mat3) -> Mat3:
    scalar = Fraction(scale)
    return tuple(
        tuple(scalar * matrix[row][column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def mat_mul(left: Mat3, right: Mat3) -> Mat3:
    return tuple(
        tuple(
            sum((left[row][k] * right[k][column] for k in range(3)), Fraction(0))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def mat_vec(matrix: Mat3, vector: Iterable[int | Fraction]) -> RatVec3:
    values = tuple(Fraction(value) for value in vector)
    return tuple(
        sum((matrix[row][column] * values[column] for column in range(3)), Fraction(0))
        for row in range(3)
    )  # type: ignore[return-value]


def outer(left: Vec3, right: Vec3) -> Mat3:
    return tuple(
        tuple(Fraction(left[row] * right[column]) for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def cross_matrix(vector: Vec3) -> Mat3:
    x, y, z = vector
    return (
        (Fraction(0), Fraction(-z), Fraction(y)),
        (Fraction(z), Fraction(0), Fraction(-x)),
        (Fraction(-y), Fraction(x), Fraction(0)),
    )


def matrix_determinant(matrix: Mat3) -> Fraction:
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def shortest_rotation(source: int, target: int) -> Mat3:
    """Rational Rodrigues matrix for the shortest proper rotation n_s -> n_t."""

    if source == target or source not in range(4) or target not in range(4):
        raise ValueError("source and target must be distinct tetrahedral vertices")
    k = cross(NORMALS[source], NORMALS[target])
    skew = cross_matrix(k)
    return mat_add(
        identity_matrix(),
        mat_add(mat_scale(Fraction(1, 3), skew), mat_scale(Fraction(1, 6), mat_mul(skew, skew))),
    )


def expected_face_holonomy(start: int) -> Mat3:
    normal = NORMALS[start]
    return mat_add(mat_scale(Fraction(2, 3), outer(normal, normal)), mat_scale(-1, identity_matrix()))


def face_holonomy(start: int, middle: int, end: int) -> Mat3:
    """Transport start -> middle -> end -> start."""

    if len({start, middle, end}) != 3:
        raise ValueError("a face loop requires three distinct vertices")
    return mat_mul(
        shortest_rotation(end, start),
        mat_mul(shortest_rotation(middle, end), shortest_rotation(start, middle)),
    )


def quat_mul(left: Quat, right: Quat) -> Quat:
    a, x, y, z = left
    b, u, v, w = right
    return (
        a * b - x * u - y * v - z * w,
        a * u + b * x + y * w - z * v,
        a * v + b * y + z * u - x * w,
        a * w + b * z + x * v - y * u,
    )


def quat_conjugate(value: Quat) -> Quat:
    a, x, y, z = value
    return a, -x, -y, -z


def quat_norm(value: Quat) -> int:
    a, x, y, z = value
    return a * a + x * x + y * y + z * z


def quat_scale(scale: int, value: Quat) -> Quat:
    return tuple(scale * coordinate for coordinate in value)  # type: ignore[return-value]


def pure_quat(vector: Vec3) -> Quat:
    return 0, vector[0], vector[1], vector[2]


def edge_spinor(source: int, target: int) -> Quat:
    """Integral p_st with unit lift q_st=p_st/sqrt(3)."""

    if source == target or source not in range(4) or target not in range(4):
        raise ValueError("source and target must be distinct tetrahedral vertices")
    k = cross(NORMALS[source], NORMALS[target])
    if any(coordinate % 2 for coordinate in k):
        raise AssertionError("tetrahedral cross products must have even coordinates")
    return 1, k[0] // 2, k[1] // 2, k[2] // 2


def face_spinor(start: int, middle: int, end: int) -> Quat:
    if len({start, middle, end}) != 3:
        raise ValueError("a face loop requires three distinct vertices")
    return quat_mul(
        edge_spinor(end, start),
        quat_mul(edge_spinor(middle, end), edge_spinor(start, middle)),
    )


def orientation_sign(start: int, middle: int, end: int) -> int:
    value = determinant(NORMALS[start], NORMALS[middle], NORMALS[end])
    if value not in (-4, 4):
        raise ValueError("three distinct tetrahedral normals must have determinant +/-4")
    return value // 4


def expected_face_spinor(start: int, middle: int, end: int) -> Quat:
    return quat_scale(3 * orientation_sign(start, middle, end), pure_quat(NORMALS[start]))


def scaled_spin_action(spinor: Quat, vector: Vec3) -> Vec3:
    """Vector part of p(0,v)p-bar; divide by N(p) for the unit rotation."""

    result = quat_mul(quat_mul(spinor, pure_quat(vector)), quat_conjugate(spinor))
    if result[0] != 0:
        raise AssertionError("quaternion conjugation of a pure vector must stay pure")
    return result[1], result[2], result[3]


def tangent_vector(start: int, target: int) -> Vec3:
    return cross(NORMALS[start], NORMALS[target])


def spherical_tangent_cosine(start: int, left: int, right: int) -> Fraction:
    """Cosine of the spherical interior angle, computed without trig."""

    if len({start, left, right}) != 3:
        raise ValueError("expected three distinct tetrahedral vertices")
    # Work with 3*t_uv = 3*n_v + n_u to avoid square roots.
    first = add_vec(scale_vec(3, NORMALS[left]), NORMALS[start])
    second = add_vec(scale_vec(3, NORMALS[right]), NORMALS[start])
    numerator = dot(first, second)
    norm_sq = dot(first, first)
    if norm_sq != dot(second, second):
        raise AssertionError("regular tetrahedral tangents must have equal norm")
    # Equal lengths make cos = dot/norm^2.
    return numerator / norm_sq


def exhaustive_certificate() -> dict[str, object]:
    normals = NORMALS
    if tuple(dot(n, n) for n in normals) != (3, 3, 3, 3):
        raise AssertionError("tetrahedral normals must have squared norm three")
    if any(dot(normals[i], normals[j]) != -1 for i in range(4) for j in range(i + 1, 4)):
        raise AssertionError("distinct tetrahedral normals must have dot product -1")
    if tuple(sum(normal[index] for normal in normals) for index in range(3)) != (0, 0, 0):
        raise AssertionError("the four tetrahedral normals must sum to zero")

    edge_checks = 0
    for source in range(4):
        for target in range(4):
            if source == target:
                continue
            rotation = shortest_rotation(source, target)
            if mat_vec(rotation, normals[source]) != scale_vec(1, normals[target]):
                raise AssertionError("shortest rotation failed to carry one normal to the other")
            if mat_mul(transpose(rotation), rotation) != identity_matrix():
                raise AssertionError("shortest rotation is not orthogonal")
            if matrix_determinant(rotation) != 1:
                raise AssertionError("shortest rotation must be proper")
            if mat_mul(shortest_rotation(target, source), rotation) != identity_matrix():
                raise AssertionError("reverse edge transport must be the inverse")
            spinor = edge_spinor(source, target)
            if quat_norm(spinor) != 3:
                raise AssertionError("every integral edge spinor must have norm three")
            edge_checks += 1

    face_checks = 0
    spin_orientation_pairs = 0
    for start, middle, end in permutations(range(4), 3):
        holonomy = face_holonomy(start, middle, end)
        expected = expected_face_holonomy(start)
        if holonomy != expected:
            raise AssertionError("tetrahedral face transport did not produce the half-turn matrix")
        if mat_vec(holonomy, normals[start]) != scale_vec(1, normals[start]):
            raise AssertionError("face holonomy must fix the starting normal")
        for target in range(4):
            if target == start:
                continue
            tangent = tangent_vector(start, target)
            if mat_vec(holonomy, tangent) != scale_vec(-1, tangent):
                raise AssertionError("face holonomy must reverse every shared-line tangent")

        spinor = face_spinor(start, middle, end)
        expected_spinor = expected_face_spinor(start, middle, end)
        if spinor != expected_spinor:
            raise AssertionError("integral face-spinor product failed")
        if quat_mul(spinor, spinor) != (-27, 0, 0, 0):
            raise AssertionError("normalized face spinor must square to -1")
        if face_spinor(start, end, middle) != quat_scale(-1, spinor):
            raise AssertionError("reversing face orientation must flip the Spin lift")
        if face_holonomy(start, end, middle) != holonomy:
            raise AssertionError("opposite Spin signs must project to the same SO(3) half-turn")
        face_checks += 1
        spin_orientation_pairs += 1

    tangent_cosines = {
        spherical_tangent_cosine(start, left, right)
        for start, left, right in permutations(range(4), 3)
    }
    if tangent_cosines != {Fraction(-1, 2)}:
        raise AssertionError("every spherical face angle must have cosine -1/2")

    return {
        "normal_count": 4,
        "directed_edge_transports_checked": edge_checks,
        "ordered_face_loops_checked": face_checks,
        "spin_orientation_reversal_pairs_checked": spin_orientation_pairs,
        "normal_squared_norm": 3,
        "distinct_normal_dot_product": -1,
        "edge_spinor_norm": 3,
        "edge_spinor_scalar_square": Fraction(1, 3),
        "face_spinor_square_after_normalization": -1,
        "face_tangent_holonomy": "minus identity",
        "spherical_interior_angle_cosine": Fraction(-1, 2),
        "continuous_spherical_excess_identification": "pi (standard Gauss-Bonnet layer)",
    }
