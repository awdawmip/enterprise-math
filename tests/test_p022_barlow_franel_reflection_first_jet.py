from enterprise_math.p022_barlow_franel_reflection_first_jet import (
    forced_midpoint_first_jet,
    reflected_exceptional_multipliers,
    reflected_first_jet_residues,
    reflection_scalar,
    simple_zero_exceptional_multiplier,
    zero_derivative_reflection,
    zero_reflection_quotient_residue,
)


def test_p_square_reflection_on_full_small_prime_ranges() -> None:
    for prime in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        assert 0 <= reflection_scalar(prime) < prime
        for index in range(prime):
            actual, predicted = reflected_first_jet_residues(prime, index)
            assert actual == predicted


def test_p149_distinguishes_reflected_simple_zero_units_and_derivatives() -> None:
    # Z_149={50,74,98}; 50 and 98 are a nontrivial reflected pair.
    u, v, derivative, scale = zero_reflection_quotient_residue(149, 50)
    assert (u, v, derivative, scale) == (141, 87, 91, pow(-8, 50, 149))
    actual, predicted = zero_derivative_reflection(149, 50)
    assert actual == predicted == 89

    left, right = reflected_exceptional_multipliers(149, 50)
    assert left == 5
    assert right == 143
    assert right == (-1 - left) % 149


def test_forced_midpoint_self_reflection_fixes_exceptional_multiplier() -> None:
    midpoint, unit, derivative = forced_midpoint_first_jet(149)
    assert midpoint == 74
    assert unit == 93
    assert derivative == 37
    assert derivative == 2 * unit % 149
    assert simple_zero_exceptional_multiplier(149, midpoint) == midpoint


def test_forced_midpoint_relation_on_smaller_simple_examples() -> None:
    # These forced midpoints are simple in the checked examples.
    for prime in (13, 23, 29, 53, 71, 101):
        midpoint, unit, derivative = forced_midpoint_first_jet(prime)
        assert midpoint == (prime - 1) // 2
        assert unit != 0
        assert derivative == 2 * unit % prime
        assert simple_zero_exceptional_multiplier(prime, midpoint) == midpoint
