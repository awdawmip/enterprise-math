"""Primitive integer obstruction vector of the N=150 Franel defect core.

The structurally reduced 40x40 core has Smith form

    diag(1,...,1,26622).

A primitive integer column x is recorded here with the exact certificate

    M_core x = -26622 e_269,

where e_269 is the selected valuation row labelled by prime 269.

Consequences:
- modulo each exceptional prime 2,3,17,29, x is a nonzero right-null vector;
- Smith rank 39 in those characteristics makes x span the unique null line;
- over Z, x is only a certificate-local near-kernel vector, NOT an actual
  multiplicative relation among the Franel defects, because one selected row
  still sees the nonzero obstruction -26622 and unselected valuations are not
  constrained by this equation.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_defect_core_compression import (
    compressed_core_defect_labels_150,
    compressed_core_row_primes_150,
    compressed_defect_core_150,
)
from .p022_barlow_defect_core_smith import (
    CORE_EXCEPTIONAL_PRIMES,
    CORE_EXACT_DETERMINANT,
    smith_invariant_factors_150,
)

OBSTRUCTION_ROW_PRIME = 269

# Coordinates are ordered by ``compressed_core_defect_labels_150()``.
_OBSTRUCTION_BY_DEFECT = {
    5: -15041,
    8: 31564,
    11: 5723,
    13: 3205,
    14: 3205,
    17: -8818,
    18: 4254,
    20: -7638,
    32: 132,
    33: 46423,
    38: 9977,
    41: -5641,
    56: 11207,
    58: 13311,
    59: -13179,
    60: 4040,
    61: 4040,
    62: -10576,
    63: 6750,
    67: 13311,
    73: 9977,
    74: 6561,
    77: -18713,
    78: -18713,
    88: -42651,
    89: -13311,
    92: 12284,
    122: 8376,
    123: -4935,
    124: -4935,
    130: 1077,
    134: -13311,
    149: 6561,
    150: -6750,
}


def primitive_obstruction_vector_150() -> tuple[int, ...]:
    labels = compressed_core_defect_labels_150()
    vector = tuple(_OBSTRUCTION_BY_DEFECT.get(label, 0) for label in labels)
    if len(vector) != 40:
        raise AssertionError("obstruction vector must have 40 coordinates")
    common = 0
    for value in vector:
        common = gcd(common, abs(value))
    if common != 1:
        raise AssertionError("obstruction vector must be primitive")
    return vector


def obstruction_vector_by_defect_150() -> tuple[tuple[int, int], ...]:
    labels = compressed_core_defect_labels_150()
    vector = primitive_obstruction_vector_150()
    return tuple(
        (label, coefficient)
        for label, coefficient in zip(labels, vector, strict=True)
        if coefficient
    )


def core_times_obstruction_vector_150() -> tuple[int, ...]:
    _, _, _, core = compressed_defect_core_150()
    vector = primitive_obstruction_vector_150()
    output = tuple(
        sum(value * coefficient for value, coefficient in zip(row, vector, strict=True))
        for row in core
    )
    rows = compressed_core_row_primes_150()
    expected = tuple(
        CORE_EXACT_DETERMINANT if prime == OBSTRUCTION_ROW_PRIME else 0
        for prime in rows
    )
    if output != expected:
        raise AssertionError("primitive obstruction equation changed")
    return output


def obstruction_support_size_150() -> int:
    return sum(value != 0 for value in primitive_obstruction_vector_150())


def exceptional_prime_null_vector_150(prime: int) -> tuple[int, ...]:
    """The unique right-null direction modulo one exceptional prime.

    The returned vector is canonical only up to multiplication by a nonzero
    scalar in F_p; we use the primitive integer obstruction reduced mod p.
    """
    if prime not in CORE_EXCEPTIONAL_PRIMES:
        raise ValueError("prime must be one of the Smith-exceptional characteristics")
    vector = tuple(value % prime for value in primitive_obstruction_vector_150())
    if not any(vector):
        raise AssertionError("primitive vector must remain nonzero modulo every prime")
    _, _, _, core = compressed_defect_core_150()
    for row in core:
        if sum(value * coefficient for value, coefficient in zip(row, vector, strict=True)) % prime:
            raise AssertionError("obstruction vector must lie in the modular nullspace")
    invariants = smith_invariant_factors_150()
    if sum(invariant % prime == 0 for invariant in invariants) != 1:
        raise AssertionError("exceptional nullspace should be one-dimensional")
    return vector


def exceptional_null_support_150(prime: int) -> tuple[int, ...]:
    labels = compressed_core_defect_labels_150()
    vector = exceptional_prime_null_vector_150(prime)
    return tuple(
        label
        for label, coefficient in zip(labels, vector, strict=True)
        if coefficient
    )
