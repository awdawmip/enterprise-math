"""Crossing-lattice certificate for nonvanishing half-defect markers.

For a forced-midpoint prime p with composite p-2, m=(p-1)/2, write

    kappa_p = v_p(D_m)
            = z_m + sum_j z_j c_j,

where z_j=v_p(F_j)>0 at earlier zero digits and c_j is the signed difference
of zero-boundary crossing multiplicities between the m and p-2 prime-halving
DAGs.

Let

    g_p = gcd{|c_j| : j<m, p|F_j, c_j!=0},

with g_p=0 when no nonzero crossing exists.  Then the correction lies in
`g_p Z`.  Hence:

* g_p=0 => kappa_p=z_m>0;
* g_p>0 and g_p does not divide z_m => kappa_p cannot vanish.

Parity is only the special case g_p=2.  The certificate is sufficient, not
necessary: when g_p divides z_m, weighted crossing valuations may still fail to
cancel the midpoint depth.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_franel_half_index import half_index_is_forced_zero
from .p022_barlow_half_defect_obstructions import franel_recurrence_table_mod
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_prime_halving_flux import prime_halving_edge_multiplicities
from .p022_barlow_zero_boundary_flux import zero_boundary_crossing_weight


def forced_composite_midpoint(prime: int) -> int:
    """Validate the broad forced-midpoint + composite-boundary setting."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 5
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be a forced-midpoint odd prime greater than five")
    if _is_prime(prime - 2):
        raise ValueError("p-2 must be composite")
    return (prime - 1) // 2


def boundary_candidate_indices(prime: int) -> tuple[int, ...]:
    """Indices touched by at least one edge of either transfer DAG."""
    midpoint = forced_composite_midpoint(prime)
    edge_primes = set(dict(prime_halving_edge_multiplicities(midpoint)))
    edge_primes.update(dict(prime_halving_edge_multiplicities(prime - 2)))
    indices: set[int] = set()
    for edge_prime in edge_primes:
        upper = (edge_prime + 1) // 2
        lower = upper - 1
        if 0 < lower < midpoint:
            indices.add(lower)
        if 0 < upper < midpoint:
            indices.add(upper)
    return tuple(sorted(indices))


def boundary_zero_coefficients(prime: int) -> tuple[tuple[int, int], ...]:
    """Return all (zero index j, nonzero crossing coefficient c_j)."""
    midpoint = forced_composite_midpoint(prime)
    candidates = boundary_candidate_indices(prime)
    if not candidates:
        return ()
    table = franel_recurrence_table_mod(prime, prime, max(candidates))
    output = []
    for index in candidates:
        if table[index] != 0:
            continue
        coefficient = zero_boundary_crossing_weight(midpoint, index) - zero_boundary_crossing_weight(
            prime - 2, index
        )
        if coefficient:
            output.append((index, coefficient))
    return tuple(output)


def crossing_lattice_modulus(prime: int) -> int:
    """g_p, with zero meaning the correction lattice is {0}."""
    modulus = 0
    for _, coefficient in boundary_zero_coefficients(prime):
        modulus = gcd(modulus, abs(coefficient))
    return modulus


def marker_congruence_residue(prime: int, midpoint_depth: int) -> tuple[int, int]:
    """Return (g_p, z_m mod g_p); use residue=z_m when g_p=0."""
    forced_composite_midpoint(prime)
    if isinstance(midpoint_depth, bool) or not isinstance(midpoint_depth, int) or midpoint_depth <= 0:
        raise ValueError("midpoint_depth must be a positive integer")
    modulus = crossing_lattice_modulus(prime)
    if modulus == 0:
        return 0, midpoint_depth
    return modulus, midpoint_depth % modulus


def crossing_lattice_certifies_nonzero(prime: int, midpoint_depth: int) -> bool:
    """Sufficient nonvanishing certificate for kappa_p.

    False means only 'inconclusive', never 'marker vanishes'.
    """
    modulus, residue = marker_congruence_residue(prime, midpoint_depth)
    if modulus == 0:
        return True
    return residue != 0
