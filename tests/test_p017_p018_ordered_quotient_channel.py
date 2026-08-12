from enterprise_math.p017_p018_ordered_quotient_channel import (
    one_dimensional_ordered_transport,
    ordered_quotient_row,
)
from enterprise_math.p017_p018_root_p3_ordered_mobius_buchstab import fourth_root_ordered_transport


def test_one_dimensional_scan_matches_ordered_buchstab_transport():
    for k in (8, 17, 31, 64, 100, 257):
        scan = one_dimensional_ordered_transport(k)
        ordered = fourth_root_ordered_transport(k)
        assert scan["ordered_transport_sum"] == ordered["ordered_transport_sum"]
        assert scan["lower_band_has_no_positive_transport"] is True


def test_every_active_lower_band_row_is_negative():
    for k in (31, 64, 100, 257):
        data = one_dimensional_ordered_transport(k)
        for row in data["active_rows"]:
            q = row["q"]
            if q**3 <= k**4:
                assert row["ordered_transport_contribution"] == -1


def test_positive_rows_force_exact_cubic_band_inequality():
    found = False
    for k in range(20, 120):
        data = one_dimensional_ordered_transport(k)
        for row in data["active_rows"]:
            if row["ordered_transport_contribution"] > 0:
                found = True
                assert row["q"] ** 3 > k**4
                assert row["mobius"] == 1
    assert found is True


def test_k1000_scan_has_same_total_as_state_ordered_transport():
    scan = one_dimensional_ordered_transport(1000)
    ordered = fourth_root_ordered_transport(1000)
    assert scan["fourth_root_cutoff"] == 31
    assert scan["ordered_transport_sum"] == ordered["ordered_transport_sum"]
