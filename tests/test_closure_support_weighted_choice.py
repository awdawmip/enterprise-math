from enterprise_math.closure_action_support_cost import largest_single_action_support
from enterprise_math.closure_support_weighted_choice import weighted_promotion_choice


def top_action(arity: int) -> frozenset[str]:
    return largest_single_action_support(arity).support_generators


def test_adjacent_switch_thresholds_are_exact_for_perfect_thirty_two_way_frontier():
    choice = weighted_promotion_choice(
        32,
        top_action(32),
        alpha=4,
        beta=1,
        gamma=1,
    )
    assert choice.adjacent_switch_thresholds == (12, 24, 32)


def test_each_frontier_depth_can_be_workload_optimal_for_suitable_weights():
    actions = top_action(32)
    expected = {
        5: (0,),
        15: (1,),
        26: (2,),
        40: (3,),
    }
    for gamma, optimum in expected.items():
        choice = weighted_promotion_choice(
            32,
            actions,
            alpha=4,
            beta=1,
            gamma=gamma,
        )
        assert choice.optimal_depths == optimum


def test_exact_switch_value_can_create_tie():
    choice = weighted_promotion_choice(
        32,
        top_action(32),
        alpha=4,
        beta=1,
        gamma=12,
    )
    assert choice.optimal_depths == (0, 1)
    assert choice.costs[0] == choice.costs[1]


def test_nonpositive_weights_rejected():
    actions = top_action(16)
    for field in ("alpha", "beta", "gamma"):
        kwargs = {"alpha": 1, "beta": 1, "gamma": 1}
        kwargs[field] = 0
        try:
            weighted_promotion_choice(16, actions, **kwargs)
        except ValueError:
            pass
        else:
            raise AssertionError(f"{field}=0 should be rejected")
