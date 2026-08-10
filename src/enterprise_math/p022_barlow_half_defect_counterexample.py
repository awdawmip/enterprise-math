"""Exact counterexample to two overstrong half-defect conjectures.

Let

    p = 369581,  m = (p-1)/2 = 184790.

Then p is prime and p=5 (mod 24), so it belongs to the forced-midpoint
composite-boundary family.  Moreover

    F_8 = 739162 = 2p.

The canonical central-binomial elimination for D_m has exponent alpha_8=2.
All other low support indices are p-units, while F_(m-1) is a p-unit by the
no-adjacent-zero property.  The midpoint is a simple p-zero (verified modulo
p^2), hence

    v_p(D_m) = 1 - 2 = -1.

Therefore both global support-avoidance and global transfer-flux balance are
false, even inside the target p=5,23 (mod 24) family.  The marker itself remains
usable for multiplicative independence because its valuation is nonzero.

No minimality in p is claimed: this is an explicit counterexample, not a proof
that 369581 is the least target-family counterexample.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_half_defect_obstructions import (
    franel_recurrence_table_mod,
    half_index_lift_quotient,
)
from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import triple_moment_factor
from .p022_barlow_prime_halving_flux import half_defect_flux_correction

EXPLICIT_SUPPORT_COLLISION_PRIME = 369_581
EXPLICIT_SUPPORT_COLLISION_MIDPOINT = 184_790
COLLISION_ZERO_INDEX = 8
EXPECTED_MIDPOINT_LIFT_QUOTIENT = 153_310
EXPECTED_DEFECT_VALUATION = -1


def explicit_counterexample_basic_arithmetic() -> bool:
    prime = EXPLICIT_SUPPORT_COLLISION_PRIME
    midpoint, _ = composite_boundary_half_witness(prime)
    if midpoint != EXPLICIT_SUPPORT_COLLISION_MIDPOINT:
        raise AssertionError("midpoint arithmetic changed")
    if triple_moment_factor(COLLISION_ZERO_INDEX) != 2 * prime:
        raise AssertionError("F_8 must equal 2p exactly")
    return True


def explicit_counterexample_relation_exponent() -> int:
    midpoint = EXPLICIT_SUPPORT_COLLISION_MIDPOINT
    exponents = dict(composite_A_relation_exponents(midpoint))
    exponent = exponents.get(COLLISION_ZERO_INDEX, 0)
    if exponent != 2:
        raise AssertionError("canonical elimination must use F_8 with exponent two")
    return exponent


def explicit_counterexample_low_support_zero_hits() -> tuple[int, ...]:
    """Check every support point except the known safe neighbor m-1.

    The largest remaining support index is 8800, so this certificate is cheap;
    F_(m-1) is separately known to be nonzero because F_m is zero and adjacent
    Franel zeros are impossible in the legal recurrence window.
    """
    prime = EXPLICIT_SUPPORT_COLLISION_PRIME
    midpoint = EXPLICIT_SUPPORT_COLLISION_MIDPOINT
    support = [
        index
        for index, _ in composite_A_relation_exponents(midpoint)
        if index != midpoint - 1
    ]
    table = franel_recurrence_table_mod(prime, prime, max(support))
    hits = tuple(sorted(index for index in support if table[index] == 0))
    if hits != (COLLISION_ZERO_INDEX,):
        raise AssertionError("F_8 must be the unique p-zero on the checked support")
    return hits


def explicit_counterexample_midpoint_is_simple() -> bool:
    quotient = half_index_lift_quotient(EXPLICIT_SUPPORT_COLLISION_PRIME)
    if quotient != EXPECTED_MIDPOINT_LIFT_QUOTIENT:
        raise AssertionError("midpoint p^2 lift certificate changed")
    if quotient == 0:
        raise AssertionError("midpoint must be a simple p-zero")
    return True


def explicit_counterexample_flux_correction() -> int:
    correction = half_defect_flux_correction(EXPLICIT_SUPPORT_COLLISION_PRIME)
    if correction != -2:
        raise AssertionError("transfer correction must be -2")
    return correction


def explicit_counterexample_defect_valuation() -> int:
    value = franel_defect_valuation(
        EXPLICIT_SUPPORT_COLLISION_MIDPOINT,
        EXPLICIT_SUPPORT_COLLISION_PRIME,
    )
    if value != EXPECTED_DEFECT_VALUATION:
        raise AssertionError("half-defect valuation must be -1")
    return value
