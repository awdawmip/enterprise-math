from math import isqrt

from enterprise_math.p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
)
from enterprise_math.p022_barlow_low_order_identifiability_65 import (
    CERTIFICATE_65_DETERMINANT_RESIDUE,
    MAX_CERTIFIED_SEGMENT_65,
    certificate_65_determinant_residue,
    identifiability_certificate_matrix_65,
    verify_bounded_identifiability_certificate_65,
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def test_length_65_certificate_is_exact_square_and_nonzero_mod_prime() -> None:
    assert MAX_CERTIFIED_SEGMENT_65 == 65
    assert _is_prime(CERTIFICATE_MODULUS)
    matrix = identifiability_certificate_matrix_65()
    assert len(matrix) == 66
    assert all(len(row) == 66 for row in matrix)
    assert CERTIFICATE_65_DETERMINANT_RESIDUE == 999_999
    assert certificate_65_determinant_residue() == 999_999
    assert verify_bounded_identifiability_certificate_65()


def test_extension_really_contains_nontrivial_new_segment_columns() -> None:
    matrix = identifiability_certificate_matrix_65()
    # Columns 50..64 correspond to segment lengths 51..65. Every new column
    # must have at least one nonzero selected valuation, otherwise it could not
    # participate in a full-rank extension.
    for column in range(50, 65):
        assert any(row[column] != 0 for row in matrix)


def test_hidden_tail_column_is_not_zero() -> None:
    matrix = identifiability_certificate_matrix_65()
    assert any(row[-1] != 0 for row in matrix)
