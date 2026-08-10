"""Explicit target-family unit crossing with unconditional positive marker.

Take

    p = 518220701 = 5 (mod 24),  m=(p-1)/2.

The exact Franel number F_50 is divisible by p exactly once.  At the zero
boundary j=50, 2j-1=99 is composite and 2j+1=101 is prime.  Prime-halving edge
multiplicities give

    w_101(m)=0,
    w_101(p-2)=1,

so Delta c_p(50)=+1.  Hence the crossing-lattice gcd is one.

A complete scan is still unnecessary: only endpoints of the two finite
prime-halving DAGs can influence the transfer.  There are 21 such indices, the
largest being 2,591,104.  An exact integer recurrence modulo p shows that j=50
is the *only* Franel p-zero among those boundary candidates.  Therefore the
entire defect correction is positive:

    kappa_p = z_m + z_50 > 0.

Thus this example simultaneously shows that congruence protection can vanish
(g_p=1) while positive-depth/sign geometry alone certifies a nonzero marker.
"""

from __future__ import annotations

from array import array

from .p022_barlow_franel_half_index import half_index_is_forced_zero
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_prime_halving_flux import prime_halving_edge_multiplicities

TARGET_UNIT_CROSSING_PRIME = 518_220_701
TARGET_UNIT_CROSSING_MIDPOINT = 259_110_350
TARGET_UNIT_ZERO_INDEX = 50
TARGET_UNIT_EDGE_PRIME = 101
TARGET_BOUNDARY_MAX_INDEX = 2_591_104


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
    if not half_index_is_forced_zero(prime):
        raise AssertionError("p=5 mod 8 must force the Franel midpoint zero")
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
    return True


def target_boundary_candidate_indices() -> tuple[int, ...]:
    """All left indices touched by an edge of either transfer DAG."""
    prime = TARGET_UNIT_CROSSING_PRIME
    midpoint = TARGET_UNIT_CROSSING_MIDPOINT
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
    result = tuple(sorted(indices))
    if len(result) != 21 or max(result) != TARGET_BOUNDARY_MAX_INDEX:
        raise AssertionError("target boundary-candidate geometry changed")
    return result


def _franel_sparse_residues_mod_32(
    prime: int,
    indices: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    """Exact Franel residues at sparse indices for one 32-bit prime.

    The recurrence is advanced once to max(indices).  Modular inverses of
    1,...,N+1 are generated by the standard prime-modulus recurrence and stored
    as unsigned 32-bit integers.  This keeps the large finite certificate
    integer-only and avoids millions of modular exponentiations.
    """
    if not indices:
        return ()
    if prime >= 2**32:
        raise ValueError("this compact certificate helper is limited to 32-bit primes")
    stop = max(indices)
    if stop >= prime:
        raise ValueError("Franel recurrence denominators must stay below prime")
    wanted = set(indices)
    inverses = array("I", [0]) * (stop + 2)
    inverses[1] = 1
    for value in range(2, stop + 2):
        inverses[value] = (prime - (prime // value) * inverses[prime % value] % prime) % prime

    output: dict[int, int] = {}
    previous = 1 % prime  # F_0
    current = 2 % prime   # F_1
    if 1 in wanted:
        output[1] = current
    for k in range(1, stop):
        numerator = (
            ((7 * k * k + 7 * k + 2) % prime) * current
            + ((8 * k * k) % prime) * previous
        ) % prime
        inverse = inverses[k + 1]
        following = (numerator * inverse % prime) * inverse % prime
        index = k + 1
        if index in wanted:
            output[index] = following
        previous, current = current, following
    return tuple((index, output[index]) for index in indices)


def target_boundary_zero_indices() -> tuple[int, ...]:
    """Exact p-zero boundary candidates for the target unit-crossing example."""
    candidates = target_boundary_candidate_indices()
    residues = _franel_sparse_residues_mod_32(TARGET_UNIT_CROSSING_PRIME, candidates)
    zeros = tuple(index for index, residue in residues if residue == 0)
    if zeros != (TARGET_UNIT_ZERO_INDEX,):
        raise AssertionError("j=50 must be the unique zero on the transfer boundary")
    return zeros


def target_unit_marker_is_positive_for_all_depths() -> bool:
    """Certify kappa_p=z_m+z_50>0 without evaluating the huge midpoint depth."""
    if target_boundary_zero_indices() != (TARGET_UNIT_ZERO_INDEX,):
        raise AssertionError("unexpected extra zero boundary")
    if target_unit_crossing_coefficient() != 1:
        raise AssertionError("unique boundary zero must have positive unit coefficient")
    # The forced midpoint theorem gives z_m>=1 and p|F_50 gives z_50=1.
    # Therefore kappa=z_m+z_50 is strictly positive regardless of z_m's depth.
    return True
