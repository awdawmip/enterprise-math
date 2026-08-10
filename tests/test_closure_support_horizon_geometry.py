from math import log2

from enterprise_math.closure_action_support_cost import largest_single_action_support
from enterprise_math.closure_support_horizon_geometry import (
    reverse_dependency_distances,
    support_horizon_geometry,
)


def top_action(arity: int) -> frozenset[str]:
    return largest_single_action_support(arity).support_generators


def test_support_layers_are_exact_reverse_dependency_balls():
    for arity in (8, 16, 32):
        report = support_horizon_geometry(arity, top_action(arity))
        assert report.ball_identity_verified
        assert report.horizon == int(log2(arity)) - 2
        assert report.layer_sizes == tuple(2 ** (t + 1) - 1 for t in range(report.horizon + 1))


def test_distance_map_has_expected_shells_for_sixteen_way_top_action():
    distances = reverse_dependency_distances(16, top_action(16))
    counts = {
        depth: sum(1 for value in distances.values() if value == depth)
        for depth in set(distances.values())
    }
    assert counts == {0: 1, 1: 2, 2: 4}


def test_first_layer_actions_have_zero_support_horizon():
    report = support_horizon_geometry(8, frozenset({"h1", "h3"}))
    assert report.horizon == 0
    assert report.layer_sizes == (2,)
