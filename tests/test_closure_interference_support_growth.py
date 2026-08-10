from enterprise_math.closure_action_support_cost import largest_single_action_support
from enterprise_math.closure_interference_support_growth import (
    interference_support_growth,
    support_growth_layers,
)


def top_action(arity: int) -> frozenset[str]:
    report = largest_single_action_support(arity)
    return report.support_generators


def test_perfect_top_action_support_grows_one_dependency_layer_at_a_time():
    expected = {
        8: (1, 3),
        16: (1, 3, 7),
        32: (1, 3, 7, 15),
    }
    for arity, sizes in expected.items():
        report = interference_support_growth(arity, top_action(arity))
        assert report.layer_sizes == sizes
        assert report.equals_dependency_closure
        assert len(report.fixed_point) == arity // 2 - 1


def test_promoting_static_support_to_actions_can_force_another_hidden_layer():
    assert not interference_support_growth(8, top_action(8)).first_promotion_legality_collision
    assert interference_support_growth(16, top_action(16)).first_promotion_legality_collision
    assert interference_support_growth(32, top_action(32)).first_promotion_legality_collision


def test_fixed_point_is_stable():
    report = interference_support_growth(16, top_action(16))
    layers = support_growth_layers(16, report.fixed_point)
    assert layers == (report.fixed_point,)
