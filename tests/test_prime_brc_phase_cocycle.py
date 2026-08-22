from fractions import Fraction

from enterprise_math.prime_brc_phase_cocycle import (
    divisor_phase,
    kappa_chi_not_phase_complete_witness,
    phase_cocycle,
    phase_refinement,
    terminal_credit_decomposition,
)


def test_true_divisor_refinement_is_nonnegative():
    # 315=3^2*5*7 inside (17^2,18^2)=(289,324).
    data = phase_refinement(289, 324, 315, 3, 9)
    assert data["fine_phase"] >= data["coarse_phase"]
    data2 = phase_refinement(289, 324, 315, 9, 45)
    assert data2["fine_phase"] >= data2["coarse_phase"]


def test_phase_cocycle_is_additive():
    data = phase_cocycle(289, 324, 315, (1, 3, 9, 45, 315))
    assert all(c >= 0 for c in data["credits"])
    assert sum(data["credits"], Fraction(0, 1)) == data["total_credit"]
    assert data["phases"][-1] == 1


def test_factor_order_has_same_endpoint_credit():
    # Two different genuine factor orders of 315.
    first = terminal_credit_decomposition(289, 324, 315, (3, 3, 5, 7))
    second = terminal_credit_decomposition(289, 324, 315, (7, 5, 3, 3))
    assert first["total_credit"] == second["total_credit"]
    assert first["total_credit"] == 1 - Fraction(315 - 289, 324 - 289)


def test_divisor_phase_starts_at_continuous_position():
    assert divisor_phase(289, 324, 315, 1) == Fraction(26, 35)


def test_kappa_chi_not_quantitative_phase_complete():
    data = kappa_chi_not_phase_complete_witness()
    assert (data["kappa"], data["chi"]) == (0, 0)
    assert data["phase_a"] != data["phase_b"]
    assert data["lead_a"] != data["lead_b"]
