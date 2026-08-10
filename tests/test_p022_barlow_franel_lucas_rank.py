from enterprise_math.p022_barlow_franel_lucas_rank import (
    base_p_digits,
    franel_rank_of_apparition,
    franel_zero_digit_count,
    franel_zero_digits,
    lucas_block_counts,
    lucas_block_divisible_count,
    lucas_block_nonzero_count,
    lucas_factorization_holds,
)
from enterprise_math.p022_barlow_low_order_identifiability import triple_moment_factor


def test_franel_p_lucas_factorization_on_small_blocks() -> None:
    for prime in (3, 5, 7, 11):
        for value in range(0, min(prime * prime, 80)):
            assert lucas_factorization_holds(value, prime)


def test_zero_digit_examples_and_ranks() -> None:
    assert franel_zero_digits(5) == (2,)
    assert franel_zero_digits(7) == (3,)
    assert franel_zero_digits(13) == (6,)
    assert franel_zero_digits(23) == (11,)
    assert franel_zero_digits(29) == (12, 14, 16)
    assert franel_rank_of_apparition(29) == 12
    assert franel_zero_digit_count(29) == 3


def test_exact_lucas_block_counts() -> None:
    # p=5 has one zero digit, so the nonzero language has exactly 4^L words.
    for length in range(0, 6):
        domain, nonzero, divisible = lucas_block_counts(5, length)
        assert domain == 5**length
        assert nonzero == 4**length
        assert divisible == 5**length - 4**length

    # p=29 has three zero digits: 12,14,16.
    for length in range(0, 4):
        assert lucas_block_nonzero_count(29, length) == 26**length
        assert lucas_block_divisible_count(29, length) == 29**length - 26**length


def test_block_formula_matches_direct_franel_divisibility_for_small_prime() -> None:
    prime = 5
    for length in (1, 2):
        limit = prime**length
        direct = sum(
            1 for value in range(limit) if triple_moment_factor(value) % prime == 0
        )
        assert direct == lucas_block_divisible_count(prime, length)


def test_digit_language_characterization_for_p_five() -> None:
    zero_digit = 2
    for value in range(5**3):
        digits = base_p_digits(value, 5)
        predicted = zero_digit in digits
        actual = triple_moment_factor(value) % 5 == 0
        assert predicted == actual
