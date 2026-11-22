from fractions import Fraction

from enterprise_math.p017_p018_walsh_cutoff_mixture import (
    cutoff_mixture_orientation_point,
    cutoff_mixture_profile,
    mixture_deletion_band_weight,
    mixture_divisor_tail_weight,
)
from enterprise_math.p017_p018_walsh_p2_cutoff_pareto import exact_linear_cutoff_zone


def test_point_mass_mixture_recovers_one_cutoff_world():
    k = 82
    z2, C = exact_linear_cutoff_zone(k)
    mixture = ((z2, Fraction(1, 1)),)
    data = cutoff_mixture_profile(k, mixture)
    assert data["safe_convex_recoalescence"] is True
    assert data["mixed_weighted_prime_signal"] > 0
    assert data["positive_iff_prime_exists"] is True


def test_prime_divisor_coefficients_are_cutoff_tail_probabilities():
    k = 82
    z2, C = exact_linear_cutoff_zone(k)
    mid = (z2 + C) // 2
    mixture = (
        (z2, Fraction(1, 4)),
        (mid, Fraction(1, 2)),
        (C, Fraction(1, 4)),
    )
    assert mixture_divisor_tail_weight(k, 1, mixture) == 1
    # Any divisor whose largest prime has entered only at the final branch gets
    # exactly the final branch mass.
    assert mixture_divisor_tail_weight(k, C if C % 2 == 1 else C - 1, mixture) in (
        Fraction(0, 1), Fraction(1, 4)
    )

    # Find one basin prime orientation and force the exact divisor-kernel audit.
    found = None
    for radius in range(1, k):
        for orientation in ("upper", "lower"):
            try:
                row = cutoff_mixture_orientation_point(k, radius, orientation, mixture)
            except ValueError:
                continue
            if row["target_prime"]:
                found = row
                break
        if found is not None:
            break
    assert found is not None
    assert found["prime_divisor_kernel_reconstruction"] == found["mixed_orientation_weight"]


def test_deletion_coefficient_is_band_mass_between_divisor_visibility_and_high_prime_absorption():
    k = 82
    z2, C = exact_linear_cutoff_zone(k)
    mid = (z2 + C) // 2
    mixture = (
        (z2, Fraction(1, 3)),
        (mid, Fraction(1, 3)),
        (C, Fraction(1, 3)),
    )
    # d=1 is visible in every world.  A high p above mid but at/below C survives
    # as a deletion in the first two worlds and is absorbed in the final world.
    p = next(value for value in range(mid + 1, C + 1) if value % 2 == 1)
    assert mixture_deletion_band_weight(k, 1, p, mixture) == Fraction(2, 3)


def test_convex_smooth_shadow_main_is_exact_branch_average():
    for k in (82, 862):
        z2, C = exact_linear_cutoff_zone(k)
        mid = (z2 + C) // 2
        mixture = (
            (z2, Fraction(1, 3)),
            (mid, Fraction(1, 3)),
            (C, Fraction(1, 3)),
        )
        data = cutoff_mixture_profile(k, mixture)
        direct = sum(weight * psi for _z, weight, psi in data["smooth_shadow_branch_rows"])
        assert direct == data["one_orientation_convex_smooth_shadow_main"]
        assert data["symmetric_convex_smooth_shadow_main"] == 2 * direct
        assert data["mixed_weighted_prime_signal"] > 0
