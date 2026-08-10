"""Recover a canonical p-power relation-module shape from a future-safe kernel.

For X=(Z/p^K Z)^d, any translation-invariant equivalence relation is a group
congruence.  Its zero class H is an additive subgroup and the safe state is the
quotient Q=X/H.  Instead of leaving Q as an opaque partition table, this module
recovers the invariant p-power exponent profile of Q from exact finite torsion
counts.

Let T_j be the number of quotient elements killed by p^j.  T_j is an exact
p-power.  If alpha_j is its integer p-power exponent and
beta_j=alpha_j-alpha_(j-1), then beta_j counts invariant cyclic axes whose
exponent depth is at least j.  Hence the complete invariant exponent multiset is
recovered by finite differences.

Congruences of groups, finite abelian p-group classification and invariant-factor
recovery are established algebra.  R004 uses them as a structured fallback in
its representation compiler before resorting to a general relation/witness
partition.
"""
from __future__ import annotations

from collections.abc import Sequence
from itertools import product

State = tuple[int, ...]
Partition = frozenset[frozenset[State]]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be prime")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1


def _positive(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be positive")


def all_product_states(prime: int, cap: int, dimension: int) -> tuple[State, ...]:
    _prime(prime)
    _positive(cap, "cap")
    _positive(dimension, "dimension")
    modulus = prime**cap
    return tuple(product(range(modulus), repeat=dimension))


def _state(state: Sequence[int], modulus: int, dimension: int) -> State:
    point = tuple(state)
    if len(point) != dimension:
        raise ValueError("state width mismatch")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in point):
        raise ValueError("state entries must be integers")
    return tuple(value % modulus for value in point)


def add_states(left: State, right: State, modulus: int) -> State:
    if len(left) != len(right):
        raise ValueError("state widths must match")
    return tuple((a + b) % modulus for a, b in zip(left, right))


def subtract_states(left: State, right: State, modulus: int) -> State:
    if len(left) != len(right):
        raise ValueError("state widths must match")
    return tuple((a - b) % modulus for a, b in zip(left, right))


def scale_state(multiplier: int, state: State, modulus: int) -> State:
    if isinstance(multiplier, bool) or not isinstance(multiplier, int):
        raise ValueError("multiplier must be integer")
    return tuple((multiplier * value) % modulus for value in state)


def normalize_partition(
    blocks: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> Partition:
    _prime(prime)
    _positive(cap, "cap")
    _positive(dimension, "dimension")
    modulus = prime**cap
    normalized_blocks = []
    seen: set[State] = set()
    for block in blocks:
        normalized = frozenset(_state(state, modulus, dimension) for state in block)
        if not normalized:
            raise ValueError("partition blocks must be nonempty")
        if seen & set(normalized):
            raise ValueError("partition blocks must be disjoint")
        seen.update(normalized)
        normalized_blocks.append(normalized)
    expected = set(all_product_states(prime, cap, dimension))
    if seen != expected:
        raise ValueError("partition must cover the full product state space")
    return frozenset(normalized_blocks)


def additive_subgroup_holds(
    subgroup: Sequence[State], prime: int, cap: int, dimension: int
) -> bool:
    _prime(prime)
    _positive(cap, "cap")
    _positive(dimension, "dimension")
    modulus = prime**cap
    group = {_state(state, modulus, dimension) for state in subgroup}
    zero = (0,) * dimension
    if zero not in group:
        return False
    for left in tuple(group):
        if tuple((-value) % modulus for value in left) not in group:
            return False
        for right in tuple(group):
            if add_states(left, right, modulus) not in group:
                return False
    return True


def coset_partition(
    subgroup: Sequence[State], prime: int, cap: int, dimension: int
) -> Partition:
    _prime(prime)
    _positive(cap, "cap")
    _positive(dimension, "dimension")
    modulus = prime**cap
    group = frozenset(_state(state, modulus, dimension) for state in subgroup)
    if not additive_subgroup_holds(tuple(group), prime, cap, dimension):
        raise ValueError("subgroup must be an additive subgroup")
    blocks = {
        frozenset(add_states(state, element, modulus) for element in group)
        for state in all_product_states(prime, cap, dimension)
    }
    return frozenset(blocks)


def zero_block(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> frozenset[State]:
    normalized = normalize_partition(partition, prime, cap, dimension)
    zero = (0,) * dimension
    return next(block for block in normalized if zero in block)


def partition_is_translation_congruence(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> bool:
    normalized = normalize_partition(partition, prime, cap, dimension)
    group = zero_block(tuple(normalized), prime, cap, dimension)
    if not additive_subgroup_holds(tuple(group), prime, cap, dimension):
        return False
    return normalized == coset_partition(tuple(group), prime, cap, dimension)


def exact_prime_power_exponent(value: int, prime: int) -> int:
    """Return e for value=p^e; reject non-powers instead of using real logs."""
    _prime(prime)
    _positive(value, "value")
    exponent = 0
    remaining = value
    while remaining % prime == 0:
        remaining //= prime
        exponent += 1
    if remaining != 1:
        raise ValueError("value must be an exact power of prime")
    return exponent


def quotient_torsion_counts(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> tuple[int, ...]:
    """T_j=# quotient classes killed by p^j, for j=0..K."""
    normalized = normalize_partition(partition, prime, cap, dimension)
    if not partition_is_translation_congruence(tuple(normalized), prime, cap, dimension):
        raise ValueError("partition must be an additive translation congruence")
    group = zero_block(tuple(normalized), prime, cap, dimension)
    modulus = prime**cap
    representatives = tuple(next(iter(block)) for block in normalized)
    counts = []
    for depth in range(cap + 1):
        multiplier = prime**depth
        counts.append(
            sum(scale_state(multiplier, representative, modulus) in group for representative in representatives)
        )
    return tuple(counts)


def quotient_invariant_exponents(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> tuple[int, ...]:
    """Recover invariant cyclic p-exponents in descending order."""
    torsion = quotient_torsion_counts(partition, prime, cap, dimension)
    alpha = tuple(exact_prime_power_exponent(count, prime) for count in torsion)
    beta = [0] * (cap + 2)
    for depth in range(1, cap + 1):
        beta[depth] = alpha[depth] - alpha[depth - 1]
        if beta[depth] < 0:
            raise AssertionError("torsion exponents must be nondecreasing")
    profile = []
    for depth in range(cap, 0, -1):
        exact_count = beta[depth] - beta[depth + 1]
        if exact_count < 0:
            raise AssertionError("axis counts by depth must be nonnegative")
        profile.extend([depth] * exact_count)
    if prime ** sum(profile) != len(normalize_partition(partition, prime, cap, dimension)):
        raise AssertionError("invariant exponent mass must reproduce quotient class count")
    return tuple(profile)


def quotient_exponent_mass(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> int:
    return sum(quotient_invariant_exponents(partition, prime, cap, dimension))


def quotient_exponent_codimension(
    partition: Sequence[Sequence[State]], prime: int, cap: int, dimension: int
) -> int:
    """Ambient p-digit mass K*d minus the quotient invariant exponent mass."""
    return cap * dimension - quotient_exponent_mass(partition, prime, cap, dimension)
