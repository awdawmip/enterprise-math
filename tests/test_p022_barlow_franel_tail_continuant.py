from enterprise_math.p022_barlow_franel_gap_continuant import (
    eliminated_gap_transfer,
)
from enterprise_math.p022_barlow_franel_tail_continuant import (
    fixed_gap_equals_tail_continuant,
    formal_reflection_scale,
    franel_tail_continuant,
    reflection_scale_ratio_identity,
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
