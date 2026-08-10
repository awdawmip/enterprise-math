"""Prime-halving edge-flow formula for the Franel transfer valuation.

Let E(x) be the canonical central-binomial exponent vector.  Recursively, each
odd prime occurrence q creates the adjacent edge

    (q-1)/2 -> (q+1)/2

and then recurses through (q+1)/2.  Recording multiplicity across the whole
factor-halving DAG gives weights w_q(x).  Away from index 1,

    E(x)_j = sum_q w_q(x) [1_(h_q=j)-1_(h_q-1=j)],
    h_q=(q+1)/2.

Since F_1=2 is a p-adic unit for every odd prime p, the p-adic valuation of the
Franel transfer Psi(x) is exactly the weighted edge flux

    v_p Psi(x)
      = sum_q w_q(x) (v_p(F_hq)-v_p(F_(hq-1))).

For the composite-boundary midpoint defect m=(p-1)/2,

    v_p(D_m)-v_p(F_m)
      = Flux_p(m)-Flux_p(p-2),

because F_(m-1) is nonzero modulo the forced-midpoint prime.

Thus support avoidance is only a strong sufficient condition.  The exact
valuation-preservation condition is equality of the two signed fluxes.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_low_order_defect_reduction import (
    _factor_integer,
    franel_defect_valuation,
    integer_in_central_binomial_basis,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@lru_cache(maxsize=None)
def prime_halving_edge_multiplicities(value: int) -> tuple[tuple[int, int], ...]:
    """Return sorted (odd prime q, recursive occurrence multiplicity w_q(x))."""
    _require_positive("value", value)
    weights: Counter[int] = Counter()
    for prime, multiplicity in _factor_integer(value):
        if prime == 2:
            continue
        weights[prime] += multiplicity
        child = (prime + 1) // 2
        for descendant, weight in prime_halving_edge_multiplicities(child):
            weights[descendant] += multiplicity * weight
    return tuple(sorted((prime, weight) for prime, weight in weights.items() if weight))


def edge_divergence_exponents(value: int) -> tuple[tuple[int, int], ...]:
    """Reconstruct the canonical A-basis exponents at indices j>=2."""
    _require_positive("value", value)
    coefficients: Counter[int] = Counter()
    for prime, weight in prime_halving_edge_multiplicities(value):
        upper = (prime + 1) // 2
        lower = upper - 1
        if upper >= 2:
            coefficients[upper] += weight
        if lower >= 2:
            coefficients[lower] -= weight
    return tuple(sorted((index, exponent) for index, exponent in coefficients.items() if exponent))


def edge_flow_reconstructs_basis(value: int) -> bool:
    """Exact equality with E(x) after dropping the p-irrelevant index 1."""
    expected = tuple((index, exponent) for index, exponent in integer_in_central_binomial_basis(value) if index >= 2)
    actual = edge_divergence_exponents(value)
    if actual != expected:
        raise AssertionError("prime-halving edge divergence failed to reconstruct E(x)")
    return True


def franel_edge_gradient(prime_edge: int, valuation_prime: int) -> int:
    """v_p(F_((q+1)/2))-v_p(F_((q-1)/2))."""
    _require_positive("prime_edge", prime_edge)
    _require_positive("valuation_prime", valuation_prime)
    upper = (prime_edge + 1) // 2
    lower = upper - 1
    return p_adic_valuation(triple_moment_factor(upper), valuation_prime) - p_adic_valuation(
        triple_moment_factor(lower), valuation_prime
    )


def franel_transfer_valuation_flux(value: int, valuation_prime: int) -> int:
    """Exact v_p(Psi(x)) for odd p, expressed as weighted edge flux."""
    _require_positive("value", value)
    _require_positive("valuation_prime", valuation_prime)
    if valuation_prime == 2:
        raise ValueError("the index-1 term is not invisible at p=2")
    return sum(
        weight * franel_edge_gradient(edge_prime, valuation_prime)
        for edge_prime, weight in prime_halving_edge_multiplicities(value)
    )


def franel_transfer_valuation_direct(value: int, valuation_prime: int) -> int:
    """Direct valuation from the canonical basis, used as an independent oracle."""
    _require_positive("value", value)
    _require_positive("valuation_prime", valuation_prime)
    return sum(
        exponent * p_adic_valuation(triple_moment_factor(index), valuation_prime)
        for index, exponent in integer_in_central_binomial_basis(value)
    )


def flux_matches_direct_transfer(value: int, valuation_prime: int) -> bool:
    if valuation_prime == 2:
        raise ValueError("flux formula intentionally removes the F_1 coordinate only for odd p")
    actual = franel_transfer_valuation_flux(value, valuation_prime)
    expected = franel_transfer_valuation_direct(value, valuation_prime)
    if actual != expected:
        raise AssertionError("edge flux must equal the direct Franel transfer valuation")
    return True


def half_defect_flux_correction(prime: int) -> int:
    """Exact correction v_p(D_m)-v_p(F_m) for the target half-defect family."""
    midpoint, _ = composite_boundary_half_witness(prime)
    return franel_transfer_valuation_flux(midpoint, prime) - franel_transfer_valuation_flux(
        prime - 2, prime
    )


def half_defect_flux_matches_exact_valuation(prime: int) -> bool:
    midpoint, _ = composite_boundary_half_witness(prime)
    exact = franel_defect_valuation(midpoint, prime) - p_adic_valuation(
        triple_moment_factor(midpoint), prime
    )
    flux = half_defect_flux_correction(prime)
    if flux != exact:
        raise AssertionError("half-defect valuation correction must equal the DAG flux difference")
    return True


def half_defect_transfer_is_valuation_balanced(prime: int) -> bool:
    """Whether the transfer correction contributes zero p-adic valuation."""
    return half_defect_flux_correction(prime) == 0
