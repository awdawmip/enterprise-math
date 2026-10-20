from math import gcd

from enterprise_math.p017_p018_euclidean_biprimitive import (
    biprimitive_reconstruction,
    symmetric_tent_channel,
    verify_biprimitive_ceiling,
)


def test_symmetric_tent_channel_is_self_dual():
    center = 46 * 47
    for n, d in ((11, 5), (11, 13), (19, 13), (37, 33)):
        if gcd(center, n * d) != 1 or gcd(n, d) != 1:
            continue
        assert symmetric_tent_channel(center, 46, n, d) == symmetric_tent_channel(center, 46, d, n)


def test_double_conductor_mobius_reconstruction_and_self_duality():
    examples = [
        (46 * 47, 46, 11, 13),
        (82 * 83, 82, 11, 5),
        (862 * 863, 862, 37, 35),
    ]
    for center, k, n, d in examples:
        if gcd(center, n * d) != 1 or gcd(n, d) != 1:
            continue
        data = biprimitive_reconstruction(center, k, n, d)
        assert data["physical_self_duality"] is True
        assert data["biprimitive_self_duality"] is True
        assert data["double_conductor_reconstruction"] is True
        assert data["physical_channel"] == data["reconstructed_channel"]


def test_biprimitive_block_obeys_low_poisson_and_high_parseval_ceilings():
    center = 82 * 83
    examples = [(5, 7), (11, 5), (11, 13), (37, 41)]
    for n, d in examples:
        if n > 82 or d > 82 or gcd(center, n * d) != 1 or gcd(n, d) != 1:
            continue
        data = verify_biprimitive_ceiling(center, 82, n, d)
        assert data["ceiling_verified"] is True
        assert abs(data["biprimitive_block"]) <= data["absolute_ceiling"]
