from enterprise_math.p017_p018_walsh_symmetric_core_cubic_descent import (
    symmetric_core_cubic_descent,
)


def test_reusable_core_descends_below_one_third_and_becomes_single_use():
    cases = ((46, 15), (46, 21), (82, 15), (82, 35), (100, 21))
    for k, m in cases:
        data = symmetric_core_cubic_descent(k, m)
        assert data["strict_one_third_contraction"] is True
        assert 3 * data["child_scale_r"] < k
        assert data["child_conductor_exceeds_child_scale"] is True
        assert data["child_root_classes_single_use"] is True
        assert data["parent_selected_column"] == data["euclidean_reconstruction"]
