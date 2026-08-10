"""Prime-halving ancestry behind the canonical central-binomial A-support.

The recursive integer-in-A-basis representation is driven by odd primes q:
with h=(q+1)/2, the representation of q introduces A_h/A_(h-1) and then
recurses on the integer h.  Therefore every nontrivial support index is born
from a prime ancestor q as one member of the adjacent pair

    ((q-1)/2, (q+1)/2).

Starting from prime divisors of m and p-2 gives a finite prime-halving ancestry
forest for the half-defect elimination.  An actual Franel cancellation at
j=m-d consequently requires both p|K_d and the ancestry condition that
2j-1 or 2j+1 occurs in that forest (up to the explicit m-1 support term).

This is a necessary structural condition.  Coefficient cancellations can make
the actual A-support smaller than the generated ancestry support.
"""

from __future__ import annotations

from functools import lru_cache

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_franel_half_integer_solution import integer_midpoint_companion
from .p022_barlow_half_support_companion import canonical_half_support
from .p022_barlow_low_order_defect_reduction import _factor_integer


def _prime_divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be positive")
    return tuple(prime for prime, _ in _factor_integer(value))


@lru_cache(maxsize=None)
def prime_halving_ancestry(value: int) -> tuple[int, ...]:
    """All primes reached from prime divisors of value by q -> factors((q+1)/2)."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be positive")
    seen: set[int] = set()
    stack = list(_prime_divisors(value))
    while stack:
        prime = stack.pop()
        if prime in seen:
            continue
        seen.add(prime)
        if prime == 2:
            continue
        half = (prime + 1) // 2
        for child in _prime_divisors(half):
            if child not in seen:
                stack.append(child)
    return tuple(sorted(seen))


def generated_A_support_from_ancestry(value: int) -> tuple[int, ...]:
    """Support superset generated before exponent cancellations."""
    ancestry = prime_halving_ancestry(value)
    indices: set[int] = set()
    for prime in ancestry:
        if prime == 2:
            indices.add(1)
            continue
        h = (prime + 1) // 2
        indices.add(h)
        indices.add(h - 1)
    return tuple(sorted(index for index in indices if index > 0))


def half_support_ancestry_primes(prime: int) -> tuple[int, ...]:
    """Union of ancestry forests rooted at m and p-2."""
    midpoint, _ = composite_boundary_half_witness(prime)
    return tuple(
        sorted(
            set(prime_halving_ancestry(midpoint))
            | set(prime_halving_ancestry(prime - 2))
        )
    )


def half_generated_support(prime: int) -> tuple[int, ...]:
    midpoint, _ = composite_boundary_half_witness(prime)
    generated = (
        set(generated_A_support_from_ancestry(midpoint))
        | set(generated_A_support_from_ancestry(prime - 2))
        | {1, midpoint - 1}
    )
    return tuple(sorted(generated))


def actual_support_is_inside_ancestry_support(prime: int) -> bool:
    actual = set(canonical_half_support(prime))
    generated = set(half_generated_support(prime))
    if not actual <= generated:
        raise AssertionError("canonical support must lie inside prime-halving ancestry support")
    return True


def terminal_ancestry_primes_for_index(index: int) -> tuple[int, ...]:
    """Prime ancestors which could directly generate support index j."""
    if isinstance(index, bool) or not isinstance(index, int) or index <= 0:
        raise ValueError("index must be positive")
    candidates = []
    for value in (2 * index - 1, 2 * index + 1):
        if value >= 2:
            factors = _factor_integer(value)
            if len(factors) == 1 and factors[0] == (value, 1):
                candidates.append(value)
    return tuple(candidates)


def ancestry_allows_support_index(prime: int, index: int) -> bool:
    """Necessary ancestry test for a non-explicit support index."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 1 <= index < midpoint:
        raise ValueError("index must lie in 1..m-1")
    if index in (1, midpoint - 1):
        return True
    ancestry = set(half_support_ancestry_primes(prime))
    return any(candidate in ancestry for candidate in terminal_ancestry_primes_for_index(index))


def companion_zero_passes_ancestry_filter(prime: int, offset: int) -> bool:
    """Necessary filter for a K_d zero to be eligible for A-support cancellation."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or not 1 <= offset < midpoint:
        raise ValueError("offset must lie in 1..m-1")
    if integer_midpoint_companion(offset) % prime:
        raise ValueError("offset is not a companion zero for this prime")
    index = midpoint - offset
    return ancestry_allows_support_index(prime, index)


def ancestry_chain_to_prime(value: int, target_prime: int) -> tuple[int, ...] | None:
    """Return one top-down ancestry chain ending at target_prime, if present.

    A chain q0,...,qr has q0|value and q_(i+1)|(q_i+1)/2.
    """
    if target_prime not in prime_halving_ancestry(value):
        return None

    def search(current: int, path: tuple[int, ...]) -> tuple[int, ...] | None:
        if current == target_prime:
            return path
        if current == 2:
            return None
        half = (current + 1) // 2
        for child in _prime_divisors(half):
            result = search(child, path + (child,))
            if result is not None:
                return result
        return None

    for root in _prime_divisors(value):
        result = search(root, (root,))
        if result is not None:
            return result
    raise AssertionError("ancestry membership must have a chain witness")
