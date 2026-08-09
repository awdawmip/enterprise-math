from enterprise_math.p022_barlow_low_order_identifiability_150 import (
    CERTIFICATE_150_DETERMINANT_RESIDUE,
    MAX_CERTIFIED_SEGMENT_150,
    certificate_150_determinant_residue,
    identifiability_certificate_matrix_150,
    verify_bounded_identifiability_certificate_150,
)


def test_length_150_certificate_is_exact_and_nonzero() -> None:
    assert MAX_CERTIFIED_SEGMENT_150 == 150
    matrix = identifiability_certificate_matrix_150()
    assert len(matrix) == 151
    assert all(len(row) == 151 for row in matrix)
    assert CERTIFICATE_150_DETERMINANT_RESIDUE == 973_381
    assert certificate_150_determinant_residue() == 973_381
    assert verify_bounded_identifiability_certificate_150()


def test_every_segment_column_and_tail_column_are_seen() -> None:
    matrix = identifiability_certificate_matrix_150()
    for column in range(150):
        assert any(row[column] != 0 for row in matrix)
    assert any(row[-1] != 0 for row in matrix)
