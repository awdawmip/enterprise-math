from enterprise_math.p022_barlow_half_support_ancestry import (
    actual_support_is_inside_ancestry_support,
    ancestry_allows_support_index,
    ancestry_chain_to_prime,
    companion_zero_passes_ancestry_filter,
    half_generated_support,
    half_support_ancestry_primes,
    prime_halving_ancestry,
    terminal_ancestry_primes_for_index,
)


def test_prime_halving_ancestry_examples() -> None:
    # 31 -> (31+1)/2=16 -> prime divisor 2.
    assert prime_halving_ancestry(31) == (2, 31)

    # 43 ->22 ->11 ->6 ->3 ->2.
    assert prime_halving_ancestry(43) == (2, 3, 11, 43)
    assert ancestry_chain_to_prime(43, 3) == (43, 11, 3)


def test_actual_half_support_is_generated_by_ancestry_forest() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 157, 173, 191, 311, 359):
        assert actual_support_is_inside_ancestry_support(prime)


def test_p157_cancellation_is_visible_as_direct_prime_ancestor() -> None:
    # m=78, zero offset 62 means j=16.  The prime 31=2*j-1 divides p-2=155.
    assert terminal_ancestry_primes_for_index(16) == (31,)
    assert 31 in half_support_ancestry_primes(157)
    assert ancestry_chain_to_prime(155, 31) == (31,)
    assert ancestry_allows_support_index(157, 16)
    assert companion_zero_passes_ancestry_filter(157, 62)


def test_target_danger_window_zeros_can_fail_the_stronger_ancestry_filter() -> None:
    # p=173 has the exact companion zero d=82 -> j=4, but 7=2*j-1 is
    # absent from both ancestry forests rooted at m=86 and p-2=171.
    assert terminal_ancestry_primes_for_index(4) == (7,)
    assert 7 not in half_support_ancestry_primes(173)
    assert not ancestry_allows_support_index(173, 4)
    assert not companion_zero_passes_ancestry_filter(173, 82)

    # p=311 has d=87 -> j=68 and the only terminal prime is 137; again absent.
    assert terminal_ancestry_primes_for_index(68) == (137,)
    assert 137 not in half_support_ancestry_primes(311)
    assert not ancestry_allows_support_index(311, 68)
    assert not companion_zero_passes_ancestry_filter(311, 87)


def test_generated_support_is_a_true_superset_not_an_equality_claim() -> None:
    # The ancestry forest records all possible pair births; exponent
    # cancellations may remove some of them from the canonical relation.
    generated = set(half_generated_support(173))
    assert {1, 2, 3, 5, 6, 9, 10, 21, 22, 85} <= generated
