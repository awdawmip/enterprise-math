"""Finite exact certificate for low-order collision identifiability.

For a selected-layer Barlow observation with observed segment multiplicities
``t_l`` and hidden tail ``u``, ordered equal-observation moments factor as

    M2 = 4^u * product_l A_l^t_l,
    A_l = C(2l,l),

    M3 = 8^u * product_l F_l^t_l,
    F_l = sum_j C(l,j)^3.

This module proves a bounded but *exact* theorem: for observed segment lengths
at most 50, the pair ``(M2,M3)`` uniquely determines all ``t_1,...,t_50`` and
``u``.  The proof is a 51x51 p-adic valuation matrix with nonzero determinant
modulo the prime 1,000,003.

Because P011 gives finite Stirling transforms between moments and collision
coefficients, the truncated collision state ``(J1,J2,J3)`` is therefore enough
to identify the same bounded checkpoint geometry.

The certificate is deliberately finite.  No global theorem for arbitrary
segment length is claimed.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb

MAX_CERTIFIED_SEGMENT = 50
CERTIFICATE_MODULUS = 1_000_003
CERTIFICATE_DETERMINANT_RESIDUE = 22

# Rows selected from the full p-adic valuation surface.  ``A`` rows inspect
# v_p(C(2l,l)); ``F3`` rows inspect v_p(sum_j C(l,j)^3).
CERTIFICATE_ROWS: tuple[tuple[str, int], ...] = (
    ("A", 2), ("A", 3), ("A", 5), ("A", 7), ("A", 11),
    ("A", 13), ("A", 17), ("A", 19), ("A", 23), ("A", 29),
    ("A", 31), ("A", 37), ("A", 41), ("A", 43), ("A", 47),
    ("A", 53), ("A", 59), ("A", 61), ("A", 67), ("A", 71),
    ("A", 73), ("A", 79), ("A", 83), ("A", 89), ("A", 97),
    ("F3", 2), ("F3", 5), ("F3", 7), ("F3", 13), ("F3", 23),
    ("F3", 29), ("F3", 31), ("F3", 37), ("F3", 41), ("F3", 47),
    ("F3", 53), ("F3", 59), ("F3", 61), ("F3", 67), ("F3", 71),
    ("F3", 73), ("F3", 79), ("F3", 101), ("F3", 109), ("F3", 131),
    ("F3", 151), ("F3", 157), ("F3", 173), ("F3", 389),
    ("F3", 421), ("F3", 563),
)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def p_adic_valuation(value: int, prime: int) -> int:
    """Exact exponent v_p(value), using only repeated integer division."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be a positive integer")
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


@lru_cache(maxsize=None)
def pair_moment_factor(segment_length: int) -> int:
    """One-segment M2 factor ``A_l=C(2l,l)``."""
    if (
        isinstance(segment_length, bool)
        or not isinstance(segment_length, int)
        or segment_length <= 0
    ):
        raise ValueError("segment_length must be positive")
    return comb(2 * segment_length, segment_length)


@lru_cache(maxsize=None)
def triple_moment_factor(segment_length: int) -> int:
    """One-segment M3 / Franel factor ``F_l=sum_j C(l,j)^3``."""
    if (
        isinstance(segment_length, bool)
        or not isinstance(segment_length, int)
        or segment_length <= 0
    ):
        raise ValueError("segment_length must be positive")
    return sum(
        comb(segment_length, index) ** 3
        for index in range(segment_length + 1)
    )


def selected_moment_pair(
    segments: tuple[int, ...], hidden_tail: int = 0
) -> tuple[int, int]:
    """Return exact ``(M2,M3)`` of one selected-layer geometry."""
    if not isinstance(segments, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in segments
    ):
        raise ValueError("segments must be a tuple of positive integers")
    _require_natural("hidden_tail", hidden_tail)
    pair = 4**hidden_tail
    triple = 8**hidden_tail
    for segment in segments:
        pair *= pair_moment_factor(segment)
        triple *= triple_moment_factor(segment)
    return pair, triple


