from enterprise_math.p022_barlow_franel_midpoint_offset import (
    companion_prime_hits,
    companion_reconstructs_zero_digits,
    left_zero_offsets_from_companion,
    midpoint_companion_fraction,
    midpoint_companion_numerator,
    rank_from_midpoint_companion,
    zero_digits_from_companion,
)


def test_first_companion_numerators_are_exact() -> None:
    expected = {
        1: 1,
        2: -29,
        3: 157,
        4: -929,
        5: 53185,
        6: -42700613,
        7: 291801013,
        8: -2037217865,
    }
    for offset, numerator in expected.items():
        assert midpoint_companion_numerator(offset) == numerator


def test_companion_recurrence_identity_is_exact_over_rationals() -> None:
    for d in range(1, 14):
        left = 8 * (2 * d + 1) ** 2 * midpoint_companion_fraction(d + 1)
        right = (
            (2 * d - 1) ** 2 * midpoint_companion_fraction(d - 1)
            - (28 * d * d + 1) * midpoint_companion_fraction(d)
        )
        assert left == right


def test_companion_reconstructs_complete_zero_alphabet_on_forced_primes() -> None:
    for prime in (5, 7, 13, 23, 29, 47, 53, 71, 101, 157, 167, 173, 191):
        assert companion_reconstructs_zero_digits(prime)


def test_midpoint_offset_examples_explain_nonprimitive_ranks() -> None:
    assert left_zero_offsets_from_companion(29) == (2,)
    assert zero_digits_from_companion(29) == (12, 14, 16)
    assert rank_from_midpoint_companion(29) == 12
    assert companion_prime_hits(2, 29)

    assert left_zero_offsets_from_companion(157) == (3, 62)
    assert zero_digits_from_companion(157) == (16, 75, 78, 81, 140)
    assert rank_from_midpoint_companion(157) == 16
    assert companion_prime_hits(3, 157)
    assert companion_prime_hits(62, 157)

    assert left_zero_offsets_from_companion(173) == (82,)
    assert zero_digits_from_companion(173) == (4, 86, 168)
    assert rank_from_midpoint_companion(173) == 4


def test_singleton_companion_hit_is_exactly_primitive_midpoint_case() -> None:
    for prime in (5, 7, 13, 23, 47, 53, 71, 101, 167, 191):
        assert left_zero_offsets_from_companion(prime) == ()
        assert rank_from_midpoint_companion(prime) == (prime - 1) // 2
