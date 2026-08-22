from enterprise_math.prime_brc_block_transform import (
    mobius_polarity_annihilation,
    multiplier_blocks,
    totient_first_moment,
    weighted_block_transform,
)
from enterprise_math.prime_brc_shadow_staircase import shadow_staircase


def test_k8_q13_block_is_adjacent_5_6_and_totient_defect_minus_one():
    blocks = multiplier_blocks(8, 13)
    assert blocks["lower_multipliers"] == (5,)
    assert blocks["upper_multipliers"] == (6,)
    moment = totient_first_moment(8, 13)
    assert moment["signed_first_moment"] == -1
    assert moment["total_first_moment"] == 11


def test_arbitrary_integer_weights_obey_dirichlet_transform_identity():
    weights = {1: 3, 2: -2, 3: 5, 5: 7, 7: -4}
    for k, q in [(8, 13), (20, 31), (31, 53), (50, 73)]:
        result = weighted_block_transform(k, q, weights)
        assert result["lhs"] == result["rhs"]


def test_mobius_polarity_annihilates_nontrivial_q_blocks():
    for k in range(8, 120):
        for edge in shadow_staircase(k)["edges"]:
            q = edge["q"]
            result = mobius_polarity_annihilation(k, q)
            assert result["mobius_polarity_sum"] == 0


def test_totient_moment_on_every_small_shadow_edge():
    for k in range(8, 100):
        for edge in shadow_staircase(k)["edges"]:
            q = edge["q"]
            moment = totient_first_moment(k, q)
            assert moment["signed_first_moment"] == -1
