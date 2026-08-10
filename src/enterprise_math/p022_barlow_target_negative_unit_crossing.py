"""Pocklington-certified target-family negative unit crossing.

This note provides a second unit crossing inside the selected residue family,
now with the opposite sign from the p=518220701 example.

Let

    P = 8895267426781770496852703 = 23 (mod 24),
    m = (P-1)/2,
    j = 49.

The exact Franel number F_49 is divisible by P exactly once.  Since
2j-1=97 is prime and 2j+1=99 is composite, the zero-boundary coefficient is
controlled by the q=97 prime-halving edge.  Exact recursive factor chains give

    w_97(m)=0,
    w_97(P-2)=1,

hence Delta c_P(49)=-1.

P is far above the range where trial division is practical.  A compact
Pocklington certificate is included here so the claim is an exact integer
certificate rather than a probable-prime assertion.  Pocklington's theorem is
classical prior art; the P022 content is the Franel/prime-halving specialization.

No claim is made about the full huge-midpoint defect marker kappa_P.  The result
only proves that both +1 and -1 unit crossing coefficients occur inside the
selected p=5,23 (mod 24) family.
"""

from __future__ import annotations

from math import gcd, isqrt

from .p022_barlow_low_order_defect_reduction import _factor_integer, _is_prime
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_prime_halving_flux import prime_halving_edge_multiplicities

TARGET_NEGATIVE_UNIT_PRIME = 8_895_267_426_781_770_496_852_703
TARGET_NEGATIVE_UNIT_MIDPOINT = 4_447_633_713_390_885_248_426_351
TARGET_NEGATIVE_UNIT_ZERO_INDEX = 49
TARGET_NEGATIVE_UNIT_EDGE_PRIME = 97

# Primes used in the Pocklington / q=97 ancestry certificates.
_P_MINUS_ONE_LARGE = 11_223_923_079_997
_P_MINUS_ONE_OTHER = 30_481_825_991
_R0 = 2_965_089_142_260_590_165_617_567
_R0_POCK = 255_275_582_047_517
_R1 = 2_906_585_391_500_468_731
_R2 = 27_475_558_687


