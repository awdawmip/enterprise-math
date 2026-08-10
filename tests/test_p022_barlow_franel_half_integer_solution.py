from fractions import Fraction

from enterprise_math.p022_barlow_franel_half_integer_solution import (
    continued_fraction_half_step_residual,
    half_integer_casoratian,
    half_integer_casoratian_closed,
    half_integer_franel_recurrence_residual,
    half_integer_franel_solution,
    integer_midpoint_companion,
    integer_normalization_identity,
    midpoint_zero_from_integer_companion,
)
from enterprise_math.p022_barlow_franel_midpoint_offset import (
    left_zero_offsets_from_companion,
)


def test_half_integer_solution_satisfies_shifted_franel_recurrence() -> None:
    assert half_integer_franel_solution(0) == 0
    assert half_integer_franel_solution(1) == -8
    for offset in range(1, 20):
        assert half_integer_franel_recurrence_residual(offset) == 0


def test_integer_companion_first_values_and_normalization() -> None:
    expected = (
        0,
        1,
        29,
        3925,
        1_138_025,
        586_364_625,
        470_774_258_325,
        543_690_942_446_925,
        854_053_932_715_790_625,
    )
    assert tuple(integer_midpoint_companion(d) for d in range(len(expected))) == expected
    for offset in range(1, 16):
        normalized, integer = integer_normalization_identity(offset)
        assert normalized == Fraction(integer, 1)
        assert integer > 0


def test_integer_companion_reconstructs_zero_offsets() -> None:
    for prime in (29, 157, 173):
        midpoint = (prime - 1) // 2
        direct_offsets = left_zero_offsets_from_companion(prime)
        integer_offsets = tuple(
            offset
            for offset in range(1, midpoint)
            if midpoint_zero_from_integer_companion(prime, offset)
        )
        assert integer_offsets == direct_offsets


def test_half_integer_casoratian_has_closed_form() -> None:
    for offset in range(0, 15):
        assert half_integer_casoratian(offset) == half_integer_casoratian_closed(offset)


def test_half_step_euler_wallis_recurrence_is_exact() -> None:
    for offset in range(2, 16):
        assert continued_fraction_half_step_residual(offset) == 0
