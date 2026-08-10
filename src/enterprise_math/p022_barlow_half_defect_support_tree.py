"""Prime-halving support geometry for the P022 half-index Franel defect.

The canonical central-binomial elimination uses ``integer_in_central_binomial_basis``.
For every odd prime q encountered there, put j=(q+1)//2.  The only new A-indices
introduced at that node are j and j-1, while the recursion continues through j.
Thus the exact A-elimination support is contained in a sparse prime-halving tree.

For the target half-index family p=5 or 23 (mod 24), m=(p-1)/2 and p-2 is
composite.  Apart from the always-present adjacent index m-1 (which cannot be a
Franel zero when F_m=0), the tree obeys the sharper location bounds

    p=5  (mod 24):  j <= (p+1)/6,
    p=23 (mod 24):  j <= (p+1)/4.

Equivalently, a dangerous companion offset d=m-j can only occur at

    d >= (p-2)/3  or  d >= (p-3)/4,

respectively.  These are support restrictions, not a proof that such far-offset
companion zeros never hit the tree.
"""

from __future__ import annotations

from functools import lru_cache

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_low_order_defect_reduction import (
    _factor_integer,
    _is_prime,
    composite_A_relation_exponents,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@lru_cache(maxsize=None)
def prime_halving_nodes(value: int) -> tuple[int, ...]:
    """Distinct odd-prime nodes reachable from the factor tree of ``value``."""
    _require_positive("value", value)
    nodes: set[int] = set()
    stack = [prime for prime, _ in _factor_integer(value) if prime != 2]
    while stack:
        prime = stack.pop()
        if prime in nodes:
            continue
        if not _is_prime(prime) or prime == 2:
            raise AssertionError("halving nodes must be odd primes")
        nodes.add(prime)
        child_value = (prime + 1) // 2
        stack.extend(q for q, _ in _factor_integer(child_value) if q != 2)
    return tuple(sorted(nodes))


def prime_halving_candidate_indices(value: int) -> tuple[int, ...]:
    """Superset of A-indices that the recursive integer basis can touch."""
    _require_positive("value", value)
    indices = {1}
    for prime in prime_halving_nodes(value):
        half = (prime + 1) // 2
        indices.add(half)
        if half > 1:
            indices.add(half - 1)
    return tuple(sorted(indices))


def half_defect_support_tree(prime: int) -> tuple[int, ...]:
    """Candidate support for the midpoint composite A-elimination."""
    segment, odd_boundary = composite_boundary_half_witness(prime)
    candidates = {1, segment - 1}
    candidates.update(prime_halving_candidate_indices(odd_boundary))
    candidates.update(prime_halving_candidate_indices(segment))
    return tuple(sorted(candidates))


def half_defect_exact_support(prime: int) -> tuple[int, ...]:
    """Exact nonzero support after integer-basis cancellations."""
    segment, _ = composite_boundary_half_witness(prime)
    return tuple(index for index, _ in composite_A_relation_exponents(segment))


def support_tree_contains_exact_support(prime: int) -> bool:
    tree = set(half_defect_support_tree(prime))
    exact = set(half_defect_exact_support(prime))
    if not exact <= tree:
        raise AssertionError("prime-halving tree must contain exact A-elimination support")
    return True


def target_low_support_bound(prime: int) -> int:
    """Sharp simple location bound for non-adjacent support in target APs."""
    composite_boundary_half_witness(prime)
    residue = prime % 24
    if residue == 5:
        return (prime + 1) // 6
    if residue == 23:
        return (prime + 1) // 4
    raise ValueError("bound is specialized to p=5 or 23 modulo 24")


def target_dangerous_offset_floor(prime: int) -> int:
    """Smallest possible offset m-j for a non-adjacent support hit."""
    segment, _ = composite_boundary_half_witness(prime)
    return segment - target_low_support_bound(prime)


def target_support_location_holds(prime: int) -> bool:
    """Certify the AP-specific low-support theorem on the exact support."""
    segment, _ = composite_boundary_half_witness(prime)
    bound = target_low_support_bound(prime)
    exact = half_defect_exact_support(prime)
    if segment - 1 not in exact:
        raise AssertionError("canonical recurrence contributes the adjacent support index")
    low = tuple(index for index in exact if index != segment - 1)
    if any(index > bound for index in low):
        raise AssertionError("non-adjacent support escaped the target AP bound")
    return True


def prime_halving_path_depth_bound(value: int) -> int:
    """Integer h with every odd-prime halving path shorter than or equal to h.

    Every odd-prime child r of q satisfies r <= (q+1)/2 <= 2q/3 for q>=3.
    We avoid floating point and iterate the worst-case 2/3 contraction.
    """
    _require_positive("value", value)
    depth = 0
    numerator = value
    while numerator >= 3:
        depth += 1
        numerator = (2 * numerator + 2) // 3
        if depth > value:  # defensive guard, unreachable for positive integers
            raise AssertionError("halving-depth iteration failed to contract")
    return depth


def prime_halving_node_count_crude_bound(value: int) -> int:
    """A rigorous O((log value)^2) bound for distinct tree nodes.

    At each depth, the product of all odd-prime nodes (with multiplicity before
    deduplication) is at most the initial value, so there can be at most
    floor(log_3(value)) nodes at that level.  This helper computes a conservative
    integer version without logarithms.
    """
    _require_positive("value", value)
    per_level = 0
    power = 1
    while power * 3 <= value:
        power *= 3
        per_level += 1
    return (prime_halving_path_depth_bound(value) + 1) * per_level
