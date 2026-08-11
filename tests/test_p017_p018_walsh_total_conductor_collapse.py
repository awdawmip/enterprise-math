from enterprise_math.p017_p018_walsh_total_conductor_collapse import (
    fixed_total_biprimitive_collapse,
    total_conductor_aggregate_collapse,
)


def test_fixed_total_split_sum_collapses_to_selected_walsh_column():
    cases = (
        (10, 21),
        (11, 35),
        (17, 35),
        (29, 15),
    )
    for k, conductor in cases:
        data = fixed_total_biprimitive_collapse(k, conductor)
        assert data["fixed_total_conductor_collapse"] is True
        assert data["split_biprimitive_sum"] == data["selected_modulus_walsh_tent"]


def test_full_low_product_plane_collapses_to_one_conductor_axis():
    for k in (10, 11, 17, 23):
        data = total_conductor_aggregate_collapse(k)
        assert data["total_conductor_collapse"] is True
        assert data["divisor_plane_aggregate"] == data["one_conductor_aggregate"]


def test_truncated_product_plane_has_same_collapse():
    for k, cutoff in ((17, 10), (23, 12), (29, 15)):
        data = total_conductor_aggregate_collapse(k, cutoff)
        assert data["total_conductor_collapse"] is True
        assert data["divisor_plane_aggregate"] == data["one_conductor_aggregate"]
