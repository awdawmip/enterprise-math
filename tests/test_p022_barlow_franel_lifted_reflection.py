from enterprise_math.p022_barlow_franel_lifted_reflection import (
    double_stationary_iff_reflected_deep,
    endpoint_franel_lift,
    lifted_reflection_first_jet,
    simple_copy_degeneracy_reflected_ratio,
    zero_digit_lifted_reflection,
)


def test_endpoint_franel_lift_matches_power_of_eight() -> None:
    for prime in (5, 7, 11, 13, 17, 29, 41, 67):
        actual, predicted = endpoint_franel_lift(prime)
        assert actual == predicted


def test_lifted_reflection_first_jet_on_full_small_digit_tables() -> None:
    for prime in (7, 11, 13, 17, 29, 41):
        for rank in range(prime):
            actual, predicted = lifted_reflection_first_jet(rank, prime)
            assert actual == predicted


def test_zero_digit_lift_removes_fermat_quotient_term() -> None:
    examples = (
        (3, 7),
        (6, 13),
        (12, 29),
        (14, 29),
        (7, 41),
        (10, 41),
        (23, 67),
    )
    for rank, prime in examples:
        actual, derivative = zero_digit_lifted_reflection(rank, prime)
        assert actual == derivative


def test_deep_rank_23_at_67_is_not_double_stationary() -> None:
    # 67^2 divides F_23, but the reflected digit 43 is only a simple zero.
    # Lifted reflection therefore forces F'_23 to remain nonzero mod 67.
    assert not double_stationary_iff_reflected_deep(23, 67)


def test_simple_copy_factor_equals_reflected_depth_ratio_form() -> None:
    for rank, prime, multiplier in (
        (6, 13, 2),
        (6, 73, 2),
        (15, 179, 1),
        (30, 1361, 2),
    ):
        source, reflected, factor = simple_copy_degeneracy_reflected_ratio(
            rank, prime, multiplier
        )
        assert source != 0
        assert reflected != 0
        # These concrete primitive-twin copies are first-jet nondegenerate.
        assert factor != 0
