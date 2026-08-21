from fractions import Fraction

from enterprise_math.prime_brc_phase import (
    complementary_collapse_residuals,
    defect,
    defect_path_flattening,
    global_least_factor_phase_sum,
    lower_midpoint_least_factor_event,
    mirror_phase_crossing,
    phase_path_flattening,
    square_basin_frame,
    square_midpoint_defect,
    square_quotient_phase,
    ternary_defect_quotient,
    transverse_prime_carry_bridge,
)


def test_square_basin_unit_defect_and_complementary_residuals():
    frame = square_basin_frame(31)
    assert frame == {
        "k": 31,
        "lower": 961,
        "center": 992,
        "upper": 1024,
        "gap": 63,
        "midpoint_defect": -1,
    }
    assert complementary_collapse_residuals(31, 7, 0, 1) == (24, -25)
    assert complementary_collapse_residuals(31, 7, 1, 0) == (-39, 38)


def test_floor_quotient_preserves_ternary_defect_on_small_exact_domain():
    for lower in range(0, 12):
        for middle in range(lower, 13):
            for upper in range(middle, 14):
                if defect(lower, middle, upper) not in (-1, 0, 1):
                    continue
                for divisor in range(2, 9):
                    data = ternary_defect_quotient(lower, middle, upper, divisor)
                    assert data["output_defect"] in (-1, 0, 1)


def test_ternary_readout_is_not_an_autonomous_markov_state():
    # Same input defect -1, same divisor 2, different residue contexts.
    first = ternary_defect_quotient(0, 0, 1, 2)
    second = ternary_defect_quotient(0, 1, 3, 2)
    assert first["input_defect"] == second["input_defect"] == -1
    assert first["output_defect"] == 0
    assert second["output_defect"] == -1


def test_defect_path_flattening_depends_only_on_total_divisor():
    data = defect_path_flattening(961, 992, 1024, (3, 3, 37))
    assert data["total_divisor"] == 333
    assert data["quotient_trace"][-1] == data["direct_final"]
    assert data["final_defect"] in (-1, 0, 1)


def test_quotient_phase_strictly_leads_continuous_position():
    lower = square_quotient_phase(31, 985, 5)
    upper = square_quotient_phase(31, 999, 3)
    assert lower["phase"] == Fraction(5, 12)
    assert lower["continuous_position"] == Fraction(8, 21)
    assert lower["phase"] > lower["continuous_position"]
    assert upper["phase"] == Fraction(13, 21)
    assert upper["continuous_position"] == Fraction(38, 63)
    assert upper["phase"] > upper["continuous_position"]


def test_phase_path_flattening_for_true_factor_path():
    data = phase_path_flattening(961, 1024, 999, (3, 3))
    assert data["total_divisor"] == 9
    assert data["path_phase"] == data["direct_phase"] == Fraction(5, 7)


def test_transverse_prime_carry_bridge_recovers_directional_bits():
    bridge = transverse_prime_carry_bridge(31, 23)
    assert bridge["t"] == 8
    assert bridge["center_remainder"] == 3
    assert bridge["lower_carry_bit"] == 1
    assert bridge["upper_carry_bit"] == 0
    assert bridge["kappa"] == 1
    assert bridge["chi"] == 1
    assert square_midpoint_defect(31, 23) == 1


def test_positive_midpoint_carry_is_one_exact_half_window_bit():
    event = lower_midpoint_least_factor_event(31, 23)
    assert event["radius"] == 3
    assert event["state"] == 989
    assert event["cofactor"] == 43
    assert event["phase_width"] == 3
    assert event["phase"] == Fraction(2, 3)
    assert event["half_bias"] == 1
    assert event["p_rough_cofactor"] is True
    assert event["least_factor_event"] is True
    assert 23 >= 2 * 3 + 3


def test_mirror_phase_crossing_exact_counter_identity():
    # 985=5*197 and 999=3^3*37 around M=992.
    data = mirror_phase_crossing(31, 7, 5, 3)
    assert data["lower_phase"] == Fraction(5, 12)
    assert data["upper_phase"] == Fraction(13, 21)
    assert data["phase_sum"] == Fraction(29, 28)
    assert data["first_counter_margin"] >= 1
    assert data["second_counter_margin"] >= 1
    assert data["product_margin"] >= 1


def test_global_phase_capacity_is_diagnostic_not_promoted_theorem():
    data = global_least_factor_phase_sum(5)
    assert data["phase_sum"] == Fraction(9, 2)
    assert data["capacity"] == 5
    assert data["phase_capacity_holds"] is True
    assert data["prime_count"] == 2
    assert data["composite_count"] == 8
    assert data["status"] == "COMPUTATIONAL_DIAGNOSTIC_NOT_THEOREM"
