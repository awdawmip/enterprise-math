from enterprise_math.p017_p018_moment_pressure import (
    full_core_gap_envelope,
    moment_pressure_profile,
    pressure_polynomial_value,
    verify_row_column_moment_identity,
)


def test_pressure_polynomial_is_nonpositive_below_threshold_and_at_most_one_above():
    a = 10.0
    b = 20.0
    for degree in (1, 2, 3, 4, 5):
        for y in (0.0, 2.5, 5.0, 7.5, 10.0):
            assert pressure_polynomial_value(y, a, b, degree) <= 1e-12
        for y in (10.0, 12.5, 15.0, 17.5, 20.0):
            value = pressure_polynomial_value(y, a, b, degree)
            assert value <= 1.0 + 1e-12


def test_degree_hierarchy_uses_maximum_safe_lower_bound_not_last_degree():
    data = moment_pressure_profile(1192, 3, 3, 5)
    bounds = [float(row["safe_high_core_lower_bound"]) for row in data["degree_rows"]]
    assert data["selected_high_core_lower_bound"] == max(bounds)
    assert data["adaptive_pressure_majorant"] <= data["ordinary_bonferroni_sum"]


def test_bounded_row_column_log_moment_identity_at_order_three():
    # k=46 has nonzero order-3 defect but remains small enough to expand the
    # exact divisor-fiber moment columns directly.
    for degree in (1, 2):
        data = verify_row_column_moment_identity(46, 3, 2, degree)
        assert data["row_column_identity"] is True


def test_full_core_spectral_gap_envelope_improves_low_negative_factor_at_moderate_degree():
    rows = [full_core_gap_envelope(10000, degree) for degree in (2, 3, 4, 5)]
    low_losses = [float(row["low_negative_magnitude_ceiling"]) for row in rows]
    assert low_losses == sorted(low_losses, reverse=True)
    for row in rows:
        assert 0.0 < float(row["high_positive_floor"]) <= 1.0
        assert 0.0 <= float(row["high_loss_ceiling_per_unit"]) < 1.0
