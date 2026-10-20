from enterprise_math.p017_p018_walsh_symmetric_core_conductor_collapse import (
    selected_odd_support_vanishes,
    symmetric_core_fixed_total_collapse,
)


def test_odd_support_selected_tent_columns_vanish_by_reflection():
    for k, m in ((46, 3), (46, 5), (82, 7), (100, 11)):
        if k * (k + 1) % m:
            data = selected_odd_support_vanishes(k, m)
            assert data["odd_support_vanishes_by_tent_symmetry"] is True
            assert data["selected_modulus_tent"] == 0


def test_reusable_symmetric_split_sum_collapses_to_one_total_conductor():
    cases = ((46, 15), (46, 21), (82, 15), (82, 35), (100, 21))
    for k, m in cases:
        data = symmetric_core_fixed_total_collapse(k, m)
        assert data["fixed_total_symmetric_core_collapse"] is True
        assert data["symmetric_split_sum"] == data["selected_total_conductor_column"]


def test_odd_reusable_total_conductor_collapses_to_zero():
    # Products of three transverse primes, when they fit below C.
    for k, m in ((200, 3 * 5 * 7), (500, 3 * 5 * 11)):
        if m <= (k - 1) // 2 and k * (k + 1) % m:
            data = symmetric_core_fixed_total_collapse(k, m)
            assert data["support_parity"] == "ODD"
            assert data["selected_total_conductor_column"] == 0
            assert data["odd_support_zero"] is True
