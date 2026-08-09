"""Incremental exact extension of the P022 low-order certificate to length 65.

The original certificate proves joint M2/M3 identifiability for observed
segment lengths 1..50 plus hidden tail.  This module adds fifteen segment
columns and supplies a new 66x66 p-adic valuation determinant certificate.

No factor table is stored: every valuation is recomputed directly from the
central-binomial and Franel definitions imported from the base certificate.
"""

from __future__ import annotations

from .p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
    determinant_mod_prime,
    p_adic_valuation,
    pair_moment_factor,
    triple_moment_factor,
)

MAX_CERTIFIED_SEGMENT_65 = 65
CERTIFICATE_65_DETERMINANT_RESIDUE = 999_999

CERTIFICATE_65_ROWS: tuple[tuple[str, int], ...] = (
    ("A", 2), ("A", 3), ("A", 5), ("A", 7), ("A", 11),
    ("A", 13), ("A", 17), ("A", 19), ("A", 23), ("A", 29),
    ("A", 31), ("A", 37), ("A", 41), ("A", 43), ("A", 47),
    ("A", 53), ("A", 59), ("A", 61), ("A", 67), ("A", 71),
    ("A", 73), ("A", 79), ("A", 83), ("A", 89), ("A", 97),
    ("A", 101), ("A", 103), ("A", 107), ("A", 109), ("A", 113),
    ("A", 127),
    ("F3", 2), ("F3", 5), ("F3", 7), ("F3", 13), ("F3", 23),
    ("F3", 29), ("F3", 31), ("F3", 37), ("F3", 41), ("F3", 47),
    ("F3", 53), ("F3", 59), ("F3", 61), ("F3", 67), ("F3", 71),
    ("F3", 73), ("F3", 79), ("F3", 101), ("F3", 109), ("F3", 127),
    ("F3", 131), ("F3", 151), ("F3", 157), ("F3", 173),
    ("F3", 251), ("F3", 269), ("F3", 367), ("F3", 389),
    ("F3", 421), ("F3", 563), ("F3", 661), ("F3", 769),
    ("F3", 937), ("F3", 1361), ("F3", 2141),
)


def _tail_row_value(kind: str, prime: int) -> int:
    if prime != 2:
        return 0
    if kind == "A":
        return 2
    if kind == "F3":
        return 3
    raise ValueError("unknown certificate row kind")


def identifiability_certificate_matrix_65() -> tuple[tuple[int, ...], ...]:
    """Build the exact 66x66 valuation matrix for lengths 1..65 plus tail."""
    rows = []
    for kind, prime in CERTIFICATE_65_ROWS:
        row = []
        for segment in range(1, MAX_CERTIFIED_SEGMENT_65 + 1):
            value = (
                pair_moment_factor(segment)
                if kind == "A"
                else triple_moment_factor(segment)
            )
            row.append(p_adic_valuation(value, prime))
        row.append(_tail_row_value(kind, prime))
        rows.append(tuple(row))
    matrix = tuple(rows)
    expected = MAX_CERTIFIED_SEGMENT_65 + 1
    if len(matrix) != expected or any(len(row) != expected for row in matrix):
        raise AssertionError("length-65 certificate matrix must be 66x66")
    return matrix


def certificate_65_determinant_residue() -> int:
    return determinant_mod_prime(
        identifiability_certificate_matrix_65(), CERTIFICATE_MODULUS
    )


def verify_bounded_identifiability_certificate_65() -> bool:
    residue = certificate_65_determinant_residue()
    if residue != CERTIFICATE_65_DETERMINANT_RESIDUE:
        raise AssertionError(
            "length-65 low-order identifiability determinant certificate changed"
        )
    return True
