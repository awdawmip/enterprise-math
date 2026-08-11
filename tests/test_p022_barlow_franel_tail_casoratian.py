from enterprise_math.p022_barlow_franel_gap_continuant import eliminated_gap_transfer
from enterprise_math.p022_barlow_franel_tail_casoratian import (
    fixed_continuant_casoratian,
    fixed_continuant_tail_sum,
    integer_casoratian,
    integer_casoratian_closed,
    primitive_second_solution_residue,
    second_integer_solution,
)


def test_integer_casoratian_has_closed_factorial_form() -> None:
    assert second_integer_solution(-1) == 0
    assert second_integer_solution(0) == 1
    assert second_integer_solution(1) == 16
    for n in range(0, 9):
        assert integer_casoratian(n) == integer_casoratian_closed(n)


def test_fixed_continuant_is_the_tail_casoratian() -> None:
    for rank in range(3, 10):
        expected = eliminated_gap_transfer(rank)
        assert fixed_continuant_casoratian(rank) == expected
        assert fixed_continuant_tail_sum(rank) == expected


def test_second_solution_residue_at_real_primitive_zeros() -> None:
    # These are known primitive Franel divisors from the P022 owner branch.
    for rank, prime in ((6, 13), (6, 73), (9, 937), (15, 179), (21, 3019)):
        actual, expected = primitive_second_solution_residue(rank, prime)
        assert actual == expected
        assert actual != 0
