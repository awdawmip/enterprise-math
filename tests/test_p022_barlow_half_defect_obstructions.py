from math import comb

from enterprise_math.p022_barlow_half_defect_obstructions import (
    canonical_defect_valuation_if_support_avoids,
    franel_recurrence_table_mod,
    half_defect_obstruction_profile,
    half_defect_support,
    half_defect_support_zero_hits,
    half_index_lift_quotient,
    half_index_mod_prime_square,
    simple_midpoint_lift_holds,
    support_avoidance_holds,
)


def _franel_exact(index: int) -> int:
    return sum(comb(index, k) ** 3 for k in range(index + 1))


def test_recurrence_mod_p_squared_matches_exact_small_franel_values() -> None:
    for prime in (23, 29, 47):
        stop = (prime - 1) // 2
        modulus = prime * prime
        table = franel_recurrence_table_mod(prime, modulus, stop)
        assert table == tuple(_franel_exact(k) % modulus for k in range(stop + 1))


def test_known_half_index_lift_quotients_are_nonzero() -> None:
    expected = {
        23: 2,
        29: 2,
        47: 41,
        53: 34,
        71: 69,
        101: 38,
        149: 93,
        167: 141,
        173: 18,
        191: 74,
    }
    for prime, quotient in expected.items():
        assert half_index_lift_quotient(prime) == quotient
        assert half_index_mod_prime_square(prime) == (prime * quotient) % (prime * prime)
        assert simple_midpoint_lift_holds(prime)


def test_canonical_support_avoids_known_earlier_zero_digits() -> None:
    # p=29 is the essential boundary: 29 already divides F_12, but the
    # canonical A-elimination support for the half index n=14 does not use 12.
    assert half_defect_support(29) == (1, 2, 3, 4, 13)
    assert _franel_exact(12) % 29 == 0
    assert half_defect_support_zero_hits(29) == ()
    assert support_avoidance_holds(29)

    for prime in (23, 47, 53, 71, 101, 149, 167, 173, 191):
        assert half_defect_support_zero_hits(prime) == ()
        assert support_avoidance_holds(prime)


def test_obstruction_profile_certifies_one_unit_only_when_both_parts_hold() -> None:
    for prime in (23, 29, 47, 53, 71, 101):
        hits, quotient, certified = half_defect_obstruction_profile(prime)
        assert hits == ()
        assert quotient != 0
        assert certified
        assert canonical_defect_valuation_if_support_avoids(prime) == 1
