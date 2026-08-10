from enterprise_math.p017_p018_walsh_symmetric_frustration import (
    canonical_triangle_tradeoffs,
    empty_high_high_triangle_cost,
)


def test_triangle_lower_bound_holds_for_varied_real_coefficients():
    for left, right in ((-3.0, 2.0), (-1.0, -1.0), (-1.0, 1.0), (0.0, 0.0), (2.5, -0.25)):
        data = empty_high_high_triangle_cost(left, right)
        assert data["triangle_l1_cost"] >= 1.0 - 1e-12
        assert data["unit_frustration_lower_bound"] is True


def test_canonical_tradeoffs_all_saturate_the_same_irreducible_unit_cost():
    rows = canonical_triangle_tradeoffs()
    assert len(rows) == 3
    for row in rows:
        assert abs(row["triangle_l1_cost"] - 1.0) < 1e-12

    kill_pure = rows[0]
    assert kill_pure["pure_left_cost"] == 0.0
    assert kill_pure["pure_right_cost"] == 0.0
    assert kill_pure["mixed_cost"] == 1.0

    kill_mixed = rows[1]
    assert kill_mixed["mixed_cost"] == 0.0
    assert kill_mixed["pure_left_cost"] + kill_mixed["pure_right_cost"] == 1.0

    split = rows[2]
    assert split["mixed_cost"] == 0.0
    assert split["pure_left_cost"] == 0.5
    assert split["pure_right_cost"] == 0.5
