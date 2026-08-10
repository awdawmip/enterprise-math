"""Sparse zero-boundary formula for Franel transfer valuations.

For an odd valuation prime p and x<p, the prime-halving flux formula is

    psi_p(x)=sum_q w_q(x)(v_p(F_h)-v_p(F_(h-1))), h=(q+1)/2.

The Franel recurrence forbids adjacent p-zeros for indices below p.  Hence a
nonzero edge gradient can occur only when exactly one endpoint is a zero digit.
For a zero index j, the only possible prime edges are q=2j-1 and q=2j+1,
with signs + and - respectively.  Therefore

    psi_p(x)=sum_{j in Z_p} z_j (w_(2j-1)(x)-w_(2j+1)(x)),

where z_j=v_p(F_j) and w_q=0 when q is not prime / absent from the DAG.

For the forced midpoint defect, this gives an exact sparse marker formula:

    v_p(D_m)=z_m + sum_{j<m, p|F_j} z_j * Delta c_j,

where Delta c_j is the difference of signed zero-boundary crossing
multiplicities between the m and p-2 prime-halving DAGs.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_half_defect_obstructions import franel_recurrence_table_mod
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_prime_halving_flux import (
    franel_transfer_valuation_flux,
    prime_halving_edge_multiplicities,
)
from .p022_barlow_low_order_defect_reduction import _is_prime, franel_defect_valuation


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def prime_edge_weight(value: int, edge_prime: int) -> int:
    """w_q(x), with zero returned for a nonprime or absent q."""
    _require_positive("value", value)
    _require_positive("edge_prime", edge_prime)
    if edge_prime == 2 or not _is_prime(edge_prime):
        return 0
    return dict(prime_halving_edge_multiplicities(value)).get(edge_prime, 0)


def zero_boundary_crossing_weight(value: int, zero_index: int) -> int:
    """c_x(j)=w_(2j-1)(x)-w_(2j+1)(x)."""
    _require_positive("value", value)
    _require_positive("zero_index", zero_index)
    return prime_edge_weight(value, 2 * zero_index - 1) - prime_edge_weight(
        value, 2 * zero_index + 1
    )


def zero_boundary_flux_direct(value: int, valuation_prime: int) -> int:
    """Exact sparse boundary sum, using direct p-adic valuations of F_j.

    Intended as a theorem oracle on modest x.  Large target-family certificates
    should use known zero indices / modular recurrence rather than constructing
    every Franel integer below x.
    """
    _require_positive("value", value)
    _require_positive("valuation_prime", valuation_prime)
    if valuation_prime == 2:
        raise ValueError("valuation prime must be odd")
    if value >= valuation_prime:
        raise ValueError("sparse zero-boundary formula is exposed here for value<p")
    total = 0
    # Any edge in Q(x) has upper endpoint at most (x+1)/2.  Nothing above that
    # can contribute, so the scan is bounded well below p.
    upper = (value + 1) // 2
    for index in range(1, upper + 1):
        valuation = p_adic_valuation(triple_moment_factor(index), valuation_prime)
        if valuation:
            total += valuation * zero_boundary_crossing_weight(value, index)
    return total


def zero_boundary_flux_matches_edge_flux(value: int, valuation_prime: int) -> bool:
    actual = zero_boundary_flux_direct(value, valuation_prime)
    expected = franel_transfer_valuation_flux(value, valuation_prime)
    if actual != expected:
        raise AssertionError("zero-boundary localization must equal full edge flux")
    return True


def half_defect_boundary_coefficient(prime: int, zero_index: int) -> int:
    """Delta c_j between midpoint and p-2 DAGs."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if not 0 < zero_index < midpoint:
        raise ValueError("zero_index must lie strictly left of the midpoint")
    return zero_boundary_crossing_weight(midpoint, zero_index) - zero_boundary_crossing_weight(
        prime - 2, zero_index
    )


def half_defect_sparse_support_zeros(prime: int) -> tuple[int, ...]:
    """Left midpoint-zero indices that have a nonzero defect crossing coefficient.

    This uses a modular recurrence only up to the largest edge endpoint touched
    by the two DAGs, rather than scanning the whole half interval.
    """
    midpoint, _ = composite_boundary_half_witness(prime)
    edges = dict(prime_halving_edge_multiplicities(midpoint))
    other = dict(prime_halving_edge_multiplicities(prime - 2))
    candidate_indices: set[int] = set()
    for edge_prime in set(edges) | set(other):
        upper = (edge_prime + 1) // 2
        lower = upper - 1
        if 0 < lower < midpoint:
            candidate_indices.add(lower)
        if 0 < upper < midpoint:
            candidate_indices.add(upper)
    if not candidate_indices:
        return ()
    table = franel_recurrence_table_mod(prime, prime, max(candidate_indices))
    return tuple(
        sorted(
            index
            for index in candidate_indices
            if table[index] == 0 and half_defect_boundary_coefficient(prime, index) != 0
        )
    )


def half_defect_sparse_marker_valuation(prime: int) -> int:
    """Reconstruct v_p(D_m) from midpoint depth plus sparse boundary corrections."""
    midpoint, _ = composite_boundary_half_witness(prime)
    marker = p_adic_valuation(triple_moment_factor(midpoint), prime)
    # This exact-integer helper is only practical for small midpoint; large
    # certificates use the modular p^2 / graded-depth tools elsewhere.
    for index in half_defect_sparse_support_zeros(prime):
        marker += p_adic_valuation(triple_moment_factor(index), prime) * half_defect_boundary_coefficient(
            prime, index
        )
    return marker


def half_defect_sparse_marker_matches_exact(prime: int) -> bool:
    actual = half_defect_sparse_marker_valuation(prime)
    midpoint, _ = composite_boundary_half_witness(prime)
    expected = franel_defect_valuation(midpoint, prime)
    if actual != expected:
        raise AssertionError("sparse zero-boundary marker must equal exact defect valuation")
    return True
