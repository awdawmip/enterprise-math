from math import comb

from enterprise_math.p017_p018_padic_product_pressure import (
    padic_product_pressure_profile,
    three_term_point_defect_upper,
    verify_row_column_pressure_identity,
)


def test_three_term_point_defect_upper_is_exact_defect_plus_positive_remainder():
    for order in (1, 3, 5):
        for support_size in range(0, 20):
            data = three_term_point_defect_upper(support_size, order)
            expected_defect = (
                comb(support_size - 1, order)
                if support_size > 0 and support_size - 1 >= order
                else 0
            )
            expected_remainder = (
                comb(support_size - 1, order + 3)
                if support_size > 0 and support_size - 1 >= order + 3
                else 0
            )
            assert data["exact_defect"] == expected_defect
            assert data["upper_remainder"] == expected_remainder
            assert data["three_term_upper"] == expected_defect + expected_remainder


def test_fixed_support_order_column_reconstructs_row_product_at_nontrivial_order_three_scale():
    # k=46 already has a nonzero order-3 Bonferroni defect, while the fixed
    # four-prime column family is still small enough for a direct exact audit.
    for valuation_cap in (1, 2):
        data = verify_row_column_pressure_identity(46, 3, valuation_cap)
        assert data["row_column_identity"] is True
        assert data["factor_exponents"]


def test_valuation_precision_is_monotone_and_can_strictly_improve_forced_high_core_pressure():
    rows = [padic_product_pressure_profile(1192, 3, cap) for cap in (1, 2, 3)]

    assert [row["three_term_defect_upper"] for row in rows] == [
        rows[0]["three_term_defect_upper"]
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


def test_product_pressure_lower_bound_never_exceeds_exact_core_adaptive_correction():
    for k in (46, 82, 1192):
        for valuation_cap in (1, 2, 3):
            data = padic_product_pressure_profile(k, 3, valuation_cap)
            assert data["forced_high_core_lower_bound"] <= data["actual_high_core_correction"]
            assert data["pressure_majorant"] >= (
                data["ordinary_bonferroni_sum"] - data["actual_high_core_correction"]
            )
