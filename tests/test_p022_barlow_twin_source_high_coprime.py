from fractions import Fraction
from math import gcd

from enterprise_math.p022_barlow_twin_source_high_18step import (
    SOURCE_HIGH_18_NUMERATOR,
    forward_zero_transfer,
)
from enterprise_math.p022_barlow_twin_source_high_coprime import (
    SOURCE_HIGH_24_DENOMINATOR,
    SOURCE_HIGH_24_NUMERATOR,
    fixed_quadratic_remainder_transfer,
    quadratic_remainder_gap_is_twenty_four,
    source_high_branch_coprime_obstruction,
    source_high_fixed_transfer_gcd,
)


def test_fixed_twenty_four_step_transfer_is_exact() -> None:
    value = fixed_quadratic_remainder_transfer()
    assert value == Fraction(SOURCE_HIGH_24_NUMERATOR, SOURCE_HIGH_24_DENOMINATOR)
    assert value == forward_zero_transfer(Fraction(289, 32), 24)


def test_eighteen_and_twenty_four_step_obstructions_are_coprime() -> None:
    assert gcd(SOURCE_HIGH_18_NUMERATOR, SOURCE_HIGH_24_NUMERATOR) == 1
    assert source_high_fixed_transfer_gcd() == 1


def test_quadratic_pair_specializes_to_a_twenty_four_gap_on_affine_line() -> None:
    # r=51 lies on the formal surviving affine line q=383 and even satisfies
    # the shifted prime constellation, but the fixed transfer obstruction will
    # still rule out simultaneous Franel zeros.
    rank = 51
    prime = 8 * rank - 25
    assert prime == 383
    assert quadratic_remainder_gap_is_twenty_four(rank, prime)
    left = 2 * (rank - 1) ** 2 % prime
    right = (2 * (rank + 1) ** 2 - 1) % prime
    assert (left, right) == (276, 300)
    assert right - left == 24


def test_formal_r51_affine_branch_is_killed_by_coprime_transfer_constants() -> None:
    rank = 51
    prime = 383
    assert SOURCE_HIGH_18_NUMERATOR % prime != 0
    assert source_high_branch_coprime_obstruction(rank, prime) == 1
