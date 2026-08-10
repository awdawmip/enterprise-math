"""Explicit target-family unit crossing: crossing-lattice modulus can be one.

Take

    p = 518220701 = 5 (mod 24),  m=(p-1)/2.

The exact Franel number F_50 is divisible by p exactly once.  At the zero
boundary j=50, 2j-1=99 is composite and 2j+1=101 is prime.  In the recursive
prime-halving edge multiplicities,

    w_101(m)=0,
    w_101(p-2)=1.

Hence

    Delta c_p(50)
      = [w_99(m)-w_101(m)]-[w_99(p-2)-w_101(p-2)]
      = 1.

Therefore the crossing-lattice gcd g_p is exactly one, regardless of any other
zero-boundary crossings.  This disproves any global target-family strategy
requiring all nonzero crossing coefficients to be even or to have gcd > 1.

No claim about the full defect marker kappa_p is made here; g_p=1 only removes
congruence protection.  The exact nonvanishing question still requires signed
positive-depth information.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_prime_halving_flux import prime_halving_edge_multiplicities

TARGET_UNIT_CROSSING_PRIME = 518_220_701
TARGET_UNIT_CROSSING_MIDPOINT = 259_110_350
TARGET_UNIT_ZERO_INDEX = 50
TARGET_UNIT_EDGE_PRIME = 101


def target_unit_crossing_prime_is_in_family() -> bool:
    prime = TARGET_UNIT_CROSSING_PRIME
    if not _is_prime(prime):
        raise AssertionError("declared target unit-crossing value must be prime")
    if prime % 24 != 5:
        raise AssertionError("declared prime must lie in the selected residue family")
    if (prime - 2) % 3:
        raise AssertionError("p-2 must be composite by the target residue arithmetic")
    if (prime - 1) // 2 != TARGET_UNIT_CROSSING_MIDPOINT:
        raise AssertionError("midpoint arithmetic changed")
    return True


def target_unit_zero_is_simple() -> bool:
    value = triple_moment_factor(TARGET_UNIT_ZERO_INDEX)
    if value % TARGET_UNIT_CROSSING_PRIME:
        raise AssertionError("p must divide F_50")
    if p_adic_valuation(value, TARGET_UNIT_CROSSING_PRIME) != 1:
        raise AssertionError("p must divide F_50 exactly once")
    return True


def target_unit_edge_multiplicities() -> tuple[int, int]:
    prime = TARGET_UNIT_CROSSING_PRIME
    midpoint = TARGET_UNIT_CROSSING_MIDPOINT
    midpoint_weights = dict(prime_halving_edge_multiplicities(midpoint))
    boundary_weights = dict(prime_halving_edge_multiplicities(prime - 2))
    actual = (
        midpoint_weights.get(TARGET_UNIT_EDGE_PRIME, 0),
        boundary_weights.get(TARGET_UNIT_EDGE_PRIME, 0),
    )
    if actual != (0, 1):
        raise AssertionError("q=101 edge multiplicities changed")
    return actual


def target_unit_crossing_coefficient() -> int:
    if 2 * TARGET_UNIT_ZERO_INDEX - 1 != 99 or _is_prime(99):
        raise AssertionError("lower adjacent edge label must be composite 99")
    if 2 * TARGET_UNIT_ZERO_INDEX + 1 != TARGET_UNIT_EDGE_PRIME or not _is_prime(
        TARGET_UNIT_EDGE_PRIME
    ):
        raise AssertionError("upper adjacent edge label must be prime 101")
    midpoint_weight, boundary_weight = target_unit_edge_multiplicities()
    coefficient = -midpoint_weight - (-boundary_weight)
    if coefficient != 1:
        raise AssertionError("declared zero boundary must have unit crossing coefficient")
    return coefficient


def target_unit_crossing_forces_lattice_one() -> bool:
    if not target_unit_crossing_prime_is_in_family():
        raise AssertionError("target-family check failed")
    if not target_unit_zero_is_simple():
        raise AssertionError("F_50 marker check failed")
    if abs(target_unit_crossing_coefficient()) != 1:
        raise AssertionError("unit coefficient is required")
    # Any gcd over a set containing 1 is one; no global zero scan is required.
    return True
