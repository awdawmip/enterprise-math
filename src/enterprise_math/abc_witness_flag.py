"""Canonical finite signatures for relation-conditioned abc witness flags.

For a fixed prime-labelled coordinate set, the additive witness lattice is the
integer kernel of a primitive row ``alpha``.  Wronskian degeneracy cuts that
lattice by a second row ``beta``.  The second row is not itself canonical:
``beta`` and ``lambda*beta + mu*alpha`` define the same rational hyperplane on
``ker(alpha)`` whenever ``lambda`` is nonzero.

The exterior product ``alpha wedge beta`` removes exactly this shear ambiguity,
up to overall nonzero scaling.  Primitive sign-normalized Pluecker coordinates
therefore give a compact exact signature of the rank-two row space and hence of
the saturated lattice flag.

This is elementary exterior/rational linear algebra.  P025 uses it as a state
representation; it is not claimed as a new exterior-algebra theorem.
"""

from __future__ import annotations

from math import gcd

from .abc_witness_precision import (
    additive_relation_vector,
    witness_coordinates,
    wronskian_relation_vector,
)


def _primitive_projective(entries: tuple[int, ...]) -> tuple[int, ...]:
    """Return the primitive sign-normalized representative of an integer ray."""
    if not entries or all(entry == 0 for entry in entries):
        raise ValueError("projective vector must be nonempty and nonzero")
    content = 0
    for entry in entries:
        content = gcd(content, abs(entry))
    normalized = tuple(entry // content for entry in entries)
    first_nonzero = next(entry for entry in normalized if entry != 0)
    if first_nonzero < 0:
        normalized = tuple(-entry for entry in normalized)
    return normalized


def exterior_two_form(
    first: tuple[int, ...], second: tuple[int, ...]
) -> tuple[int, ...]:
    """Return pair-indexed coordinates of ``first wedge second``.

    Coordinates are ordered lexicographically by index pairs ``i<j``.
    """
    if len(first) != len(second):
        raise ValueError("vectors must have the same dimension")
    if len(first) < 2:
        raise ValueError("exterior two-form requires dimension at least two")
    return tuple(
        first[i] * second[j] - first[j] * second[i]
        for i in range(len(first))
        for j in range(i + 1, len(first))
    )


def primitive_flag_two_form(
    additive_normal: tuple[int, ...], degeneracy_normal: tuple[int, ...]
) -> tuple[int, ...]:
    """Return the canonical projective two-form of a non-degenerate row pair."""
    return _primitive_projective(
        exterior_two_form(additive_normal, degeneracy_normal)
    )


def witness_flag_signature(a: int, b: int, c: int) -> dict[str, object]:
    """Return the canonical labelled signature of the saturated witness flag."""
    coordinates = witness_coordinates(a, b, c)
    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    two_form = primitive_flag_two_form(alpha, beta)
    return {
        "coordinates": coordinates,
        "additive_normal": alpha,
        "flag_two_form": two_form,
    }


def same_saturated_flag(
    alpha_left: tuple[int, ...],
    beta_left: tuple[int, ...],
    alpha_right: tuple[int, ...],
    beta_right: tuple[int, ...],
) -> bool:
    """Compare canonical rational/saturated flags in one labelled ambient lattice.

    The first primitive row must define the same additive hyperplane and the
    primitive exterior two-form must define the same rank-two row space.  These
    two conditions are equivalent to equality of the nested rational subspaces

        ker(alpha) superset ker(alpha) intersect ker(beta),

    and therefore equality of their intersections with the ambient integer
    lattice.  Coordinate labels and the inherited L-infinity norm are external
    to this helper and must be the same on both sides.
    """
    if not (
        len(alpha_left)
        == len(beta_left)
        == len(alpha_right)
        == len(beta_right)
    ):
        raise ValueError("all rows must have the same dimension")
    return (
        _primitive_projective(alpha_left)
        == _primitive_projective(alpha_right)
        and primitive_flag_two_form(alpha_left, beta_left)
        == primitive_flag_two_form(alpha_right, beta_right)
    )


def shear_degeneracy_normal(
    alpha: tuple[int, ...], beta: tuple[int, ...], scale: int, shear: int
) -> tuple[int, ...]:
    """Return ``scale*beta + shear*alpha`` for invariance regression tests."""
    if len(alpha) != len(beta):
        raise ValueError("rows must have the same dimension")
    if isinstance(scale, bool) or not isinstance(scale, int) or scale == 0:
        raise ValueError("scale must be a nonzero integer")
    if isinstance(shear, bool) or not isinstance(shear, int):
        raise ValueError("shear must be an integer")
    return tuple(scale * b + shear * a for a, b in zip(alpha, beta, strict=True))
