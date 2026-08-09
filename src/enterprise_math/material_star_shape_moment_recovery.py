"""Exact adaptive-moment encoding of an unlabeled star response partition.

The parent E001 owner shows that no fixed finite number of low-order power sums
can universally replace the exact response histogram as branching complexity
grows.  This module records the complementary positive result.

Let one identity-free response shape have ``ell`` positive integer parts
``x_1,...,x_ell`` and define power sums

    p_k = sum_i x_i^k,     k=1,...,ell.

Newton's identities recover the elementary symmetric functions exactly:

    k e_k = sum_{i=1}^k (-1)^(i-1) e_{k-i} p_i,
    e_0=1.

Therefore ``p_1,...,p_ell`` determine the monic integer polynomial

    prod_i (X-x_i)

and hence the complete response multiset, including multiplicities.  The
reference implementation uses only exact integer arithmetic and reconstructs
positive integer roots by repeated synthetic division.

Consequences for precision:

* a fixed moment order ``d`` is not a universal exact shape state;
* an adaptive moment horizon equal to active-part count ``ell`` is always
  sufficient;
* inside one fixed star residue shell the total ``p_1=R`` is already known from
  the shell, so an exact shell-local signature may omit ``p_1`` and retain only
  ``ell`` together with ``p_2,...,p_ell``.

This is an E001/P024 finite-state encoding statement.  Newton identities and
power-sum reconstruction are standard mathematics; no generic moment-problem
novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_star_shape_observables import response_shape_histogram


def _require_shape(shape: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = tuple(shape)
    if not values:
        raise ValueError("response shape must be nonempty")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in values
    ):
        raise ValueError("response-shape parts must be positive integers")
    if tuple(sorted(values, reverse=True)) != values:
        raise ValueError("response shape must be sorted in non-increasing order")
    return values


def adaptive_shape_power_sums(
    shape: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Return exactly the first ``ell`` power sums for an ``ell``-part shape."""
    values = _require_shape(shape)
    return tuple(
        sum(value**power for value in values)
        for power in range(1, len(values) + 1)
    )


def elementary_symmetric_from_power_sums(
    power_sums: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Recover ``(e_0,...,e_ell)`` exactly via Newton identities."""
    powers = tuple(power_sums)
    if not powers:
        raise ValueError("at least one power sum is required")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in powers
    ):
        raise ValueError("power sums must be positive integers")

    elementary = [1]
    for degree in range(1, len(powers) + 1):
        numerator = 0
        for index in range(1, degree + 1):
            sign = 1 if (index - 1) % 2 == 0 else -1
            numerator += (
                sign
                * elementary[degree - index]
                * powers[index - 1]
            )
        if numerator % degree:
            raise ValueError("power sums do not define integral Newton coefficients")
        coefficient = numerator // degree
        if coefficient <= 0:
            raise ValueError("power sums do not describe a positive-part multiset")
        elementary.append(coefficient)
    return tuple(elementary)


def monic_polynomial_from_power_sums(
    power_sums: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Return descending coefficients of ``prod_i (X-x_i)``."""
    elementary = elementary_symmetric_from_power_sums(power_sums)
    return tuple(
        [1]
        + [
            (-1 if degree % 2 else 1) * elementary[degree]
            for degree in range(1, len(elementary))
        ]
    )


def _evaluate_polynomial(coefficients: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in coefficients:
        result = result * value + coefficient
    return result


def _divide_by_integer_root(
    coefficients: tuple[int, ...],
    root: int,
) -> tuple[int, ...]:
    if len(coefficients) <= 1:
        raise ValueError("constant polynomial has no root factor to remove")
    quotient = [coefficients[0]]
    for coefficient in coefficients[1:-1]:
        quotient.append(coefficient + quotient[-1] * root)
    remainder = coefficients[-1] + quotient[-1] * root
    if remainder != 0:
        raise ValueError("requested value is not an exact polynomial root")
    return tuple(quotient)


def recover_shape_from_adaptive_power_sums(
    power_sums: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Recover the exact positive integer response partition from ``ell`` moments."""
    powers = tuple(power_sums)
    coefficients = monic_polynomial_from_power_sums(powers)
    expected_parts = len(powers)
    # p_1 is the exact total response, hence every positive integer root is in
    # ``1..p_1``.  Repeated synthetic division preserves multiplicity exactly.
    recovered: list[int] = []
    for candidate in range(1, powers[0] + 1):
        while len(coefficients) > 1 and _evaluate_polynomial(
            coefficients, candidate
        ) == 0:
            recovered.append(candidate)
            coefficients = _divide_by_integer_root(coefficients, candidate)
    if len(recovered) != expected_parts or coefficients != (1,):
        raise ValueError("power sums do not reconstruct a positive integer partition")
    return tuple(sorted(recovered, reverse=True))


@dataclass(frozen=True)
class AdaptiveMomentShapeSignature:
    active_count: int
    power_sums: tuple[int, ...]
    exact_histogram: tuple[tuple[int, int], ...]


def adaptive_moment_shape_signature(
    shape: tuple[int, ...] | list[int],
) -> AdaptiveMomentShapeSignature:
    """Return one exact adaptive-moment certificate for the response shape."""
    values = _require_shape(shape)
    powers = adaptive_shape_power_sums(values)
    recovered = recover_shape_from_adaptive_power_sums(powers)
    if recovered != values:
        raise AssertionError("adaptive moment signature failed exact reconstruction")
    return AdaptiveMomentShapeSignature(
        active_count=len(values),
        power_sums=powers,
        exact_histogram=response_shape_histogram(values),
    )


def fixed_shell_adaptive_moment_signature(
    shape: tuple[int, ...] | list[int],
    residue_total: int,
) -> tuple[int, tuple[int, ...]]:
    """Omit ``p_1`` when the star residue shell already declares the total.

    Returns ``(ell, (p_2,...,p_ell))``.  For ``ell=1`` the second component is
    empty; the single part is already fixed by ``residue_total``.
    """
    values = _require_shape(shape)
    if (
        isinstance(residue_total, bool)
        or not isinstance(residue_total, int)
        or residue_total <= 0
    ):
        raise ValueError("residue_total must be a positive integer")
    if sum(values) != residue_total:
        raise ValueError("response shape does not belong to the declared residue shell")
    powers = adaptive_shape_power_sums(values)
    return len(values), powers[1:]
