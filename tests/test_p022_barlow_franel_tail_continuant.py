from math import factorial

from enterprise_math.p022_barlow_franel_gap_continuant import (
    eliminated_gap_transfer,
)
from enterprise_math.p022_barlow_franel_tail_continuant import (
    euler_wallis_convergent,
    euler_wallis_franel_numerator_identity,
    fixed_gap_equals_tail_continuant,
    fixed_gap_euler_wallis_determinant,
    formal_reflection_scale,
    franel_tail_continuant,
    primitive_large_gap_is_projective_return,
    reflection_scale_ratio_identity,
    source_denominator_residue,
    terminal_franel_residue_from_gap,
)


def test_first_tail_continuants_give_the_fixed_gap_sequence() -> None:
    expected = {
        4: -848,
        5: 2_173_312,
        6: -10_712_812_544,
        7: 88_888_688_640_000,
        8: -1_120_986_365_845_045_248,
    }
    for rank, fixed in expected.items():
        assert eliminated_gap_transfer(rank) == fixed
        assert fixed_gap_equals_tail_continuant(rank) == (fixed, fixed)
        assert fixed == (
            (-1) ** (rank + 1)
            * 4 ** (rank - 3)
            * franel_tail_continuant(rank)
        )


def test_formal_reflection_scale_has_exact_closed_form() -> None:
    assert formal_reflection_scale(4) == 12
    assert formal_reflection_scale(5) == 224
    assert formal_reflection_scale(6) == 5_760
    assert formal_reflection_scale(7) == 190_080


def test_factorial_normalization_collapses_to_power_of_four() -> None:
    for rank in range(4, 25):
        assert reflection_scale_ratio_identity(rank)
        fixed_gap_equals_tail_continuant(rank)


def test_odd_prime_divisors_are_unchanged_by_tail_normalization() -> None:
    for rank in range(4, 15):
        fixed = abs(eliminated_gap_transfer(rank))
        tail = abs(franel_tail_continuant(rank))
        for prime in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            assert (fixed % prime == 0) == (tail % prime == 0)


def test_euler_wallis_numerators_are_factorial_scaled_franel_numbers() -> None:
    expected_p = {
        0: 2,
        1: 40,
        2: 2_016,
        3: 199_296,
    }
    for index, p_n in expected_p.items():
        actual_p, _ = euler_wallis_convergent(index)
        assert actual_p == p_n
        assert euler_wallis_franel_numerator_identity(index)


def test_fixed_gap_is_exact_euler_wallis_cross_determinant() -> None:
    for rank in range(4, 15):
        determinant, predicted = fixed_gap_euler_wallis_determinant(rank)
        assert determinant == predicted
        assert determinant == (
            2 ** (rank + 6)
            * factorial(rank) ** 4
            * eliminated_gap_transfer(rank)
        )


def test_source_denominator_and_terminal_unit_normalization() -> None:
    expected = {
        (6, 73): (11, 57),
        (9, 937): (484, 709),
        (15, 179): (164, 137),
        (21, 3019): (1149, 2112),
        (30, 2593): (2340, 1840),
    }
    for (rank, prime), (source_denominator, terminal) in expected.items():
        assert source_denominator_residue(rank, prime) == source_denominator
        assert terminal_franel_residue_from_gap(rank, prime) == (
            terminal,
            terminal,
        )


def test_known_large_primitive_rows_do_not_return_to_zero_at_terminal_gap() -> None:
    for rank, prime in ((6, 73), (9, 937), (15, 179), (21, 3019), (30, 2593)):
        assert not primitive_large_gap_is_projective_return(rank, prime)
