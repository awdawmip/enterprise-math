from fractions import Fraction

import pytest

from enterprise_math.p022_barlow_franel_boundary_rank2_pullback import (
    cusp_transfer_determinant_characters,
    cusp_transfer_matrices,
    even_franel_rank2_hypergeometric,
    exact_even_franel_rank2_identity,
    franel_cusp_states,
    franel_rank2_pullback_coefficient,
    one_eighth_to_minus_one_transfer,
    rank2_boundary_coefficient_identity,
    rank2_pullback_franel_hasse_coefficients,
)
from enterprise_math.p022_barlow_low_order_identifiability import triple_moment_factor


def test_exact_rank2_pullback_coefficients() -> None:
    for n in range(16):
        assert franel_rank2_pullback_coefficient(n) == triple_moment_factor(n)


def test_exact_even_franel_3f2_identity() -> None:
    assert even_franel_rank2_hypergeometric(0) == Fraction(1)
    for M in range(11):
        assert exact_even_franel_rank2_identity(M)


def test_finite_rank2_pullback_reconstructs_franel_hasse() -> None:
    for prime in (5, 11, 17, 23, 29, 41, 53, 71):
        coefficients = rank2_pullback_franel_hasse_coefficients(prime)
        assert len(coefficients) == prime
        assert coefficients[0] == 1
        assert coefficients[1] == 2


def test_boundary_coefficient_specialization() -> None:
    for prime in (5, 11, 17, 23, 29, 41, 53, 71, 149):
        M, value = rank2_boundary_coefficient_identity(prime)
        assert value == triple_moment_factor(2 * M) % prime


def test_cusp_states_and_two_by_two_transfers() -> None:
    for prime in (5, 11, 17, 23, 29, 41, 53, 71, 149):
        states = franel_cusp_states(prime)
        assert states["0"] == (1, 2 % prime)
        matrices = cusp_transfer_matrices(prime)
        assert set(matrices) == {"A", "D"}
        inter = one_eighth_to_minus_one_transfer(prime)
        assert inter[0] == (1, 0)


def test_cusp_transfer_discriminant_is_minus_two_character() -> None:
    expected = {
        5: -1,
        11: 1,
        17: 1,
        23: -1,
        29: -1,
        41: 1,
    }
    for prime, minus_two in expected.items():
        chars = cusp_transfer_determinant_characters(prime)
        assert chars[0] == minus_two


def test_invalid_rank2_prime_rejected() -> None:
    with pytest.raises(ValueError):
        rank2_pullback_franel_hasse_coefficients(13)
