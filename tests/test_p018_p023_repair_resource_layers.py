from enterprise_math.p018_p023_repair_resource_layers import (
    minimum_global_divisor_cover,
    prime_hard_semantic_targets,
    repair_resource_layers,
)


def test_orthogonal_cover_only_witness() -> None:
    data = repair_resource_layers(18, 5, 2)
    assert data["direction_demand"] == 1
    assert data["divisor_cover"] == 2
    assert data["exact_macro_storage"] == 2
    assert data["mixed_divisor_overhead"] == 1
    assert data["residual_depth_overhead"] == 0
    assert set(data["prime_hard_targets"]) == {8, 12, 16, 18}


def test_orthogonal_depth_only_witness() -> None:
    data = repair_resource_layers(27, 5, 2)
    assert data["direction_demand"] == 2
    assert data["divisor_cover"] == 2
    assert data["exact_macro_storage"] == 3
    assert data["mixed_divisor_overhead"] == 0
    assert data["residual_depth_overhead"] == 1
    assert set(data["prime_hard_targets"]) == {8, 12, 16, 18, 20, 24, 27}
    assert minimum_global_divisor_cover(27, 5, 2)[0] == 2


def test_horizon_three_interleaved_resource_staircase() -> None:
    expected = {
        16: (1, 1, 1),
        54: (1, 2, 2),
        81: (2, 2, 2),
        96: (2, 2, 3),
        150: (2, 3, 4),
    }
    for max_state, want in expected.items():
        data = repair_resource_layers(max_state, 8, 3)
        got = (
            data["direction_demand"],
            data["divisor_cover"],
            data["exact_macro_storage"],
        )
        assert got == want


def test_prime_hard_targets_drop_prime_easy_semantics() -> None:
    hard = prime_hard_semantic_targets(27, 5, 2)
    assert 2 not in hard
    assert 4 not in hard
    assert 8 in hard
    assert 27 in hard
