"""Exact tetrahedral slice-transport and Euler-holonomy certificates.

The four FCC three-axis slice normals are the vertices of a regular tetrahedron.
For each ordered pair of distinct slices this module constructs two exact
orthogonal bridges fixing the shared line:

* ``proper_transport``: the shortest orientation-preserving rotation;
* ``mirror_transport``: the orientation-reversing bisector reflection.

All calculations use :class:`fractions.Fraction`.  No floating-point angle,
trigonometric function, exponential, or numerical value of pi is used in the
finite theorem checker.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Iterable

Scalar = Fraction
Vector = tuple[Scalar, Scalar, Scalar]
Matrix = tuple[Vector, Vector, Vector]

ZERO: Scalar = Fraction(0)
ONE: Scalar = Fraction(1)

NORMALS: tuple[Vector, ...] = (
    (ONE, ONE, ONE),
    (ONE, -ONE, -ONE),
    (-ONE, ONE, -ONE),
    (-ONE, -ONE, ONE),
)

IDENTITY: Matrix = (
    (ONE, ZERO, ZERO),
    (ZERO, ONE, ZERO),
    (ZERO, ZERO, ONE),
)


def _f(value: int | Fraction) -> Fraction:
    return Fraction(value)


def vadd(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def vsub(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def vneg(value: Vector) -> Vector:
    return tuple(-entry for entry in value)  # type: ignore[return-value]


def vscale(scale: Scalar, value: Vector) -> Vector:
    return tuple(scale * entry for entry in value)  # type: ignore[return-value]


def dot(left: Vector, right: Vector) -> Scalar:
    return sum((left[i] * right[i] for i in range(3)), ZERO)


def cross(left: Vector, right: Vector) -> Vector:
    x, y, z = left
    u, v, w = right
    return (y * w - z * v, z * u - x * w, x * v - y * u)


def madd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mneg(value: Matrix) -> Matrix:
    return tuple(
        tuple(-value[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def msub(left: Matrix, right: Matrix) -> Matrix:
    return madd(left, mneg(right))


def mscale(scale: Scalar, value: Matrix) -> Matrix:
    return tuple(
        tuple(scale * value[i][j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def transpose(value: Matrix) -> Matrix:
    return tuple(
        tuple(value[j][i] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(3)), ZERO)
            for j in range(3)
        )
        for i in range(3)
    )  # type: ignore[return-value]


def mapply(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][k] * vector[k] for k in range(3)), ZERO)
        for i in range(3)
    )  # type: ignore[return-value]


def outer(left: Vector, right: Vector) -> Matrix:
    return tuple(
        tuple(left[i] * right[j] for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def skew(vector: Vector) -> Matrix:
    x, y, z = vector
    return (
        (ZERO, -z, y),
        (z, ZERO, -x),
        (-y, x, ZERO),
    )


def determinant(value: Matrix) -> Scalar:
    a, b, c = value[0]
    d, e, f = value[1]
    g, h, i = value[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def matrix_pow(value: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("matrix_pow expects a non-negative exponent")
    result = IDENTITY
    base = value
    power = exponent
    while power:
        if power & 1:
            result = mmul(result, base)
        base = mmul(base, base)
        power >>= 1
    return result


def _normal(index: int) -> Vector:
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < 4:
        raise ValueError("slice index must lie in {0,1,2,3}")
    return NORMALS[index]


def shared_axis(i: int, j: int) -> Vector:
    if i == j:
        raise ValueError("a shared axis requires distinct slices")
    return cross(_normal(i), _normal(j))


def chiral_skew(index: int) -> Matrix:
    """Unnormalized local chiral operator ``v -> n_i cross v``."""

    return skew(_normal(index))


def proper_transport(i: int, j: int) -> Matrix:
    """Shortest proper bridge fixing the shared line and mapping n_i to n_j.

    Formula:
        A_ij = -I/3 + c c^T/6 + [c]_x/3,
    where c=n_i cross n_j.
    """

    c = shared_axis(i, j)
    return madd(
        mscale(Fraction(-1, 3), IDENTITY),
        madd(mscale(Fraction(1, 6), outer(c, c)), mscale(Fraction(1, 3), skew(c))),
    )


def mirror_transport(i: int, j: int) -> Matrix:
    """Improper bisector reflection fixing the shared line.

    Formula:
        H_ij = I - (n_i-n_j)(n_i-n_j)^T/4.
    """

    if i == j:
        raise ValueError("a bridge requires distinct slices")
    m = vsub(_normal(i), _normal(j))
    return msub(IDENTITY, mscale(Fraction(1, 4), outer(m, m)))


def face_half_turn(i: int) -> Matrix:
    """The half-turn fixing n_i and negating its orthogonal slice plane."""

    n = _normal(i)
    return msub(mscale(Fraction(2, 3), outer(n, n)), IDENTITY)


def proper_face_holonomy(i: int, j: int, k: int) -> Matrix:
    if len({i, j, k}) != 3:
        raise ValueError("face holonomy requires three distinct slices")
    return mmul(proper_transport(k, i), mmul(proper_transport(j, k), proper_transport(i, j)))


def mirror_face_holonomy(i: int, j: int, k: int) -> Matrix:
    if len({i, j, k}) != 3:
        raise ValueError("face holonomy requires three distinct slices")
    return mmul(mirror_transport(k, i), mmul(mirror_transport(j, k), mirror_transport(i, j)))


def is_orthogonal(matrix: Matrix) -> bool:
    return mmul(transpose(matrix), matrix) == IDENTITY


def tangent_witnesses(i: int) -> tuple[Vector, Vector, Vector]:
    others = [j for j in range(4) if j != i]
    return tuple(shared_axis(i, j) for j in others)  # type: ignore[return-value]


def spherical_cosine_certificate() -> dict[str, Fraction]:
    """Exact rational part of the normal-sphere triangle calculation.

    If ``c=cos(alpha)=-1/3`` is the common side cosine, spherical cosine law
    gives ``cos(beta)=(c-c^2)/(1-c^2)=-1/2`` for every vertex angle.
    """

    side_cosine = Fraction(-1, 3)
    vertex_cosine = (side_cosine - side_cosine * side_cosine) / (
        1 - side_cosine * side_cosine
    )
    if vertex_cosine != Fraction(-1, 2):
        raise AssertionError("spherical vertex-cosine certificate failed")
    return {
        "side_cosine": side_cosine,
        "side_sine_squared": 1 - side_cosine * side_cosine,
        "vertex_cosine": vertex_cosine,
    }


@dataclass(frozen=True)
class TransportCertificate:
    pair_count: int
    oriented_face_count: int
    proper_determinant: int
    mirror_determinant: int
    proper_triangle_tangent_sign: int
    mirror_triangle_determinant: int
    all_checks_passed: bool


def verify_transport_pair(i: int, j: int) -> None:
    if i == j:
        raise ValueError("pair must be distinct")
    ni = _normal(i)
    nj = _normal(j)
    axis = shared_axis(i, j)
    proper = proper_transport(i, j)
    proper_inverse = proper_transport(j, i)
    mirror = mirror_transport(i, j)

    assert dot(ni, ni) == 3
    assert dot(ni, nj) == -1
    assert dot(axis, axis) == 8

    assert is_orthogonal(proper)
    assert determinant(proper) == 1
    assert mapply(proper, ni) == nj
    assert mapply(proper, axis) == axis
    assert mmul(proper_inverse, proper) == IDENTITY
    assert transpose(proper) == proper_inverse

    assert is_orthogonal(mirror)
    assert determinant(mirror) == -1
    assert mapply(mirror, ni) == nj
    assert mapply(mirror, axis) == axis
    assert matrix_pow(mirror, 2) == IDENTITY

    di = chiral_skew(i)
    dj = chiral_skew(j)
    assert mmul(proper, mmul(di, proper_inverse)) == dj
    assert mmul(mirror, mmul(di, mirror)) == mneg(dj)


def verify_proper_face(i: int, j: int, k: int) -> None:
    holonomy = proper_face_holonomy(i, j, k)
    expected = face_half_turn(i)
    assert holonomy == expected
    assert is_orthogonal(holonomy)
    assert determinant(holonomy) == 1
    assert matrix_pow(holonomy, 2) == IDENTITY
    assert mapply(holonomy, _normal(i)) == _normal(i)

    di = chiral_skew(i)
    # The unnormalized local complex structure squares to -3 on the slice.
    for tangent in tangent_witnesses(i):
        assert dot(_normal(i), tangent) == 0
        assert mapply(holonomy, tangent) == vneg(tangent)
        assert mapply(mmul(di, di), tangent) == vscale(Fraction(-3), tangent)

    # Holonomy preserves J even though it reverses all tangent vectors.
    assert mmul(holonomy, di) == mmul(di, holonomy)


def verify_mirror_face(i: int, j: int, k: int) -> None:
    holonomy = mirror_face_holonomy(i, j, k)
    inverse = mmul(
        mirror_transport(i, j),
        mmul(mirror_transport(j, k), mirror_transport(k, i)),
    )
    assert is_orthogonal(holonomy)
    assert determinant(holonomy) == -1
    assert mapply(holonomy, _normal(i)) == _normal(i)
    assert mmul(inverse, holonomy) == IDENTITY
    di = chiral_skew(i)
    assert mmul(holonomy, mmul(di, inverse)) == mneg(di)


def verify_all() -> TransportCertificate:
    pair_count = 0
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            verify_transport_pair(i, j)
            pair_count += 1

    face_count = 0
    for i, j, k in permutations(range(4), 3):
        verify_proper_face(i, j, k)
        verify_mirror_face(i, j, k)
        face_count += 1

    spherical_cosine_certificate()

    # Explicit base-face matrix from the manuscript.
    expected_q0: Matrix = (
        (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)),
        (Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)),
        (Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)),
    )
    assert proper_face_holonomy(0, 1, 2) == expected_q0

    return TransportCertificate(
        pair_count=pair_count,
        oriented_face_count=face_count,
        proper_determinant=1,
        mirror_determinant=-1,
        proper_triangle_tangent_sign=-1,
        mirror_triangle_determinant=-1,
        all_checks_passed=True,
    )


if __name__ == "__main__":
    print(verify_all())
