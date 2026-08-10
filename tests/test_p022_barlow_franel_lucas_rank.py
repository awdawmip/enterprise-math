from math import comb

import pytest

from enterprise_math.p022_barlow_franel_lucas_rank import (
    base_p_digits,
    franel_lucas_residue,
    franel_midpoint_zero_criterion,
    franel_rank_of_apparition,
    franel_rank_reflection_bound,
    franel_reflection_residue_holds,
    franel_residue,
    franel_zero_digit_count,
    franel_zero_digit_reflection_holds,
    franel_zero_digits,
    lucas_block_counts,
    lucas_block_divisible_count,
    lucas_block_nonzero_count,
    lucas_divisibility_from_digits,
    lucas_factorization_holds,
    primitive_divisor_requires_large_prime,
    primitive_marker_recurrence_index,
)


def _direct_franel(value: int) -> int:
    return sum(comb(value, index) ** 3 for index in range(value + 1))


def _direct_base_p_digits(value: int, prime: int) -> tuple[int, ...]:
    if value == 0:
        return (0,)
    digits = []
    remaining = value
    while remaining:
        digits.append(remaining % prime)
        remaining //= prime
    return tuple(digits)


def _direct_lucas_product(value: int, prime: int) -> int:
    result = 1
    for digit in _direct_base_p_digits(value, prime):
        result = result * (_direct_franel(digit) % prime) % prime
    return result


def _direct_zero_digits(prime: int) -> tuple[int, ...]:
    return tuple(
        digit for digit in range(1, prime) if _direct_franel(digit) % prime == 0
    )


def test_f_zero_is_lucas_unit_and_zero_digits_do_not_crash() -> None:
    for prime in (2, 3, 5, 7, 11):
        assert franel_residue(0, prime) == 1 % prime
        assert franel_lucas_residue(0, prime) == 1 % prime
        assert lucas_factorization_holds(0, prime)
        assert franel_lucas_residue(prime, prime) == _direct_franel(prime) % prime


def test_franel_p_lucas_factorization_against_independent_binomial_oracle() -> None:
    for prime in (3, 5, 7, 11):
        for value in range(0, min(prime * prime, 80)):
            expected = _direct_franel(value) % prime
            assert franel_residue(value, prime) == expected
            assert franel_lucas_residue(value, prime) == _direct_lucas_product(
                value, prime
            )
            assert franel_lucas_residue(value, prime) == expected
            assert lucas_factorization_holds(value, prime)


def test_zero_digit_examples_and_ranks_against_independent_oracle() -> None:
    expected = {
        5: (2,),
        7: (3,),
        13: (6,),
        23: (11,),
        29: (12, 14, 16),
        41: (7, 10, 30, 33),
        61: (10, 16, 30, 44, 50),
    }
    for prime, zeros in expected.items():
        assert _direct_zero_digits(prime) == zeros
        assert franel_zero_digits(prime) == zeros
        assert franel_rank_of_apparition(prime) == zeros[0]
        assert franel_zero_digit_count(prime) == len(zeros)

    assert franel_rank_of_apparition(3) is None
    assert franel_rank_of_apparition(11) is None


def test_jarvis_verrill_reflection_against_independent_oracle() -> None:
    for prime in (3, 5, 7, 11, 13, 29, 41):
        for digit in range(prime):
            left = _direct_franel(digit) % prime
            right = (
                pow(-8, digit, prime)
                * (_direct_franel(prime - 1 - digit) % prime)
            ) % prime
            assert left == right
            assert franel_reflection_residue_holds(digit, prime)
        assert franel_zero_digit_reflection_holds(prime)


def test_reflection_sharpens_rank_to_half_prime_interval() -> None:
    for prime, rank in ((5, 2), (7, 3), (13, 6), (29, 12), (41, 7), (61, 10)):
        assert franel_rank_reflection_bound(prime) == (rank, (prime - 1) // 2)
        assert rank <= (prime - 1) // 2
    assert franel_rank_reflection_bound(11) is None


def test_midpoint_zero_criterion_is_prior_art_not_primitive_criterion() -> None:
    for prime in (5, 7, 13, 23, 29, 61):
        assert franel_midpoint_zero_criterion(prime)
    for prime in (3, 11, 17, 41):
        assert not franel_midpoint_zero_criterion(prime)

    # Midpoint divisibility need not be the first zero: p=29 has r_p=12<14.
    assert franel_rank_of_apparition(29) == 12
    assert _direct_franel(14) % 29 == 0


def test_exact_lucas_block_counts() -> None:
    for length in range(0, 6):
        domain, nonzero, divisible = lucas_block_counts(5, length)
        assert domain == 5**length
        assert nonzero == 4**length
        assert divisible == 5**length - 4**length

    for length in range(0, 4):
        assert lucas_block_nonzero_count(29, length) == 26**length
        assert lucas_block_divisible_count(29, length) == 29**length - 26**length


def test_block_formula_matches_independent_franel_divisibility() -> None:
    prime = 5
    for length in (1, 2, 3):
        limit = prime**length
        direct = sum(1 for value in range(limit) if _direct_franel(value) % prime == 0)
        assert direct == lucas_block_divisible_count(prime, length)
        for value in range(limit):
            assert lucas_divisibility_from_digits(value, prime) == (
                _direct_franel(value) % prime == 0
            )


def test_primitive_divisor_bound_is_p_at_least_two_n_plus_one_for_odd_p() -> None:
    for segment, prime in ((1, 2), (2, 5), (3, 7), (4, 173), (6, 13)):
        assert primitive_divisor_requires_large_prime(segment, prime)
        if prime != 2:
            assert prime >= 2 * segment + 1
        assert primitive_marker_recurrence_index(segment, prime) == segment + prime


def test_reflection_helpers_reject_even_prime_and_out_of_range_digit() -> None:
    with pytest.raises(ValueError, match="odd prime"):
        franel_reflection_residue_holds(0, 2)
    with pytest.raises(ValueError, match="smaller than prime"):
        franel_reflection_residue_holds(5, 5)
