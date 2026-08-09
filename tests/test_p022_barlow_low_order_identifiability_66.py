from enterprise_math.p022_barlow_low_order_identifiability_66 import (
    CERTIFICATE_66_DETERMINANT_RESIDUE,
    MAX_CERTIFIED_SEGMENT_66,
    certificate_66_determinant_residue,
    identifiability_certificate_matrix_66,
    verify_bounded_identifiability_certificate_66,
)


def test_length_66_certificate_is_exact_and_nonzero() -> None:
    assert MAX_CERTIFIED_SEGMENT_66 == 66
    matrix = identifiability_certificate_matrix_66()
    assert len(matrix) == 67
    assert all(len(row) == 67 for row in matrix)
    assert CERTIFICATE_66_DETERMINANT_RESIDUE == 999_999
    assert certificate_66_determinant_residue() == 999_999
    assert verify_bounded_identifiability_certificate_66()


def test_segment_66_column_is_nonzero() -> None:
    matrix = identifiability_certificate_matrix_66()
    # zero-based column 65 is segment length 66; final column is hidden tail.
    assert any(row[65] != 0 for row in matrix)
    assert any(row[-1] != 0 for row in matrix)
