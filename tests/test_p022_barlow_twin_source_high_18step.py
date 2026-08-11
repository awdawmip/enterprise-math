from fractions import Fraction

import pytest

from enterprise_math.p022_barlow_twin_source_high_18step import (
    SOURCE_HIGH_18_COFACTOR,
    SOURCE_HIGH_18_DENOMINATOR,
    SOURCE_HIGH_18_NUMERATOR,
    affine_source_high_prime,
    fixed_source_high_partial_factorization,
    fixed_source_high_transfer,
    forward_zero_transfer,
)


def test_fixed_eighteen_step_transfer_is_exact() -> None:
    value = fixed_source_high_transfer()
    assert value == Fraction(SOURCE_HIGH_18_NUMERATOR, SOURCE_HIGH_18_DENOMINATOR)
    assert value == forward_zero_transfer(Fraction(25, 8), 18)


def test_fixed_numerator_partial_factorization_is_exact() -> None:
    factors = fixed_source_high_partial_factorization()
    assert factors == (71, 5_329_603, SOURCE_HIGH_18_COFACTOR)
    product = 1
    for factor in factors:
        product *= factor
    assert product == SOURCE_HIGH_18_NUMERATOR
    assert SOURCE_HIGH_18_COFACTOR % 24 == 23


def test_small_factor_71_is_only_formally_affine_and_not_a_twin_source() -> None:
    # 71=8*12-25 is a genuine factor of the fixed transfer numerator, but
    # r=12 is not a twin center because 2r+1=25.
    assert affine_source_high_prime(12) == 71
    assert (SOURCE_HIGH_18_NUMERATOR % 71) == 0
    assert (2 * 12 + 1) == 25


def test_non_affine_partial_factor_is_rejected_by_integrality() -> None:
    # 5329603 is 3 mod 8, so it cannot equal 8r-25 for integral r.
    assert 5_329_603 % 8 == 3
    with pytest.raises(ValueError, match="8r-25 must be prime"):
        affine_source_high_prime((5_329_603 + 25) // 8)
