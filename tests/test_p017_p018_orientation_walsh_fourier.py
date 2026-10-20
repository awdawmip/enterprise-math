from fractions import Fraction

from enterprise_math.p017_p018_orientation_walsh_fourier import (
    signed_root_fourier,
    walsh_complete_period_correlation,
    walsh_complete_period_moments,
    walsh_local_correlation,
)


def _local_factor(k: int, prime: int, radius: int) -> int:
    M = k * (k + 1)
    residue = radius % prime
    if residue == M % prime:
        return 2
    if residue == (-M) % prime:
        return 0
    return 1


def test_signed_root_fourier_factorizes_into_local_sine_factors():
    for selected in ((3,), (3, 5), (3, 5, 7)):
        for frequency in (0, 1, 2, 7):
            data = signed_root_fourier(46, selected, frequency)
            assert data["constant_mode_zero"] is True
            assert abs(data["direct_fourier_sum"] - data["product_fourier_sum"]) < 1e-7
            assert abs(data["direct_fourier_sum"] - data["sine_fourier_sum"]) < 1e-7


def test_local_correlation_matches_direct_complete_prime_period_count():
    k = 46
    for prime in (3, 5, 7, 11):
        for shift in range(-2 * prime, 2 * prime + 1):
            direct = Fraction(
                sum(
                    _local_factor(k, prime, radius)
                    * _local_factor(k, prime, radius + shift)
                    for radius in range(prime)
                ),
                prime,
            )
            assert walsh_local_correlation(k, prime, shift) == direct


def test_complete_period_second_moment_is_product_of_local_second_moments():
    k = 46
    primes = (3, 5, 7)
    modulus = 3 * 5 * 7
    values = [
        _local_factor(k, 3, radius)
        * _local_factor(k, 5, radius)
        * _local_factor(k, 7, radius)
        for radius in range(modulus)
    ]
    data = walsh_complete_period_moments(k, primes)
    assert data["mean"] == Fraction(sum(values), modulus) == 1
    assert data["second_moment"] == Fraction(sum(value * value for value in values), modulus)
    assert data["variance"] == data["second_moment"] - 1


def test_complete_period_shift_correlation_factors_over_primes():
    k = 46
    primes = (3, 5, 7)
    modulus = 3 * 5 * 7
    for shift in (0, 1, 2, 3, 7, 11, 14, 21):
        direct = Fraction(
            sum(
                (
                    _local_factor(k, 3, radius)
                    * _local_factor(k, 5, radius)
                    * _local_factor(k, 7, radius)
                )
                * (
                    _local_factor(k, 3, radius + shift)
                    * _local_factor(k, 5, radius + shift)
                    * _local_factor(k, 7, radius + shift)
                )
                for radius in range(modulus)
            ),
            modulus,
        )
        data = walsh_complete_period_correlation(k, shift, primes)
        assert data["correlation"] == direct
