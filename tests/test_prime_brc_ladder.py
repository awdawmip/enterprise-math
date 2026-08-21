from fractions import Fraction

from enterprise_math.prime_brc_ladder import (
    midpoint_absorption_minus,
    midpoint_absorption_plus,
    mirror_critical_bilinear_carry,
    mirror_phase_ladder,
    positive_entry_factor_lock,
)


def test_plus_defect_is_absorbing_under_midpoint_divisors():
    # Defect +1: 2*5-3-6=1, and 5 is divisible by 5.
    data = midpoint_absorption_plus(3, 5, 6, 5)
    assert data["output"] == (0, 1, 1)
    assert data["defect"] == 1


def test_minus_defect_is_absorbing_under_upper_adjacent_midpoint_divisors():
    # Defect -1: 2*4-2-7=-1, and M+1=5 is divisible by 5.
    data = midpoint_absorption_minus(2, 4, 7, 5)
    assert data["output"] == (0, 0, 1)
    assert data["defect"] == -1


def test_mirror_ladder_k31_r7():
    # 985=5*197, 999=3^3*37 around M=992.
    lo = mirror_phase_ladder(31, 7, 5, "lower")
    hi = mirror_phase_ladder(31, 7, 3, "upper")
    assert lo["chi"] == 0
    assert lo["ladder_index"] == 1
    assert lo["half_window_bias"] == -2
    assert lo["width"] == 12
    assert lo["phase"] == Fraction(5, 12)
    assert hi["chi"] == -1
    assert hi["ladder_index"] == 3
    assert hi["half_window_bias"] == 5
    assert hi["width"] == 21
    assert hi["phase"] == Fraction(13, 21)


def test_critical_bilinear_carry_k31_r7():
    data = mirror_critical_bilinear_carry(31, 7, 5, 3)
    assert data["integer_margin"] == 18
    assert data["product_margin"] == 9
    assert data["phase_margin"] == Fraction(1, 28)


def test_positive_entry_locks_full_suffix_factor_path():
    # k=36, M=1332, lower r=1 gives 1331=11^3.
    # The first 11 is a +1 lower midpoint entry; the remaining 11,11 divide
    # the successive midpoint states, so all downstream defects stay +1.
    data = positive_entry_factor_lock(36, 1, 11, (11, 11))
    assert data["midpoint_states"] == (121, 11, 1)
    assert data["defect_trace"] == (1, 1, 1)
