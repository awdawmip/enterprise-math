from itertools import product

from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_coordination_recurrence import (
    ball_generating_denominator,
    ball_stride_recurrence_residual,
    coordination_phase_signature,
    coordination_residue_quadratic,
    shell_from_phase_signature,
    shell_generating_denominator,
    shell_stride_third_difference,
)
from enterprise_math.p022_barlow_stacking import stacking_prefix_imbalance


def _shell(pattern, radius: int) -> int:
    return barlow_shell_vertex_count_from_extreme_imbalances(
        radius,
        stacking_prefix_imbalance(pattern, radius),
        stacking_prefix_imbalance(pattern, -radius),
    )


def _ball(pattern, radius: int) -> int:
    return sum(_shell(pattern, current) for current in range(radius + 1))


def test_residue_quadratics_reconstruct_every_checked_shell() -> None:
    for period in range(1, 7):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            signature = coordination_phase_signature(pattern)
            assert len(signature) == period
            for radius in range(0, 10 * period + 1):
                assert shell_from_phase_signature(radius, signature) == _shell(
                    pattern, radius
                )


def test_residue_numerators_are_explicit_quadratics_in_period_index() -> None:
    pattern = (-1, -1, 1)
    period = len(pattern)
    signature = coordination_phase_signature(pattern)
    for residue in range(period):
        c0, c1, c2 = coordination_residue_quadratic(pattern, residue)
        assert signature[residue] == (c0, c1, c2)
        for quotient in range(0, 8):
            radius = quotient * period + residue
            if radius == 0:
                continue
            numerator = c0 + c1 * quotient + c2 * quotient * quotient
            assert numerator == 4 * _shell(pattern, radius)


def test_shell_sequence_satisfies_uniform_stride_third_difference() -> None:
    for period in range(1, 7):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            sequence = tuple(_shell(pattern, radius) for radius in range(0, 9 * period + 4))
            # S_0=1 is a special convention rather than the quasi-polynomial
            # continuation, so require the oldest term to have positive radius.
            for index in range(3 * period + 1, len(sequence)):
                assert shell_stride_third_difference(sequence, index, period) == 0


def test_ball_sequence_satisfies_one_extra_cumulative_factor() -> None:
    for period in range(1, 6):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            sequence = tuple(_ball(pattern, radius) for radius in range(0, 9 * period + 6))
            for index in range(3 * period + 2, len(sequence)):
                assert ball_stride_recurrence_residual(sequence, index, period) == 0


def test_generating_denominators_have_expected_sparse_form() -> None:
    assert shell_generating_denominator(1) == (1, -3, 3, -1)
    assert ball_generating_denominator(1) == (1, -4, 6, -4, 1)

    assert shell_generating_denominator(2) == (1, 0, -3, 0, 3, 0, -1)
    assert ball_generating_denominator(2) == (
        1,
        -1,
        -3,
        3,
        3,
        -3,
        -1,
        1,
    )


def test_same_period_can_have_different_phase_signatures_but_same_quadratic_lead() -> None:
    first = (-1, -1, 1, 1)
    second = (-1, 1, -1, 1)
    first_signature = coordination_phase_signature(first)
    second_signature = coordination_phase_signature(second)
    assert first_signature != second_signature
    # Same period length and zero drift force the same m^2 coefficient in
    # every residue even though lower-order phase data differ.
    assert {quadratic[2] for quadratic in first_signature} == {
        quadratic[2] for quadratic in second_signature
    } == {42 * 4 * 4}
