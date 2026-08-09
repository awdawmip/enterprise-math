from enterprise_math.p022_barlow_franel_transfer_defect import (
    boundary_transfer_defect,
    boundary_transfer_defect_valuation,
    composite_boundary_defect_matches_reduction,
    composite_defect_local_formula,
    franel_transfer,
    franel_transfer_valuation,
    odd_prime_transfer_recursion,
    prime_boundary_defect_is_trivial,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import (
    composite_indices,
    primes_through,
)
from enterprise_math.p022_barlow_low_order_identifiability import (
    p_adic_valuation,
)


def test_transfer_is_multiplicative_on_small_integer_products() -> None:
    for left in range(1, 40):
        for right in range(1, 40):
            assert franel_transfer(left * right) == franel_transfer(left) * franel_transfer(
                right
            )


def test_prime_boundary_defect_is_exactly_one() -> None:
    for segment in range(2, 151):
        if 2 * segment - 1 in primes_through(2 * segment - 1):
            assert prime_boundary_defect_is_trivial(segment)
            assert boundary_transfer_defect(segment) == 1


def test_composite_boundary_transfer_defect_equals_pure_reduction_defect() -> None:
    for segment in composite_indices(80):
        assert composite_boundary_defect_matches_reduction(segment)


def test_local_valuation_formula_matches_explicit_transfer_rational() -> None:
    for segment in range(2, 45):
        defect = boundary_transfer_defect(segment)
        for prime in primes_through(120):
            direct = p_adic_valuation(defect.numerator, prime) - p_adic_valuation(
                defect.denominator, prime
            )
            assert boundary_transfer_defect_valuation(segment, prime) == direct


def test_odd_prime_transfer_recursion_is_exact() -> None:
    valuation_primes = primes_through(80)
    for odd_prime in tuple(prime for prime in primes_through(120) if prime > 2):
        for valuation_prime in valuation_primes:
            lhs, rhs = odd_prime_transfer_recursion(odd_prime, valuation_prime)
            assert lhs == rhs


def test_composite_local_formula_matches_A_elimination_valuation() -> None:
    for segment in composite_indices(70):
        for prime in primes_through(100):
            local, eliminated = composite_defect_local_formula(segment, prime)
            assert local == eliminated


def test_segment_67_row_337_is_locally_zero() -> None:
    # The famous 337 row does not see the new D_67 locally.  Its value is zero;
    # it closes the extension by rejecting a global old-defect dependence.
    assert boundary_transfer_defect_valuation(67, 337) == 0
    assert franel_transfer_valuation(67, 337) == 0
    assert franel_transfer_valuation(133, 337) == 0
