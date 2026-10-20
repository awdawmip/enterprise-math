from math import comb

from enterprise_math.p017_p018_padic_product_pressure import (
    adaptive_support_tail_upper,
    alternating_tail_point_defect_upper,
    padic_product_pressure_profile,
    three_term_point_defect_upper,
    verify_row_column_pressure_identity,
)


def test_odd_support_tail_upper_is_exact_defect_plus_positive_remainder():
    for order in (1, 3, 5):
        for tail_terms in (1, 3, 5):
            for support_size in range(0, 24):
                data = alternating_tail_point_defect_upper(
                    support_size,
                    order,
                    tail_terms,
                )
                end_order = order + tail_terms
                expected_defect = (
                    comb(support_size - 1, order)
                    if support_size > 0 and support_size - 1 >= order
                    else 0
                )
                expected_remainder = (
                    comb(support_size - 1, end_order)
                    if support_size > 0 and support_size - 1 >= end_order
                    else 0
                )
                assert data["exact_defect"] == expected_defect
                assert data["upper_remainder"] == expected_remainder
                assert data["support_tail_upper"] == expected_defect + expected_remainder


def test_three_term_compatibility_wrapper_matches_general_tail_identity():
    for order in (1, 3, 5):
        for support_size in range(0, 20):
            direct = alternating_tail_point_defect_upper(support_size, order, 3)
            wrapped = three_term_point_defect_upper(support_size, order)
            assert wrapped["exact_defect"] == direct["exact_defect"]
            assert wrapped["upper_remainder"] == direct["upper_remainder"]
            assert wrapped["three_term_upper"] == direct["support_tail_upper"]


def test_fixed_support_order_column_reconstructs_row_product_at_nontrivial_order_three_scale():
    # k=46 already has a nonzero order-3 Bonferroni defect, while the fixed
    # four-prime column family is still small enough for a direct exact audit.
    for valuation_cap in (1, 2):
        data = verify_row_column_pressure_identity(46, 3, valuation_cap)
        assert data["row_column_identity"] is True
        assert data["factor_exponents"]


def test_valuation_precision_is_monotone_and_can_strictly_improve_forced_high_core_pressure():
    rows = [padic_product_pressure_profile(1192, 3, cap) for cap in (1, 2, 3)]

    assert [row["support_tail_defect_upper"] for row in rows] == [
        rows[0]["support_tail_defect_upper"]
    ] * 3
    assert rows[0]["pressure_product"] <= rows[1]["pressure_product"] <= rows[2]["pressure_product"]
    assert (
        rows[0]["forced_high_core_lower_bound"]
        <= rows[1]["forced_high_core_lower_bound"]
        <= rows[2]["forced_high_core_lower_bound"]
    )
    assert rows[0]["forced_high_core_lower_bound"] < rows[1]["forced_high_core_lower_bound"]
    assert rows[0]["pressure_certificate"] is True
    assert rows[1]["pressure_certificate"] is True
    assert rows[2]["pressure_certificate"] is True


def test_adaptive_support_tail_uses_minimum_of_safe_nonmonotone_candidates():
    wide = padic_product_pressure_profile(1192, 3, 1, support_tail_terms=5)
    selected = adaptive_support_tail_upper(
        tuple(wide["support_moments"]),
        3,
        (1, 3, 5),
    )
    values = tuple(int(row["defect_upper"]) for row in selected["candidate_rows"])
    assert selected["selected_defect_upper"] == min(values)
    assert selected["selected_defect_upper"] >= wide["exact_bonferroni_defect"]


def test_product_pressure_lower_bound_never_exceeds_exact_core_adaptive_correction():
    for k in (46, 82, 1192):
        for valuation_cap in (1, 2, 3):
            data = padic_product_pressure_profile(k, 3, valuation_cap)
            assert data["forced_high_core_lower_bound"] <= data["actual_high_core_correction"]
            assert data["forced_high_core_lower_bound_exact_defect"] <= data["actual_high_core_correction"]
            assert data["forced_high_core_lower_bound"] <= data["forced_high_core_lower_bound_exact_defect"]
            assert data["pressure_majorant"] >= (
                data["ordinary_bonferroni_sum"] - data["actual_high_core_correction"]
            )
