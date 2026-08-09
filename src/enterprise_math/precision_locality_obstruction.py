"""Exact finite Bell/CHSH obstruction for R004 latent-completion research.

The module is deliberately integer/rational-first.  It does not claim Bell or
CHSH mathematics as an Enterprise Math invention.  R004 uses the established
local-hidden-variable boundary to answer a narrower question left open by its
finite response-table no-go: once a pre-sampled table is required to be
setting-local and its seed distribution is independent of the chosen settings,
some finite rational correlation tables are impossible.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Mapping, Sequence

Setting = tuple[int, int]
ResponseTable = tuple[int, int, int, int]


def _sign(value: int, name: str = "outcome") -> None:
    if isinstance(value, bool) or value not in (-1, 1):
        raise ValueError(f"{name} must be -1 or 1")


def local_response_tables() -> tuple[ResponseTable, ...]:
    """All deterministic setting-local binary response tables.

    A table is ``(A_0,A_1,B_0,B_1)``.  Alice's response therefore depends only
    on her local setting and the already-selected table; Bob's response depends
    only on his local setting and the same table.
    """
    return tuple(product((-1, 1), repeat=4))


def deterministic_chsh(table: ResponseTable) -> int:
    if len(table) != 4:
        raise ValueError("response table must have four local outcomes")
    a0, a1, b0, b1 = table
    for value in table:
        _sign(value)
    return a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1


def weighted_local_chsh(weights: Sequence[int]) -> tuple[int, int]:
    """Return the exact CHSH numerator and common seed weight.

    The weight vector is aligned with ``local_response_tables()``.  The same
    weights are used for all four setting pairs, encoding measurement-setting
    independence of the latent seed distribution.  No division is needed for
    the Bell bound: every valid local mixture obeys ``abs(numerator)<=2*total``.
    """
    tables = local_response_tables()
    row = tuple(weights)
    if len(row) != len(tables):
        raise ValueError("one non-negative integer weight is required per table")
    if any(isinstance(weight, bool) or not isinstance(weight, int) or weight < 0 for weight in row):
        raise ValueError("weights must be non-negative integers")
    total = sum(row)
    if total <= 0:
        raise ValueError("at least one latent seed atom is required")
    numerator = sum(weight * deterministic_chsh(table) for weight, table in zip(row, tables))
    return numerator, total


def local_chsh_bound_holds(weights: Sequence[int]) -> bool:
    numerator, total = weighted_local_chsh(weights)
    return abs(numerator) <= 2 * total


def weighted_local_correlations(weights: Sequence[int]) -> dict[Setting, Fraction]:
    tables = local_response_tables()
    row = tuple(weights)
    numerator, total = weighted_local_chsh(row)
    del numerator
    correlations: dict[Setting, Fraction] = {}
    for x, y in product((0, 1), repeat=2):
        value = 0
        for weight, table in zip(row, tables):
            a0, a1, b0, b1 = table
            a = (a0, a1)[x]
            b = (b0, b1)[y]
            value += weight * a * b
        correlations[(x, y)] = Fraction(value, total)
    return correlations


def chsh_value(correlations: Mapping[Setting, Fraction]) -> Fraction:
    required = {(0, 0), (0, 1), (1, 0), (1, 1)}
    if set(correlations) != required:
        raise ValueError("exactly four CHSH setting correlations are required")
    if any(not isinstance(value, Fraction) for value in correlations.values()):
        raise ValueError("correlations must be exact Fractions")
    return (
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )


def _rational_unit_vector(x: int, y: int, denominator: int) -> tuple[int, int, int]:
    if isinstance(denominator, bool) or not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("denominator must be positive")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (x, y)):
        raise ValueError("vector coordinates must be integers")
    if x * x + y * y != denominator * denominator:
        raise ValueError("coordinates must form an exact rational unit vector")
    return x, y, denominator


def _dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> Fraction:
    lx, ly, ld = left
    rx, ry, rd = right
    return Fraction(lx * rx + ly * ry, ld * rd)


def rational_singlet_correlations() -> dict[Setting, Fraction]:
    """One exact rational CHSH-violating singlet correlation table.

    Alice uses directions ``(1,0)`` and ``(0,1)``.  Bob uses the Pythagorean
    directions ``(3/5,4/5)`` and ``(3/5,-4/5)``.  For the spin singlet the
    established quantum correlation is ``E(a,b)=-a dot b``.  All four values
    are therefore rational and the CHSH magnitude is exactly ``14/5``.
    """
    alice = (
        _rational_unit_vector(1, 0, 1),
        _rational_unit_vector(0, 1, 1),
    )
    bob = (
        _rational_unit_vector(3, 4, 5),
        _rational_unit_vector(3, -4, 5),
    )
    return {
        (x, y): -_dot(alice[x], bob[y])
        for x, y in product((0, 1), repeat=2)
    }


def rational_singlet_joint_counts() -> dict[Setting, dict[tuple[int, int], int]]:
    """Exact 20-atom joint counts for the rational singlet target.

    With unbiased binary singlet marginals,
    ``P(A=a,B=b|x,y)=(1+a*b*E_xy)/4``.  The selected rational directions make
    every probability an integer multiple of ``1/20``.
    """
    correlations = rational_singlet_correlations()
    output: dict[Setting, dict[tuple[int, int], int]] = {}
    for setting, correlation in correlations.items():
        counts: dict[tuple[int, int], int] = {}
        for a, b in product((-1, 1), repeat=2):
            probability = Fraction(1 + a * b * correlation, 4)
            count = probability * 20
            if count.denominator != 1:
                raise AssertionError("selected rational target must clear at denominator 20")
            counts[(a, b)] = count.numerator
        output[setting] = counts
    return output


def correlation_from_joint_counts(counts: Mapping[tuple[int, int], int]) -> Fraction:
    required = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
    if set(counts) != required:
        raise ValueError("all four binary joint outcomes are required")
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in counts.values()):
        raise ValueError("joint counts must be non-negative integers")
    total = sum(counts.values())
    if total <= 0:
        raise ValueError("joint table must be nonempty")
    numerator = sum(a * b * counts[(a, b)] for a, b in required)
    return Fraction(numerator, total)
