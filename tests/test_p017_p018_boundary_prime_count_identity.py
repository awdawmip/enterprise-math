from enterprise_math.p017_p018_boundary_prime_count_identity import (
    boundary_carry_prime_count_diagnostic,
    dyadic_bulk_axis_count,
    terminal_boundary_structure,
    terminal_core_exactness_diagnostic,
)


def test_terminal_bulk_gap_is_dyadic_axis_plus_anchor_parity_carry():
    for k in (5, 9, 46, 82, 1192):
        data = terminal_boundary_structure(k)
        assert data["terminal_bulk_gap"] == (
            data["dyadic_bulk_axis_count"]
            + data["anchor_parity_boundary_carry"]
        )
        assert data["signed_state_count_from_bulk_plus_parity"] >= 0


def test_single_use_terminal_order_removes_all_low_core_bonferroni_defect():
    for k in (46, 82, 1192):
        data = terminal_core_exactness_diagnostic(k)
        assert data["terminal_core_adaptive_exact"] is True
        assert data["residual_core_excess"] == 0
        assert data["exact_composite_union"] == (
            data["ordinary_bonferroni_sum"] - data["high_core_correction"]
        )


def test_full_mobius_boundary_carry_plus_dyadic_axis_is_exact_prime_count():
    for k in (5, 9, 46):
        data = boundary_carry_prime_count_diagnostic(k)
        assert data["boundary_prime_count_identity"] is True
        assert data["predicted_prime_count"] == data["actual_prime_count"]


def test_boundary_carry_sum_is_not_naively_nonnegative():
    # Explicit finite negative boundary: between 5^2 and 6^2 there are only
    # two primes, while the small-shadow dyadic bulk axis has size three.
    data = boundary_carry_prime_count_diagnostic(5)
    assert dyadic_bulk_axis_count(5) == 3
    assert data["actual_prime_count"] == 2
    assert data["full_boundary_mobius_carry_sum"] == -1
