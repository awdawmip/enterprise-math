"""Exact one-step extension of the P022 low-order certificate to length 66.

This certificate adds the segment-length-66 column to the length-65 result and
recomputes a 67x67 p-adic valuation determinant.  The determinant remains
nonzero modulo 1,000,003.
"""

from __future__ import annotations

from .p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
    determinant_mod_prime,
    p_adic_valuation,
    pair_moment_factor,
    triple_moment_factor,
)

MAX_CERTIFIED_SEGMENT_66 = 66
CERTIFICATE_66_DETERMINANT_RESIDUE = 999_999

CERTIFICATE_66_ROWS: tuple[tuple[str, int], ...] = (
    ("A", 2), ("A", 3), ("A", 5), ("A", 7), ("A", 11),
    ("A", 13), ("A", 17), ("A", 19), ("A", 23), ("A", 29),
    ("A", 31), ("A", 37), ("A", 41), ("A", 43), ("A", 47),
    ("A", 53), ("A", 59), ("A", 61), ("A", 67), ("A", 71),
    ("A", 73), ("A", 79), ("A", 83), ("A", 89), ("A", 97),
    ("A", 101), ("A", 103), ("A", 107), ("A", 109), ("A", 113),
    ("A", 127), ("A", 131),
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
    return 2 if kind == "A" else 3


def identifiability_certificate_matrix_66() -> tuple[tuple[int, ...], ...]:
    rows = []
    for kind, prime in CERTIFICATE_66_ROWS:
        row = []
        for segment in range(1, MAX_CERTIFIED_SEGMENT_66 + 1):
            value = (
                pair_moment_factor(segment)
                if kind == "A"
                else triple_moment_factor(segment)
            )
            row.append(p_adic_valuation(value, prime))
        row.append(_tail_row_value(kind, prime))
        rows.append(tuple(row))
    matrix = tuple(rows)
    if len(matrix) != 67 or any(len(row) != 67 for row in matrix):
        raise AssertionError("length-66 certificate matrix must be 67x67")
    return matrix


def certificate_66_determinant_residue() -> int:
    return determinant_mod_prime(
        identifiability_certificate_matrix_66(), CERTIFICATE_MODULUS
    )


def verify_bounded_identifiability_certificate_66() -> bool:
    if certificate_66_determinant_residue() != CERTIFICATE_66_DETERMINANT_RESIDUE:
        raise AssertionError("length-66 determinant certificate changed")
    return True