def first_three_collision_coefficients_from_moments(
    domain_size: int, pair_moment: int, triple_moment: int
) -> tuple[int, int, int]:
    """Convert ``(M1,M2,M3)`` to P011 ``(J1,J2,J3)`` exactly."""
    for name, value in (
        ("domain_size", domain_size),
        ("pair_moment", pair_moment),
        ("triple_moment", triple_moment),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be positive")
    j1 = domain_size
    j2_num = pair_moment - domain_size
    j3_num = triple_moment - 3 * pair_moment + 2 * domain_size
    if j2_num < 0 or j2_num % 2 or j3_num < 0 or j3_num % 6:
        raise ValueError("moments do not encode finite integer collision counts")
    return j1, j2_num // 2, j3_num // 6


def moment_pair_from_first_three_collisions(
    collisions: tuple[int, int, int]
) -> tuple[int, int]:
    """Recover ``(M2,M3)`` from ``(J1,J2,J3)``."""
    if (
        not isinstance(collisions, tuple)
        or len(collisions) != 3
        or any(
            isinstance(value, bool) or not isinstance(value, int) or value < 0
            for value in collisions
        )
    ):
        raise ValueError("collisions must be a non-negative integer triple")
    j1, j2, j3 = collisions
    if j1 <= 0:
        raise ValueError("J1/domain size must be positive")
    pair = 2 * j2 + j1
    triple = 6 * j3 + 3 * pair - 2 * j1
    return pair, triple


def _tail_row_value(kind: str, prime: int) -> int:
    """Valuation contribution of one completely hidden tail step."""
    if prime != 2:
        return 0
    if kind == "A":
        return 2  # M2 tail factor 4
    if kind == "F3":
        return 3  # M3 tail factor 8
    raise ValueError("unknown certificate row kind")


def identifiability_certificate_matrix() -> tuple[tuple[int, ...], ...]:
    """Build the exact 51x51 valuation matrix.

    Columns 0..49 are segment lengths 1..50.  Column 50 is one unit of hidden
    tail.  A nonzero determinant proves that equality of M2 and M3 forces all
    51 multiplicity differences to vanish.
    """
    rows = []
    for kind, prime in CERTIFICATE_ROWS:
        row = []
        for segment in range(1, MAX_CERTIFIED_SEGMENT + 1):
            value = (
                pair_moment_factor(segment)
                if kind == "A"
                else triple_moment_factor(segment)
            )
            row.append(p_adic_valuation(value, prime))
        row.append(_tail_row_value(kind, prime))
        rows.append(tuple(row))
    matrix = tuple(rows)
    if len(matrix) != 51 or any(len(row) != 51 for row in matrix):
        raise AssertionError("certificate matrix must be 51x51")
    return matrix


def determinant_mod_prime(
    matrix: tuple[tuple[int, ...], ...], modulus: int
) -> int:
    """Exact modular determinant by Gaussian elimination.

    ``modulus`` is required to be the known certificate prime in normal use;
    the routine assumes nonzero pivots are invertible modulo the supplied value.
    """
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 2:
        raise ValueError("modulus must exceed two")
    work = [[value % modulus for value in row] for row in matrix]
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = (-determinant) % modulus
        pivot_value = work[column][column]
        determinant = (determinant * pivot_value) % modulus
        inverse = pow(pivot_value, modulus - 2, modulus)
        for index in range(column, size):
            work[column][index] = (
                work[column][index] * inverse
            ) % modulus
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor:
                for index in range(column, size):
                    work[row][index] = (
                        work[row][index]
                        - factor * work[column][index]
                    ) % modulus
    return determinant


def certificate_determinant_residue() -> int:
    """Recompute the stored modular determinant certificate from definitions."""
    return determinant_mod_prime(
        identifiability_certificate_matrix(), CERTIFICATE_MODULUS
    )


def verify_bounded_identifiability_certificate() -> bool:
    """Verify the exact nonzero determinant residue ``22``."""
    residue = certificate_determinant_residue()
    if residue != CERTIFICATE_DETERMINANT_RESIDUE:
        raise AssertionError(
            "bounded low-order identifiability determinant certificate changed"
        )
    return True
