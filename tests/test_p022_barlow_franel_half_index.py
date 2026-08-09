from enterprise_math.p022_barlow_franel_half_index import (
    composite_boundary_half_witness,
    half_index,
    half_index_is_forced_zero,
    jarvis_verrill_mirror_residues,
    minus_two_legendre_from_residue,
    mirror_zero_set_is_symmetric,
    verify_forced_half_index_divisibility,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import primes_through
from enterprise_math.p022_barlow_low_order_identifiability import triple_moment_factor


def test_jarvis_verrill_mirror_congruence_on_small_primes() -> None:
    for prime in primes_through(79):
        if prime <= 2:
            continue
        for index in range(prime):
            left, right = jarvis_verrill_mirror_residues(prime, index)
            assert left == right


def test_half_index_forced_zero_classes_are_exactly_five_and_seven_mod_eight() -> None:
    for prime in primes_through(199):
        if prime <= 2:
            continue
        expected = prime % 8 in (5, 7)
        assert half_index_is_forced_zero(prime) == expected
        assert minus_two_legendre_from_residue(prime) == (-1 if expected else 1)
        if expected:
            assert verify_forced_half_index_divisibility(prime)
            assert triple_moment_factor(half_index(prime)) % prime == 0


def test_mirror_zero_set_is_symmetric() -> None:
    for prime in (5, 7, 11, 13, 23, 29, 31, 47):
        for index in range(prime):
            assert mirror_zero_set_is_symmetric(prime, index)


def test_composite_boundary_half_witness_family() -> None:
    # Every listed prime is 5 or 23 mod 24 and exceeds five.
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191):
        segment, witness = composite_boundary_half_witness(prime)
        assert witness == prime
        assert segment == (prime - 1) // 2
        assert (2 * segment - 1) == prime - 2
        assert (prime - 2) % 3 == 0
        assert triple_moment_factor(segment) % prime == 0


def test_forced_zero_does_not_mean_primitive_divisor() -> None:
    # p=29 divides the forced half-index term F_14, but it already divides F_12.
    prime = 29
    assert verify_forced_half_index_divisibility(prime)
    assert triple_moment_factor(12) % prime == 0
    assert triple_moment_factor(14) % prime == 0
