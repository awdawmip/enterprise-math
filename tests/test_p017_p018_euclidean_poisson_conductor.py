from fractions import Fraction

from enterprise_math.p017_p018_euclidean_poisson_conductor import (
    critical_frequency_closure,
    euclidean_poisson_frequency_state,
    tent_frequency_scale,
    tent_tail_error_ceiling,
)


def test_frequency_conductor_descent_is_exact_modulo_one():
    examples = [
        (46 * 47, 11, 35, 3),
        (82 * 83, 17, 15, 6),
        (862 * 863, 37, 55, 10),
        (8191 * 8192, 127, 105, 21),
    ]
    for center, n, d, h in examples:
        data = euclidean_poisson_frequency_state(center, n, d, h)
        assert data["frequency_conductor_descent_exact"] is True
        assert isinstance(data["original_phase"], Fraction)
        assert isinstance(data["reduced_phase"], Fraction)
        assert data["phase_difference_integer"] == int(
            data["original_phase"] - data["reduced_phase"]
        )
        q = data["reduced_conductor_q"]
        if q > 1:
            from math import gcd
            assert gcd(data["primitive_frequency_h_prime"], q) == 1
            assert gcd(data["reduced_remainder_t_q"], q) == 1


def test_zero_frequency_descends_to_trivial_conductor():
    data = euclidean_poisson_frequency_state(46 * 47, 11, 35, 0)
    assert data["reduced_conductor_q"] == 1
    assert data["primitive_frequency_h_prime"] == 0
    assert data["original_phase"] == data["reduced_phase"] == 0


def test_critical_divisor_range_closes_frequency_precision_at_every_conductor():
    for k in (46, 82, 862):
        for q in (1, 3, 5, 11, 17):
            for d in (1, 3, min(k, 35), k):
                data = critical_frequency_closure(k, q, d)
                if d <= k:
                    assert data["frequency_scale_H_q"] <= q
                    assert data["frequency_no_finer_than_conductor"] is True
                    assert data["frequency_scale_H_q"] == tent_frequency_scale(k, q, d)


def test_tent_tail_ceiling_decays_uniformly_with_precision_multiplier():
    assert tent_tail_error_ceiling(3.0) < tent_tail_error_ceiling(2.0)
    assert tent_tail_error_ceiling(10.0) < 0.03
