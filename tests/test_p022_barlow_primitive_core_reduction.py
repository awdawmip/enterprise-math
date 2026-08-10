from enterprise_math.p022_barlow_primitive_core_reduction import (
    EXPECTED_CAPTURE_COUNT,
    EXPECTED_RESIDUAL_COLUMNS,
    augmented_residual_full_minor_witnesses_150,
    augmented_residual_is_saturated_150,
    capture_diagonal_150,
    primitive_residual_22_150,
    primitive_residual_determinant_150,
    primitive_residual_smith_invariants_150,
    primitive_residual_smith_witnesses_150,
    projected_saturation_row_176459_150,
)


def test_eighteen_local_primitive_capture_pivots_are_units() -> None:
    diagonal = capture_diagonal_150()
    assert len(diagonal) == EXPECTED_CAPTURE_COUNT == 18
    assert all(abs(value) == 1 for value in diagonal)


def test_old_40_core_reduces_to_exact_22_residual() -> None:
    residual = primitive_residual_22_150()
    assert len(residual) == len(EXPECTED_RESIDUAL_COLUMNS) == 22
    assert all(len(row) == 22 for row in residual)
    assert primitive_residual_determinant_150() == -13_311


def test_22_residual_has_one_cyclic_smith_index() -> None:
    assert primitive_residual_smith_witnesses_150() == (-69, -70)
    assert primitive_residual_smith_invariants_150() == (1,) * 21 + (13_311,)


def test_second_real_predecessor_row_saturates_residual_lattice() -> None:
    projected = projected_saturation_row_176459_150()
    assert len(projected) == 22
    assert augmented_residual_full_minor_witnesses_150() == (-13_311, -1_585)
    assert augmented_residual_is_saturated_150()
