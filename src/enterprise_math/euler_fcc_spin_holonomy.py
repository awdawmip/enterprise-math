"""Exact FCC tetrahedral slice transport and Euler face holonomy.

The four close-packed slice normals form a regular tetrahedral frame. Their
pairwise cross products are the six oriented FCC line-family representatives.
This module checks, using exact rational arithmetic, that the minimal proper
rotation across a shared line transports one slice normal to the next and that
a triangular loop has tangent-plane holonomy ``-I``.

No floating point, trigonometric function, numerical value of pi, or continuous
circle is used in the finite algebraic core.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product
from typing import Mapping

Slice = str
Vec3 = tuple[Fraction, Fraction, Fraction]
Quaternion = tuple[Fraction, Fraction, Fraction, Fraction]
Matrix3 = tuple[Vec3, Vec3, Vec3]

SLICES: tuple[Slice, ...] = ("A", "B", "C", "D")
NORMALS: Mapping[Slice, Vec3] = {
    "A": (Fraction(-1), Fraction(1), Fraction(1)),
    "B": (Fraction(1), Fraction(-1), Fraction(1)),
    "C": (Fraction(1), Fraction(1), Fraction(-1)),
    "D": (Fraction(-1), Fraction(-1), Fraction(-1)),
}
BASIS: tuple[Vec3, ...] = (
    (Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
)

FCC_LINE_FAMILIES: Mapping[str, Vec3] = {
    "L1": (Fraction(1), Fraction(1), Fraction(0)),
    "L2": (Fraction(1), Fraction(-1), Fraction(0)),
    "L3": (Fraction(1), Fraction(0), Fraction(1)),
    "L4": (Fraction(1), Fraction(0), Fraction(-1)),
    "L5": (Fraction(0), Fraction(1), Fraction(1)),
    "L6": (Fraction(0), Fraction(1), Fraction(-1)),
}
PAIR_TO_LINE_FAMILY: Mapping[frozenset[Slice], str] = {
    frozenset(("A", "B")): "L1",
    frozenset(("A", "C")): "L3",
    frozenset(("A", "D")): "L6",
    frozenset(("B", "C")): "L5",
    frozenset(("B", "D")): "L4",
    frozenset(("C", "D")): "L2",
}


def _fraction(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("scalar must be an integer or Fraction")
    return Fraction(value)


def vec(x: int | Fraction, y: int | Fraction, z: int | Fraction) -> Vec3:
    return _fraction(x), _fraction(y), _fraction(z)


def add(left: Vec3, right: Vec3) -> Vec3:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(value: Vec3) -> Vec3:
    return tuple(-coordinate for coordinate in value)  # type: ignore[return-value]


def sub(left: Vec3, right: Vec3) -> Vec3:
    return add(left, neg(right))


def scale(scalar: int | Fraction, value: Vec3) -> Vec3:
    coefficient = _fraction(scalar)
    return tuple(coefficient * coordinate for coordinate in value)  # type: ignore[return-value]


def dot(left: Vec3, right: Vec3) -> Fraction:
    return sum(left[index] * right[index] for index in range(3))


def cross(left: Vec3, right: Vec3) -> Vec3:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def determinant(first: Vec3, second: Vec3, third: Vec3) -> Fraction:
    return dot(first, cross(second, third))


def _require_slice(name: Slice) -> None:
    if name not in NORMALS:
        raise ValueError(f"unknown slice label: {name!r}")


def _require_distinct(*labels: Slice) -> None:
    for label in labels:
        _require_slice(label)
    if len(set(labels)) != len(labels):
        raise ValueError("slice labels must be pairwise distinct")


def shared_line(source: Slice, target: Slice) -> Vec3:
    """Oriented shared-line representative ``(n_source x n_target)/2``."""

    _require_distinct(source, target)
    return scale(Fraction(1, 2), cross(NORMALS[source], NORMALS[target]))


def unoriented_line_family(source: Slice, target: Slice) -> str:
    _require_distinct(source, target)
    return PAIR_TO_LINE_FAMILY[frozenset((source, target))]


def agrees_up_to_sign(left: Vec3, right: Vec3) -> bool:
    return left == right or left == neg(right)


def outgoing_chart(source: Slice) -> tuple[Vec3, Vec3, Vec3]:
    """The three canonically oriented shared lines leaving one slice."""

    _require_slice(source)
    return tuple(shared_line(source, target) for target in SLICES if target != source)  # type: ignore[return-value]


def transition(source: Slice, target: Slice, value: Vec3) -> Vec3:
    """Exact minimal proper rotation across the shared line.

    If ``ell=(n_source x n_target)/2``, the unit spin rotor is formally
    ``(1+ell)/sqrt(3)``. Conjugation removes the square root and gives

        T(v) = (-v + 2 ell (ell dot v) + 2 ell x v) / 3.
    """

    ell = shared_line(source, target)
    return scale(
        Fraction(1, 3),
        add(add(neg(value), scale(2 * dot(ell, value), ell)), scale(2, cross(ell, value))),
    )


def half_turn_about_slice(slice_label: Slice, value: Vec3) -> Vec3:
    """Half-turn around the slice normal; it negates the slice plane."""

    _require_slice(slice_label)
    normal = NORMALS[slice_label]
    return sub(scale(Fraction(2, 3) * dot(normal, value), normal), value)


def face_transport(first: Slice, second: Slice, third: Slice, value: Vec3) -> Vec3:
    """Transport around ``first -> second -> third -> first``."""

    _require_distinct(first, second, third)
    return transition(
        third,
        first,
        transition(second, third, transition(first, second, value)),
    )


def quaternion_multiply(left: Quaternion, right: Quaternion) -> Quaternion:
    left_scalar, left_vector = left[0], left[1:]
    right_scalar, right_vector = right[0], right[1:]
    vector_part = add(
        add(scale(left_scalar, right_vector), scale(right_scalar, left_vector)),
        cross(left_vector, right_vector),
    )
    return left_scalar * right_scalar - dot(left_vector, right_vector), *vector_part


def quaternion_conjugate(value: Quaternion) -> Quaternion:
    return value[0], -value[1], -value[2], -value[3]


def quaternion_scale(scalar: int | Fraction, value: Quaternion) -> Quaternion:
    coefficient = _fraction(scalar)
    return tuple(coefficient * coordinate for coordinate in value)  # type: ignore[return-value]


def quaternion_norm_square(value: Quaternion) -> Fraction:
    return value[0] * value[0] + dot(value[1:], value[1:])


def pure(value: Vec3) -> Quaternion:
    return Fraction(0), *value


def transition_spin_numerator(source: Slice, target: Slice) -> Quaternion:
    """Numerator ``1+ell`` of the unit rotor ``(1+ell)/sqrt(3)``."""

    return Fraction(1), *shared_line(source, target)


def spin_conjugation_numerator(source: Slice, target: Slice) -> Quaternion:
    """Return ``(1+ell)n_source(1-ell)``, which equals ``3 n_target``."""

    numerator = transition_spin_numerator(source, target)
    return quaternion_multiply(
        numerator,
        quaternion_multiply(pure(NORMALS[source]), quaternion_conjugate(numerator)),
    )


def oriented_face_sign(first: Slice, second: Slice, third: Slice) -> int:
    """Orientation sign of one ordered tetrahedral face."""

    _require_distinct(first, second, third)
    value = determinant(NORMALS[first], NORMALS[second], NORMALS[third])
    if value not in (Fraction(-4), Fraction(4)):
        raise AssertionError("tetrahedral face determinant lost its +/-4 normalization")
    return 1 if value > 0 else -1


def face_spin_numerator(first: Slice, second: Slice, third: Slice) -> Quaternion:
    """Numerator of the three-transition spin holonomy."""

    _require_distinct(first, second, third)
    return quaternion_multiply(
        transition_spin_numerator(third, first),
        quaternion_multiply(
            transition_spin_numerator(second, third),
            transition_spin_numerator(first, second),
        ),
    )


def expected_face_spin_numerator(first: Slice, second: Slice, third: Slice) -> Quaternion:
    sign = oriented_face_sign(first, second, third)
    return quaternion_scale(3 * sign, pure(NORMALS[first]))


def tangent_complex_numerator(slice_label: Slice, value: Vec3) -> Vec3:
    """Unnormalized local complex structure ``n_slice x value``."""

    _require_slice(slice_label)
    return cross(NORMALS[slice_label], value)


def matrix_columns_of_transition(source: Slice, target: Slice) -> Matrix3:
    """Columns of the exact transition matrix in the standard carrier basis."""

    return tuple(transition(source, target, basis) for basis in BASIS)  # type: ignore[return-value]


def matrix_determinant_from_columns(columns: Matrix3) -> Fraction:
    return determinant(columns[0], columns[1], columns[2])


def scalar_orientation_flattening_exists() -> bool:
    """Whether vertex sign gauges can make all shared-line orientations agree."""

    for choices in product((-1, 1), repeat=4):
        gauge = dict(zip(SLICES, choices, strict=True))
        if all(
            scale(gauge[source], shared_line(source, target))
            == scale(gauge[target], shared_line(target, source))
            for source, target in combinations(SLICES, 2)
        ):
            return True
    return False


def spherical_face_area_fraction_of_full_sphere() -> Fraction:
    """The four congruent tetrahedral normal faces partition the sphere."""

    return Fraction(1, 4)


def exact_certificate() -> dict[str, object]:
    """Run the complete exact finite certificate and return a summary."""

    for label in SLICES:
        normal = NORMALS[label]
        if dot(normal, normal) != 3:
            raise AssertionError("slice normal does not have square norm three")

    for source, target in permutations(SLICES, 2):
        if dot(NORMALS[source], NORMALS[target]) != -1:
            raise AssertionError("slice normals are not tetrahedrally equiangular")
        ell = shared_line(source, target)
        if dot(ell, ell) != 2 or shared_line(target, source) != neg(ell):
            raise AssertionError("shared line normalization failed")
        family = FCC_LINE_FAMILIES[unoriented_line_family(source, target)]
        if not agrees_up_to_sign(ell, family):
            raise AssertionError("cross-normal line does not match the FCC family")
        if quaternion_norm_square(transition_spin_numerator(source, target)) != 3:
            raise AssertionError("transition spin numerator does not have norm square three")
        if spin_conjugation_numerator(source, target) != quaternion_scale(
            3, pure(NORMALS[target])
        ):
            raise AssertionError("spin transition does not transport the slice normal")
        if transition(source, target, NORMALS[source]) != NORMALS[target]:
            raise AssertionError("transition does not map source normal to target normal")
        if transition(source, target, ell) != ell:
            raise AssertionError("transition does not fix the shared line")
        columns = matrix_columns_of_transition(source, target)
        if matrix_determinant_from_columns(columns) != 1:
            raise AssertionError("transition is not a proper rotation")
        for left_index, left_basis in enumerate(BASIS):
            for right_index, right_basis in enumerate(BASIS):
                expected_dot = Fraction(1 if left_index == right_index else 0)
                if dot(
                    transition(source, target, left_basis),
                    transition(source, target, right_basis),
                ) != expected_dot:
                    raise AssertionError("transition does not preserve the carrier dot form")
                if transition(
                    target,
                    source,
                    transition(source, target, left_basis),
                ) != left_basis:
                    raise AssertionError("reverse transition is not the inverse")
        for basis in BASIS:
            left = transition(
                source, target, tangent_complex_numerator(source, basis)
            )
            right = tangent_complex_numerator(
                target, transition(source, target, basis)
            )
            if left != right:
                raise AssertionError("local complex structures do not intertwine")

    for source in SLICES:
        chart = outgoing_chart(source)
        if add(add(chart[0], chart[1]), chart[2]) != vec(0, 0, 0):
            raise AssertionError("outgoing chart directions do not sum to zero")
        if any(dot(direction, direction) != 2 for direction in chart):
            raise AssertionError("outgoing chart directions do not have equal norm")
        if any(dot(left, right) != -1 for left, right in combinations(chart, 2)):
            raise AssertionError("outgoing chart directions are not pairwise 120-degree")

    for first, second, third in permutations(SLICES, 3):
        if face_spin_numerator(first, second, third) != expected_face_spin_numerator(
            first, second, third
        ):
            raise AssertionError("spin face product is not +/- the local complex normal")
        face_numerator = face_spin_numerator(first, second, third)
        if quaternion_multiply(face_numerator, face_numerator) != (
            Fraction(-27),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ):
            raise AssertionError("normalized face spin holonomy does not square to -1")
        for basis in BASIS:
            if face_transport(first, second, third, basis) != half_turn_about_slice(
                first, basis
            ):
                raise AssertionError("face transport is not the tangent half-turn")

    if scalar_orientation_flattening_exists():
        raise AssertionError("a forbidden scalar orientation flattening was found")

    return {
        "slices": len(SLICES),
        "ordered_transitions": len(tuple(permutations(SLICES, 2))),
        "ordered_triangular_loops": len(tuple(permutations(SLICES, 3))),
        "unoriented_line_families": len(FCC_LINE_FAMILIES),
        "scalar_orientation_flattening_exists": False,
        "face_vector_holonomy": "half-turn about starting slice normal",
        "face_spin_holonomy": "+/- normalized slice normal",
        "spin_holonomy_square": -1,
        "spherical_face_fraction": spherical_face_area_fraction_of_full_sphere(),
        "status": "PASS",
    }
