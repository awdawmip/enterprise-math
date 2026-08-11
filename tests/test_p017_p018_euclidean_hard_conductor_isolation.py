from fractions import Fraction
from math import gcd

from enterprise_math.p017_p018_euclidean_hard_conductor_isolation import (
    hard_conductor_isolation,
    low_primitive_block_ceiling,
)


def test_low_primitive_ceiling_is_exact_declared_scale():
    assert low_primitive_block_ceiling(82, 5, 7) == Fraction(35, 3 * 82)


def test_low_region_has_no_hard_conductors():
    center = 82 * 83
    data = hard_conductor_isolation(center, 82, 5, 7)
    assert data["hard_conductors_absent"] is True
    assert data["hard_conductor_block"] == 0
    assert data["hard_conductor_isolation_exact"] is True


def test_hard_region_isolated_to_divisors_q_with_qd_above_k():
    examples = [
        (46 * 47, 46, 11, 5),
        (82 * 83, 82, 17, 7),
        (862 * 863, 862, 37, 35),
    ]
    for center, k, n, d in examples:
        if gcd(center, n) != 1 or gcd(n, d) != 1:
            continue
        data = hard_conductor_isolation(center, k, n, d)
        assert data["hard_conductor_isolation_exact"] is True
        assert data["coarse_q1_block"] + data["controlled_low_block"] + data["hard_conductor_block"] == data["physical_channel"]
        assert abs(data["coarse_error"]) <= data["coarse_error_ceiling"]
        assert data["controlled_low_absolute_ceiling"] <= data["sigma_over_3n_ceiling"]
        for row in data["hard_rows"]:
            assert row["q"] * d > k
