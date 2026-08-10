"""Additive Franel transfer valuation behind canonical half-defect correction.

Let beta(v) be the exponent vector expressing a positive integer v in the
central-binomial basis A_j.  For any integer weight field w_j define

    tau_w(v) = <beta(v), w>.

Because beta is additive under multiplication, tau_w is completely additive.
When w_j=v_p(F_j), tau becomes the p-adic valuation of the Franel transfer
Psi(v) obtained by replacing each A_j by F_j.

For an odd prime q, h=(q+1)/2 gives

    tau_p(q) = tau_p(h) + v_p(F_h) - v_p(F_(h-1)),

since p is odd and v_p(F_1)=v_p(2)=0.

For a composite A-boundary n,

    v_p(D_n)=w_n-w_(n-1)-w_1+tau_p(n)-tau_p(2n-1).

At a forced midpoint m=(p-1)/2, w_(m-1)=w_1=0, hence

    v_p(D_m)=v_p(F_m)+tau_p(m)-tau_p(p-2).

This converts support cancellation and sign reversal into a prime-halving-tree
transfer imbalance.
"""

from __future__ import annotations

from collections.abc import Mapping

from .p022_barlow_low_order_defect_reduction import (
    _factor_integer,
    composite_A_relation_exponents,
    integer_in_central_binomial_basis,
)

WeightField = Mapping[int, int]


def transfer_pairing(value: int, weights: WeightField) -> int:
    """<beta(value),weights> for a sparse integer weight field."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be positive")
    return sum(
        exponent * weights.get(index, 0)
        for index, exponent in integer_in_central_binomial_basis(value)
    )


def transfer_is_additive(left: int, right: int, weights: WeightField) -> bool:
    """Exact complete-additivity check tau(ab)=tau(a)+tau(b)."""
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in (left, right)
    ):
        raise ValueError("inputs must be positive")
    lhs = transfer_pairing(left * right, weights)
    rhs = transfer_pairing(left, weights) + transfer_pairing(right, weights)
    if lhs != rhs:
        raise AssertionError("central-binomial transfer pairing must be additive")
    return True


def prime_halving_transfer_identity(prime: int, weights: WeightField) -> tuple[int, int]:
    """Return both sides of the odd-prime transfer recursion.

    For h=(q+1)/2,

        beta(q)=beta(h)-beta(2)+e_h-e_(h-1).

    Therefore

        tau(q)=tau(h)-tau(2)+w_h-w_(h-1).

    With Franel p-adic weights for an odd modulus, tau(2)=w_1=0.
    """
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or _factor_integer(prime) != ((prime, 1),)
    ):
        raise ValueError("prime must be an odd prime")
    half = (prime + 1) // 2
    left = transfer_pairing(prime, weights)
    right = (
        transfer_pairing(half, weights)
        - transfer_pairing(2, weights)
        + weights.get(half, 0)
        - weights.get(half - 1, 0)
    )
    if left != right:
        raise AssertionError("prime-halving transfer recursion failed")
    return left, right


def defect_valuation_from_transfer(
    segment: int, weights: WeightField
) -> int:
    """Pair the canonical pure-defect exponent vector against weights.

    ``weights[j]`` may be any integer field.  For p-adic Franel weights it is
    exactly v_p(D_segment).
    """
    if isinstance(segment, bool) or not isinstance(segment, int) or segment < 2:
        raise ValueError("segment must be at least two")
    relation = composite_A_relation_exponents(segment)
    direct = weights.get(segment, 0) - sum(
        exponent * weights.get(index, 0) for index, exponent in relation
    )
    transferred = (
        weights.get(segment, 0)
        - weights.get(segment - 1, 0)
        - weights.get(1, 0)
        + transfer_pairing(segment, weights)
        - transfer_pairing(2 * segment - 1, weights)
    )
    if direct != transferred:
        raise AssertionError("defect valuation and transfer imbalance must agree")
    return direct


def forced_midpoint_transfer_formula(
    midpoint: int, weights: WeightField
) -> int:
    """Simplified forced-midpoint formula when w_(m-1)=w_1=0.

    The caller supplies a valuation-like field and this helper verifies the
    prerequisite before applying

        w_m + tau(m) - tau(2m-1).
    """
    if isinstance(midpoint, bool) or not isinstance(midpoint, int) or midpoint < 2:
        raise ValueError("midpoint must be at least two")
    if weights.get(midpoint - 1, 0) != 0 or weights.get(1, 0) != 0:
        raise ValueError("forced-midpoint simplification requires zero adjacent/base weights")
    exact = defect_valuation_from_transfer(midpoint, weights)
    simplified = (
        weights.get(midpoint, 0)
        + transfer_pairing(midpoint, weights)
        - transfer_pairing(2 * midpoint - 1, weights)
    )
    if exact != simplified:
        raise AssertionError("forced midpoint transfer formula failed")
    return exact


def transfer_imbalance(midpoint: int, weights: WeightField) -> tuple[int, int, int]:
    """Return (tau(m),tau(2m-1),difference)."""
    left = transfer_pairing(midpoint, weights)
    right = transfer_pairing(2 * midpoint - 1, weights)
    return left, right, left - right
