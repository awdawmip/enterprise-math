from itertools import combinations, product
from math import comb, log

from enterprise_math.p017_p018_bernstein_boundary_carry_recovery import (
    bernstein_bulk_shadow_diagnostic,
    bernstein_divisor_kernel,
    carry_only_recovery_parameters,
)
from enterprise_math.p017_p018_bernstein_core_recovery import bernstein_tail_value


def _divisor_rows(valuations):
    primes = tuple(sorted(valuations))
    for size in range(1, len(primes) + 1):
        for support in combinations(primes, size):
            for exponents in product(
                *(range(1, valuations[p] + 1) for p in support)
            ):
                divisor = 1
                for prime, exponent in zip(support, exponents):
                    divisor *= prime**exponent
                yield divisor


def test_distinct_prime_mixed_difference_kernel_reassembles_one_row():
    # Pure combinatorial audit of
    #   E_m(c) R_n(log C/log X) = sum_{D|C} K_{m,n}(D)
    # for one four-support row with a nontrivial p-adic level.
    k = 100
    order = 3
    degree = 32
    threshold = 21
    valuations = {3: 2, 5: 1, 7: 1, 11: 1}
    core = 1
    for prime, exponent in valuations.items():
        core *= prime**exponent
    xmax = k * (k + 2) - 1
    defect = comb(len(valuations) - 1, order)
    direct = defect * bernstein_tail_value(
        log(core) / log(xmax), degree, threshold
    )
    reconstructed = sum(
        bernstein_divisor_kernel(k, order, divisor, degree, threshold)
        for divisor in _divisor_rows(valuations)
    )
    assert abs(reconstructed - direct) < 1e-12


def test_carry_only_recovery_parameters_stay_inside_quarter_unit_budget():
    for k in (46, 82, 1192, 8191):
        data = carry_only_recovery_parameters(k, 3)
        if data["exact_high_core_correction_is_zero"]:
            assert data["carry_only_error_ceiling"] == 0.0
            continue
        assert data["carry_only_error_ceiling"] <= 0.25
        assert data["bernstein_degree"] == 16 * data["epsilon_exponent"]
        assert 1 <= data["bernstein_threshold"] <= data["bernstein_degree"]


def test_floor_bulk_collapses_to_low_band_shadow_and_is_tiny():
    # k=1192 has a genuine nonzero order-3 low shadow (the four-prime core
    # 3*5*7*11=1155), so this is not a vacuous zero-bulk regression.
    data = bernstein_bulk_shadow_diagnostic(1192, 3)
    assert data["bulk_shadow_nonnegative"] is True
    assert data["bulk_shadow_value"] > 0.0
    assert data["bulk_shadow_value"] <= data["bulk_shadow_bound"]
