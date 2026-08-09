from enterprise_math.p022_barlow_defect_core_compression import (
    EXPECTED_CORE_DETERMINANT_RESIDUE,
    EXPECTED_CORE_SIZE,
    EXPECTED_PEELED_PIVOTS,
    compressed_core_defect_labels_150,
    compressed_core_determinant_residue_150,
    compressed_core_row_primes_150,
    compressed_defect_core_150,
    core_support_degrees_150,
    core_support_is_connected_150,
    defect_matrix_150,
    singleton_peel,
    verify_150_core_compression,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import (
    DEFECT_150_DETERMINANT_RESIDUE,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    CERTIFICATE_MODULUS,
    determinant_mod_prime,
)
from enterprise_math.p022_barlow_low_order_identifiability_150 import (
    CERTIFICATE_150_DETERMINANT_RESIDUE,
)


def test_singleton_peel_on_toy_matrix_is_exact_support_elimination() -> None:
    matrix = (
        (1, 0, 0),
        (3, 2, 0),
        (0, 5, -1),
    )
    pivots, rows, cols = singleton_peel(matrix)
    assert len(pivots) == 3
    assert rows == ()
    assert cols == ()
    assert all(value != 0 for _, _, value in pivots)


def test_N150_peels_exactly_49_unit_pivots() -> None:
    pivots, rows, cols, core = compressed_defect_core_150()
    assert len(pivots) == EXPECTED_PEELED_PIVOTS == 49
    assert all(abs(value) == 1 for _, _, value in pivots)
    assert len(rows) == len(cols) == len(core) == EXPECTED_CORE_SIZE == 40


def test_residual_core_has_no_singletons_and_is_connected() -> None:
    row_degrees, col_degrees = core_support_degrees_150()
    assert min(row_degrees) >= 2
    assert min(col_degrees) >= 2
    assert core_support_is_connected_150()


def test_40x40_core_carries_the_raw_joint_certificate_residue() -> None:
    residue = compressed_core_determinant_residue_150()
    assert residue == EXPECTED_CORE_DETERMINANT_RESIDUE == 973_381
    assert residue == CERTIFICATE_150_DETERMINANT_RESIDUE


def test_89x89_and_40x40_determinants_differ_only_by_sign() -> None:
    assert DEFECT_150_DETERMINANT_RESIDUE == 26_622
    assert (
        DEFECT_150_DETERMINANT_RESIDUE
        + compressed_core_determinant_residue_150()
    ) % CERTIFICATE_MODULUS == 0


def test_core_labels_are_exactly_40_rows_and_40_defect_columns() -> None:
    rows = compressed_core_row_primes_150()
    cols = compressed_core_defect_labels_150()
    assert len(rows) == len(cols) == 40
    assert "tail" not in cols
    assert rows[:5] == (5, 7, 13, 23, 29)
    assert cols[:5] == (5, 8, 11, 13, 14)
    assert cols[-2:] == (149, 150)


def test_full_verifier_passes() -> None:
    assert verify_150_core_compression()
