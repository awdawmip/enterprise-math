from enterprise_math.p017_p018_walsh_total_conductor_child_atlas import (
    child_conductor_family,
    conductor_child_bijection,
    total_conductor_child_atlas_sum,
)


def test_parent_conductor_descends_to_strict_half_scale_large_divisor_child():
    cases = ((46, 21), (46, 35), (82, 15), (82, 69), (100, 91))
    for k, m in cases:
        data = conductor_child_bijection(k, m)
        assert data["child_strictly_below_half_parent"] is True
        assert data["conductor_divides_gap"] is True
        assert data["conductor_exceeds_child"] is True
        assert m in data["child_conductor_family"]


def test_child_family_reconstructs_all_declared_large_divisors():
    assert child_conductor_family(46, 4) == (21,)
    assert 39 in child_conductor_family(46, 7)
    assert 35 in child_conductor_family(46, 11)


def test_grouped_child_atlas_reconstructs_parent_selected_sum():
    families = (
        (46, (21, 33, 35, 39)),
        (82, (15, 33, 35, 51, 55, 57, 65, 69)),
    )
    for k, conductors in families:
        data = total_conductor_child_atlas_sum(k, conductors)
        assert data["strict_half_scale_child_atlas"] is True
        assert data["parent_selected_sum"] == data["child_atlas_sum"]
        assert all(2 * row["child_scale_r"] < k for row in data["rows"])