def _trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _verify_pocklington(
    value: int,
    factors: tuple[tuple[int, int, int], ...],
    certified_large_primes: tuple[int, ...] = (),
) -> bool:
    """Verify one classical Pocklington certificate.

    Each entry is (q, exponent in the known factor F of value-1, witness a).
    Every q must be trial-prime or supplied in certified_large_primes.  The
    known factor product F must exceed sqrt(value).
    """
    known_large = set(certified_large_primes)
    known_factor = 1
    for prime, exponent, _ in factors:
        if exponent <= 0:
            raise ValueError("Pocklington exponents must be positive")
        if prime not in known_large and not _trial_prime(prime):
            raise AssertionError(f"uncertified Pocklington factor {prime}")
        known_factor *= prime**exponent
    if (value - 1) % known_factor:
        raise AssertionError("known Pocklington factor must divide N-1")
    if known_factor <= isqrt(value):
        raise AssertionError("Pocklington known factor must exceed sqrt(N)")
    for prime, _, witness in factors:
        if pow(witness, value - 1, value) != 1:
            raise AssertionError("Pocklington Fermat condition failed")
        residue = pow(witness, (value - 1) // prime, value) - 1
        if gcd(residue, value) != 1:
            raise AssertionError("Pocklington gcd condition failed")
    return True


def certify_p_minus_one_large_prime() -> bool:
    # 5,896,243 is trial-prime (sqrt < 2500); the remaining factors are smaller.
    factors = (
        (2, 2, 2),
        (3, 2, 2),
        (11, 2, 2),
        (19, 1, 2),
        (23, 1, 2),
        (5_896_243, 1, 2),
    )
    return _verify_pocklington(_P_MINUS_ONE_LARGE, factors)


def certify_target_negative_unit_prime() -> bool:
    if not certify_p_minus_one_large_prime():
        raise AssertionError("large P-1 factor certificate failed")
    factors = (
        (2, 1, 5),
        (13, 1, 2),
        (_P_MINUS_ONE_LARGE, 1, 2),
    )
    if not _verify_pocklington(
        TARGET_NEGATIVE_UNIT_PRIME,
        factors,
        certified_large_primes=(_P_MINUS_ONE_LARGE,),
    ):
        raise AssertionError("target Pocklington certificate failed")
    if TARGET_NEGATIVE_UNIT_PRIME % 24 != 23:
        raise AssertionError("target must lie in residue 23 mod 24")
    if (TARGET_NEGATIVE_UNIT_PRIME - 1) // 2 != TARGET_NEGATIVE_UNIT_MIDPOINT:
        raise AssertionError("target midpoint arithmetic changed")
    return True


def certify_r0_pocklington_factor() -> bool:
    # 144,917,459 is trial-prime (sqrt < 13,000), so all factors are exact.
    factors = (
        (2, 2, 2),
        (23, 1, 2),
        (41, 1, 2),
        (467, 1, 2),
        (144_917_459, 1, 2),
    )
    return _verify_pocklington(_R0_POCK, factors)


def certify_r0_prime() -> bool:
    if not certify_r0_pocklington_factor():
        raise AssertionError("R0 Pocklington factor certificate failed")
    # The single known factor already exceeds sqrt(R0).
    return _verify_pocklington(
        _R0,
        ((_R0_POCK, 1, 2),),
        certified_large_primes=(_R0_POCK,),
    )


def certify_r1_prime() -> bool:
    # Full factorization of R1-1, all prime factors < 10^6.
    factors = (
        (2, 1, 2),
        (3, 2, 2),
        (5, 1, 3),
        (13, 1, 2),
        (19, 1, 2),
        (28_279, 1, 2),
        (5_171, 1, 2),
        (894_139, 1, 2),
    )
    return _verify_pocklington(_R1, factors)


def target_negative_unit_zero_is_simple() -> bool:
    value = triple_moment_factor(TARGET_NEGATIVE_UNIT_ZERO_INDEX)
    if value % TARGET_NEGATIVE_UNIT_PRIME:
        raise AssertionError("P must divide F_49")
    if p_adic_valuation(value, TARGET_NEGATIVE_UNIT_PRIME) != 1:
        raise AssertionError("P must divide F_49 exactly once")
    return True


def _edge_97_from_known_prime(prime: int) -> int:
    """q=97 multiplicity from one already-certified prime edge."""
    if prime == TARGET_NEGATIVE_UNIT_EDGE_PRIME:
        direct = 1
    else:
        direct = 0
    child = (prime + 1) // 2
    descendant = dict(prime_halving_edge_multiplicities(child)).get(
        TARGET_NEGATIVE_UNIT_EDGE_PRIME,
        0,
    )
    return direct + descendant


def _edge_97_from_r0() -> int:
    if not certify_r0_prime() or not certify_r1_prime():
        raise AssertionError("large ancestry primes must be certified")
    child = (_R0 + 1) // 2
    expected = 2**4 * 71 * 449 * _R1
    if child != expected:
        raise AssertionError("R0 half-factorization changed")
    # q=71 and q=449 have no 97 descendant; R1 contributes exactly one.
    value = (
        _edge_97_from_known_prime(71)
        + _edge_97_from_known_prime(449)
        + _edge_97_from_known_prime(_R1)
    )
    if value != 1:
        raise AssertionError("R0 branch must contain q=97 exactly once")
    return value


def target_negative_unit_edge_multiplicities() -> tuple[int, int]:
    """Return (w_97(m), w_97(P-2)) with exact factor/primality checks."""
    if not certify_target_negative_unit_prime():
        raise AssertionError("target prime certificate failed")
    if not _trial_prime(_P_MINUS_ONE_OTHER):
        raise AssertionError("middle factor of m must be prime")

    midpoint = TARGET_NEGATIVE_UNIT_MIDPOINT
    if midpoint != 13 * _P_MINUS_ONE_OTHER * _P_MINUS_ONE_LARGE:
        raise AssertionError("midpoint factorization changed")

    midpoint_weight = (
        _edge_97_from_known_prime(13)
        + _edge_97_from_known_prime(_P_MINUS_ONE_OTHER)
        + _edge_97_from_known_prime(_P_MINUS_ONE_LARGE)
    )

    boundary = TARGET_NEGATIVE_UNIT_PRIME - 2
    if boundary != 3 * _R0:
        raise AssertionError("P-2 factorization changed")
    boundary_weight = _edge_97_from_known_prime(3) + _edge_97_from_r0()

    actual = (midpoint_weight, boundary_weight)
    if actual != (0, 1):
        raise AssertionError("target q=97 edge multiplicities must be (0,1)")
    return actual


def target_negative_unit_crossing_coefficient() -> int:
    if 2 * TARGET_NEGATIVE_UNIT_ZERO_INDEX - 1 != TARGET_NEGATIVE_UNIT_EDGE_PRIME:
        raise AssertionError("j=49 must use lower prime edge q=97")
    if _is_prime(2 * TARGET_NEGATIVE_UNIT_ZERO_INDEX + 1):
        raise AssertionError("upper edge label 99 must be composite")
    midpoint_weight, boundary_weight = target_negative_unit_edge_multiplicities()
    coefficient = midpoint_weight - boundary_weight
    if coefficient != -1:
        raise AssertionError("target negative crossing must be a unit -1")
    return coefficient


def target_negative_unit_forces_lattice_one() -> bool:
    if not target_negative_unit_zero_is_simple():
        raise AssertionError("F_49 divisibility certificate failed")
    if target_negative_unit_crossing_coefficient() != -1:
        raise AssertionError("negative unit coefficient required")
    return True
