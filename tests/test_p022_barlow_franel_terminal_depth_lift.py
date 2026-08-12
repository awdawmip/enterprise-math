from enterprise_math.p022_barlow_franel_terminal_depth_lift import (
    large_common_square_primes,
    terminal_linear_decomposition,
    terminal_source_transfer_gcd,
)


def test_terminal_linear_decomposition_is_exact() -> None:
    for rank in range(2, 15):
        c, e, terminal = terminal_linear_decomposition(rank)
        assert c.denominator > 0
        assert e.denominator > 0
        assert terminal > 0


def test_known_large_terminal_common_primes_are_only_simple_in_pressure_range() -> None:
    # r=16,q=61 and r=50,q=149 are the two familiar large terminal common
    # factors.  Neither is a common square factor.
    assert terminal_source_transfer_gcd(16) % 61 == 0
    assert terminal_source_transfer_gcd(50) % 149 == 0
    assert large_common_square_primes(16) == ()
    assert large_common_square_primes(50) == ()


def test_no_large_common_square_prime_in_selected_late_ranks() -> None:
    for rank in (23, 30, 49, 60, 67, 96, 120):
        assert large_common_square_primes(rank) == ()
