from enterprise_math.p017_p018_core_adaptive_bonferroni import core_adaptive_signed_profile
from enterprise_math.p017_p018_moment_precision_ceiling import (
    logarithmic_degree,
    logarithmic_degree_precision_ceiling,
    universal_full_valuation_cap,
)
from enterprise_math.p017_p018_moment_pressure import moment_pressure_profile


def test_logarithmic_degree_is_least_power_of_two_ceiling():
    for k in range(3, 200):
        degree = logarithmic_degree(k)
        assert 2**degree >= k
        assert 2 ** (degree - 1) < k


def test_universal_full_valuation_cap_reaches_every_odd_prime_power_layer():
    for k in (3, 10, 46, 1192):
        cap = universal_full_valuation_cap(k)
        xmax = k * (k + 2) - 1
        assert 3**cap <= xmax
        assert 3 ** (cap + 1) > xmax


def test_simple_precision_ceiling_dominates_exact_support_depth_envelope():
    for k in (46, 1192, 8191):
        data = logarithmic_degree_precision_ceiling(k, 3)
        assert data["exact_support_depth_information_loss_ceiling"] <= data["simple_information_loss_ceiling"]
        assert data["simple_information_loss_ceiling"] >= 0.0


def test_actual_full_core_information_loss_is_below_logarithmic_degree_ceiling():
    k = 1192
    order = 3
    ceiling = logarithmic_degree_precision_ceiling(k, order)
    degree = int(ceiling["logarithmic_degree"])
    cap = int(ceiling["universal_full_valuation_cap"])

    moment = moment_pressure_profile(k, order, cap, degree)
    core = core_adaptive_signed_profile(k, order)
    actual_high = float(core["high_core_defect_correction"])
    selected_degree_row = next(
        row for row in moment["degree_rows"] if int(row["degree"]) == degree
    )
    lower = float(selected_degree_row["safe_high_core_lower_bound"])
    loss = actual_high - lower

    assert loss >= -1e-8
    assert loss <= float(ceiling["exact_support_depth_information_loss_ceiling"]) + 1e-7
