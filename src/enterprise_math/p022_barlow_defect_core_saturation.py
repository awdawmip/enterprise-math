"""Unimodular saturation of the N=150 40x40 Franel defect core.

The historical selected 40 valuation rows give determinant -26622.  Let x be
the primitive adjugate/Smith obstruction vector satisfying

    M x = -26622 e_269.

If the row v_269 is replaced by any new valuation row r, determinant
multilinearity gives det(M[r]) = r*x.  Two unselected genuine prime-valuation
rows have exact obstruction pairings

    v_73589 * x = -13311,
    v_176459 * x = 2518.

These integers are coprime.  The derived integer valuation functional

    lambda = 915 v_73589 + 4837 v_176459

therefore pairs with x by one, so replacing v_269 by lambda gives determinant
exactly +1.  Hence the residual Franel core becomes unimodular after adjoining
those two real prime-valuation observations.  The old Smith index 26622 is a
row-selection index, not an intrinsic saturation obstruction of this bounded
defect family.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_defect_core_compression import (
    compressed_core_defect_labels_150,
    compressed_core_row_primes_150,
    compressed_defect_core_150,
)
from .p022_barlow_defect_core_obstruction import (
    OBSTRUCTION_ROW_PRIME,
    primitive_obstruction_vector_150,
)
from .p022_barlow_defect_core_smith import exact_determinant_bareiss
from .p022_barlow_low_order_defect_reduction import franel_defect_valuation

SATURATION_PRIME_ONE = 73_589
SATURATION_PRIME_TWO = 176_459
PAIRING_ONE = -13_311
PAIRING_TWO = 2_518
BEZOUT_ONE = 915
BEZOUT_TWO = 4_837
UNIMODULAR_DETERMINANT = 1


def core_valuation_row_150(prime: int) -> tuple[int, ...]:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
        raise ValueError("prime must exceed one")
    labels = compressed_core_defect_labels_150()
    return tuple(franel_defect_valuation(segment, prime) for segment in labels)


def obstruction_pairing_150(prime: int) -> int:
    row = core_valuation_row_150(prime)
    vector = primitive_obstruction_vector_150()
    return sum(value * coefficient for value, coefficient in zip(row, vector, strict=True))


def saturation_pairings_150() -> tuple[int, int]:
    first = obstruction_pairing_150(SATURATION_PRIME_ONE)
    second = obstruction_pairing_150(SATURATION_PRIME_TWO)
    if (first, second) != (PAIRING_ONE, PAIRING_TWO):
        raise AssertionError("saturation-prime obstruction pairings changed")
    if gcd(abs(first), abs(second)) != 1:
        raise AssertionError("saturation pairings must be coprime")
    return first, second


def derived_unimodular_row_150() -> tuple[int, ...]:
    """Integer valuation functional lambda with lambda*x=1."""
    first = core_valuation_row_150(SATURATION_PRIME_ONE)
    second = core_valuation_row_150(SATURATION_PRIME_TWO)
    row = tuple(
        BEZOUT_ONE * left + BEZOUT_TWO * right
        for left, right in zip(first, second, strict=True)
    )
    vector = primitive_obstruction_vector_150()
    pairing = sum(value * coefficient for value, coefficient in zip(row, vector, strict=True))
    if pairing != 1:
        raise AssertionError("derived valuation row must pair with obstruction by one")
    return row


def unimodular_core_matrix_150() -> tuple[tuple[int, ...], ...]:
    """Replace the historical v_269 core row by the derived valuation row."""
    _, _, _, core = compressed_defect_core_150()
    row_primes = compressed_core_row_primes_150()
    row_index = row_primes.index(OBSTRUCTION_ROW_PRIME)
    derived = derived_unimodular_row_150()
    matrix = tuple(
        derived if index == row_index else row
        for index, row in enumerate(core)
    )
    return matrix


def unimodular_core_determinant_150() -> int:
    value = exact_determinant_bareiss(unimodular_core_matrix_150())
    if value != UNIMODULAR_DETERMINANT:
        raise AssertionError("saturated core determinant must be +1")
    return value


def verify_core_saturation_150() -> bool:
    first, second = saturation_pairings_150()
    if BEZOUT_ONE * first + BEZOUT_TWO * second != 1:
        raise AssertionError("stored Bezout coefficients changed")
    if unimodular_core_determinant_150() != 1:
        raise AssertionError("core is not unimodular after derived-row replacement")
    return True
