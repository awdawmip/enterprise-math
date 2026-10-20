from math import exp, log

from enterprise_math.p017_p018_walsh_spectral_scale import (
    conductor_energy_partition,
    conductor_prime_inclusion_probabilities,
    generalized_dickman_two_log_mgf,
    normalized_log_conductor_mgf,
    physical_transverse_primes,
)


def test_exact_conductor_energy_partition_for_3_5_7():
    data = conductor_energy_partition((3, 5, 7))
    expected = {
        1: 1,
        3: 2 / 3,
        5: 2 / 5,
        7: 2 / 7,
        15: 4 / 15,
        21: 4 / 21,
        35: 4 / 35,
        105: 8 / 105,
    }
    assert float(data["total_second_moment"]) == 3.0
    for conductor, energy in data["energy_rows"]:
        assert abs(float(energy) - expected[conductor]) < 1e-15
    assert sum(probability for _q, probability in data["normalized_energy_rows"]) == 1


def test_normalized_energy_prime_inclusions_are_independent_bernoulli_probabilities():
    probabilities = dict(conductor_prime_inclusion_probabilities((3, 5, 7)))
    assert probabilities[3].numerator == 2 and probabilities[3].denominator == 5
    assert probabilities[5].numerator == 2 and probabilities[5].denominator == 7
    assert probabilities[7].numerator == 2 and probabilities[7].denominator == 9

    data = conductor_energy_partition((3, 5, 7))
    for prime in (3, 5, 7):
        direct = sum(
            probability
            for conductor, probability in data["normalized_energy_rows"]
            if conductor % prime == 0
        )
        assert direct == probabilities[prime]


def test_finite_normalized_log_mgf_matches_direct_energy_enumeration():
    k = 46
    primes = physical_transverse_primes(k)
    data = conductor_energy_partition(primes)
    s = 0.7
    direct = sum(
        float(probability) * exp(s * log(conductor) / log(k))
        for conductor, probability in data["normalized_energy_rows"]
    )
    assert abs(normalized_log_conductor_mgf(k, s) - direct) < 1e-12


def test_generalized_dickman_two_limit_log_mgf_has_expected_first_two_cumulants():
    h = 1e-4
    f0 = generalized_dickman_two_log_mgf(0.0)
    fp = generalized_dickman_two_log_mgf(h)
    fm = generalized_dickman_two_log_mgf(-h)
    first = (fp - fm) / (2 * h)
    second = (fp - 2 * f0 + fm) / (h * h)
    assert abs(first - 2.0) < 1e-6
    assert abs(second - 1.0) < 1e-5
