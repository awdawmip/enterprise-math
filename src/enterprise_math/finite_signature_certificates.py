"""Exact finite certificate verifiers for operational-signature separation.

This module does not solve a linear program or select a causal/physical axiom.
It verifies certificates that arise after a finite model/experiment language has
already been declared:

* Boolean join certificates for possibilistic support completion;
* rational convex-mixture certificates when shared randomization is admissible;
* rational affine separating witnesses for exclusion from a finite convex hull;
* denominator-free integer-cone witnesses used by historical R004 examples.

All of these are standard finite Boolean/linear/convex constructions.  The
Enterprise Math use is the FQ-004/FQ-007 routing from an operational signature
to explicit completion or separation evidence.
"""

from __future__ import annotations

from collections.abc import Sequence
from fractions import Fraction


Rational = int | Fraction
RationalWord = tuple[Fraction, ...]
IntegerWord = tuple[int, ...]
BooleanWord = tuple[bool, ...]


def _rational(value: Rational) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError("rational certificate coordinates must be int or Fraction")
    return Fraction(value)


def _rational_word(values: Sequence[Rational]) -> RationalWord:
    word = tuple(_rational(value) for value in values)
    if not word:
        raise ValueError("certificate words must have nonzero width")
    return word


def rational_dot(functional: Sequence[Rational], state: Sequence[Rational]) -> Fraction:
    """Exact rational dot product with strict width/type validation."""
    coefficients = _rational_word(functional)
    values = _rational_word(state)
    if len(coefficients) != len(values):
        raise ValueError("functional and state must have the same nonzero width")
    return sum(
        (coefficient * value for coefficient, value in zip(coefficients, values, strict=True)),
        start=Fraction(0),
    )


def integer_dot(functional: Sequence[int], state: Sequence[int]) -> int:
    """Exact integer dot product used by denominator-cleared certificates."""
    coefficients = tuple(functional)
    values = tuple(state)
    if not coefficients or len(coefficients) != len(values):
        raise ValueError("functional and state must have the same nonzero width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in coefficients + values
    ):
        raise ValueError("integer certificate words require integers")
    return sum(
        coefficient * value
        for coefficient, value in zip(coefficients, values, strict=True)
    )


def nonnegative_integer_combination(
    generators: Sequence[Sequence[int]], weights: Sequence[int]
) -> IntegerWord:
    """Return a non-negative integer combination of fixed-width generators."""
    atoms = tuple(tuple(generator) for generator in generators)
    row = tuple(weights)
    if not atoms or len(atoms) != len(row):
        raise ValueError("one weight is required per nonempty generator family")
    width = len(atoms[0])
    if width == 0 or any(len(atom) != width for atom in atoms):
        raise ValueError("generators must have common nonzero width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for atom in atoms
        for value in atom
    ):
        raise ValueError("integer certificate words require integers")
    if any(
        isinstance(weight, bool) or not isinstance(weight, int) or weight < 0
        for weight in row
    ):
        raise ValueError("generator weights must be non-negative integers")
    return tuple(
        sum(weight * atom[index] for weight, atom in zip(row, atoms, strict=True))
        for index in range(width)
    )


def integer_cone_separation_certificate_holds(
    generators: Sequence[Sequence[int]],
    target: Sequence[int],
    functional: Sequence[int],
) -> bool:
    """Check h(g)<=0 for all generators while h(target)>0."""
    atoms = tuple(tuple(generator) for generator in generators)
    if not atoms:
        raise ValueError("at least one generator is required")
    target_word = tuple(target)
    coefficients = tuple(functional)
    width = len(target_word)
    if width == 0 or len(coefficients) != width or any(
        len(atom) != width for atom in atoms
    ):
        raise ValueError("all cone words must have common nonzero width")
    return all(integer_dot(coefficients, atom) <= 0 for atom in atoms) and (
        integer_dot(coefficients, target_word) > 0
    )


def boolean_join(words: Sequence[Sequence[bool]]) -> BooleanWord:
    """Coordinatewise OR of a nonempty family of Boolean signatures."""
    atoms = tuple(tuple(word) for word in words)
    if not atoms:
        raise ValueError("at least one Boolean word is required")
    width = len(atoms[0])
    if width == 0 or any(len(atom) != width for atom in atoms):
        raise ValueError("Boolean words must have common nonzero width")
    if any(type(value) is not bool for atom in atoms for value in atom):
        raise ValueError("Boolean support coordinates must be bool")
    return tuple(any(atom[index] for atom in atoms) for index in range(width))


def boolean_join_certificate_holds(
    generators: Sequence[Sequence[bool]],
    selected_indices: Sequence[int],
    target: Sequence[bool],
) -> bool:
    """Verify that selected deterministic support signatures join to target."""
    atoms = tuple(tuple(generator) for generator in generators)
    if not atoms:
        raise ValueError("at least one generator is required")
    indices = tuple(selected_indices)
    if not indices:
        raise ValueError("a completion certificate must select at least one generator")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= len(atoms)
        for index in indices
    ):
        raise ValueError("selected generator index is out of range")
    target_word = tuple(target)
    if any(type(value) is not bool for value in target_word):
        raise ValueError("Boolean support coordinates must be bool")
    selected = tuple(atoms[index] for index in indices)
    if any(len(atom) != len(target_word) for atom in atoms) or not target_word:
        raise ValueError("generators and target must have common nonzero width")
    return boolean_join(selected) == target_word


def rational_convex_combination(
    vertices: Sequence[Sequence[Rational]], weights: Sequence[Rational]
) -> RationalWord:
    """Return an exact rational convex combination after certificate validation."""
    points = tuple(_rational_word(vertex) for vertex in vertices)
    row = tuple(_rational(weight) for weight in weights)
    if not points or len(points) != len(row):
        raise ValueError("one weight is required per nonempty vertex family")
    width = len(points[0])
    if any(len(point) != width for point in points):
        raise ValueError("vertices must have common nonzero width")
    if any(weight < 0 for weight in row):
        raise ValueError("convex weights must be non-negative")
    if sum(row, start=Fraction(0)) != 1:
        raise ValueError("convex weights must sum exactly to one")
    return tuple(
        sum(
            (weight * point[index] for weight, point in zip(row, points, strict=True)),
            start=Fraction(0),
        )
        for index in range(width)
    )


def convex_membership_certificate_holds(
    vertices: Sequence[Sequence[Rational]],
    target: Sequence[Rational],
    weights: Sequence[Rational],
) -> bool:
    """Verify exact membership of target in the declared finite convex hull."""
    target_word = _rational_word(target)
    combination = rational_convex_combination(vertices, weights)
    if len(combination) != len(target_word):
        raise ValueError("vertices and target must have common nonzero width")
    return combination == target_word


def affine_separation_certificate_holds(
    vertices: Sequence[Sequence[Rational]],
    target: Sequence[Rational],
    functional: Sequence[Rational],
    threshold: Rational,
) -> bool:
    """Verify c·v <= beta for every vertex and c·target > beta exactly.

    When arbitrary convex mixing of the declared vertices is admissible, this
    certificate separates the target from the whole finite convex hull.
    """
    points = tuple(_rational_word(vertex) for vertex in vertices)
    if not points:
        raise ValueError("at least one vertex is required")
    target_word = _rational_word(target)
    coefficients = _rational_word(functional)
    beta = _rational(threshold)
    width = len(target_word)
    if len(coefficients) != width or any(len(point) != width for point in points):
        raise ValueError("vertices, target, and functional must have common width")
    return all(rational_dot(coefficients, point) <= beta for point in points) and (
        rational_dot(coefficients, target_word) > beta
    )
