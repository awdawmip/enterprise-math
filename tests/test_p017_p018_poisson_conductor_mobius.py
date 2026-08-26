from fractions import Fraction
from math import gcd

from enterprise_math.p017_p018_poisson_conductor_mobius import (
    conductor_mobius_reconstruction,
    primitive_conductor_block,
    tent_smoothed_channel_count,
)


def test_tent_channel_count_is_exact_nonnegative_rational():
    center = 46 * 47
    for n, d in ((11, 35), (13, 15), (17, 7)):
        if gcd(center, n) != 1 or gcd(n, d) != 1:
            continue
        value = tent_smoothed_channel_count(center, 46, n, d)
        assert isinstance(value, Fraction)
        assert value >= 0


def test_conductor_mobius_inversion_reconstructs_physical_channels_exactly():
    examples = [
        (46 * 47, 46, 11, 35),
        (82 * 83, 82, 17, 15),
        (862 * 863, 862, 37, 55),
    ]
    for center, k, n, d in examples:
        if gcd(center, n) != 1 or gcd(n, d) != 1:
            continue
        data = conductor_mobius_reconstruction(center, k, n, d)
        assert data["conductor_mobius_identity"] is True
        assert data["physical_channel_C_n_d"] == data["reconstructed_channel"]


def test_nontrivial_primitive_layer_is_a_signed_mobius_repair():
    center = 46 * 47
    n, d = 11, 35
    primitive = primitive_conductor_block(center, 46, n, d)
    direct = tent_smoothed_channel_count(center, 46, n, d)
    coarse = tent_smoothed_channel_count(center, 46, 1, d)
    # For prime n, P(n,d)=C(n,d)-C(1,d)/n.
    assert primitive == direct - coarse / n
