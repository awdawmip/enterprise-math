from enterprise_math.closure_support_radius_volume import support_radius_volume_extremes


def test_binary_support_radius_volume_bounds_are_sharp():
    for horizon in range(0, 5):
        report = support_radius_volume_extremes(horizon)
        assert report.lower_bound == horizon + 1
        assert report.upper_bound == 2 ** (horizon + 1) - 1
        assert report.sequential_support_count == report.lower_bound
        assert report.balanced_support_count == report.upper_bound
        assert report.lower_sharp
        assert report.upper_sharp


def test_same_horizon_can_have_exponentially_different_support_volume():
    report = support_radius_volume_extremes(4)
    assert report.sequential_support_count == 5
    assert report.balanced_support_count == 31
    assert report.sequential_arity == 7
    assert report.balanced_arity == 64
