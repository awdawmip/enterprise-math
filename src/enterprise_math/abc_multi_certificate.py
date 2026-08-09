"""Multi-certificate linear image calculus on the P025 block-value lattice.

Once a future language depends on a fine arithmetic witness only through block
derivative values ``(u,v,u+v)``, every additional integer-linear certificate is
a row ``(r,s)`` acting on ``(u,v)``.  The compressed relation lattice has rank
at most two, so the joint certificate image of *any number* of such observables
has rank at most two.

This module records exact labelled generator columns and the standard Smith /
determinantal invariant factors of the resulting ``q x 2`` integer matrix.  It
also keeps an explicit negative boundary: invariant factors classify the
abstract image module up to unimodular coordinate changes but do not determine
the labelled certificate image required by a labelled future language.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_block_floor_line import block_value_lattice_basis
from .abc_support import abc_support_state


CertificateRow = tuple[int, int]


@dataclass(frozen=True)
class MultiCertificateImage:
    abc: tuple[int, int, int]
    certificate_rows: tuple[CertificateRow, ...]
    lattice_basis: tuple[tuple[int, int], ...]
    generator_columns: tuple[tuple[int, ...], ...]
    rational_rank: int
    invariant_factors: tuple[int, ...]


def _validate_certificate_rows(rows: tuple[CertificateRow, ...]) -> None:
    for row in rows:
        if len(row) != 2:
            raise ValueError("each certificate row must have two integer coefficients")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("certificate coefficients must be integers")


def certificate_vector(
    rows: tuple[CertificateRow, ...], u: int, v: int
) -> tuple[int, ...]:
    """Evaluate all labelled linear certificate observables on one block state."""
    _validate_certificate_rows(rows)
    if isinstance(u, bool) or not isinstance(u, int):
        raise ValueError("u must be an integer")
    if isinstance(v, bool) or not isinstance(v, int):
        raise ValueError("v must be an integer")
    return tuple(r * u + s * v for r, s in rows)


def _content(values: tuple[int, ...]) -> int:
    result = 0
    for value in values:
        result = gcd(result, abs(value))
    return result


def _matrix_rank_and_invariants(
    columns: tuple[tuple[int, ...], ...]
) -> tuple[int, tuple[int, ...]]:
    """Return rational rank and nonzero Smith invariant factors for <=2 columns."""
    if not columns:
        return 0, ()
    if len(columns) > 2:
        raise ValueError("compressed relation lattice has at most two basis columns")
    entries = tuple(value for column in columns for value in column)
    d1 = _content(entries)
    if d1 == 0:
        return 0, ()
    if len(columns) == 1:
        return 1, (d1,)

    left, right = columns
    if len(left) != len(right):
        raise ValueError("certificate image columns must have equal labelled dimension")
    minors = tuple(
        left[i] * right[j] - left[j] * right[i]
        for i in range(len(left))
        for j in range(i + 1, len(left))
    )
    delta2 = _content(minors)
    if delta2 == 0:
        return 1, (d1,)
    if delta2 % d1:
        raise AssertionError("Smith determinantal divisors lost divisibility")
    return 2, (d1, delta2 // d1)


def multi_certificate_image(
    a: int,
    b: int,
    c: int,
    rows: tuple[CertificateRow, ...],
) -> MultiCertificateImage:
    """Return labelled image generators and abstract Smith invariants."""
    abc_support_state(a, b, c)
    _validate_certificate_rows(rows)
    basis = block_value_lattice_basis(a, b, c)
    columns = tuple(certificate_vector(rows, *point) for point in basis)
    rank, invariants = _matrix_rank_and_invariants(columns)
    return MultiCertificateImage(
        abc=(a, b, c),
        certificate_rows=rows,
        lattice_basis=basis,
        generator_columns=columns,
        rational_rank=rank,
        invariant_factors=invariants,
    )


def full_rank_certificate_rows_are_block_value_injective(
    a: int,
    b: int,
    c: int,
    rows: tuple[CertificateRow, ...],
) -> bool:
    """Return whether the labelled certificate vector is injective on Lambda_abc.

    A rational rank-two linear map on the ambient ``Q^2`` is injective, hence
    its restriction to any integer sublattice is injective.  Rank below two is
    non-injective on every rank-two compressed lattice.  Rank-one unit-relation
    lattices are treated by the actual image rank of their single basis column.
    """
    image = multi_certificate_image(a, b, c, rows)
    lattice_rank = len(image.lattice_basis)
    return image.rational_rank == lattice_rank


def recover_block_value_from_two_independent_rows(
    rows: tuple[CertificateRow, CertificateRow],
    values: tuple[int, int],
) -> tuple[Fraction, Fraction]:
    """Recover ``(u,v)`` over Q from two independent labelled certificate rows."""
    _validate_certificate_rows(rows)
    if len(values) != 2:
        raise ValueError("need exactly two certificate values")
    (r1, s1), (r2, s2) = rows
    determinant = r1 * s2 - r2 * s1
    if determinant == 0:
        raise ValueError("certificate rows are rationally dependent")
    y1, y2 = values
    u = Fraction(y1 * s2 - y2 * s1, determinant)
    v = Fraction(r1 * y2 - r2 * y1, determinant)
    return u, v


def labelled_image_membership_by_small_coefficients(
    image: MultiCertificateImage,
    target: tuple[int, ...],
    coefficient_bound: int = 20,
) -> bool:
    """Small exact oracle for labelled-image counterexamples/regressions."""
    if len(target) != len(image.certificate_rows):
        raise ValueError("target dimension must match certificate labels")
    if isinstance(coefficient_bound, bool) or not isinstance(coefficient_bound, int) or coefficient_bound < 0:
        raise ValueError("coefficient_bound must be a non-negative integer")
    columns = image.generator_columns
    if not columns:
        return all(value == 0 for value in target)
    if len(columns) == 1:
        column = columns[0]
        return any(
            tuple(k * value for value in column) == target
            for k in range(-coefficient_bound, coefficient_bound + 1)
        )
    first, second = columns
    for x in range(-coefficient_bound, coefficient_bound + 1):
        for y in range(-coefficient_bound, coefficient_bound + 1):
            if tuple(
                x * a + y * b for a, b in zip(first, second, strict=True)
            ) == target:
                return True
    return False


def same_smith_different_labelled_image_counterexample() -> dict[str, object]:
    """Show Smith invariant factors do not determine labelled certificate images."""
    # Use the full prime triple so Lambda=Z^2.  These two certificate matrices
    # have Smith invariants (1,2), but impose different parity constraints in
    # the fixed labelled output coordinates.
    triple = (2, 3, 5)
    first_rows = ((1, 0), (0, 2))
    second_rows = ((1, 0), (1, 2))
    first = multi_certificate_image(*triple, first_rows)
    second = multi_certificate_image(*triple, second_rows)
    if first.invariant_factors != (1, 2) or second.invariant_factors != (1, 2):
        raise AssertionError("counterexample lost equal Smith invariants")
    witness_target = (1, 0)
    first_contains = labelled_image_membership_by_small_coefficients(first, witness_target)
    second_contains = labelled_image_membership_by_small_coefficients(second, witness_target)
    if not first_contains or second_contains:
        raise AssertionError("counterexample lost distinct labelled image membership")
    return {
        "triple": triple,
        "first_rows": first_rows,
        "second_rows": second_rows,
        "invariant_factors": (1, 2),
        "distinguishing_target": witness_target,
        "membership": (first_contains, second_contains),
    }
