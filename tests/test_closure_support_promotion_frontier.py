from enterprise_math.closure_action_support_cost import largest_single_action_support
from enterprise_math.closure_support_promotion_frontier import support_promotion_frontier


def top_action(arity: int) -> frozenset[str]:
    return largest_single_action_support(arity).support_generators


def test_perfect_top_action_frontier_points_are_exact_and_nondominated():
    expected = {
        8: ((1, 3, 1), (3, 3, 0)),
        16: ((1, 3, 2), (3, 7, 1), (7, 7, 0)),
        32: ((1, 3, 3), (3, 7, 2), (7, 15, 1), (15, 15, 0)),
    }
    for arity, vectors in expected.items():
        frontier = support_promotion_frontier(arity, top_action(arity))
        actual = tuple(
            (
                point.executable_action_count,
                point.static_state_support_count,
                point.remaining_horizon,
            )
            for point in frontier.points
        )
        assert actual == vectors
        assert frontier.all_points_nondominated


def test_fully_closed_endpoint_has_equal_state_and_action_support():
    frontier = support_promotion_frontier(16, top_action(16))
    final = frontier.points[-1]
    assert final.remaining_horizon == 0
    assert final.actions == final.state_support


def test_initial_point_is_small_action_large_future_obligation_trade():
    frontier = support_promotion_frontier(32, top_action(32))
    initial = frontier.points[0]
    assert (
        initial.executable_action_count,
        initial.static_state_support_count,
        initial.remaining_horizon,
    ) == (1, 3, 3)
