from fractions import Fraction

from enterprise_math.p022_barlow_franel_boundary_double_horizon import (
    double_horizon_exact_identity,
    double_horizon_integer_kernel,
    double_horizon_modular_certificate,
    double_horizon_old_integer_ratio,
    double_horizon_prefactor,
    sign_free_companion_kernel,
    twin_boundary_double_horizon_certificate,
)


def test_double_horizon_kernel_has_expected_initial_values() -> None:
    assert [double_horizon_integer_kernel(M) for M in range(1, 6)] == [
        15,
        1351,
        154374,
        19594887,
        2639533390,
    ]


def test_four_step_terminating_transform_is_exact() -> None:
    for M in range(1, 9):
        tail, kernel, transformed = double_horizon_exact_identity(M)
        assert tail == transformed
        assert transformed == double_horizon_prefactor(M) * kernel

    assert double_horizon_exact_identity(1)[0] == Fraction(10, 9)
    assert double_horizon_exact_identity(2)[0] == Fraction(386, 315)
    assert double_horizon_exact_identity(3)[0] == Fraction(4678, 3465)


def test_double_horizon_kernel_is_unit_equivalent_to_existing_integer_kernel() -> None:
    expected_ratios = {
        1: Fraction(3, 2),
        2: Fraction(7, 2),
        3: Fraction(33, 4),
        4: Fraction(39, 2),
        5: Fraction(323, 7),
    }
    for M, expected in expected_ratios.items():
        assert double_horizon_old_integer_ratio(M) == expected


def test_sign_free_companion_has_same_prime_residue() -> None:
    expected = {
        1: (5, 0, 0, 0),
        2: (11, 9, 9, 1),
        3: (17, 14, 14, 12),
        4: (23, 14, 14, 19),
        5: (29, 22, 22, 24),
        25: (149, 0, 0, 0),
    }
    for M, row in expected.items():
        assert double_horizon_modular_certificate(M) == row
        assert double_horizon_integer_kernel(M) % row[0] == (
            sign_free_companion_kernel(M) % row[0]
        )


def test_known_p149_zero_survives_but_is_not_a_three_divisible_boundary() -> None:
    prime, kernel, companion, old_integer = double_horizon_modular_certificate(25)
    assert prime == 149
    assert kernel == companion == old_integer == 0
    assert 25 % 3 == 1


def test_actual_twin_boundary_samples_are_nonzero_regression_only() -> None:
    assert twin_boundary_double_horizon_certificate(1) == (17, 6, 3, 14, 14)
    assert twin_boundary_double_horizon_certificate(5) == (89, 30, 54, 74, 74)
    assert twin_boundary_double_horizon_certificate(6) == (107, 36, 77, 51, 51)
