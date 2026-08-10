from enterprise_math.p022_barlow_franel_gap_continuant import eliminated_gap_transfer
from enterprise_math.p022_barlow_franel_gap_equivalence import (
    companion_gap_transfer_determinant,
    companion_gap_transfer_matrix,
    large_terminal_zero_iff_fixed_gap_divisor,
)


def test_gap_transfer_matrix_has_unit_determinant_formula() -> None:
    matrix = companion_gap_transfer_matrix(3, 2)
    assert matrix[0][1] == -(28 * 4**2 + 1)
    assert companion_gap_transfer_determinant(3, 2) == (
        (-8 * 7**4) * (-8 * 9**4)
    )


def test_known_large_primitive_sources_have_no_terminal_fixed_divisor() -> None:
    for rank, prime in ((6, 73), (15, 179), (9, 937), (30, 1361), (30, 2593), (21, 3019)):
        assert not large_terminal_zero_iff_fixed_gap_divisor(rank, prime)
        assert eliminated_gap_transfer(rank) % prime != 0
