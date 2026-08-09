"""Complete quotient coordinates for two guards with rank-one hidden image.

Let the hidden score lattice be L=Z*h in Z^2 and write h=d*p with p primitive.
Choose Bezout integers u,v with u*p1+v*p2=1. The unimodular transform

    T = [[u, v], [-p2, p1]]

maps h to (d,0). Hence the quotient Z^2/L is represented exactly by

    torsion = (u*x1+v*x2) mod d,
    free    = -p2*x1+p1*x2.

For a coordinate partition, these quotient coordinates are independent of the
fine representative chosen inside one coarse fiber. They can be computed as an
integer-linear (plus modular) function of the coarse block totals.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .guard_branch_erasure import rank_one_reachable_patterns
from .guard_image_lattice import GuardFamily, guard_kernel_image_rank, guard_rank_one_step
from .linear_relation_quotient import Partition


@dataclass(frozen=True)
class TwoGuardQuotientBasis:
    hidden_step: tuple[int, int]
    primitive_direction: tuple[int, int]
    torsion_modulus: int
    bezout_row: tuple[int, int]
    free_row: tuple[int, int]


@dataclass(frozen=True)
class TwoGuardQuotientCoordinate:
    torsion_residue: int
    free_coordinate: int
    torsion_modulus: int


@dataclass(frozen=True)
class TwoGuardCoarseMap:
    basis: TwoGuardQuotientBasis
    torsion_coefficients: tuple[int, ...]
    torsion_bias: int
    free_coefficients: tuple[int, ...]
    free_bias: int


def _extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    old_r, r = abs(left), abs(right)
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    if old_r == 0:
        return 0, 0, 0
    return (
        old_r,
        old_s if left >= 0 else -old_s,
        old_t if right >= 0 else -old_t,
    )


def two_guard_quotient_basis(step: tuple[int, int]) -> TwoGuardQuotientBasis:
    """Construct an exact quotient basis for Z^2 / Z*step."""
    if not isinstance(step, tuple) or len(step) != 2:
        raise ValueError("step must be a 2D integer tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in step):
        raise ValueError("step entries must be integers")
    divisor = gcd(abs(step[0]), abs(step[1]))
    if divisor == 0:
        raise ValueError("step must be nonzero")
    primitive = (step[0] // divisor, step[1] // divisor)
    bezout_gcd, left, right = _extended_gcd(primitive[0], primitive[1])
    if bezout_gcd != 1:
        raise AssertionError("primitive direction must have gcd one")
    bezout = (left, right)
    free = (-primitive[1], primitive[0])
    if bezout[0] * primitive[0] + bezout[1] * primitive[1] != 1:
        raise AssertionError("Bezout row must pair to one with primitive direction")
    return TwoGuardQuotientBasis(
        hidden_step=step,
        primitive_direction=primitive,
        torsion_modulus=divisor,
        bezout_row=bezout,
        free_row=free,
    )


def two_guard_coset_coordinate(
    scores: tuple[int, int], step: tuple[int, int]
) -> TwoGuardQuotientCoordinate:
    """Complete invariant of one score vector modulo the hidden lattice Z*step."""
    if not isinstance(scores, tuple) or len(scores) != 2:
        raise ValueError("scores must be a 2D integer tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in scores):
        raise ValueError("scores must be integers")
    basis = two_guard_quotient_basis(step)
    torsion_raw = basis.bezout_row[0] * scores[0] + basis.bezout_row[1] * scores[1]
    free = basis.free_row[0] * scores[0] + basis.free_row[1] * scores[1]
    return TwoGuardQuotientCoordinate(
        torsion_residue=torsion_raw % basis.torsion_modulus,
        free_coordinate=free,
        torsion_modulus=basis.torsion_modulus,
    )


def two_guard_same_hidden_coset(
    left_scores: tuple[int, int],
    right_scores: tuple[int, int],
    step: tuple[int, int],
) -> bool:
    """Whether two score vectors differ by an integer multiple of the hidden step."""
    return two_guard_coset_coordinate(left_scores, step) == two_guard_coset_coordinate(
        right_scores, step
    )


def canonical_scores_from_two_guard_coordinate(
    coordinate: TwoGuardQuotientCoordinate,
    step: tuple[int, int],
) -> tuple[int, int]:
    """Choose one deterministic integer score representative of a quotient coordinate."""
    basis = two_guard_quotient_basis(step)
    if coordinate.torsion_modulus != basis.torsion_modulus:
        raise ValueError("coordinate torsion modulus does not match step")
    torsion = coordinate.torsion_residue % basis.torsion_modulus
    free = coordinate.free_coordinate
    # Inverse of [[u,v],[-p2,p1]] is [[p1,-v],[p2,u]].
    u, v = basis.bezout_row
    p1, p2 = basis.primitive_direction
    return (
        p1 * torsion - v * free,
        p2 * torsion + u * free,
    )


def two_guard_reachable_patterns_from_coordinate(
    coordinate: TwoGuardQuotientCoordinate,
    step: tuple[int, int],
) -> tuple[tuple[bool, bool], ...]:
    """Exact reachable binary patterns of one two-guard hidden coset."""
    base = canonical_scores_from_two_guard_coordinate(coordinate, step)
    return rank_one_reachable_patterns(base, step)


def two_guard_coarse_map(
    guards: GuardFamily,
    biases: tuple[int, int],
    partition: Partition,
) -> TwoGuardCoarseMap:
    """Symbolic map from coarse block totals to complete two-guard coset coordinates."""
    if len(guards) != 2:
        raise ValueError("exactly two guards are required")
    if not isinstance(biases, tuple) or len(biases) != 2:
        raise ValueError("biases must be a two-integer tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in biases):
        raise ValueError("biases must be integers")
    if guard_kernel_image_rank(guards, partition) != 1:
        raise ValueError("partition guard-image lattice must have rank one")
    step = guard_rank_one_step(guards, partition)
    if len(step) != 2:
        raise AssertionError("two guards must produce a two-dimensional score step")
    basis = two_guard_quotient_basis((step[0], step[1]))

    torsion_coefficients = []
    free_coefficients = []
    for group in partition:
        anchor = group[0]
        score_coefficients = (guards[0][anchor], guards[1][anchor])
        torsion_coefficients.append(
            (
                basis.bezout_row[0] * score_coefficients[0]
                + basis.bezout_row[1] * score_coefficients[1]
            )
            % basis.torsion_modulus
        )
        free_coefficients.append(
            basis.free_row[0] * score_coefficients[0]
            + basis.free_row[1] * score_coefficients[1]
        )

    torsion_bias = (
        basis.bezout_row[0] * biases[0]
        + basis.bezout_row[1] * biases[1]
    ) % basis.torsion_modulus
    free_bias = basis.free_row[0] * biases[0] + basis.free_row[1] * biases[1]
    return TwoGuardCoarseMap(
        basis=basis,
        torsion_coefficients=tuple(torsion_coefficients),
        torsion_bias=torsion_bias,
        free_coefficients=tuple(free_coefficients),
        free_bias=free_bias,
    )


def evaluate_two_guard_coarse_map(
    coarse_map: TwoGuardCoarseMap,
    coarse_totals: tuple[int, ...],
) -> TwoGuardQuotientCoordinate:
    """Evaluate the symbolic quotient coordinate on one coarse state."""
    if not isinstance(coarse_totals, tuple) or len(coarse_totals) != len(
        coarse_map.free_coefficients
    ):
        raise ValueError("coarse_totals must match the coarse block count")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in coarse_totals
    ):
        raise ValueError("coarse totals must be integers")
    modulus = coarse_map.basis.torsion_modulus
    torsion = (
        coarse_map.torsion_bias
        + sum(
            coefficient * total
            for coefficient, total in zip(
                coarse_map.torsion_coefficients, coarse_totals
            )
        )
    ) % modulus
    free = coarse_map.free_bias + sum(
        coefficient * total
        for coefficient, total in zip(coarse_map.free_coefficients, coarse_totals)
    )
    return TwoGuardQuotientCoordinate(
        torsion_residue=torsion,
        free_coordinate=free,
        torsion_modulus=modulus,
    )
